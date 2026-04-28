"""
Weekly paper tracker: searches Semantic Scholar, updates papers_index.csv,
writes Markdown summaries per topic, and generates a weekly report.
"""

import csv
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Research topics and their search keywords
# ---------------------------------------------------------------------------
TOPICS = {
    "01_intent_communication": {
        "name": "Intent-Aware Communication",
        "keywords": [
            "intent-aware communication",
            "semantic communication goal-oriented",
            "task-oriented communication wireless",
        ],
    },
    "02_v2x_safety": {
        "name": "V2X Safety",
        "keywords": [
            "V2X safety communication",
            "vehicular network reliability",
            "vehicle-to-everything cooperative driving",
        ],
    },
    "03_vlc_isc": {
        "name": "VLC and Optical Wireless",
        "keywords": [
            "visible light communication VLC",
            "optical wireless communication",
            "intelligent surface optical communication",
        ],
    },
    "04_mission_reliability": {
        "name": "Mission Reliability",
        "keywords": [
            "mission reliability wireless communication",
            "ultra-reliable low-latency URLLC",
            "mission-critical finite blocklength",
        ],
    },
    "05_non_ergodic_channels": {
        "name": "Non-Ergodic Channels",
        "keywords": [
            "non-ergodic channel capacity outage",
            "delay-sensitive communication outage probability",
            "finite blocklength non-ergodic",
        ],
    },
    "06_importance_aware_coding": {
        "name": "Importance-Aware Coding",
        "keywords": [
            "importance-aware channel coding",
            "unequal error protection source coding",
            "significance-aware wireless transmission",
        ],
    },
    "07_ai_for_comm_design": {
        "name": "AI for Communication Design",
        "keywords": [
            "deep learning physical layer design",
            "machine learning channel coding",
            "neural network autoencoder communication",
        ],
    },
}

CSV_PATH = Path("papers_index.csv")
SUMMARIES_DIR = Path("paper_summaries")
WEEKLY_DIR = Path("weekly_reports")

CSV_FIELDS = [
    "id", "title", "authors", "year", "venue",
    "topic", "topic_folder", "keyword_matched",
    "abstract", "semantic_scholar_id", "arxiv_id", "doi", "url",
    "gdrive_link", "date_added", "summary_file",
]

SS_API = "https://api.semanticscholar.org/graph/v1/paper/search"
SS_FIELDS = "paperId,title,authors,year,venue,abstract,externalIds"
DAYS_BACK = 8
RESULTS_PER_QUERY = 20


def load_existing_ids() -> set:
    if not CSV_PATH.exists():
        return set()
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return {row["semantic_scholar_id"] for row in csv.DictReader(f) if row["semantic_scholar_id"]}


def append_to_csv(rows: list) -> None:
    write_header = not CSV_PATH.exists()
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)


