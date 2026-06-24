# Copilot Instructions for This Repository

## Scope and goals

- This repository contains a multilingual MkDocs manual (`docs/en`, `docs/fr`, `docs/nl`).
- Primary goal: help contributors translate and maintain parity across languages without breaking links, headings, or structure.

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
  - Document *why* a non-literal translation was chosen (e.g., industry convention, clarity for end-users, legal accuracy).
- **When to deviate from literal translation**:
  - Domain-specific acronyms (FSP, CVA, KOBO) remain unchanged.
  - Role/permission names should match the glossary to avoid user confusion in the UI.
  - Legal or regulatory terms may require non-literal translation per jurisdiction.
  - Always flag non-literal choices in PR comments for review.

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
