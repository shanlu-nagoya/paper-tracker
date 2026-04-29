"""
Local search tool for papers_index.csv

Usage:
  python scripts/search_papers.py "VLC"
  python scripts/search_papers.py --topic 03_vlc_isc
  python scripts/search_papers.py --year 2024 "channel coding"
  python scripts/search_papers.py --author "Wang"
  python scripts/search_papers.py --topic 02_v2x_safety --year 2025
"""

import csv
import argparse
from pathlib import Path

CSV_PATH = Path("papers_index.csv")


def search(query: str = "", topic: str = "", year: str = "", author: str = "") -> list:
    if not CSV_PATH.exists():
        print("papers_index.csv not found. Run paper_tracker.py first.")
        return []

    results = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            searchable = (row["title"] + row["abstract"] + row["keyword_matched"] + row["topic_folder"] + row["topic"]).lower()
            if query and query.lower() not in searchable:
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
    parser.add_argument("query", nargs="?", default="", help="Keyword in title/abstract")
    parser.add_argument("--topic", default="", help="Topic folder, e.g. 03_vlc_isc")
    parser.add_argument("--year",  default="", help="Publication year, e.g. 2024")
    parser.add_argument("--author", default="", help="Author name")
    args = parser.parse_args()

    results = search(args.query, args.topic, args.year, args.author)
    print_results(results)


if __name__ == "__main__":
    main()
