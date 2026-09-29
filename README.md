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

<!-- NOTE: The Docker-way to serve/build is not compatible with the multi-lingual setup currently in use. -->
<!-- 
#### With Docker

- Install Docker: <https://docs.docker.com/get-docker/>

- Open a terminal at this folder to build a Docker-container:

  ```sh
  docker build --tag manual-121 .
  ```

- Run the Docker-container:

  ```sh
  docker run --rm -it -p 8000:8000 -v ${PWD}:/docs manual-121
  ```
-->

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

## Copilot and PR guidance

- Repository-wide Copilot instructions for translation and ToC-anchor safety are in `.github/copilot-instructions.md`.
- Pull request guidance and translation/ToC checklists are in `.github/pull_request_template.md`.