def search_semantic_scholar(keyword: str) -> list:
    cutoff = (datetime.now() - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")
    params = {
        "query": keyword,
        "fields": SS_FIELDS,
        "limit": RESULTS_PER_QUERY,
        "publicationDateOrYear": f"{cutoff}:",
    }
    try:
        resp = requests.get(SS_API, params=params, timeout=30)
        resp.raise_for_status()
        return resp.json().get("data", [])
    except Exception as e:
        print(f"  [ERROR] '{keyword}': {e}")
        return []


def format_authors(paper: dict) -> str:
    authors = paper.get("authors", [])
    names = [a["name"] for a in authors[:5]]
    result = ", ".join(names)
    if len(authors) > 5:
        result += f" et al. (+{len(authors) - 5})"
    return result


def make_summary_path(topic_folder: str, paper_id: str, title: str) -> Path:
    safe = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
    safe = safe.strip().replace(" ", "_")[:60]
    return SUMMARIES_DIR / topic_folder / f"{paper_id[:8]}_{safe}.md"


def write_summary(path: Path, paper: dict, topic_name: str, keyword: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    authors = format_authors(paper)
    ext = paper.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv", "")
    doi = ext.get("DOI", "")
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "N/A"
    ss_url = f"https://www.semanticscholar.org/paper/{paper.get('paperId', '')}"

    content = f"""# {paper.get('title', 'Untitled')}

## Metadata
- **Authors**: {authors}
- **Year**: {paper.get('year', 'N/A')}
- **Venue**: {paper.get('venue', 'N/A')}
- **Topic**: {topic_name}
- **Keyword matched**: `{keyword}`
- **Semantic Scholar**: {ss_url}
- **arXiv**: {arxiv_url}
- **DOI**: {doi or 'N/A'}
- **Google Drive PDF**: <!-- paste link here -->
- **Date added**: {datetime.now().strftime('%Y-%m-%d')}

## Abstract
{paper.get('abstract') or '_No abstract available._'}

## Notes
<!-- Your notes after reading -->

## Key contributions
<!-- Fill in after reading -->

## Relevance to your research
<!-- How this connects to your work -->
"""
    path.write_text(content, encoding="utf-8")


def generate_weekly_report(new_papers: list) -> None:
    WEEKLY_DIR.mkdir(exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_path = WEEKLY_DIR / f"{date_str}_weekly_report.md"

    by_topic: dict = {}
    for p in new_papers:
        by_topic.setdefault(p["topic_folder"], []).append(p)

    lines = [
        f"# Weekly Paper Report — {date_str}",
        "",
        f"**Total new papers this week**: {len(new_papers)}",
        "",
    ]

    for folder in sorted(by_topic):
        papers = by_topic[folder]
        topic_name = TOPICS[folder]["name"]
        lines.append(f"## {topic_name} ({len(papers)})")
        lines.append("")
        for p in papers:
            lines.append(f"- **{p['title']}** ({p['year']})")
            lines.append(f"  - Authors: {p['authors'][:100]}")
            lines.append(f"  - Keyword: `{p['keyword_matched']}`")
            lines.append(f"  - [Summary]({p['summary_file']})")
            lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Weekly report → {report_path}")


def main() -> None:
    existing_ids = load_existing_ids()
    print(f"Loaded {len(existing_ids)} existing papers.")

    new_rows = []
    next_id = len(existing_ids) + 1

    for topic_folder, topic_info in TOPICS.items():
        topic_name = topic_info["name"]
        print(f"\n[{topic_folder}] {topic_name}")
        seen_this_topic: set = set()

        for keyword in topic_info["keywords"]:
            print(f"  Searching: '{keyword}'")
            papers = search_semantic_scholar(keyword)

            for paper in papers:
                pid = paper.get("paperId", "")
                if not pid or pid in existing_ids or pid in seen_this_topic:
                    continue
                seen_this_topic.add(pid)

                authors = format_authors(paper)
                ext = paper.get("externalIds") or {}
                summary_path = make_summary_path(topic_folder, pid, paper.get("title", ""))
                write_summary(summary_path, paper, topic_name, keyword)

                row = {
                    "id": next_id,
                    "title": paper.get("title", ""),
                    "authors": authors,
                    "year": paper.get("year", ""),
                    "venue": paper.get("venue", ""),
                    "topic": topic_name,
                    "topic_folder": topic_folder,
                    "keyword_matched": keyword,
                    "abstract": (paper.get("abstract") or "")[:300].replace("\n", " "),
                    "semantic_scholar_id": pid,
                    "arxiv_id": ext.get("ArXiv", ""),
                    "doi": ext.get("DOI", ""),
                    "url": f"https://www.semanticscholar.org/paper/{pid}",
                    "gdrive_link": "",
                    "date_added": datetime.now().strftime("%Y-%m-%d"),
                    "summary_file": str(summary_path).replace("\\", "/"),
                }
                new_rows.append(row)
                next_id += 1
                print(f"    + {paper.get('title', '')[:70]}")

            time.sleep(1)

    if new_rows:
        append_to_csv(new_rows)
        generate_weekly_report(new_rows)
        print(f"\nDone. Added {len(new_rows)} new papers.")
    else:
        print("\nNo new papers this week.")


if __name__ == "__main__":
    main()
