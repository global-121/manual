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
from .seed import PEOPLE


@dataclass
class Scenario:
    name: str
    shows: str
    prepare: Callable[[Portal], Page | Locator]
    clip: tuple[int, int, int, int] | None = None  # x, y, width, height in CSS px


def top(height: int) -> tuple[int, int, int, int]:
    return (0, 0, 1280, height)


INCLUDED = next(p[0] for p in PEOPLE if p[4] == "included")
PAUSED = next(p[0] for p in PEOPLE if p[4] == "paused")
TO_DECLINE = "Lara Schmitt"
NEW = next(p[0] for p in PEOPLE if p[4] == "new")
DUPLICATE = "Nadia Rahman"
UNIQUE = "Lara Schmitt"


# --- helpers -------------------------------------------------------------------


def block_writes(page: Page, dry_run: bool = False) -> None:
    page.route(
        "**/api/**",
        lambda r: r.continue_()
        if r.request.method == "GET" or (dry_run and "dryRun=true" in r.request.url)
        else r.abort(),
    )


def registrations(portal: Portal) -> Page:
    page = portal.open("program:/registrations")
    reset_table(portal, page)
    return page


def reset_table(portal: Portal, page: Page) -> Locator:
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
    reg = next((r for r in portal.registrations() if r.get("fullName") == name), None)
    if reg is None:
        raise LookupError(f"registration '{name}' not found (run with --seed)")
    page = portal.open(f"program:/registrations/{reg['id']}")
    page.get_by_role("tab", name="Activity log").wait_for()
    return page


def filter_status(page: Page, status: str) -> None:
    Portal.column_filter_button(page, "Registration Status").click()
    page.get_by_text("Choose option(s)").click()
    page.get_by_role("option", name=status, exact=True).click()


def search(page: Page, text: str) -> None:
    table = Portal.table(page)
    table.get_by_title("Filter by keyword").click()
    table.get_by_placeholder("Filter by keyword").fill(text)
    page.wait_for_timeout(800)
    page.wait_for_load_state("networkidle")


def select_row(page: Page, name: str) -> None:
    Portal.row(page, name).get_by_role("checkbox").first.click()


def unfocus(page: Page) -> None:
    page.evaluate("document.activeElement.blur()")
    page.mouse.move(640, 180)


def full_height(page: Page) -> Page:
    unfocus(page)
    page.set_viewport_size({"width": 1280, "height": page.evaluate("document.documentElement.scrollHeight")})
    return page


def open_dialog(page: Page, title: str) -> Locator:
    dialog = page.get_by_role("dialog").filter(has_text=title)
    dialog.get_by_role("switch").wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(dialog)


def payment_ids(portal: Portal) -> list[int]:
    ids = sorted(p["paymentId"] for p in portal.api("GET", "program:/payments"))
    if len(ids) < 2:
        raise LookupError("demo program needs a started and a pending payment (seed needs an approver, see README)")
    return ids


def payments(portal: Portal) -> Page:
    payment_ids(portal)
    page = portal.open("program:/payments")
    block_writes(page, dry_run=True)
    page.get_by_test_id("card-with-link").last.wait_for()
    return page


def started_payment(portal: Portal) -> Page:
    page = portal.open(f"program:/payments/{payment_ids(portal)[0]}")
    block_writes(page)
    reset_table(portal, page)
    page.wait_for_timeout(1000)
    return page


def transactions_card(page: Page) -> Locator:
    return page.locator("p-card").filter(has=page.get_by_test_id("query-table"))


def filter_failed(page: Page) -> None:
    full_height(page)
    Portal.column_filter_button(page, "Transaction status").click()
    page.get_by_role("dialog").filter(visible=True).get_by_text("Choose option(s)").click()
    page.get_by_role("option", name="Failed", exact=True).click()
    page.get_by_text("Showing 1 to 1 of 1 records").wait_for()
    page.wait_for_timeout(400)


# --- general ---------------------------------------------------------------------


