"""One scenario per portal screenshot in overrides/assets/img.

Each prepare() drives the portal into the state shown in the image and returns the
Page (full viewport, optionally clipped) or a Locator to capture.
Images that are not portal screenshots (diagrams, GIFs, Power BI, Excel, NLRC 2FA) are not covered.
"""

import os
import re
from collections.abc import Callable
from dataclasses import dataclass

from playwright.sync_api import Locator, Page

from .portal import LOCALE, Portal
from .seed import PEOPLE, TEAM_MEMBER


@dataclass
class Scenario:
    """One screenshot: file name, what it shows, how to prepare it, and an optional clip."""

    name: str
    shows: str
    prepare: Callable[[Portal], Page | Locator]
    clip: tuple[int, int, int, int] | None = None  # x, y, width, height in CSS px


def top(height: int) -> tuple[int, int, int, int]:
    """Return a clip of the top `height` pixels of the full 1280px-wide viewport."""
    return (0, 0, 1280, height)


INCLUDED = next(p[0] for p in PEOPLE if p[4] == "included")
PAUSED = next(p[0] for p in PEOPLE if p[4] == "paused")
TO_DECLINE = "Lara Schmitt"
NEW = next(p[0] for p in PEOPLE if p[4] == "new")
DUPLICATE = "Nadia Rahman"
UNIQUE = "Lara Schmitt"


# --- helpers -------------------------------------------------------------------


def block_writes(page: Page, dry_run: bool = False) -> None:
    """Abort every non-GET API call from the page, optionally allowing dry-run calls."""
    page.route(
        "**/api/**",
        lambda r: (
            r.continue_()
            if r.request.method == "GET" or (dry_run and "dryRun=true" in r.request.url)
            else r.abort()
        ),
    )


def registrations(portal: Portal) -> Page:
    """Open the registrations page with a clean table."""
    page = portal.open("program:/registrations")
    reset_table(portal, page)
    return page


def reset_table(portal: Portal, page: Page) -> Locator:
    """Clear the search, filters and selection that the portal remembers between pages."""
    table = portal.wait_for_table(page)
    keyword = table.get_by_placeholder("Filter by keyword")
    if keyword.is_visible() and keyword.input_value():
        keyword.fill("")
        page.wait_for_timeout(800)
        portal.wait_for_table(page)
    clear = table.get_by_role("button", name="Clear filters")
    if clear.is_visible() and clear.is_enabled():
        clear.click()
        portal.wait_for_table(page)
    selected = table.get_by_label("Row Selected", exact=True)
    for _ in range(selected.count()):
        selected.first.click()
    return table


def registration(portal: Portal, name: str) -> Page:
    """Open the page of the demo registration called `name`.

    Raises:
        LookupError: If the registration does not exist (run with --seed).
    """
    reg = next((r for r in portal.registrations() if r.get("fullName") == name), None)
    if reg is None:
        raise LookupError(f"registration '{name}' not found (run with --seed)")
    page = portal.open(f"program:/registrations/{reg['id']}")
    page.get_by_role("tab", name="Activity log").wait_for()
    return page


def filter_status(page: Page, status: str) -> None:
    """Filter the registrations table on one registration status."""
    Portal.column_filter_button(page, "Registration Status").click()
    page.get_by_text("Choose option(s)").click()
    page.get_by_role("option", name=status, exact=True).click()


def search(page: Page, text: str) -> None:
    """Type `text` in the table's keyword filter and wait for the results."""
    table = Portal.table(page)
    table.get_by_title("Filter by keyword").click()
    table.get_by_placeholder("Filter by keyword").fill(text)
    page.wait_for_timeout(800)
    page.wait_for_load_state("networkidle")


def select_row(page: Page, name: str) -> None:
    """Tick the checkbox of the table row for registration `name`."""
    Portal.row(page, name).get_by_role("checkbox").first.click()


def unfocus(page: Page) -> None:
    """Remove focus rings and hover effects before taking a screenshot."""
    page.evaluate("document.activeElement.blur()")
    page.mouse.move(640, 180)


def full_height(page: Page) -> Page:
    """Resize the viewport to the full page height, so nothing is cut off."""
    unfocus(page)
    page.set_viewport_size(
        {"width": 1280, "height": page.evaluate("document.documentElement.scrollHeight")}
    )
    return page


def open_dialog(page: Page, title: str) -> Locator:
    """Wait for the status-change dialog `title` and return a clip around it."""
    dialog = page.get_by_role("dialog").filter(has_text=title)
    dialog.get_by_role("switch").wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(dialog)


def payment_state(summary: dict) -> str:
    """Return 'pending', 'approved', 'processing' or 'reconciled' for a payment summary."""
    if not summary["isPaymentApproved"]:
        return "pending"
    if not summary["hasBeenStarted"]:
        return "approved"
    return "processing" if summary["aggregationsPerStatus"]["waiting"]["count"] else "reconciled"


