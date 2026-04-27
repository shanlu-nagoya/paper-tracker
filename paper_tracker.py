"""
Weekly arXiv paper tracker — syncs new papers to a Notion database.
Searches papers published in the last SEARCH_DAYS days and adds any
not already present in Notion (deduplication via arXiv ID).
"""

import os
import sys
import requests
import arxiv
from datetime import datetime, timedelta, timezone

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
SEARCH_DAYS = 8

KEYWORDS = [
    "visible light communication VLC",
    "optical wireless communication",
    "LED communication",
    "V2X optical vehicular communication",
    "intelligent surface communication ISC",
]


def notion_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


def get_existing_ids(token: str, database_id: str) -> set[str]:
    existing: set[str] = set()
    cursor = None
    while True:
        body: dict = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        resp = requests.post(
            f"{NOTION_API}/databases/{database_id}/query",
            headers=notion_headers(token),
            json=body,
        )
        resp.raise_for_status()
        data = resp.json()
        for page in data["results"]:
            prop = page["properties"].get("arXiv ID", {})
            rich_text = prop.get("rich_text", [])
            if rich_text:
                existing.add(rich_text[0]["text"]["content"])
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
    return existing


def format_authors(paper: arxiv.Result) -> str:
    names = [a.name for a in paper.authors[:5]]
    result = ", ".join(names)
    if len(paper.authors) > 5:
        result += f" et al. (+{len(paper.authors) - 5})"
    return result


def add_paper(token: str, database_id: str, paper: arxiv.Result, keyword: str) -> None:
    body = {
        "parent": {"database_id": database_id},
        "properties": {
            "Title":    {"title":     [{"text": {"content": paper.title[:2000]}}]},
            "Authors":  {"rich_text": [{"text": {"content": format_authors(paper)[:2000]}}]},
            "Abstract": {"rich_text": [{"text": {"content": paper.summary[:2000]}}]},
            "URL":      {"url": paper.entry_id},
            "Published":{"date": {"start": paper.published.strftime("%Y-%m-%d")}},
            "Keywords": {"multi_select": [{"name": keyword}]},
            "arXiv ID": {"rich_text": [{"text": {"content": paper.entry_id}}]},
        },
    }
    resp = requests.post(
        f"{NOTION_API}/pages",
        headers=notion_headers(token),
        json=body,
    )
    resp.raise_for_status()


def search_papers(keyword: str, days: int = SEARCH_DAYS) -> list[arxiv.Result]:
    client = arxiv.Client()
    search = arxiv.Search(
        query=keyword,
        max_results=30,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    papers = []
    for result in client.results(search):
        if result.published < cutoff:
            break
        papers.append(result)
    return papers


def main() -> None:
    token = os.environ.get("NOTION_TOKEN")
    database_id = os.environ.get("NOTION_DATABASE_ID")
    if not token or not database_id:
        print("Error: set NOTION_TOKEN and NOTION_DATABASE_ID.")
        sys.exit(1)

    existing_ids = get_existing_ids(token, database_id)
    print(f"Existing papers in Notion: {len(existing_ids)}")

    added = 0
    for keyword in KEYWORDS:
        print(f"Searching: {keyword}")
        try:
            papers = search_papers(keyword)
        except Exception as e:
            print(f"  Search failed: {e}")
            continue
        for paper in papers:
            if paper.entry_id in existing_ids:
                continue
            try:
                add_paper(token, database_id, paper, keyword)
                existing_ids.add(paper.entry_id)
                added += 1
                print(f"  + {paper.title[:70]}...")
            except requests.exceptions.HTTPError as e:
                print(f"  Failed to add: {e}")
                print(f"  Notion response: {e.response.text[:500]}")
                break  # Only show first error per keyword
            except Exception as e:
                print(f"  Failed to add: {e}")
                break

    print(f"\nDone. Added {added} new paper(s).")


if __name__ == "__main__":
    main()