def login_page(portal: Portal) -> Page:
    ctx = portal.ctx.browser.new_context(viewport={"width": 1280, "height": 720}, locale="en-GB")
    page = ctx.new_page()
    page.goto(f"{portal.portal_url}/{LOCALE}/login")
    page.get_by_label("E-mail").wait_for()
    page.evaluate("['blur', 'focusout'].forEach(t => window.addEventListener(t, e => e.stopImmediatePropagation(), true))")
    page.get_by_test_id("locale-dropdown").click()
    page.get_by_role("option", name="Français").wait_for()
    return page


def sidebar_language(portal: Portal) -> Page:
    page = portal.open("/programs")
    page.get_by_test_id("sidebar-toggle").get_by_role("button", name="Menu").click()
    page.get_by_test_id("locale-dropdown").click()
    page.get_by_role("option").first.wait_for()
    return page


def account_menu(portal: Portal) -> Page:
    page = portal.open("/programs")
    page.get_by_role("button", name="Account").click()
    page.get_by_role("menuitem", name="Change password").wait_for()
    return page


def change_password(portal: Portal) -> Page:
    page = portal.open("/change-password")
    page.get_by_label("Current Password").wait_for()
    return page


# --- users -----------------------------------------------------------------------


def users(portal: Portal) -> Page:
    page = portal.open("/users")
    portal.wait_for_table(page)
    return page


def user_menu(portal: Portal) -> Page:
    page = users(portal)
    page.get_by_test_id("sidebar-toggle").get_by_role("button", name="Menu").click()
    page.get_by_test_id("sidebar").get_by_role("link", name="Users").wait_for()
    return page


def add_user_button(portal: Portal) -> Page:
    page = users(portal)
    Portal.highlight(page.get_by_role("button", name="Add new user"))
    return page


def add_user_dialog(portal: Portal) -> Locator:
    page = users(portal)
    page.get_by_role("button", name="Add new user").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_label("Full name").fill("FirstName LastName")
    dialog.get_by_label("E-mail").fill("username@example.org")
    page.evaluate("document.activeElement.blur()")
    return Portal.clip_around(dialog)


def reset_password(portal: Portal) -> Locator:
    page = users(portal)
    row = Portal.table(page).locator("tbody tr").filter(has_text="@example.org").first
    row.locator("button").last.click()
    item = page.get_by_role("menuitem", name="Reset password")
    item.wait_for()
    Portal.highlight(item)
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), page.get_by_role("menu"), full_width=True)


# --- registrations -----------------------------------------------------------------


def registrations_page(portal: Portal) -> Page:
    return full_height(registrations(portal))


def import_button(portal: Portal) -> Page:
    page = registrations_page(portal)
    Portal.highlight(page.get_by_role("button", name="Import"))
    return page


def import_dialog(portal: Portal) -> Page:
    page = registrations(portal)
    page.get_by_role("button", name="Import").click()
    page.get_by_role("menuitem", name="Import new registrations").click()
    page.get_by_role("button", name="Download the template").wait_for()
    return page


def clear_filters(portal: Portal) -> Page:
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
    page = registrations(portal)
    filter_status(page, "New")
    return page


def search_registration(portal: Portal) -> Page:
    page = registrations(portal)
    Portal.column_filter_button(page, "Name").click()
    dialog = page.get_by_role("dialog").filter(visible=True)
    dialog.get_by_role("textbox").fill(INCLUDED)
    dialog.get_by_role("button", name="Apply").click()
    dialog.wait_for(state="hidden")
    page.get_by_text("Showing 1 to 1 of 1 records").wait_for()
    unfocus(page)
    return page


def row_menu(portal: Portal) -> Locator:
    page = registrations(portal)
    Portal.row(page, INCLUDED).click(button="right")
    item = page.get_by_role("menuitem", name="Pause")
    item.wait_for()
    page.wait_for_timeout(400)
    Portal.highlight(item)
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), page.get_by_role("menu"), full_width=True)


def pause_dialog(portal: Portal) -> Locator:
    page = registrations(portal)
    search(page, INCLUDED)
    select_row(page, INCLUDED)
    page.get_by_role("button", name="Pause").click()
    return open_dialog(page, "Pause registration")