def payment_id(portal: Portal, state: str) -> int:
    """Return the id of the first demo payment in `state` (see payment_state).

    Raises:
        LookupError: If no payment is in that state.
    """
    for p in sorted(portal.api("GET", "program:/payments"), key=lambda p: p["paymentId"]):
        if payment_state(portal.api("GET", f"program:/payments/{p['paymentId']}")) == state:
            return p["paymentId"]
    raise LookupError(f"demo program has no {state} payment (seed needs an approver, see README)")


def payments(portal: Portal) -> Page:
    """Open the payments overview (writes blocked, dry runs allowed)."""
    payment_id(portal, "processing")
    page = portal.open("program:/payments")
    block_writes(page, dry_run=True)
    page.get_by_test_id("card-with-link").last.wait_for()
    return page


def started_payment(portal: Portal, state: str = "reconciled") -> Page:
    """Open the page of a started payment in `state`, with writes blocked."""
    page = portal.open(f"program:/payments/{payment_id(portal, state)}")
    block_writes(page)
    reset_table(portal, page)
    page.wait_for_timeout(1000)
    return page


def transactions_card(page: Page) -> Locator:
    """Return the card with the transactions table on a payment page."""
    return page.locator("p-card").filter(has=page.get_by_test_id("query-table"))


def filter_failed(page: Page) -> None:
    """Filter the transactions table on status Failed."""
    full_height(page)
    Portal.column_filter_button(page, "Transaction status").click()
    page.get_by_role("dialog").filter(visible=True).get_by_text("Choose option(s)").click()
    page.get_by_role("option", name="Failed", exact=True).click()
    page.get_by_text("Showing 1 to 1 of 1 records").wait_for()
    page.wait_for_timeout(400)


# --- general ---------------------------------------------------------------------


def login_page(portal: Portal) -> Page:
    """Login page (logged out) with the language menu open."""
    ctx = portal.ctx.browser.new_context(viewport={"width": 1280, "height": 720}, locale="en-GB")
    page = ctx.new_page()
    page.goto(f"{portal.portal_url}/{LOCALE}/login")
    page.get_by_label("E-mail").wait_for()
    page.evaluate(
        "['blur', 'focusout'].forEach(t => "
        "window.addEventListener(t, e => e.stopImmediatePropagation(), true))"
    )
    page.get_by_test_id("locale-dropdown").click()
    page.get_by_role("option", name="Français").wait_for()
    return page


def sidebar_language(portal: Portal) -> Page:
    """Sidebar open with the language menu open."""
    page = portal.open("/programs")
    page.get_by_test_id("sidebar-toggle").get_by_role("button", name="Menu").click()
    page.get_by_test_id("locale-dropdown").click()
    page.get_by_role("option").first.wait_for()
    return page


def account_menu(portal: Portal) -> Page:
    """Account menu open in the top bar."""
    page = portal.open("/programs")
    page.get_by_role("button", name="Account").click()
    page.get_by_role("menuitem", name="Change password").wait_for()
    return page


def change_password(portal: Portal) -> Page:
    """Change password page."""
    page = portal.open("/change-password")
    page.get_by_label("Current Password").wait_for()
    return page


# --- users -----------------------------------------------------------------------


def users(portal: Portal) -> Page:
    """Open the users page and wait for its table."""
    page = portal.open("/users")
    portal.wait_for_table(page)
    return page


def user_menu(portal: Portal) -> Page:
    """Users page with the sidebar open."""
    page = users(portal)
    page.get_by_test_id("sidebar-toggle").get_by_role("button", name="Menu").click()
    page.get_by_test_id("sidebar").get_by_role("link", name="Users").wait_for()
    return page


def add_user_button(portal: Portal) -> Page:
    """Users page with 'Add new user' highlighted."""
    page = users(portal)
    Portal.highlight(page.get_by_role("button", name="Add new user"))
    return page


def add_user_dialog(portal: Portal) -> Locator:
    """Add user dialog filled in with an example name and e-mail."""
    page = users(portal)
    page.get_by_role("button", name="Add new user").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_label("Full name").fill("FirstName LastName")
    dialog.get_by_label("E-mail").fill("username@example.org")
    page.evaluate("document.activeElement.blur()")
    return Portal.clip_around(dialog)


def reset_password(portal: Portal) -> Locator:
    """User row menu open with 'Reset password' highlighted."""
    page = users(portal)
    row = Portal.table(page).locator("tbody tr").filter(has_text="@example.org").first
    row.locator("button").last.click()
    item = page.get_by_role("menuitem", name="Reset password")
    item.wait_for()
    Portal.highlight(item)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), page.get_by_role("menu"), full_width=True
    )


# --- registrations -----------------------------------------------------------------


def registrations_page(portal: Portal) -> Page:
    """Full registrations page."""
    return full_height(registrations(portal))


def import_button(portal: Portal) -> Page:
    """Registrations page with the Import button highlighted."""
    page = registrations_page(portal)
    Portal.highlight(page.get_by_role("button", name="Import"))
    return page


