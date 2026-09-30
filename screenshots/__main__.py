"""Regenerate 121 Portal screenshots for the manual.

Usage: uv run --env-file .env python -m screenshots [--seed] [--only NAME ...] [--out DIR]
"""

import argparse
import logging
import os
import sys
from pathlib import Path

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, sync_playwright

from .portal import PROGRAM_TITLE, Portal
from .scenarios import SCENARIOS
from .seed import seed

logger = logging.getLogger(__name__)

VIEWPORT = {"width": 1280, "height": 720}
HIDE_CSS = """
[data-screenshot-hide], app-toast, p-toast { visibility: hidden !important; }
"""
# Real e-mail addresses of staging users must not end up in the manual.
MASK_EMAILS_JS = """() => {
    const re = /[\\w.+-]+@(?!(example\\.org|121\\.global)\\b)[\\w-]+(\\.[\\w-]+)+/g;
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n; (n = walker.nextNode()); ) {
        const v = n.nodeValue.replace(re, 'user@example.org');
        if (v !== n.nodeValue) n.nodeValue = v;
    }
    document.querySelectorAll('input').forEach((i) => {
        i.value = i.value.replace(re, 'user@example.org');
    });
}"""


def main() -> int:
    """Parse the arguments, log in, optionally seed, and take the selected screenshots.

    Returns:
        0 if all screenshots were written, 1 otherwise.
    """
    ap = argparse.ArgumentParser(prog="python -m screenshots", description=__doc__)
    ap.add_argument("--portal-url", default=os.environ.get("PORTAL_URL_121"))
    ap.add_argument("--api-url", default=os.environ.get("API_URL_121"))
    ap.add_argument("--only", action="append", default=[], help="scenario name (repeatable)")
    ap.add_argument("--out", type=Path, default=Path("screenshots/output"))
    ap.add_argument(
        "--seed",
        action="store_true",
        help=f"create/update the '{PROGRAM_TITLE}' demo program (writes to the target environment)",
    )
    ap.add_argument("--headed", action="store_true")
    ap.add_argument("--list", action="store_true", help="list scenarios and exit")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s", stream=sys.stdout, force=True)

    if args.list:
        for s in SCENARIOS:
            print(f"{s.name:50} {s.shows}")  # noqa: T201
        return 0
    if not (args.portal_url and args.api_url):
        ap.error("set PORTAL_URL_121 and API_URL_121 (or pass --portal-url/--api-url)")
    username, password = os.environ.get("USERNAME_121"), os.environ.get("PASSWORD_121")
    if not (username and password):
        ap.error("set USERNAME_121 and PASSWORD_121")

    unknown = set(args.only) - {s.name for s in SCENARIOS}
    if unknown:
        ap.error(f"unknown scenario(s): {', '.join(sorted(unknown))}")
    selected = [s for s in SCENARIOS if not args.only or s.name in args.only]
    args.out.mkdir(parents=True, exist_ok=True)

    failed = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        ctx = browser.new_context(
            viewport=VIEWPORT, device_scale_factor=1, locale="en-GB", timezone_id="Europe/Amsterdam"
        )
        ctx.set_default_timeout(15_000)
        portal = Portal(ctx, args.portal_url, args.api_url)
        portal.login(username, password)
        if args.seed:
            approver = None
            if os.environ.get("APPROVER_USERNAME_121") and os.environ.get("APPROVER_PASSWORD_121"):
                approver = portal.api_login(
                    p, os.environ["APPROVER_USERNAME_121"], os.environ["APPROVER_PASSWORD_121"]
                )
            seed(portal, approver)
        else:
            portal.program_id = portal.find_program()
            if portal.program_id is None:
                logger.error("Program '%s' not found; run once with --seed.", PROGRAM_TITLE)
                return 1

        for s in selected:
            try:
                target = s.prepare(portal)
                page = target if isinstance(target, Page) else target.page
                page.add_style_tag(content=HIDE_CSS)
                page.evaluate(MASK_EMAILS_JS)
                page.wait_for_timeout(300)
                path = args.out / s.name
                if isinstance(target, Page) and s.clip:
                    x, y, w, h = s.clip
                    clip = {"x": x, "y": y, "width": w, "height": h}
                    page.screenshot(path=path, animations="disabled", clip=clip)
                else:
                    target.screenshot(path=path, animations="disabled")
                logger.info("ok      %s", s.name)
            except (PlaywrightError, LookupError, RuntimeError, TimeoutError) as e:
                failed += 1
                logger.error("FAILED  %s: %s", s.name, str(e).splitlines()[0])
            finally:
                for c in browser.contexts:
                    if c is not ctx:
                        c.close()
                for pg in ctx.pages:
                    pg.close()
        browser.close()

    logger.info(
        "\n%d/%d screenshots written to %s", len(selected) - failed, len(selected), args.out
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