def paused_status(portal: Portal) -> Page:
    page = registrations(portal)
    search(page, PAUSED)
    unfocus(page)
    return page


def decline_dialog(portal: Portal) -> Locator:
    page = registrations(portal)
    select_row(page, TO_DECLINE)
    page.get_by_role("button", name="Decline").click()
    return open_dialog(page, "Decline registration")


def personal_information_tab(portal: Portal, name: str) -> Page:
    page = registration(portal, name)
    page.get_by_role("tab", name="Personal information").click()
    page.get_by_role("button", name="Edit information").wait_for()
    return page


def registration_details(page: Page) -> Locator:
    full_height(page)
    card = page.locator("p-card").filter(has=page.get_by_test_id("registration-menu"))
    return Portal.clip_around(page.get_by_role("link", name="All Registrations"), card, full_width=True)


def personal_information(portal: Portal) -> Locator:
    return registration_details(personal_information_tab(portal, UNIQUE))


def update_information_dialog(portal: Portal) -> Page:
    page = personal_information_tab(portal, UNIQUE)
    page.get_by_role("button", name="Edit information").click()
    page.get_by_label("village").fill("Sarville")
    page.get_by_role("button", name="Save").click()
    page.get_by_test_id("form-dialog-submit-button").wait_for()
    return page


def edit_duplicate(portal: Portal) -> Locator:
    page = personal_information_tab(portal, DUPLICATE)
    page.get_by_role("button", name="Edit information").click()
    page.get_by_role("button", name="Save").wait_for()
    return registration_details(page)


def manage_table(portal: Portal) -> Page:
    page = registrations(portal)
    page.get_by_title("Manage table").click()
    page.get_by_role("complementary").get_by_role("checkbox").first.wait_for()
    return page


def filter_duplicates(portal: Portal) -> Page:
    page = registrations(portal)
    Portal.column_filter_button(page, "Duplicates").click()
    page.get_by_text("Choose option(s)").click()
    page.get_by_role("option", name="Duplicate", exact=True).click()
    page.get_by_text("Showing 1 to 2 of 2 records").wait_for()
    return page


def duplicate_actions(portal: Portal) -> Locator:
    page = full_height(registration(portal, DUPLICATE))
    page.get_by_role("button", name="Actions").click()
    page.get_by_role("menuitem", name="Ignore duplication").wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(
        page.get_by_role("link", name="All Registrations"), page.get_by_role("menu"), full_width=True
    )


def mass_update_button(portal: Portal) -> Page:
    page = registrations(portal)
    search(page, NEW)
    select_row(page, NEW)
    page.get_by_role("button", name="Import").click()
    page.get_by_role("menuitem", name="Update selected registrations").hover()
    page.get_by_text("(1 selected)").wait_for()
    return page


def mass_update_dialog(portal: Portal) -> Locator:
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
    page = portal.open("program:/monitoring/dashboard")
    page.get_by_test_id("metric-people-registered").wait_for()
    return page


def tabs_card(page: Page) -> Locator:
    return page.locator("p-card").filter(has=page.get_by_test_id("monitoring-menu"))


def dashboard_charts(portal: Portal) -> Page:
    page = full_height(monitoring(portal))
    page.locator("p-chart canvas").first.wait_for()
    page.wait_for_timeout(1000)
    return page


def monitoring_page(portal: Portal) -> Locator:
    page = dashboard_charts(portal)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), page.locator("p-chart").first, full_width=True
    )


def dashboard(portal: Portal) -> Locator:
    return Portal.clip_around(tabs_card(dashboard_charts(portal)))


def monitoring_tab(tab: str) -> Callable[[Portal], Page]:
    def prepare(portal: Portal) -> Page:
        page = monitoring(portal)
        page.get_by_test_id("monitoring-menu").get_by_role("tab", name=tab).click()
        page.wait_for_url("**/monitoring/" + tab.lower().replace(" ", "-"))
        page.wait_for_load_state("networkidle")
        portal.wait_for_table(page)
        return full_height(page)

    return prepare


def monitoring_tab_card(tab: str) -> Callable[[Portal], Locator]:
    return lambda portal: Portal.clip_around(tabs_card(monitoring_tab(tab)(portal)))


