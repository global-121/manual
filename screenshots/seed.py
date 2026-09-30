"""Idempotent seed: one fixed program with a fixed set of registrations and payments.

Every run converges to the same state; nothing is created twice.
"""

import logging
from datetime import UTC, datetime

from playwright.sync_api import APIRequestContext

from .portal import PROGRAM_NGO, PROGRAM_TITLE, Portal

logger = logging.getLogger(__name__)

FSP = "Excel"
FSP_CONFIG = {
    "name": FSP,
    "label": {"en": "Excel"},
    "fspName": FSP,
    "properties": [
        {"name": "columnToMatch", "value": "phoneNumber"},
        {"name": "columnsToExport", "value": ["fullName", "phoneNumber", "village", "idNumber"]},
    ],
}


def _attr(name: str, label: str, type_: str = "text", **extra) -> dict:
    """Return a program registration attribute with defaults, overridden by `extra`."""
    return {
        "name": name,
        "label": {"en": label},
        "type": type_,
        "isRequired": False,
        "options": [],
        "scoring": {},
        "pattern": "",
        "showInPeopleAffectedTable": False,
        "editableInPortal": True,
        "export": ["payment"],
        "duplicateCheck": False,
        "placeholder": "",
        **extra,
    }


PROGRAM = {
    "location": "Netherlands",
    "ngo": PROGRAM_NGO,
    "titlePortal": {
        "en": PROGRAM_TITLE,
        "fr": "Espèces à usages multiples",
        "nl": "Multipurpose cash",
    },
    "description": {"en": "Multipurpose cash assistance for households affected by the floods."},
    "validation": True,
    "startDate": "2025-01-01T00:00:00.000Z",
    "endDate": "2027-12-31T00:00:00.000Z",
    "currency": "USD",
    "distributionFrequency": "month",
    "distributionDuration": 5,
    "fixedTransferValue": 50,
    "paymentAmountMultiplierFormula": "",
    "targetNrRegistrations": 100,
    "budget": 100000,
    "fsps": [FSP],
    "fullnameNamingConvention": ["fullName"],
    "languages": ["en", "fr", "nl"],
    "enableMaxPayments": True,
    "enableScope": False,
    "monitoringDashboardUrl": "",
    "programRegistrationAttributes": [
        _attr("fullName", "Name"),
        _attr(
            "phoneNumber",
            "Phone Number",
            isRequired=True,
            showInPeopleAffectedTable=True,
            duplicateCheck=True,
        ),
        _attr("village", "village", showInPeopleAffectedTable=True),
        _attr("idNumber", "idNumber", showInPeopleAffectedTable=True),
    ],
}

# (fullName, phoneNumber, village, idNumber, target status)
PEOPLE = [
    ("Alonso Garcia", "0712449657", "Molinos", "346987720", "included"),
    ("Barbara Case", "0748856321", "Molinos", "346987722", "included"),
    ("Alvin Callahan", "0755869424", "Molinos", "346987721", "new"),
    ("Lara Schmitt", "0754666589", "Molinos", "964875643", "new"),
    ("Melany Beck", "07536694544", "Sarville", "988865754", "validated"),
    ("Aspen Bradley", "0845663217", "Sarville", "234569675", "paused"),
    ("Alia Knapp", "0812442251", "Sarville", "234569676", "declined"),
    ("Omar Haddad", "0798112233", "Sarville", "234569677", "included"),
    # Same phone number as Alvin Callahan, so both are flagged as duplicates.
    ("Nadia Rahman", "0755869424", "Molinos", "346987723", "new"),
    ("Pieter de Vries", "0611223344", "Molinos", "346987724", "included"),
]

REGISTRATIONS = [
    {
        "referenceId": f"manual-screenshots-{i:02d}",
        "fullName": name,
        "phoneNumber": phone,
        "village": village,
        "idNumber": id_number,
        "preferredLanguage": "en",
        "paymentAmountMultiplier": 1,
        "maxPayments": 5,
        "scope": "",
        "programFspConfigurationName": FSP,
    }
    for i, (name, phone, village, id_number, _) in enumerate(PEOPLE, start=1)
]
TARGET_STATUS = {r["referenceId"]: p[4] for r, p in zip(REGISTRATIONS, PEOPLE, strict=True)}
# Edited once after import so the Data changes tab has a row.
DATA_CHANGE = ("manual-screenshots-10", "village", "Sarville")
# Reconciled once: this transaction of the first payment fails, the others succeed.
FAILED_TRANSACTION = ("manual-screenshots-08", "Incorrect phone number")

# Status changes go through "included" first where the platform requires it.
STATUS_PATH = {
    "new": [],
    "validated": ["validated"],
    "included": ["included"],
    "paused": ["included", "paused"],
    "declined": ["declined"],
}

# Extra team member: a 2nd eligible approver and a user to edit (you cannot edit your own roles).
TEAM_MEMBER = ("cva-officer@example.org", "cva-officer")