def import_dialog(portal: Portal) -> Page:
    """Import new registrations dialog."""
    page = registrations(portal)
    page.get_by_role("button", name="Import").click()
    page.get_by_role("menuitem", name="Import new registrations").click()
    page.get_by_role("button", name="Download the template").wait_for()
    return page


def clear_filters(portal: Portal) -> Page:
    """Registrations filtered on New, with 'Clear filters' highlighted."""
    page = registrations(portal)
    filter_status(page, "New")
    page.get_by_role("heading", name="Registrations", level=1).click()
    page.get_by_role("dialog").wait_for(state="hidden")
    unfocus(page)
    button = Portal.table(page).get_by_role("button", name="Clear filters")
    button.wait_for()
    Portal.highlight(button)
    return page


def status_filter_new(portal: Portal) -> Page:
    """Registration status filter open with New selected."""
    page = registrations(portal)
    filter_status(page, "New")
    return page


def search_registration(portal: Portal) -> Locator:
    """Name column filter open with a registration name typed in."""
    page = registrations(portal)
    Portal.column_filter_button(page, "Name").click()
    dialog = page.get_by_role("dialog").filter(visible=True)
    dialog.get_by_role("textbox").fill(INCLUDED)
    page.mouse.move(640, 600)
    page.wait_for_timeout(400)
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), dialog, full_width=True)


def row_menu(portal: Portal) -> Locator:
    """Right-click menu on the first registration row."""
    page = registrations(portal)
    Portal.table(page).locator("tbody tr").first.click(button="right")
    page.get_by_role("menuitem", name="Pause").wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), page.get_by_role("menu"), full_width=True
    )


def pause_dialog(portal: Portal) -> Locator:
    """Pause registration dialog for an included registration."""
    page = registrations(portal)
    search(page, INCLUDED)
    select_row(page, INCLUDED)
    page.get_by_role("button", name="Pause").click()
    return open_dialog(page, "Pause registration")


def paused_status(portal: Portal) -> Locator:
    """Registrations table showing a registration with status Paused."""
    page = registrations(portal)
    search(page, PAUSED)
    unfocus(page)
    return Portal.clip_around(
        page.get_by_role("heading", name="Registrations", level=1),
        page.get_by_role("button", name="Delete").first,
        page.get_by_text("Showing 1 to 1 of 1 records"),
        padding=24,
    )


def decline_dialog(portal: Portal) -> Locator:
    """Decline registration dialog."""
    page = registrations(portal)
    select_row(page, TO_DECLINE)
    page.get_by_role("button", name="Decline").click()
    return open_dialog(page, "Decline registration")


def personal_information_tab(portal: Portal, name: str) -> Page:
    """Open the Personal information tab of registration `name`."""
    page = registration(portal, name)
    page.get_by_role("tab", name="Personal information").click()
    page.get_by_role("button", name="Edit information").wait_for()
    return page


def registration_details(page: Page) -> Locator:
    """Return a clip from the breadcrumb down to the registration details card."""
    full_height(page)
    card = page.locator("p-card").filter(has=page.get_by_test_id("registration-menu"))
    return Portal.clip_around(
        page.get_by_role("link", name="All Registrations"), card, full_width=True
    )


def personal_information(portal: Portal) -> Locator:
    """Registration page on the Personal information tab."""
    return registration_details(personal_information_tab(portal, UNIQUE))


def update_information_dialog(portal: Portal) -> Locator:
    """Update information dialog that asks for a reason after editing a field."""
    page = personal_information_tab(portal, UNIQUE)
    page.get_by_role("button", name="Edit information").click()
    page.get_by_label("village").fill("Sarville")
    page.get_by_role("button", name="Save").click()
    submit = page.get_by_test_id("form-dialog-submit-button")
    submit.wait_for()
    page.wait_for_timeout(400)
    dialog = page.locator("[role=dialog], [role=alertdialog]").filter(has=submit)
    return Portal.clip_around(dialog, padding=48)


def edit_duplicate(portal: Portal) -> Locator:
    """Duplicate registration with personal information in edit mode."""
    page = full_height(personal_information_tab(portal, DUPLICATE))
    page.get_by_role("button", name="Edit information").click()
    page.get_by_role("button", name="Save").wait_for()
    unfocus(page)
    # First visible select is the FSP field in the second form row.
    return Portal.clip_around(
        page.get_by_role("link", name="All Registrations"),
        page.locator("p-select").filter(visible=True).first,
        full_width=True,
    )


def manage_table(portal: Portal) -> Page:
    """Manage table sidebar open on the registrations page."""
    page = registrations(portal)
    page.get_by_title("Manage table").click()
    page.get_by_role("complementary").get_by_role("checkbox").first.wait_for()
    return page


def filter_duplicates(portal: Portal) -> Page:
    """Duplicates column filter open with Duplicate selected."""
    page = registrations(portal)
    Portal.column_filter_button(page, "Duplicates").click()
    page.get_by_text("Choose option(s)").click()
    page.get_by_role("option", name="Duplicate", exact=True).click()
    page.get_by_text("Showing 1 to 2 of 2 records").wait_for()
    return page


