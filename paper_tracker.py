"""
Weekly Semantic Scholar paper tracker — syncs new papers to a Notion database.
Searches papers published in the last SEARCH_DAYS days and adds any
not already present (deduplication via Semantic Scholar paper ID).
"""

import os
import sys
import time
import requests
from datetime import datetime, timedelta, timezone

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
S2_API = "https://api.semanticscholar.org/graph/v1"
SEARCH_DAYS = 8
S2_FIELDS = "title,authors,abstract,publicationDate,externalIds,paperId"

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


def ensure_schema(token: str, database_id: str) -> None:
    resp = requests.get(f"{NOTION_API}/databases/{database_id}", headers=notion_headers(token))
    resp.raise_for_status()
    existing = set(resp.json().get("properties", {}).keys())

    update: dict = {"properties": {}}

    if "Name" in existing and "Title" not in existing:
        update["properties"]["Name"] = {"name": "Title"}
        existing.add("Title")
        existing.discard("Name")

    if "arXiv ID" in existing and "Paper ID" not in existing:
        update["properties"]["arXiv ID"] = {"name": "Paper ID"}
        existing.add("Paper ID")
        existing.discard("arXiv ID")

    needed = {
        "Authors":  {"rich_text": {}},
        "Abstract": {"rich_text": {}},
        "URL":      {"url": {}},
        "Published":{"date": {}},
        "Keywords": {"multi_select": {}},
        "Paper ID": {"rich_text": {}},
    }
    for name, schema in needed.items():
        if name not in existing:
            update["properties"][name] = schema

    if update["properties"]:
        r = requests.patch(
            f"{NOTION_API}/databases/{database_id}",
            headers=notion_headers(token),
            json=update,
        )
        r.raise_for_status()
        print("Database schema updated.")


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
            prop = page["properties"].get("Paper ID", {})
            rich_text = prop.get("rich_text", [])
            if rich_text:
                existing.add(rich_text[0]["text"]["content"])
        if not data.get("has_more"):
            break
        cursor = data["next_cursor"]
    return existing


def search_papers(keyword: str, days: int = SEARCH_DAYS) -> list[dict]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")
    params = {
        "query": keyword,
        "fields": S2_FIELDS,
        "limit": 50,
        "publicationDateOrYear": f"{cutoff}:",
    }
    resp = requests.get(f"{S2_API}/paper/search", params=params)
    resp.raise_for_status()
    return resp.json().get("data", [])


def format_authors(authors: list[dict]) -> str:
    names = [a.get("name", "") for a in authors[:5]]
    result = ", ".join(names)
    if len(authors) > 5:
        result += f" et al. (+{len(authors) - 5})"
    return result


def paper_url(paper: dict) -> str:
    ext = paper.get("externalIds") or {}
    if ext.get("DOI"):
        return f"https://doi.org/{ext['DOI']}"
    if ext.get("ArXiv"):
        return f"https://arxiv.org/abs/{ext['ArXiv']}"
    return f"https://www.semanticscholar.org/paper/{paper.get('paperId', '')}"


def add_paper(token: str, database_id: str, paper: dict, keyword: str) -> None:
    title = (paper.get("title") or "Untitled")[:2000]
    authors = format_authors(paper.get("authors") or [])
    abstract = (paper.get("abstract") or "")[:2000]
    paper_id = paper.get("paperId", "")
    pub_date = paper.get("publicationDate")

    properties: dict = {
        "Title":    {"title":     [{"text": {"content": title}}]},
        "Authors":  {"rich_text": [{"text": {"content": authors[:2000]}}]},
        "Abstract": {"rich_text": [{"text": {"content": abstract}}]},
        "URL":      {"url": paper_url(paper)},
        "Keywords": {"multi_select": [{"name": keyword}]},
        "Paper ID": {"rich_text": [{"text": {"content": paper_id}}]},
    }
    if pub_date:
        properties["Published"] = {"date": {"start": pub_date}}

    resp = requests.post(
        f"{NOTION_API}/pages",
        headers=notion_headers(token),
        json={"parent": {"database_id": database_id}, "properties": properties},
    )
    if not resp.ok:
        print(f"  Notion error: {resp.text[:300]}")
    resp.raise_for_status()


def main() -> None:
    token = os.environ.get("NOTION_TOKEN")
    database_id = os.environ.get("NOTION_DATABASE_ID")
    if not token or not database_id:
        print("Error: set NOTION_TOKEN and NOTION_DATABASE_ID.")
        sys.exit(1)

    ensure_schema(token, database_id)
    existing_ids = get_existing_ids(token, database_id)
    print(f"Existing papers in Notion: {len(existing_ids)}")

    added = 0
    for keyword in KEYWORDS:
        print(f"Searching: {keyword}")
        try:
            papers = search_papers(keyword)
            time.sleep(1)
        except Exception as e:
            print(f"  Search failed: {e}")
            continue

        for paper in papers:
            paper_id = paper.get("paperId", "")
            if not paper_id or paper_id in existing_ids:
                continue
            try:
                add_paper(token, database_id, paper, keyword)
                existing_ids.add(paper_id)
                added += 1
                print(f"  + {(paper.get('title') or '')[:70]}...")
            except Exception as e:
                print(f"  Failed: {e}")

    print(f"\nDone. Added {added} new paper(s).")


if __name__ == "__main__":
    main()
```