def upload_file_dialog(portal: Portal) -> Locator:
    page = monitoring_tab("Files")(portal)
    block_writes(page)
    page.get_by_role("button", name="Upload file").click()
    dialog = page.get_by_role("dialog").filter(has_text="Upload file")
    dialog.wait_for()
    page.wait_for_timeout(800)
    dialog.locator("input[type=file]").first.set_input_files(
        {"name": "distribution-plan.pdf", "mimeType": "application/pdf", "buffer": b"%PDF-1.4\n%%EOF\n"}
    )
    dialog.get_by_placeholder("Name the file for easy identification").fill("Distribution plan")
    unfocus(page)
    page.wait_for_timeout(400)
    if not dialog.get_by_role("button", name="Import file").is_enabled():
        raise LookupError("'Import file' is still disabled after choosing a file")
    return Portal.clip_around(dialog)


def attachment_menu(portal: Portal) -> Locator:
    page = monitoring_tab("Files")(portal)
    Portal.table(page).locator("tbody tr").first.locator("button").last.click()
    page.get_by_role("menuitem").first.wait_for()
    page.wait_for_timeout(400)
    return Portal.clip_around(tabs_card(page), page.get_by_role("menu"))


# --- payments ----------------------------------------------------------------------


def payments_page(portal: Portal) -> Locator:
    page = payments(portal)
    return Portal.clip_around(
        page.get_by_test_id("sidebar-toggle"), page.get_by_test_id("card-with-link").last, full_width=True
    )


def create_payment_select(portal: Portal) -> Page:
    page = payments(portal)
    page.get_by_role("button", name="Create new payment").click()
    page.get_by_role("button", name="Continue to registration").click()
    portal.wait_for_table(page)
    unfocus(page)
    return page


def create_payment_summary(portal: Portal) -> Page:
    page = create_payment_select(portal)
    Portal.table(page).get_by_role("checkbox", name="All items unselected").click()
    page.get_by_role("button", name="Add to payment").click()
    page.get_by_role("button", name="Create payment").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return page


def approve_dialog(portal: Portal) -> Locator:
    username, password = os.environ.get("APPROVER_USERNAME_121"), os.environ.get("APPROVER_PASSWORD_121")
    if not (username and password):
        raise LookupError("set APPROVER_USERNAME_121/APPROVER_PASSWORD_121 to open the page as the approver")
    ctx = portal.ctx.browser.new_context(
        viewport={"width": 1280, "height": 720}, locale="en-GB", timezone_id="Europe/Amsterdam"
    )
    ctx.set_default_timeout(15_000)
    approver = Portal(ctx, portal.portal_url, portal.api_url)
    approver.program_id = portal.program_id
    approver.login(username, password)
    page = approver.open(f"program:/payments/{payment_ids(portal)[-1]}")
    block_writes(page)
    page.get_by_role("button", name="Approve payment").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button", name="Approve payment").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24)


def payment_page(portal: Portal) -> Locator:
    page = full_height(started_payment(portal))
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), transactions_card(page), full_width=True)


def payment_export_menu(portal: Portal) -> Locator:
    page = started_payment(portal)
    page.get_by_role("button", name="Export").click()
    page.get_by_role("menuitem", name="Payment report").wait_for()
    page.wait_for_timeout(400)
    charts = page.locator("p-card").filter(has_text="Transactions data")
    return Portal.clip_around(page.get_by_test_id("sidebar-toggle"), charts, full_width=True)


def reconciliation_dialog(portal: Portal) -> Locator:
    page = started_payment(portal)
    page.get_by_role("button", name="Import reconciliation data").click()
    dialog = page.get_by_role("dialog").filter(has_text="Import reconciliation data")
    dialog.get_by_role("button", name="Download the template").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24, full_width=True)


def payments_export_dialog(portal: Portal) -> Locator:
    page = payments(portal)
    page.get_by_role("button", name="Export").click()
    page.get_by_role("menuitem", name="Payments").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button", name="Proceed").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(dialog, padding=24)