MINIMAL_PDF = (
    b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
    b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
    b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 595 842]>>endobj\n"
    b"trailer<</Root 1 0 R>>\n%%EOF\n"
)


def seed(portal: Portal, approver: APIRequestContext | None) -> int:
    """Create the demo program if needed and bring it to its expected state.

    Only touches the demo program. Payments are skipped without an approver, because
    the platform does not let users approve their own payments.

    Args:
        portal: Logged-in admin session.
        approver: API session of a second user who approves the demo payments, or None.

    Returns:
        The id of the demo program.
    """
    pid = portal.find_program()
    if pid is None:
        created = portal.api("POST", "/programs", data=PROGRAM)
        pid = created["id"]
        logger.info("seed: created program %s '%s'", pid, PROGRAM_TITLE)
    else:
        logger.info("seed: reusing program %s '%s'", pid, PROGRAM_TITLE)
    portal.program_id = pid

    _program(portal)
    _fsp(portal)
    _team(portal)
    _registrations(portal)
    _statuses(portal)
    _data_change(portal)
    _attachment(portal)
    if approver is None:
        # The platform does not let users assign themselves as approver.
        logger.warning("seed: SKIPPED payments (set APPROVER_USERNAME_121/APPROVER_PASSWORD_121)")
    else:
        _approval_threshold(portal, approver)
        _payments(portal, approver)
    _reconciliation(portal)
    return pid


def _approval_threshold(portal: Portal, approver: APIRequestContext) -> None:
    """Make the approver the only approver of all payments in the demo program."""
    me = portal.api("GET", "/users/current", session=approver)
    approver_id = (me.get("user") or me)["id"]
    thresholds = portal.api("GET", "program:/approval-thresholds")
    if any(approver_id in [a.get("userId") for a in t.get("approvers", [])] for t in thresholds):
        return
    portal.api("PUT", f"program:/users/{approver_id}", data={"roles": ["approver"], "scope": ""})
    portal.api(
        "PUT",
        "program:/approval-thresholds",
        data=[{"thresholdAmount": 0, "userIds": [approver_id]}],
    )
    logger.info("seed: set approval threshold (approver user %s)", approver_id)


def _team(portal: Portal) -> None:
    """Add TEAM_MEMBER to the program team."""
    username, role = TEAM_MEMBER
    if any(u.get("username") == username for u in portal.api("GET", "program:/users")):
        return
    user = next((u for u in portal.api("GET", "/users") if u.get("username") == username), None)
    if user is None:
        raise LookupError(f"user {username} not found on this environment")
    portal.api("PUT", f"program:/users/{user['id']}", data={"roles": [role], "scope": ""})
    logger.info("seed: added %s to the program team", username)


def _program(portal: Portal) -> None:
    """Restore program settings that screenshots depend on."""
    current = portal.api("GET", "program:")
    changed = {k: PROGRAM[k] for k in ("description", "validation") if current.get(k) != PROGRAM[k]}
    if changed:
        portal.api("PATCH", "program:", data=changed)
        logger.info("seed: updated program %s", ", ".join(changed))


def _fsp(portal: Portal) -> None:
    """Configure the Excel FSP."""
    if any(c["name"] == FSP for c in portal.api("GET", "program:/fsp-configurations")):
        return
    portal.api("POST", "program:/fsp-configurations", data=FSP_CONFIG)
    logger.info("seed: configured FSP %s", FSP)


def _registrations(portal: Portal) -> None:
    """Import the missing demo registrations, and re-create those that should be New but are not.

    The platform cannot move a registration back to New, so such a registration is deleted
    and imported again, under its seeded referenceId plus a `.<timestamp>` suffix (a deleted
    referenceId cannot be reused).
    """
    live = {r["referenceId"].split(".")[0]: r for r in portal.registrations()}
    stale = [
        live[ref]["referenceId"]
        for ref, target in TARGET_STATUS.items()
        if target == "new" and ref in live and live[ref]["status"] != "new"
    ]
    if stale:
        portal.api(
            "DELETE",
            "program:/registrations",
            params={"filter.referenceId": "$in:" + ",".join(stale)},
            data={"reason": "Manual screenshots seed: reset to New"},
        )
        portal.wait_for(
            lambda: not any(r["referenceId"] in stale for r in portal.registrations()),
            "registrations to be deleted",
        )
        logger.info("seed: deleted %d registrations to re-create them as New", len(stale))
    suffix = datetime.now(UTC).strftime(".%Y%m%d%H%M%S")
    stale_refs = {ref.split(".")[0] for ref in stale}
    missing = [r for r in REGISTRATIONS if r["referenceId"] not in live] + [
        {**r, "referenceId": r["referenceId"] + suffix}
        for r in REGISTRATIONS
        if r["referenceId"] in stale_refs
    ]
    if missing:
        portal.api("POST", "program:/registrations", data=missing)
        logger.info("seed: imported %d registrations", len(missing))


