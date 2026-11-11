"""Regression tests for the release PR review handoff."""

import unittest
from copy import deepcopy
from unittest.mock import call, patch

from release_sync_review import finalize

REPO = "global-121/manual"
PATH = f"/repos/{REPO}/pulls/155"
PR = {
    "state": "open",
    "user": {"login": "Copilot"},
    "head": {"repo": {"full_name": REPO}},
    "base": {"ref": "main"},
    "title": "docs: update manual for 121 release v26.11-1",
    "draft": True,
    "node_id": "PR_155",
    "requested_reviewers": [{"login": "jmargutt"}],
    "requested_teams": [],
}
READY = {"data": {"markPullRequestReadyForReview": {"pullRequest": {"isDraft": False}}}}


class FinalizeTests(unittest.TestCase):
    """Keep the automated handoff scoped to completed release PRs."""

    @patch("release_sync_review.api")
    def test_marks_ready_and_replaces_initiator_review(self, api):
        """A draft release PR is made ready and routed to the user and team."""
        api.side_effect = [deepcopy(PR), READY, {}, {}]
        finalize(REPO, 155, "token")
        self.assertEqual(api.call_args_list[1].args[:3], ("/graphql", "token", "POST"))
        self.assertIn("markPullRequestReadyForReview", api.call_args_list[1].args[3]["query"])
        self.assertEqual(api.call_args_list[1].args[3]["variables"], {"id": "PR_155"})
        self.assertEqual(
            api.call_args_list[2:],
            [
                call(f"{PATH}/requested_reviewers", "token", "DELETE", {"reviewers": ["jmargutt"]}),
                call(
                    f"{PATH}/requested_reviewers",
                    "token",
                    "POST",
                    {"reviewers": ["Gabriele510"], "team_reviewers": ["121-support"]},
                ),
            ],
        )

    @patch("release_sync_review.api")
    def test_already_finalized_is_idempotent(self, api):
        """Repeated completion events do not repeat pending review requests."""
        pr = deepcopy(PR)
        pr.update(
            draft=False,
            requested_reviewers=[{"login": "Gabriele510"}],
            requested_teams=[{"slug": "121-support"}],
        )
        api.return_value = pr
        finalize(REPO, 155, "token")
        api.assert_called_once_with(PATH, "token")

    @patch("release_sync_review.api")
    def test_skips_unrelated_or_closed_prs(self, api):
        """Manual dispatch cannot finalize unrelated, forked or closed PRs."""
        for change in (
            {"state": "closed"},
            {"user": {"login": "someone-else"}},
            {"head": {"repo": {"full_name": "someone/fork"}}},
            {"head": {"repo": None}},
            {"base": {"ref": "another-branch"}},
            {"title": "fix: something else"},
        ):
            with self.subTest(change=change):
                api.reset_mock()
                api.return_value = deepcopy(PR) | change
                finalize(REPO, 155, "token")
                api.assert_called_once_with(PATH, "token")

    @patch("release_sync_review.api")
    def test_graphql_failure_does_not_report_success(self, api):
        """GraphQL errors in HTTP 200 responses must fail the workflow."""
        api.side_effect = [deepcopy(PR), {"errors": [{"message": "Permission denied"}]}]
        with self.assertRaisesRegex(RuntimeError, "Permission denied"):
            finalize(REPO, 155, "token")
        self.assertEqual(api.call_count, 2)


if __name__ == "__main__":
    unittest.main()
