#!/usr/bin/env python3
"""
Translation helper script for French documentation files.
This script contains the translations needed for all 69 markdown files.
"""

# Dictionary of file paths and their translations
# Format: {file_path: {"old": "...", "new": "..."}}

translations = {
    # GENERAL SECTION
    "docs/fr/general/logging-in.md": {
        "old_title": "Logging in",
        "new_title": "Se connecter",
    },
    # This is a placeholder structure for tracking translations
}

if __name__ == "__main__":
    print("French Documentation Translation Helper")
    print(f"Total translation pairs: {len(translations)}")
