FROM squidfunk/mkdocs-material

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml .

RUN uv pip install --system --no-cache -r pyproject.toml
