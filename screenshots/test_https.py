"""Regression tests for screenshot HTTPS options across isolated sessions."""

import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from . import __main__ as runner
from .portal import Portal
from .scenarios import approve_dialog, login_page


class HttpsTests(unittest.TestCase):
    """Preserve certificate checks by default and propagate explicit opt-in."""

    def test_runner_certificate_option(self):
        """The cloud setting and CLI flag reach the main browser context."""
        for env_value, flags, expected in (
            ("0", [], False),
            ("1", [], True),
            ("0", ["--ignore-https-errors"], True),
        ):
            with (
                self.subTest(env=env_value, flags=flags),
                tempfile.TemporaryDirectory() as out,
                patch.dict(
                    os.environ,
                    {
                        "SCREENSHOTS_IGNORE_HTTPS_ERRORS": env_value,
                        "PORTAL_URL_121": "https://portal.example.org",
                        "API_URL_121": "https://api.example.org",
                        "USERNAME_121": "user@example.org",
                        "PASSWORD_121": "test-only",
                    },
                ),
                patch("sys.argv", ["screenshots", "--out", out, *flags]),
                patch.object(runner, "sync_playwright") as playwright,
                patch.object(runner.Portal, "login"),
                patch.object(runner.Portal, "find_program", return_value=1),
                patch.object(runner, "SCENARIOS", []),
            ):
                self.assertEqual(runner.main(), 0)
                browser = (
                    playwright.return_value.__enter__.return_value.chromium.launch.return_value
                )
                self.assertIs(browser.new_context.call_args.kwargs["ignore_https_errors"], expected)

    def test_additional_sessions_inherit_certificate_option(self):
        """Login screenshots and approver API/browser sessions use the same policy."""
        for enabled in (False, True):
            with self.subTest(ignore_https_errors=enabled):
                ctx = MagicMock()
                portal = Portal(
                    ctx,
                    "https://portal.example.org",
                    "https://api.example.org",
                    ignore_https_errors=enabled,
                )
                playwright = MagicMock()
                portal.api_login(playwright, "approver@example.org", "test-only")
                playwright.request.new_context.assert_called_once_with(ignore_https_errors=enabled)

                login_page(portal)
                self.assertIs(
                    ctx.browser.new_context.call_args.kwargs["ignore_https_errors"], enabled
                )

                with (
                    patch.dict(
                        os.environ,
                        {
                            "APPROVER_USERNAME_121": "approver@example.org",
                            "APPROVER_PASSWORD_121": "test-only",
                        },
                    ),
                    patch.object(Portal, "login", autospec=True) as login,
                    patch.object(Portal, "open"),
                    patch.object(Portal, "clip_around"),
                    patch("screenshots.scenarios.payment_id", return_value=1),
                ):
                    approve_dialog(portal)
                    self.assertIs(
                        ctx.browser.new_context.call_args.kwargs["ignore_https_errors"], enabled
                    )
                    self.assertIs(login.call_args.args[0].ignore_https_errors, enabled)


if __name__ == "__main__":
    unittest.main()
