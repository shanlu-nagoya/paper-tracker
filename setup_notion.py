"""
Run once locally to create the Notion database.
Prints the NOTION_DATABASE_ID you need to save as a GitHub secret.

Usage (PowerShell):
    $env:NOTION_TOKEN="your_token"
    $env:NOTION_PARENT_PAGE_ID="your_page_id"
    python setup_notion.py
"""

import os
import sys
from notion_client import Client


def create_database(notion: Client, parent_page_id: str) -> str:
    response = notion.databases.create(
        parent={"type": "page_id", "page_id": parent_page_id},
        title=[{"type": "text", "text": {"content": "Paper Tracker"}}],
        properties={
            "Title":     {"title": {}},
            "Authors":   {"rich_text": {}},
            "Abstract":  {"rich_text": {}},
            "URL":       {"url": {}},
            "Published": {"date": {}},
            "Keywords":  {"multi_select": {}},
            "arXiv ID":  {"rich_text": {}},
        },
    )
    return response["id"]


def main() -> None:
    token = os.environ.get("NOTION_TOKEN")
    parent_page_id = os.environ.get("NOTION_PARENT_PAGE_ID")

    if not token or not parent_page_id:
        print("Error: set NOTION_TOKEN and NOTION_PARENT_PAGE_ID environment variables.")
        sys.exit(1)

    notion = Client(auth=token)
    db_id = create_database(notion, parent_page_id)

    print("Database created successfully!")
    print()
    print(f"NOTION_DATABASE_ID={db_id}")
    print()
    print("Add this value as a GitHub Actions secret named NOTION_DATABASE_ID.")


if __name__ == "__main__":
    main()
