"""Page object for the 121 Portal, plus API helpers that reuse the browser session.

Locators mirror the e2e page objects in global-121/121-platform (e2e/portal/pages).
"""

import time
from urllib.parse import quote

from playwright.sync_api import APIRequestContext, BrowserContext, Locator, Page, Playwright

LOCALE = "en-GB"
PROGRAM_TITLE = "Multipurpose cash"
PROGRAM_NGO = "510 manual screenshots"


class Portal:
    def __init__(self, ctx: BrowserContext, portal_url: str, api_url: str):
        self.ctx = ctx
        self.portal_url = portal_url.rstrip("/")
        self.api_url = api_url.rstrip("/").removesuffix("/api") + "/api"
        self.program_id: int | None = None
        self.permissions: dict = {}

    # --- session -------------------------------------------------------------

    def login(self, username: str, password: str) -> None:
        page = self.ctx.new_page()
        page.goto(f"{self.portal_url}/{LOCALE}/login")
        page.get_by_label("E-mail").fill(username)
        page.get_by_label("Password").fill(password)
        with page.expect_response(lambda r: r.url.endswith("/users/login")) as resp:
            page.get_by_role("button", name="Log in").click()
        if not resp.value.ok:
            raise RuntimeError(f"login failed: HTTP {resp.value.status}")
        self.permissions = resp.value.json().get("permissions") or {}
        page.wait_for_url("**/programs**", timeout=30_000)
        page.close()

    def open(self, path: str) -> Page:
        """Open a portal route (e.g. '/users' or 'program:/registrations') in a new page."""
        if path.startswith("program:"):
            path = f"/program/{self.program_id}{path.removeprefix('program:')}"
        page = self.ctx.new_page()
        page.goto(f"{self.portal_url}/{LOCALE}{path}")
        page.wait_for_load_state("networkidle")
        return page

    # --- API -----------------------------------------------------------------

    def api(
        self,
        method: str,
        path: str,
        *,
        params: dict | None = None,
        session: APIRequestContext | None = None,
        **kwargs,
    ):
        """Call the 121 API as the logged-in portal user, or as another `session` (see api_login)."""
        if path.startswith("program:"):
            path = f"/programs/{self.program_id}{path.removeprefix('program:')}"
        url = f"{self.api_url}{path}"
        if params:
            url += "?" + "&".join(f"{k}={quote(str(v), safe=':$,')}" for k, v in params.items())
        headers = {"x-121-interface": "portal"}
        r = (session or self.ctx.request).fetch(url, method=method, headers=headers, **kwargs)
        if not r.ok:
            raise RuntimeError(f"{method} {path} -> HTTP {r.status}: {r.text()[:500]}")
        return r.json() if r.body() else None

    def api_login(self, playwright: Playwright, username: str, password: str) -> APIRequestContext:
        session = playwright.request.new_context()
        self.api("POST", "/users/login", session=session, data={"username": username, "password": password})
        return session

    def find_program(self) -> int | None:
        for pid in sorted(self.permissions, key=int):
            p = self.api("GET", f"/programs/{pid}")
            if (p.get("titlePortal") or {}).get("en") == PROGRAM_TITLE and p.get("ngo") == PROGRAM_NGO:
                return int(pid)
        return None

    def registrations(self, **params) -> list[dict]:
        return self.api("GET", "program:/registrations", params={"limit": 1000, **params})["data"]

    def wait_for(self, check, what: str, timeout: float = 60) -> None:
        end = time.monotonic() + timeout
        while not check():
            if time.monotonic() > end:
                raise TimeoutError(f"timed out waiting for {what}")
            time.sleep(1)

    # --- locators (see e2e/portal/pages) --------------------------------------

    @staticmethod
    def table(page: Page, test_id: str = "query-table") -> Locator:
        return page.get_by_test_id(test_id)

    @staticmethod
    def wait_for_table(page: Page, test_id: str = "query-table") -> Locator:
        table = page.get_by_test_id(test_id)
        table.locator("tbody tr").first.wait_for()
        table.get_by_test_id("query-table-loading").first.wait_for(state="detached")
        return table

    @staticmethod
    def row(page: Page, name: str) -> Locator:
        return page.get_by_test_id("query-table").locator("tbody tr").filter(
            has=page.get_by_role("link", name=name, exact=True)
        )

    @staticmethod
    def column_filter_button(page: Page, column: str) -> Locator:
        return (
            page.get_by_test_id("query-table")
            .get_by_role("columnheader", name=column)
            .get_by_label("Show Filter Menu")
        )

    @staticmethod
    def clip_around(*targets: Locator, padding: int = 16, full_width: bool = False) -> Locator:
        """Return an invisible element covering the union of targets plus padding, to screenshot that region."""
        boxes = [t.bounding_box() for t in targets]
        if None in boxes:
            raise LookupError("clip target not visible")
        page = targets[0].page
        vw, vh = page.viewport_size["width"], page.viewport_size["height"]
        left = 0 if full_width else max(0, min(b["x"] for b in boxes) - padding)
        right = vw if full_width else min(vw, max(b["x"] + b["width"] for b in boxes) + padding)
        top = max(0, min(b["y"] for b in boxes) - padding)
        bottom = min(vh, max(b["y"] + b["height"] for b in boxes) + padding)
        page.evaluate(
            """([l, t, w, h]) => {
                const el = document.createElement('div');
                el.dataset.screenshotRegion = '';
                Object.assign(el.style, {
                    position: 'fixed', zIndex: -1, pointerEvents: 'none',
                    left: `${l}px`, top: `${t}px`, width: `${w}px`, height: `${h}px`,
                });
                document.body.appendChild(el);
            }""",
            [round(left), round(top), round(right - left), round(bottom - top)],
        )
        return page.locator("[data-screenshot-region]").last

    @staticmethod
    def highlight(target: Locator, padding: int = 4) -> None:
        """Draw a red box around target, like the hand-made annotations in the existing images."""
        target.evaluate(
            """(el, pad) => {
                const r = el.getBoundingClientRect();
                const box = document.createElement('div');
                box.dataset.screenshotHighlight = '';
                Object.assign(box.style, {
                    position: 'fixed', zIndex: 2147483647, pointerEvents: 'none',
                    left: `${r.left - pad}px`, top: `${r.top - pad}px`,
                    width: `${r.width + 2 * pad}px`, height: `${r.height + 2 * pad}px`,
                    border: '3px solid #e00', borderRadius: '6px',
                });
                document.body.appendChild(box);
            }""",
            padding,
        )
