"""
Local search tool for papers_index.csv

Usage:
  python scripts/search_papers.py "VLC"
  python scripts/search_papers.py "VLC" "RIS"          # AND: must match all keywords
  python scripts/search_papers.py "VLC" "RIS" --any    # OR:  match any keyword
  python scripts/search_papers.py --topic 03_vlc_isc
  python scripts/search_papers.py --year 2024 "channel coding"
  python scripts/search_papers.py --author "Wang"
  python scripts/search_papers.py --topic 02_v2x_safety --year 2025
"""

import csv
import argparse
from pathlib import Path

CSV_PATH = Path("papers_index.csv")


def search(queries: list = None, topic: str = "", year: str = "", author: str = "", match_any: bool = False) -> list:
    if not CSV_PATH.exists():
        print("papers_index.csv not found. Run paper_tracker.py first.")
        return []

    queries = [q.lower() for q in queries] if queries else []

    results = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            searchable = (row["title"] + row["abstract"] + row["keyword_matched"] + row["topic_folder"] + row["topic"]).lower()
            if queries:
                if match_any:
                    if not any(q in searchable for q in queries):
                        continue
                else:
                    if not all(q in searchable for q in queries):
                        continue
            if topic and topic.lower() not in row["topic_folder"].lower():
                continue
            if year and str(row["year"]) != str(year):
                continue
            if author and author.lower() not in row["authors"].lower():
                continue
            results.append(row)
    return results


def print_results(results: list) -> None:
    if not results:
        print("No papers found.")
        return
    print(f"\nFound {len(results)} paper(s):\n" + "-" * 60)
    for r in results:
        print(f"[{r['topic_folder']}] {r['title']} ({r['year']})")
        print(f"  Authors : {r['authors'][:90]}")
        print(f"  Venue   : {r['venue'] or 'N/A'}")
        print(f"  Added   : {r['date_added']}")
        print(f"  Summary : {r['summary_file']}")
        if r["gdrive_link"]:
            print(f"  PDF     : {r['gdrive_link']}")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Search papers_index.csv")
    parser.add_argument("query", nargs="*", help="One or more keywords (default: AND logic)")
    parser.add_argument("--any",    dest="match_any", action="store_true", help="OR logic: match any keyword")
    parser.add_argument("--topic",  default="", help="Topic folder, e.g. 03_vlc_isc")
    parser.add_argument("--year",   default="", help="Publication year, e.g. 2024")
    parser.add_argument("--author", default="", help="Author name")
    args = parser.parse_args()

    results = search(args.query, args.topic, args.year, args.author, args.match_any)
    print_results(results)


if __name__ == "__main__":
    main()