def duplicate_actions(portal: Portal) -> Locator:
    """Duplicate registration page with the Actions menu open."""
    page = full_height(registration(portal, DUPLICATE))
    page.get_by_role("button", name="Actions").click()
    page.get_by_role("menuitem", name="Ignore duplication").wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(
        page.get_by_role("link", name="All Registrations"),
        page.get_by_role("menu"),
        full_width=True,
    )


def mass_update_button(portal: Portal) -> Page:
    """Import menu with 'Update selected registrations' for one selected registration."""
    page = registrations(portal)
    search(page, NEW)
    select_row(page, NEW)
    page.get_by_role("button", name="Import").click()
    page.get_by_role("menuitem", name="Update selected registrations").hover()
    page.get_by_text("(1 selected)").wait_for()
    return page


def mass_update_dialog(portal: Portal) -> Locator:
    """Update selected registrations dialog with the column picker open."""
    page = mass_update_button(portal)
    page.get_by_role("menuitem", name="Update selected registrations").click()
    dialog = page.get_by_role("dialog").filter(has_text="Update selected registrations")
    dialog.get_by_text("Select 1 or more columns").click()
    page.get_by_role("searchbox").fill("")
    page.get_by_role("option", name="Name", exact=True).click()
    page.wait_for_timeout(400)
    return Portal.clip_around(dialog, page.get_by_role("listbox"))


# --- monitoring ----------------------------------------------------------------------


def monitoring(portal: Portal) -> Page:
    """Open the monitoring dashboard and wait for its metrics."""
    page = portal.open("program:/monitoring/dashboard")
    page.get_by_test_id("metric-people-registered").wait_for()
    return page


def tabs_card(page: Page) -> Locator:
    """Return the card with the monitoring tabs and their content."""
    return page.locator("p-card").filter(has=page.get_by_test_id("monitoring-menu"))


def dashboard_charts(portal: Portal) -> Page:
    """Open the monitoring dashboard at full height and wait for the charts."""
    page = full_height(monitoring(portal))
    page.locator("p-chart canvas").first.wait_for()
    page.wait_for_timeout(1000)
    return page


def monitoring_page(portal: Portal) -> Locator:
    """Monitoring page down to the first row of charts."""
    page = dashboard_charts(portal)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), page.locator("p-chart").first, full_width=True
    )


def dashboard(portal: Portal) -> Locator:
    """Monitoring Dashboard tab with all charts, 1920px wide."""
    page = dashboard_charts(portal)
    # At 1280px the five-status payment legends wrap and squash the payment charts.
    page.set_viewport_size({"width": 1920, "height": page.viewport_size["height"]})
    page.wait_for_timeout(1000)
    page.set_viewport_size(
        {"width": 1920, "height": page.evaluate("document.documentElement.scrollHeight")}
    )
    page.wait_for_timeout(1000)
    return Portal.clip_around(tabs_card(page))


def monitoring_tab(tab: str) -> Callable[[Portal], Page]:
    """Return a prepare function that opens monitoring tab `tab` at full height."""

    def prepare(portal: Portal) -> Page:
        page = monitoring(portal)
        page.get_by_test_id("monitoring-menu").get_by_role("tab", name=tab).click()
        page.wait_for_url("**/monitoring/" + tab.lower().replace(" ", "-"))
        page.wait_for_load_state("networkidle")
        portal.wait_for_table(page)
        return full_height(page)

    return prepare


def monitoring_tab_card(tab: str) -> Callable[[Portal], Locator]:
    """Return a prepare function that clips monitoring tab `tab` to its card."""
    return lambda portal: Portal.clip_around(tabs_card(monitoring_tab(tab)(portal)))


def upload_file_dialog(portal: Portal) -> Locator:
    """Upload file dialog with a file chosen and named (upload blocked).

    Raises:
        LookupError: If 'Import file' stays disabled after choosing the file.
    """
    page = monitoring_tab("Files")(portal)
    block_writes(page)
    page.get_by_role("button", name="Upload file").click()
    dialog = page.get_by_role("dialog").filter(has_text="Upload file")
    dialog.wait_for()
    page.wait_for_timeout(800)
    dialog.locator("input[type=file]").first.set_input_files(
        {
            "name": "distribution-plan.pdf",
            "mimeType": "application/pdf",
            "buffer": b"%PDF-1.4\n%%EOF\n",
        }
    )
    dialog.get_by_placeholder("Name the file for easy identification").fill("Distribution plan")
    unfocus(page)
    page.wait_for_timeout(400)
    if not dialog.get_by_role("button", name="Import file").is_enabled():
        raise LookupError("'Import file' is still disabled after choosing a file")
    return Portal.clip_around(dialog)