def failed_status(portal: Portal) -> Locator:
    page = started_payment(portal)
    filter_failed(page)
    return Portal.clip_around(transactions_card(page), page.get_by_role("listbox"), full_width=True)


def retry_button(page: Page) -> Locator:
    return page.get_by_role("button", name=re.compile("Retry failed"))


def select_failed(portal: Portal) -> Page:
    page = started_payment(portal)
    filter_failed(page)
    page.get_by_role("heading", level=1).click()
    page.get_by_role("dialog").filter(visible=True).wait_for(state="hidden")
    Portal.table(page).locator("tbody").get_by_role("checkbox").first.click()
    unfocus(page)
    return page


def retry_failed_button(portal: Portal) -> Locator:
    page = select_failed(portal)
    Portal.highlight(retry_button(page))
    return Portal.clip_around(transactions_card(page), full_width=True)


def retry_failed_confirm(portal: Portal) -> Locator:
    page = select_failed(portal)
    retry_button(page).click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    dialog.get_by_role("button").last.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(transactions_card(page), dialog, full_width=True)


# --- settings ----------------------------------------------------------------------


def settings(path: str) -> Callable[[Portal], Page]:
    def prepare(portal: Portal) -> Page:
        page = portal.open(f"program:/settings/{path}")
        block_writes(page)
        page.get_by_role("heading", name="Program settings").wait_for()
        return page

    return prepare


def card(page: Page, title: str) -> Locator:
    return page.locator("p-card").filter(has_text=title).first


def pick(page: Page, field: Locator, option: str | None = None) -> None:
    field.click()
    options = page.get_by_role("option")
    (options.filter(has_text=option) if option else options).first.click()


def basic_information(portal: Portal) -> Locator:
    page = settings("information")(portal)
    return Portal.clip_around(card(page, "Basic information"))


def edit_basic_information(portal: Portal) -> Locator:
    page = settings("information")(portal)
    page.get_by_role("button", name="Edit basic information").click()
    page.get_by_role("button", name="Save").wait_for()
    full_height(page)
    return Portal.clip_around(card(page, "Basic information"))


def fsps(portal: Portal) -> Page:
    page = settings("fsps")(portal)
    page.locator("p-accordion-header").first.wait_for()
    return page


def expand_form_requirements(page: Page) -> None:
    header = page.locator("p-accordion-header").first
    header.click()
    page.locator("p-accordion-header[aria-expanded=true]").wait_for()
    page.wait_for_timeout(400)
    unfocus(page)


def fsp_required_fields(portal: Portal) -> Locator:
    page = fsps(portal)
    Portal.highlight(page.locator("p-accordion-header [data-pc-section=toggleicon]").first, padding=8)
    return Portal.clip_around(card(page, "Financial Service Providers"))


def fsp_required_fields_expanded(portal: Portal) -> Locator:
    page = fsps(portal)
    expand_form_requirements(page)
    column = card(page, "Financial Service Providers").locator("tr > :nth-child(2)")
    Portal.highlight(Portal.clip_around(column.first, column.last, padding=0))
    return Portal.clip_around(card(page, "Financial Service Providers"))


def fsp_reconfigure(portal: Portal) -> Page:
    page = fsps(portal)
    expand_form_requirements(page)
    card(page, "Financial Service Providers").locator("button").first.click()
    item = page.get_by_role("menuitem", name="Reconfigure")
    item.wait_for()
    page.wait_for_timeout(400)
    for target in (page.get_by_role("tab", name="Settings"), page.get_by_role("link", name="FSP integration"), item):
        Portal.highlight(target)
    return page


def link_kobo_dialog(portal: Portal) -> Locator:
    page = settings("registration-data")(portal)
    page.get_by_test_id("kobo-integration-card").locator("a").first.click()
    dialog = page.get_by_role("alertdialog").filter(has_text="Link with KoboToolbox")
    dialog.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    return Portal.clip_around(card(page, "Registration integration"), dialog)


def add_user_to_team(portal: Portal) -> Locator:
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