def _statuses(portal: Portal) -> None:
    """Move each demo registration to its target status, step by step (see STATUS_PATH)."""
    for step in ["validated", "included", "paused", "declined"]:
        current = {r["referenceId"]: r["status"] for r in portal.registrations()}
        refs = [
            ref
            for ref, target in TARGET_STATUS.items()
            if step in STATUS_PATH[target]
            and current.get(ref) != target
            and current.get(ref) != step
        ]
        if not refs:
            continue
        portal.api(
            "PATCH",
            "program:/registrations/status",
            params={"filter.referenceId": "$in:" + ",".join(refs)},
            data={"status": step, "reason": "Manual screenshots seed"},
        )
        portal.wait_for(
            lambda step=step, refs=refs: all(
                r["status"] == step for r in portal.registrations() if r["referenceId"] in refs
            ),
            f"status {step}",
        )
        logger.info("seed: set %d registrations to %s", len(refs), step)


def _data_change(portal: Portal) -> None:
    """Edit one registration once, so the Data changes tab has a row."""
    ref, field, value = DATA_CHANGE
    reg = next(r for r in portal.registrations() if r["referenceId"] == ref)
    if reg.get(field) == value:
        return
    portal.api(
        "PATCH",
        f"program:/registrations/{ref}",
        data={"data": {field: value}, "reason": "Moved to another village"},
    )
    logger.info("seed: changed %s of %s", field, ref)


def _attachment(portal: Portal) -> None:
    """Upload one PDF, so the Files tab has a row."""
    if portal.api("GET", "program:/attachments"):
        return
    portal.api(
        "POST",
        "program:/attachments",
        multipart={
            "file": {
                "name": "distribution-plan.pdf",
                "mimeType": "application/pdf",
                "buffer": MINIMAL_PDF,
            },
            "filename": "Distribution plan",
        },
    )
    logger.info("seed: uploaded attachment")


def _payments(portal: Portal, approver: APIRequestContext) -> None:
    """Create four payments in the states the payment screenshots need."""
    included = [ref for ref, s in TARGET_STATUS.items() if s == "included"]
    # In creation order: (registrations, approve, start).
    # The first is reconciled later; the third is approved but not started;
    # the fourth stays unreconciled.
    plan = [
        (included, True, True),
        (included[:2], False, False),
        (included[2:], True, False),
        (included, True, True),
    ]
    for i, (refs, approve, start) in enumerate(plan):
        ids = sorted(p["paymentId"] for p in portal.api("GET", "program:/payments"))
        if len(ids) > i:
            pay_id = ids[i]
        else:
            now = datetime.now(UTC).strftime("%d/%m/%Y, %H:%M")
            pay_id = portal.api(
                "POST",
                "program:/payments",
                params={"filter.referenceId": "$in:" + ",".join(refs)},
                data={"name": f"Payment {now}", "transferValue": 50, "note": ""},
            )["id"]
            logger.info("seed: created payment %s", pay_id)
        summary = portal.api("GET", f"program:/payments/{pay_id}")
        if approve and not summary["isPaymentApproved"]:
            portal.api("POST", f"program:/payments/{pay_id}/approve", session=approver, data={})
            logger.info("seed: approved payment %s", pay_id)
        if start and not summary["hasBeenStarted"]:
            portal.api("POST", f"program:/payments/{pay_id}/start")
            portal.wait_for(
                lambda: not portal.api("GET", "program:/payments/status")["inProgress"],
                "payment to finish",
            )
            logger.info("seed: started payment %s", pay_id)


def _reconciliation(portal: Portal) -> None:
    """Reconcile the first payment once: one failed transaction, the others successful."""
    payments = sorted(portal.api("GET", "program:/payments"), key=lambda p: p["paymentId"])
    if not payments:
        return
    pay_id = payments[0]["paymentId"]

    def transactions() -> list[dict]:
        return portal.api("GET", f"program:/payments/{pay_id}/transactions", params={"limit": 100})[
            "data"
        ]

    txs = transactions()
    if not txs or any(t["status"] != "waiting" for t in txs):
        return
    phones = {r["referenceId"]: r["phoneNumber"] for r in portal.registrations()}
    failed_ref, reason = FAILED_TRANSACTION
    rows = ["phoneNumber,status,errorMessage"] + [
        f"{phones[t['registrationReferenceId']]},error,{reason}"
        if t["registrationReferenceId"] == failed_ref
        else f"{phones[t['registrationReferenceId']]},success,"
        for t in txs
    ]
    portal.api(
        "POST",
        f"program:/payments/{pay_id}/excel-reconciliation",
        multipart={
            "file": {
                "name": "reconciliation.csv",
                "mimeType": "text/csv",
                "buffer": "\n".join(rows).encode(),
            }
        },
    )
    portal.wait_for(lambda: all(t["status"] != "waiting" for t in transactions()), "reconciliation")
    logger.info("seed: reconciled payment %s (1 failed, %d successful)", pay_id, len(txs) - 1)