def attachment_menu(portal: Portal) -> Locator:
    """Files tab with the row menu of an attachment open."""
    page = monitoring_tab("Files")(portal)
    # Extra height moves the footer away from the open menu.
    page.set_viewport_size({"width": 1280, "height": page.viewport_size["height"] + 150})
    Portal.table(page).locator("tbody tr").first.locator("button").last.click()
    page.get_by_role("menuitem").first.wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(tabs_card(page), page.get_by_role("menu"))


# --- payments ----------------------------------------------------------------------


def payments_page(portal: Portal) -> Locator:
    """Payments overview with the payment cards."""
    page = payments(portal)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"),
        page.get_by_test_id("card-with-link").last,
        full_width=True,
    )


def create_payment_select(portal: Portal) -> Page:
    """Create payment, step where registrations are selected."""
    page = payments(portal)
    page.get_by_role("button", name="Create new payment").click()
    page.get_by_role("button", name="Continue to registration").click()
    portal.wait_for_table(page)
    unfocus(page)
    return page


def create_payment_summary(portal: Portal) -> Page:
    """Create payment, summary step before 'Create payment'."""
    page = create_payment_select(portal)
    Portal.table(page).get_by_role("checkbox", name="All items unselected").click()
    page.get_by_role("button", name="Add to payment").click()
    page.get_by_role("button", name="Create payment").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return page


def approve_dialog(portal: Portal) -> Locator:
    """Approve payment dialog, opened as the approver account.

    Raises:
        LookupError: If the approver credentials are not set.
    """
    username, password = (
        os.environ.get("APPROVER_USERNAME_121"),
        os.environ.get("APPROVER_PASSWORD_121"),
    )
    if not (username and password):
        raise LookupError(
            "set APPROVER_USERNAME_121/APPROVER_PASSWORD_121 to open the page as the approver"
        )
    ctx = portal.ctx.browser.new_context(
        viewport={"width": 1280, "height": 720}, locale="en-GB", timezone_id="Europe/Amsterdam"
    )
    ctx.set_default_timeout(15_000)
    approver = Portal(ctx, portal.portal_url, portal.api_url)
    approver.program_id = portal.program_id
    approver.login(username, password)
    page = approver.open(f"program:/payments/{payment_id(portal, 'pending')}")
    block_writes(page)
    page.get_by_role("button", name="Approve payment").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button", name="Approve payment").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24)


def start_payment_button(portal: Portal) -> Page:
    """Approved payment with 'Start payment' highlighted."""
    page = portal.open(f"program:/payments/{payment_id(portal, 'approved')}")
    block_writes(page)
    button = page.get_by_role("button", name="Start payment")
    button.wait_for()
    page.wait_for_timeout(1000)
    unfocus(page)
    Portal.highlight(button)
    return page


def payment_page(portal: Portal, state: str = "reconciled") -> Locator:
    """Payment page in `state` down to the transactions table."""
    page = full_height(started_payment(portal, state))
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), transactions_card(page), full_width=True
    )


def payment_export_menu(portal: Portal) -> Locator:
    """Payment page with the Export menu open."""
    page = started_payment(portal)
    page.get_by_role("button", name="Export").click()
    page.get_by_role("menuitem", name="Payment report").wait_for()
    page.wait_for_timeout(400)
    charts = page.locator("p-card").filter(has_text="Transactions data")
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), charts, full_width=True)


def reconciliation_dialog(portal: Portal) -> Locator:
    """Import reconciliation data dialog."""
    page = started_payment(portal)
    page.get_by_role("button", name="Import reconciliation data").click()
    dialog = page.get_by_role("dialog").filter(has_text="Import reconciliation data")
    dialog.get_by_role("button", name="Download the template").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24, full_width=True)


def payments_export_dialog(portal: Portal) -> Locator:
    """Export payments dialog on the payments overview."""
    page = payments(portal)
    page.get_by_role("button", name="Export").click()
    page.get_by_role("menuitem", name="Payments").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button", name="Proceed").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24)


def failed_status(portal: Portal) -> Locator:
    """Transactions filtered on Failed, with the failure reason highlighted."""
    page = started_payment(portal)
    filter_failed(page)
    page.get_by_role("heading", level=1).click()
    page.get_by_role("dialog").filter(visible=True).wait_for(state="hidden")
    unfocus(page)
    table = Portal.table(page)
    headers = table.locator("thead th").all_inner_texts()
    reason = next(i for i, h in enumerate(headers) if h.strip().startswith("Reason"))
    Portal.highlight(table.locator("tbody tr").first.locator("td").nth(reason))
    return Portal.clip_around(transactions_card(page), full_width=True)


def retry_button(page: Page) -> Locator:
    """Return the 'Retry failed transaction(s)' button."""
    return page.get_by_role("button", name=re.compile("Retry failed"))


def select_failed(portal: Portal) -> Page:
    """Open a payment with its failed transaction filtered and selected."""
    page = started_payment(portal)
    filter_failed(page)
    page.get_by_role("heading", level=1).click()
    page.get_by_role("dialog").filter(visible=True).wait_for(state="hidden")
    Portal.table(page).locator("tbody").get_by_role("checkbox").first.click()
    unfocus(page)
    return page