def team_row_menu(portal: Portal) -> Page:
    page = settings("users/team")(portal)
    table = portal.wait_for_table(page)
    more = table.locator("tbody tr").first.locator("button").last
    more.click()
    page.get_by_role("menuitem").first.wait_for()
    page.wait_for_timeout(400)
    return page


def team_remove(portal: Portal) -> Locator:
    page = team_row_menu(portal)
    Portal.highlight(Portal.table(page).locator("tbody tr").first.locator("button").last)
    Portal.highlight(page.get_by_role("menuitem", name="Remove user"))
    return Portal.clip_around(card(page, "Program team"), page.get_by_role("menu"))


def team_edit(portal: Portal) -> Locator:
    page = team_row_menu(portal)
    page.get_by_role("menuitem", name="Edit").click()
    dialog = page.get_by_role("alertdialog").filter(visible=True)
    button = dialog.get_by_role("button", name="Save changes")
    button.wait_for()
    page.wait_for_timeout(400)
    unfocus(page)
    Portal.highlight(button)
    return Portal.clip_around(dialog)


def edit_payment_approval(portal: Portal) -> tuple[Page, Locator]:
    page = settings("users/payment-approval")(portal)
    page.get_by_role("button", name="Edit payment approval settings").click()
    approval = card(page, "Payment approval")
    approval.locator("p-multiselect").first.wait_for()
    return page, approval


def payment_approval_users(portal: Portal) -> Locator:
    page, approval = edit_payment_approval(portal)
    unfocus(page)
    Portal.highlight(approval.locator("p-multiselect").first)
    return Portal.clip_around(approval)


def payment_approval_steps(page: Page, approval: Locator) -> Locator:
    approval.get_by_role("button", name="Add approval step").click()
    approval.get_by_role("spinbutton").last.fill("1000")
    unfocus(page)
    page.wait_for_timeout(400)
    return approval.locator("button").filter(has_not_text=re.compile(r"\w")).last


def payment_approval_step(portal: Portal) -> Locator:
    page, approval = edit_payment_approval(portal)
    delete = payment_approval_steps(page, approval)
    Portal.highlight(
        Portal.clip_around(approval.get_by_text("Select users for this approval step"), delete, padding=6)
    )
    return Portal.clip_around(approval)


def payment_approval_delete_step(portal: Portal) -> Locator:
    page, approval = edit_payment_approval(portal)
    Portal.highlight(payment_approval_steps(page, approval))
    return Portal.clip_around(approval)


