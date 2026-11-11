"""Finalize Copilot release PRs when the agent signals completion by requesting review."""

import logging
import os

from release_sync_issue import api

logger = logging.getLogger(__name__)
REVIEWERS = ["Gabriele510"]
TEAM = "121-support"
COPILOT_LOGINS = {"Copilot", "copilot-swe-agent[bot]"}


def finalize(repo: str, number: int, token: str) -> None:
    """Mark a same-repository Copilot release PR ready and route its review requests."""
    path = f"/repos/{repo}/pulls/{number}"
    pr = api(path, token)
    if not (
        pr["state"] == "open"
        and pr["user"]["login"] in COPILOT_LOGINS
        and pr["head"]["repo"]
        and pr["head"]["repo"]["full_name"] == repo
        and pr["base"]["ref"] == "main"
        and pr["title"].startswith("docs: update manual for 121 release ")
    ):
        logger.info("Skipping PR #%s: not an open Copilot release-sync PR targeting main.", number)
        return

    if pr["draft"]:
        result = api(
            "/graphql",
            token,
            "POST",
            {
                "query": (
                    "mutation($id: ID!) { markPullRequestReadyForReview("
                    "input: {pullRequestId: $id}) { pullRequest { isDraft } } }"
                ),
                "variables": {"id": pr["node_id"]},
            },
        )
        if (
            result.get("errors")
            or result["data"]["markPullRequestReadyForReview"]["pullRequest"]["isDraft"]
        ):
            raise RuntimeError(f"Could not mark PR #{number} ready: {result}")

    pending = {r["login"] for r in pr["requested_reviewers"]}
    if "jmargutt" in pending:
        api(f"{path}/requested_reviewers", token, "DELETE", {"reviewers": ["jmargutt"]})
    reviewers = [r for r in REVIEWERS if r not in pending]
    teams = [] if TEAM in {t["slug"] for t in pr["requested_teams"]} else [TEAM]
    if reviewers or teams:
        api(
            f"{path}/requested_reviewers",
            token,
            "POST",
            {"reviewers": reviewers, "team_reviewers": teams},
        )
    logger.info(
        "PR #%s is ready; review requested from Gabriele510 and global-121/121-support.", number
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    pr_number = int(os.environ["PR_NUMBER"])
    if pr_number <= 0:
        raise ValueError("PR_NUMBER must be a positive integer")
    finalize(os.environ["GITHUB_REPOSITORY"], pr_number, os.environ["GITHUB_TOKEN"])
