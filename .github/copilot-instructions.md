# Copilot Instructions for This Repository

## Scope and goals

- This repository contains a multilingual MkDocs manual (`docs/en`, `docs/fr`, `docs/nl`).
- Primary goal: help contributors translate and maintain parity across languages without breaking links, headings, or structure.

## Overall way of work

Contributors to this repo are content experts, but not necessarily skilled with git and other tools used in this project. When making changes, the suggested division of tasks would be:

The contributor updates the docs and assets, usually in English.

The agent helps with:

- Creating a change plan splitting the work into discrete commits. Take time to mirror each sub-task in the French and Dutch versions, and ensure that the contributor is aware of the scope of work.
- Basic git tasks such as git fetch, branch, pull, push, and PR creation. Ensure that the contributor is working on the correct branch and that the PR is created against the correct target branch.
- Ensuring that the contributor's changes do not break the structure of the manual, including links, headings, and anchors. The agent can run the validation commands below to check for errors.
- Translate English content to French. Only check for changes in Dutch when the files in the docs/en/nlrc folder are updated. The agent should ensure that the translation is accurate and consistent with the source page intent, and that it follows the glossary and terminology rules below.

## Translation workflow

- Treat English pages in `docs/en` as source unless stated otherwise.
- Preserve source structure exactly where possible:
  - same heading levels and order
  - same admonition types (`!!! Important`, `!!! Note`, etc.)
  - same lists, tables, snippets, and image references
- Translate user-facing text, but do not translate:
  - file paths
  - markdown syntax
  - icon tokens like `:material-...:`
  - snippet includes like `-8<- "docs/.../_snippets/..."`
- Keep relative links valid for the target language folder.
- Ensure the language specific mkdocs config file in ./config is updated with any new pages or renamed files.

## Field-specific terminology and glossary

- **Preferred translations reference**: Consult `docs/{lang}/glossary-121.md` for field-specific terms and their preferred translations across all pages.
  - The glossary contains both general terms and domain-specific translations (e.g., CVA, FSP, 121 Platform concepts).
  - Use consistent terminology across all pages in the same language.
- **Adding new preferred translations**:
  - If a term appears frequently and has a non-literal or field-specific translation, add it to the glossary with:
    - English term and definition
    - Target language term and definition
  - Document _why_ a non-literal translation was chosen (e.g., industry convention, clarity for end-users, legal accuracy).
- **When to deviate from literal translation**:
  - Domain-specific acronyms (FSP, CVA, KOBO) remain unchanged.
  - Role/permission names should match the glossary to avoid user confusion in the UI.
  - Legal or regulatory terms may require non-literal translation per jurisdiction.
  - Always flag non-literal choices in PR comments for review.

## Markdown syntax and structure

- The layout of warnings, notes and notifications are marked with `!!! Important`, `!!! Note`, `!!! Info`, and `!!! Question`. Make sure the text following the title is preceded by exactly four spaces, as otherwise the markdown parser will not render it correctly inside the notification box. Please note though that hard tabs are not allowed by the markdown linter, so make sure to use spaces instead of tabs.

## ToC and anchor safety

- Do not add inline heading IDs like `{ #my-id }` to headings in this repo.
  - Reason: this can create a rewrite loop with Markdown All in One and break generated ToC hashes.
- If a page uses in-page ToC links and generated hashes include URL-encoded characters (for example `%C3%A9`), prefer this pattern:
  1. keep the heading plain markdown
  2. add a standalone alias anchor directly above the heading:
     - `<a id="...encoded-or-expected-hash..."></a>`
- When editing manual ToC lists, ensure each `(#hash)` exists as an anchor/heading ID in output.

## Review behavior for PR comments

When asked to review translation PRs, prioritize:

- translation accuracy and consistency with source page intent
- structure parity with source page
- broken internal links and hash anchors
- glossary/term consistency across files
- accidental changes to snippets, assets, or non-translatable tokens

Call out issues with file paths and concrete suggested replacements.

## Validation commands

- Use language-specific MkDocs config:
  - `mkdocs serve --config-file config/en/mkdocs.yml --dev-addr localhost:8000`
  - `mkdocs serve --config-file config/fr/mkdocs.yml --dev-addr localhost:8003`
  - `mkdocs serve --config-file config/nl/mkdocs.yml --dev-addr localhost:8080`