SCENARIOS = [
    # general
    Scenario("LoginPage.png", "Login page with language dropdown open", login_page),
    Scenario("ChangeLanguage.png", "Sidebar with language dropdown open", sidebar_language, (0, 0, 728, 720)),
    Scenario("AccountUser.png", "Account menu open", account_menu, (844, 0, 436, 352)),
    Scenario("ChangePassword.png", "Change password page", change_password, (0, 0, 672, 520)),
    # users
    Scenario("UserMenu.png", "Sidebar open on the users page", user_menu),
    Scenario("AddUser.png", "Users page, 'Add new user' highlighted", add_user_button, top(609)),
    Scenario("AddingNewUser.png", "Add new user dialog", add_user_dialog),
    Scenario("ResetPasswordUser.png", "User row menu, 'Reset password' highlighted", reset_password),
    # registrations
    Scenario("RegistrationsPage.png", "Registrations page", registrations_page),
    Scenario("RegistrationsPageImport.png", "Registrations page, 'Import' highlighted", import_button),
    Scenario("ImportRegistrationTemplate.png", "Import new registrations dialog", import_dialog),
    Scenario("ClearFilterButton.png", "Filtered table, 'Clear filters' highlighted", clear_filters, top(540)),
    Scenario("RegisteredStatusFilter.png", "Status column filter with 'New' selected", status_filter_new, top(570)),
    Scenario("SearchReg.png", "Registrations table filtered by name", search_registration, top(440)),
    Scenario("RegistationsStatusRighList.png", "Right-click menu on a registration row", row_menu),
    Scenario("PausePANotification.png", "Pause registration dialog", pause_dialog),
    Scenario("PauseStatus.png", "Registration with status Paused", paused_status, top(444)),
    Scenario("RegistrationDeclined.png", "Decline registration(s) dialog", decline_dialog),
    Scenario("PersonalInformationPA.png", "Registration page, Personal information tab", personal_information),
    Scenario("UpdateInformationPopUp.png", "Reason dialog after editing personal information", update_information_dialog),
    Scenario("EditInformationDuplicate.png", "Editing personal information of a duplicate", edit_duplicate),
    Scenario("ShowDuplicateColumn.png", "Manage table sidebar", manage_table, (498, 0, 782, 720)),
    Scenario("FilterDuplicate.png", "Duplicates column filter", filter_duplicates, top(520)),
    Scenario("DeclineIgnoreDuplicate.png", "Duplicate registration with Actions menu open", duplicate_actions),
    Scenario("MassUpdateButton.png", "Import menu with 'Update selected registrations'", mass_update_button, top(420)),
    Scenario("MassUpdateWindow.png", "Update selected registrations dialog", mass_update_dialog),
    # monitoring
    Scenario("MonitoringPage.png", "Monitoring page with the first row of charts", monitoring_page),
    Scenario("Dashboard.png", "Monitoring, Dashboard tab with charts", dashboard),
    Scenario("DataChangestab.png", "Monitoring, Data changes tab", monitoring_tab_card("Data changes")),
    Scenario("MonitoringPageFilestab.png", "Monitoring, Files tab", monitoring_tab_card("Files")),
    Scenario("UploadFilesInfo.png", "Upload file dialog", upload_file_dialog),
    Scenario("RenameDeleteAttachment.png", "Attachment row menu", attachment_menu),
    # payments
    Scenario("PaymentsPage.png", "Payments page with payment cards", payments_page),
    Scenario("CreateNewpaymentSelect.png", "Create payment, registration selection", create_payment_select),
    Scenario("StartPayment.png", "Create payment summary", create_payment_summary),
    Scenario("ApprovePaymentFinal.png", "Approve payment dialog (as the approver)", approve_dialog),
    Scenario("PaymentReportBoard.png", "Payment page with transaction list", payment_page),
    Scenario("IndividualExportReport.png", "Payment page, Export menu", payment_export_menu),
    Scenario("ReconciliationImport.png", "Import reconciliation data dialog", reconciliation_dialog),
    Scenario("ApprovePaymentExport.png", "Payments export dialog", payments_export_dialog),
    Scenario("FailedPaymentstatus.png", "Transaction status filter with 'Failed' selected", failed_status),
    Scenario("RetryPaiementbutton.png", "Failed transaction selected, 'Retry failed' highlighted", retry_failed_button),
    Scenario("RetryPaymentConfirm.png", "Retry failed transactions dialog", retry_failed_confirm),
    # settings
    Scenario("settings-programinformation-updatebasicinformation.png", "Basic information card", basic_information),
    Scenario("settings-programinformation-updatebasicinformation2.png", "Basic information in edit mode", edit_basic_information),
    Scenario("settings-fspintegration-requiredfields.png", "FSP card, 'Form requirements' chevron highlighted", fsp_required_fields),
    Scenario("settings-fspintegration-requiredfields2.png", "FSP form requirements expanded", fsp_required_fields_expanded),
    Scenario("settings-fspintegration-reconfigure2.png", "FSP menu, 'Reconfigure' highlighted", fsp_reconfigure),
    Scenario("settings-registrationdata4.png", "Link with KoboToolbox dialog", link_kobo_dialog),
    Scenario("settings-programteampng.png", "Add user to team dialog", add_user_to_team),
    Scenario("settings-programteamremove.png", "Program team row menu, 'Remove user' highlighted", team_remove),
    Scenario("settings-programteameditpng.png", "Edit user dialog", team_edit),
    Scenario("settings-paymentapproval1.png", "Payment approval, first step users", payment_approval_users),
    Scenario("settings-paymentapproval2.png", "Payment approval with a second step", payment_approval_step),
    Scenario("settings-paymentapproval3.png", "Payment approval, delete step highlighted", payment_approval_delete_step),
]
