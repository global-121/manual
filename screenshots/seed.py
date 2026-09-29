"""Idempotent seed: one fixed program with a fixed set of registrations and payments.

Every run converges to the same state; nothing is created twice.
"""

from datetime import datetime, timezone

from playwright.sync_api import APIRequestContext

from .portal import PROGRAM_NGO, PROGRAM_TITLE, Portal

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
    "titlePortal": {"en": PROGRAM_TITLE, "fr": "Espèces à usages multiples", "nl": "Multipurpose cash"},
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
        _attr("phoneNumber", "Phone Number", isRequired=True, showInPeopleAffectedTable=True, duplicateCheck=True),
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
    ("Nadia Rahman", "0755869424", "Molinos", "346987723", "new"),  # duplicate phone of Alvin Callahan
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
TARGET_STATUS = {r["referenceId"]: p[4] for r, p in zip(REGISTRATIONS, PEOPLE)}
# Edited once after import so the Data changes tab has a row.
DATA_CHANGE = ("manual-screenshots-10", "village", "Sarville")
# Reconciled once: this transaction of the first payment fails, the others succeed.
FAILED_TRANSACTION = ("manual-screenshots-08", "Incorrect phone number")

# Status changes go through "included" first where the platform requires it.
STATUS_PATH = {"new": [], "validated": ["validated"], "included": ["included"], "paused": ["included", "paused"], "declined": ["declined"]}

MINIMAL_PDF = (
    b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
    b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
    b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 595 842]>>endobj\n"
    b"trailer<</Root 1 0 R>>\n%%EOF\n"
)


def seed(portal: Portal, approver: APIRequestContext | None) -> int:
    pid = portal.find_program()
    if pid is None:
        created = portal.api("POST", "/programs", data=PROGRAM)
        pid = created["id"]
        print(f"seed: created program {pid} '{PROGRAM_TITLE}'")
    else:
        print(f"seed: reusing program {pid} '{PROGRAM_TITLE}'")
    portal.program_id = pid

    _program(portal)
    _fsp(portal)
    _registrations(portal)
    _statuses(portal)
    _data_change(portal)
    _attachment(portal)
    if approver is None:
        # The platform does not let users assign themselves as approver.
        print("seed: SKIPPED payments (set APPROVER_USERNAME_121/APPROVER_PASSWORD_121)")
    else:
        _approval_threshold(portal, approver)
        _payments(portal, approver)
    _reconciliation(portal)
    return pid


def _approval_threshold(portal: Portal, approver: APIRequestContext) -> None:
    me = portal.api("GET", "/users/current", session=approver)
    approver_id = (me.get("user") or me)["id"]
    thresholds = portal.api("GET", "program:/approval-thresholds")
    if any(approver_id in [a.get("userId") for a in t.get("approvers", [])] for t in thresholds):
        return
    portal.api("PUT", f"program:/users/{approver_id}", data={"roles": ["approver"], "scope": ""})
    portal.api("PUT", "program:/approval-thresholds", data=[{"thresholdAmount": 0, "userIds": [approver_id]}])
    print(f"seed: set approval threshold (approver user {approver_id})")


def _program(portal: Portal) -> None:
    current = portal.api("GET", "program:")
    changed = {k: PROGRAM[k] for k in ("description", "validation") if current.get(k) != PROGRAM[k]}
    if changed:
        portal.api("PATCH", "program:", data=changed)
        print(f"seed: updated program {', '.join(changed)}")


def _fsp(portal: Portal) -> None:
    if any(c["name"] == FSP for c in portal.api("GET", "program:/fsp-configurations")):
        return
    portal.api("POST", "program:/fsp-configurations", data=FSP_CONFIG)
    print(f"seed: configured FSP {FSP}")


def _registrations(portal: Portal) -> None:
    existing = {r["referenceId"] for r in portal.registrations()}
    missing = [r for r in REGISTRATIONS if r["referenceId"] not in existing]
    if missing:
        portal.api("POST", "program:/registrations", data=missing)
        print(f"seed: imported {len(missing)} registrations")


def _statuses(portal: Portal) -> None:
    for step in ["validated", "included", "paused", "declined"]:
        current = {r["referenceId"]: r["status"] for r in portal.registrations()}
        refs = [
            ref for ref, target in TARGET_STATUS.items()
            if step in STATUS_PATH[target] and current.get(ref) != target and current.get(ref) != step
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
            lambda: all(
                r["status"] == step for r in portal.registrations() if r["referenceId"] in refs
            ),
            f"status {step}",
        )
        print(f"seed: set {len(refs)} registrations to {step}")


def _data_change(portal: Portal) -> None:
    ref, field, value = DATA_CHANGE
    reg = next(r for r in portal.registrations() if r["referenceId"] == ref)
    if reg.get(field) == value:
        return
    portal.api(
        "PATCH",
        f"program:/registrations/{ref}",
        data={"data": {field: value}, "reason": "Moved to another village"},
    )
    print(f"seed: changed {field} of {ref}")


def _attachment(portal: Portal) -> None:
    if portal.api("GET", "program:/attachments"):
        return
    portal.api(
        "POST",
        "program:/attachments",
        multipart={
            "file": {"name": "distribution-plan.pdf", "mimeType": "application/pdf", "buffer": MINIMAL_PDF},
            "filename": "Distribution plan",
        },
    )
    print("seed: uploaded attachment")


def _payments(portal: Portal, approver: APIRequestContext) -> None:
    payments = portal.api("GET", "program:/payments")
    included = [ref for ref, s in TARGET_STATUS.items() if s == "included"]
    now = datetime.now(timezone.utc).strftime("%d/%m/%Y, %H:%M")
    if len(payments) == 0:
        pay = portal.api(
            "POST",
            "program:/payments",
            params={"filter.referenceId": "$in:" + ",".join(included)},
            data={"name": f"Payment {now}", "transferValue": 50, "note": ""},
        )
        portal.api("POST", f"program:/payments/{pay['id']}/approve", session=approver, data={})
        portal.api("POST", f"program:/payments/{pay['id']}/start")
        portal.wait_for(
            lambda: not portal.api("GET", "program:/payments/status")["inProgress"], "payment to finish"
        )
        print(f"seed: created, approved and started payment {pay['id']}")
        payments = portal.api("GET", "program:/payments")
    if len(payments) == 1:
        pay = portal.api(
            "POST",
            "program:/payments",
            params={"filter.referenceId": "$in:" + ",".join(included[:2])},
            data={"name": f"Payment {now}", "transferValue": 50, "note": ""},
        )
        print(f"seed: created payment {pay['id']} (pending approval)")


def _reconciliation(portal: Portal) -> None:
    payments = sorted(portal.api("GET", "program:/payments"), key=lambda p: p["paymentId"])
    if not payments:
        return
    pay_id = payments[0]["paymentId"]

    def transactions() -> list[dict]:
        return portal.api("GET", f"program:/payments/{pay_id}/transactions", params={"limit": 100})["data"]

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
        multipart={"file": {"name": "reconciliation.csv", "mimeType": "text/csv", "buffer": "\n".join(rows).encode()}},
    )
    portal.wait_for(lambda: all(t["status"] != "waiting" for t in transactions()), "reconciliation")
    print(f"seed: reconciled payment {pay_id} (1 failed, {len(txs) - 1} successful)")