def retry_failed_button(portal: Portal) -> Locator:
    """Failed transaction selected, with the retry button highlighted."""
    page = select_failed(portal)
    Portal.highlight(retry_button(page))
    return Portal.clip_around(transactions_card(page), full_width=True)


def retry_failed_confirm(portal: Portal) -> Locator:
    """Retry failed transactions confirmation dialog."""
    page = select_failed(portal)
    retry_button(page).click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button").last.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(transactions_card(page), dialog, full_width=True)


# --- settings ----------------------------------------------------------------------


def settings(path: str) -> Callable[[Portal], Page]:
    """Return a prepare function that opens program settings page `path` (writes blocked)."""

    def prepare(portal: Portal) -> Page:
        page = portal.open(f"program:/settings/{path}")
        block_writes(page)
        page.get_by_role("heading", name="Program settings").wait_for()
        return page

    return prepare


def card(page: Page, title: str) -> Locator:
    """Return the first card that contains `title`."""
    return page.locator("p-card").filter(has_text=title).first


def pick(page: Page, field: Locator, option: str | None = None) -> None:
    """Open a dropdown and click the option containing `option` (or the first one)."""
    field.click()
    options = page.get_by_role("option")
    (options.filter(has_text=option) if option else options).first.click()


def basic_information(portal: Portal) -> Locator:
    """Basic information card in the program settings."""
    page = settings("information")(portal)
    return Portal.clip_around(card(page, "Basic information"))


def edit_basic_information(portal: Portal) -> Locator:
    """Basic information card in edit mode."""
    page = settings("information")(portal)
    page.get_by_role("button", name="Edit basic information").click()
    page.get_by_role("button", name="Save").wait_for()
    full_height(page)
    return Portal.clip_around(card(page, "Basic information"))


def fsps(portal: Portal) -> Page:
    """Open the FSP integration settings page."""
    page = settings("fsps")(portal)
    page.locator("p-accordion-header").first.wait_for()
    return page


def expand_form_requirements(page: Page) -> None:
    """Expand the form requirements of the first FSP."""
    header = page.locator("p-accordion-header").first
    header.click()
    page.locator("p-accordion-header[aria-expanded=true]").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)


def fsp_required_fields(portal: Portal) -> Locator:
    """FSP card with the form requirements chevron highlighted."""
    page = fsps(portal)
    Portal.highlight(
        page.locator("p-accordion-header [data-pc-section=toggleicon]").first, padding=8
    )
    return Portal.clip_around(card(page, "Financial Service Providers"))


def fsp_required_fields_expanded(portal: Portal) -> Locator:
    """FSP form requirements expanded, with the data column names highlighted."""
    page = fsps(portal)
    expand_form_requirements(page)
    column = card(page, "Financial Service Providers").locator("tr > :nth-child(2)")
    Portal.highlight(Portal.clip_around(column.first, column.last, padding=0))
    return Portal.clip_around(card(page, "Financial Service Providers"))


def fsp_reconfigure(portal: Portal) -> Page:
    """FSP menu open, with Settings, FSP integration and 'Reconfigure' highlighted."""
    page = fsps(portal)
    expand_form_requirements(page)
    card(page, "Financial Service Providers").locator("button").first.click()
    item = page.get_by_role("menuitem", name="Reconfigure")
    item.wait_for()
    page.wait_for_timeout(400)
    for target in (
        page.get_by_role("tab", name="Settings"),
        page.get_by_role("link", name="FSP integration"),
        item,
    ):
        Portal.highlight(target)
    return page


def link_kobo_dialog(portal: Portal) -> Locator:
    """Link with KoboToolbox dialog on the registration data page."""
    page = settings("registration-data")(portal)
    page.get_by_test_id("kobo-integration-card").locator("a").first.click()
    dialog = page.get_by_role("alertdialog").filter(has_text="Link with KoboToolbox")
    dialog.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(card(page, "Registration integration"), dialog)


def add_user_to_team(portal: Portal) -> Locator:
    """Add user to team dialog filled in, with 'Add to team' highlighted."""
    page = settings("users/team")(portal)
    page.get_by_role("button", name="Add user to team").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    pick(page, dialog.locator("p-select").first, "cva-manager@example.org")
    pick(page, dialog.locator("p-multiselect").first, "Manager")
    dialog.get_by_text("Choose a user from the dropdown").click()
    page.get_by_role("listbox").wait_for(state="hidden")
    unfocus(page)
    Portal.highlight(dialog.get_by_role("button", name="Add to team"))
    return Portal.clip_around(dialog)


def team_row(page: Page) -> Locator:
    """Return the program team row of the seeded extra team member."""
    return Portal.table(page).locator("tbody tr").filter(has_text=TEAM_MEMBER[0])


