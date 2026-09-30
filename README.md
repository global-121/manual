# 121 Manual

> [!TIP]
> Read the manual: <https://manual.121.global>

## Development

### Getting Started

#### With Python

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

- Install dependencies

  ```sh
  uv sync
  ```

- Build the documentation (for each language separately):
  - For English, preview at: <http://localhost:8000>

    ```sh
    uv run python -m mkdocs serve --config-file config/en/mkdocs.yml --dev-addr localhost:8000
    ```

  - For Dutch, preview at: <http://localhost:8080>

    ```sh
    uv run python -m mkdocs serve --config-file config/nl/mkdocs.yml --dev-addr localhost:8080
    ```

  - For French, preview at: <http://localhost:8003>

    ```sh
    uv run python -m mkdocs serve --config-file config/fr/mkdocs.yml --dev-addr localhost:8003
    ```

### Tools in use

- Material for MkDocs: <https://squidfunk.github.io/mkdocs-material/>

### Screenshots

Portal screenshots in `overrides/assets/img` can be regenerated with [Playwright](https://playwright.dev/python/).
Each image has a scenario in `screenshots/scenarios.py` that drives the 121 Portal into the state shown.

- Install the browser (once):

  ```sh
  uv sync --group screenshots
  uv run python -m playwright install chromium
  ```

- Copy `example.env` to `.env` and fill in the portal/API URLs and a login (the `.env` file is git-ignored).

- Take the screenshots (written to `screenshots/output/`, also git-ignored), then compare them with the existing images and copy over the ones you want to update:

  ```sh
  uv run --env-file .env python -m screenshots
  uv run --env-file .env python -m screenshots --only RegistrationsPage.png --only PaymentsPage.png
  uv run --env-file .env python -m screenshots --list
  ```

- The screenshots use one fixed demo program, "Multipurpose cash". To create it (or bring it back to its expected state), add `--seed`.
  This **writes to the target environment**: it creates the program once and afterwards only restores the same registrations, statuses and payments. Only use it on a test environment.
  Payments need a second account as approver (`APPROVER_USERNAME_121`/`APPROVER_PASSWORD_121`), because the platform does not allow you to approve your own payments.

- E-mail addresses that do not end in `@example.org` are masked in the screenshots.

## Deployment notes

- The Azure Static Web App config includes explicit CORS rules for `en/faq/*` and `fr/faq/*`.
- Reason: FAQ pages from this manual are embedded in a 510.global context (Using in-page JS, using `fetch()`.), so `Access-Control-Allow-Origin: https://510.global` must remain in `staticwebapp.config.json` for those routes.

## Automation

The AI agent (GitHub Copilot) follows the instructions in `.github/copilot-instructions.md`: how to translate pages, the mandatory French terminology, markdown rules, and how to keep in-page links working.

For every new [121 Platform release](https://github.com/global-121/121-platform/releases), Copilot drafts the manual update:

1. The workflow `.github/workflows/release-sync.yml` runs every Monday morning (or by hand from the Actions tab). When there is a new release, it opens a `release-sync` issue with the release notes, commits and changed portal files since the last documented release. It waits as long as a previous `release-sync` issue is still open, so there is only one manual update at a time; the next issue then covers all releases since.
2. The issue is assigned to Copilot cloud agent with the custom agent `.github/agents/release-sync.agent.md`. Copilot reviews every commit, updates the EN and FR pages (and screenshots where possible), and opens a pull request with a table of all release items and their manual impact.
3. Review the pull request and check the `<!-- VERIFY -->` items. To have something changed, comment on the pull request and mention `@copilot` (e.g. "@copilot also update the glossary"); Copilot pushes the changes to the same pull request. Collect several remarks in one review (**Start a review** > **Submit review**) so they are handled in one run. Comments on the issue are not picked up.
4. Merge when it is right; this closes the issue as completed. To reject the update, close the pull request and close the issue as **not planned**: its releases are then included again in the next issue.

## AI Disclaimer

Parts of the code in this repository were written and reviewed with the assistance of AI tools, including large language models (LLMs).

All AI-generated code has been reviewed by human contributors before being merged. The humans involved take responsibility for the correctness and quality of the code.

If you have questions or concerns, please contact the maintainers.

<!-- One-time setup (repository admin):

- Enable Copilot cloud agent for this repository. The agent and `.github/workflows/copilot-setup-steps.yml` only work once they are on `main`.
- Add an Actions secret `COPILOT_ASSIGN_TOKEN`: a fine-grained personal access token of a user with a Copilot license, for this repository, with read access to metadata and read/write access to actions, contents, issues and pull requests. Without it, the issue is created unassigned; assign it to Copilot and pick the `release-sync` agent by hand.
- Optional, to let Copilot regenerate screenshots: add `PORTAL_URL_121`, `API_URL_121`, `USERNAME_121` and `PASSWORD_121` (and `APPROVER_USERNAME_121`/`APPROVER_PASSWORD_121`, so Copilot can re-create the demo payments with `--seed` after the test environment is reset) under **Settings > Secrets and variables > Agents**, and add the portal and API hosts to the custom allowlist under **Settings > Copilot > Internet access**. Only use a test environment such as staging. -->