def team_row_menu(portal: Portal) -> Page:
    """Open the program team page with the extra team member's row menu open."""
    page = settings("users/team")(portal)
    portal.wait_for_table(page)
    team_row(page).locator("button").last.click()
    page.get_by_role("menuitem").first.wait_for()
    page.wait_for_timeout(400)
    return page


def team_remove(portal: Portal) -> Locator:
    """Program team row menu with 'Remove user' highlighted."""
    page = team_row_menu(portal)
    Portal.highlight(team_row(page).locator("button").last)
    Portal.highlight(page.get_by_role("menuitem", name="Remove user"))
    return Portal.clip_around(card(page, "Program team"), page.get_by_role("menu"))


def team_edit(portal: Portal) -> Locator:
    """Edit team member dialog with the roles field and 'Save changes' highlighted."""
    page = team_row_menu(portal)
    page.get_by_role("menuitem", name="Edit").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    button = dialog.get_by_role("button", name="Save changes")
    button.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    Portal.highlight(dialog.locator("p-multiselect").first)
    Portal.highlight(button)
    return Portal.clip_around(dialog)


def edit_payment_approval(portal: Portal) -> tuple[Page, Locator]:
    """Open the payment approval settings in edit mode; return the page and the card."""
    page = settings("users/payment-approval")(portal)
    page.get_by_role("button", name="Edit payment approval settings").click()
    approval = card(page, "Payment approval")
    approval.locator("p-multiselect").first.wait_for()
    return page, approval


def payment_approval_users(portal: Portal) -> Locator:
    """First approval step with the user list open and the selected user highlighted."""
    page, approval = edit_payment_approval(portal)
    approval.locator("p-multiselect").first.click()
    listbox = page.get_by_role("listbox")
    option = listbox.get_by_role("option", selected=True).first
    option.wait_for()
    page.mouse.move(1270, 10)
    page.wait_for_timeout(400)
    Portal.highlight(option)
    return Portal.clip_around(approval, listbox)


def payment_approval_steps(page: Page, approval: Locator) -> Locator:
    """Add a second approval step with a user and amount; return its delete button."""
    approval.get_by_role("button", name="Add approval step").click()
    first_step = approval.locator("p-multiselect").first.inner_text().strip()
    approval.get_by_text("Select 1 or more users from your program team").click()
    options = page.get_by_role("listbox").get_by_role("option", selected=False)
    options.filter(has_not_text=first_step).first.click()
    approval.get_by_text("Payment approval", exact=True).click()
    page.get_by_role("listbox").wait_for(state="hidden")
    approval.get_by_role("spinbutton").last.fill("1000")
    unfocus(page)
    page.wait_for_timeout(400)
    return approval.locator("button").filter(has_not_text=re.compile(r"\w")).last


def payment_approval_step(portal: Portal) -> Locator:
    """Payment approval with a second step, highlighted."""
    page, approval = edit_payment_approval(portal)
    delete = payment_approval_steps(page, approval)
    Portal.highlight(
        Portal.clip_around(
            approval.get_by_text("Select users for this approval step"), delete, padding=6
        )
    )
    return Portal.clip_around(approval)


def payment_approval_delete_step(portal: Portal) -> Locator:
    """Payment approval with a second step and its delete button highlighted."""
    page, approval = edit_payment_approval(portal)
    Portal.highlight(payment_approval_steps(page, approval))
    return Portal.clip_around(approval)


SCENARIOS = [
    # general
    Scenario("LoginPage.png", "Login page with language dropdown open", login_page),
    Scenario(
        "ChangeLanguage.png",
        "Sidebar with language dropdown open",
        sidebar_language,
        (0, 0, 728, 720),
    ),
    Scenario("AccountUser.png", "Account menu open", account_menu, (844, 0, 436, 352)),
    Scenario("ChangePassword.png", "Change password page", change_password, (0, 0, 672, 520)),
    # users
    Scenario("UserMenu.png", "Sidebar open on the users page", user_menu),
    Scenario("AddUser.png", "Users page, 'Add new user' highlighted", add_user_button, top(609)),
    Scenario("AddingNewUser.png", "Add new user dialog", add_user_dialog),
    Scenario(
        "ResetPasswordUser.png", "User row menu, 'Reset password' highlighted", reset_password
    ),
    # registrations
    Scenario("RegistrationsPage.png", "Registrations page", registrations_page),
    Scenario(
        "RegistrationsPageImport.png", "Registrations page, 'Import' highlighted", import_button
    ),
    Scenario("ImportRegistrationTemplate.png", "Import new registrations dialog", import_dialog),
    Scenario(
        "ClearFilterButton.png",
        "Filtered table, 'Clear filters' highlighted",
        clear_filters,
        top(540),
    ),
    Scenario(
        "RegisteredStatusFilter.png",
        "Status column filter with 'New' selected",
        status_filter_new,
        top(570),
    ),
    Scenario("SearchReg.png", "Name column filter with a name typed in", search_registration),
    Scenario("RegistationsStatusRighList.png", "Right-click menu on a registration row", row_menu),
    Scenario("PausePANotification.png", "Pause registration dialog", pause_dialog),
    Scenario("PauseStatus.png", "Registration with status Paused", paused_status),
    Scenario("RegistrationDeclined.png", "Decline registration(s) dialog", decline_dialog),
    Scenario(
        "PersonalInformationPA.png",
        "Registration page, Personal information tab",
        personal_information,
    ),
    Scenario(
        "UpdateInformationPopUp.png",
        "Reason dialog after editing personal information",
        update_information_dialog,
    ),
    Scenario(
        "EditInformationDuplicate.png",
        "Editing personal information of a duplicate",
        edit_duplicate,
    ),
    Scenario("ShowDuplicateColumn.png", "Manage table sidebar", manage_table, (498, 0, 782, 720)),
    Scenario("FilterDuplicate.png", "Duplicates column filter", filter_duplicates, top(520)),
    Scenario(
        "DeclineIgnoreDuplicate.png",
        "Duplicate registration with Actions menu open",
        duplicate_actions,
    ),
    Scenario(
        "MassUpdateButton.png",
        "Import menu with 'Update selected registrations'",
        mass_update_button,
        top(420),
    ),
    Scenario("MassUpdateWindow.png", "Update selected registrations dialog", mass_update_dialog),
    # monitoring
    Scenario("MonitoringPage.png", "Monitoring page with the first row of charts", monitoring_page),
    Scenario("Dashboard.png", "Monitoring, Dashboard tab with charts", dashboard),
    Scenario(
        "DataChangestab.png", "Monitoring, Data changes tab", monitoring_tab_card("Data changes")
    ),
    Scenario("MonitoringPageFilestab.png", "Monitoring, Files tab", monitoring_tab_card("Files")),
    Scenario("UploadFilesInfo.png", "Upload file dialog", upload_file_dialog),
    Scenario("RenameDeleteAttachment.png", "Attachment row menu", attachment_menu),
    # payments
    Scenario("PaymentsPage.png", "Payments page with payment cards", payments_page),
    Scenario(
        "CreateNewpaymentSelect.png",
        "Create payment, registration selection",
        create_payment_select,
    ),
    Scenario("StartPayment.png", "Create payment summary", create_payment_summary),
    Scenario("ApprovePaymentFinal.png", "Approve payment dialog (as the approver)", approve_dialog),
    Scenario(
        "StartPaymentApproved.png",
        "Approved payment, 'Start payment' highlighted",
        start_payment_button,
        top(424),
    ),
    Scenario("PaymentReportBoard.png", "Payment page with transaction list", payment_page),
    Scenario(
        "PendingStatusExcel.png",
        "Started Excel payment waiting for reconciliation",
        lambda portal: payment_page(portal, "processing"),
    ),
    Scenario("IndividualExportReport.png", "Payment page, Export menu", payment_export_menu),
    Scenario(
        "ReconciliationImport.png", "Import reconciliation data dialog", reconciliation_dialog
    ),
    Scenario("ApprovePaymentExport.png", "Payments export dialog", payments_export_dialog),
    Scenario(
        "FailedPaymentstatus.png",
        "Transactions filtered on 'Failed', reason highlighted",
        failed_status,
    ),
    Scenario(
        "RetryPaiementbutton.png",
        "Failed transaction selected, 'Retry failed' highlighted",
        retry_failed_button,
    ),
    Scenario("RetryPaymentConfirm.png", "Retry failed transactions dialog", retry_failed_confirm),
    # settings
    Scenario(
        "settings-programinformation-updatebasicinformation.png",
        "Basic information card",
        basic_information,
    ),
    Scenario(
        "settings-programinformation-updatebasicinformation2.png",
        "Basic information in edit mode",
        edit_basic_information,
    ),
    Scenario(
        "settings-fspintegration-requiredfields.png",
        "FSP card, 'Form requirements' chevron highlighted",
        fsp_required_fields,
    ),
    Scenario(
        "settings-fspintegration-requiredfields2.png",
        "FSP form requirements expanded",
        fsp_required_fields_expanded,
    ),
    Scenario(
        "settings-fspintegration-reconfigure2.png",
        "FSP menu, 'Reconfigure' highlighted",
        fsp_reconfigure,
    ),
    Scenario("settings-registrationdata4.png", "Link with KoboToolbox dialog", link_kobo_dialog),
    Scenario("settings-programteampng.png", "Add user to team dialog", add_user_to_team),
    Scenario(
        "settings-programteamremove.png",
        "Program team row menu, 'Remove user' highlighted",
        team_remove,
    ),
    Scenario("settings-programteameditpng.png", "Edit user dialog", team_edit),
    Scenario(
        "settings-paymentapproval1.png",
        "Payment approval, first step users",
        payment_approval_users,
    ),
    Scenario(
        "settings-paymentapproval2.png",
        "Payment approval with a second step",
        payment_approval_step,
    ),
    Scenario(
        "settings-paymentapproval3.png",
        "Payment approval, delete step highlighted",
        payment_approval_delete_step,
    ),
]
