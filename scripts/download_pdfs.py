"""
Download open-access PDFs for papers already in papers_index.csv.

Usage:
  python scripts/download_pdfs.py           # download all missing PDFs
  python scripts/download_pdfs.py --dry-run # show what would be downloaded
"""

import csv
import sys
import time
import argparse
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CSV_PATH = Path("papers_index.csv")

# University OneDrive - change if needed
# Personal: C:\Users\shanl\OneDrive
ONEDRIVE_PDF_DIR = Path(r"C:\Users\shanl\OneDrive - 国立大学法人東海国立大学機構\paper-tracker\pdfs")

SS_PAPER_API = "https://api.semanticscholar.org/graph/v1/paper/{paper_id}"


def get_open_access_url(semantic_scholar_id: str, arxiv_id: str) -> str:
    """Return a downloadable PDF URL, or empty string if not available."""
    if semantic_scholar_id:
        try:
            resp = requests.get(
                SS_PAPER_API.format(paper_id=semantic_scholar_id),
                params={"fields": "openAccessPdf,externalIds"},
                timeout=30,
            )
            if resp.ok:
                data = resp.json()
                oa = data.get("openAccessPdf") or {}
                if oa.get("url"):
                    return oa["url"]
                # Also check arXiv from API response (may differ from CSV)
                ext = data.get("externalIds") or {}
                arxiv_id = arxiv_id or ext.get("ArXiv", "")
        except Exception:
            pass

    if arxiv_id:
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    return ""


def download_pdf(pdf_url: str, dest: Path) -> bool:
    try:
        resp = requests.get(
            pdf_url, timeout=60, stream=True,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        resp.raise_for_status()
        content_type = resp.headers.get("content-type", "")
        if "pdf" not in content_type and not pdf_url.lower().endswith(".pdf"):
            return False
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        print(f"    [FAIL] {e}")
        return False


def update_csv(rows: list) -> None:
    fieldnames = rows[0].keys()
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Download open-access PDFs to OneDrive")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be downloaded without downloading")
    args = parser.parse_args()

    if not CSV_PATH.exists():
        print("papers_index.csv not found.")
        return

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("No papers found.")
        return

    # Add pdf_path column if missing
    for row in rows:
        row.setdefault("pdf_path", "")

    downloaded = 0
    skipped = 0
    unavailable = 0

    for row in rows:
        title = row["title"]
        topic_folder = row["topic_folder"]
        ss_id = row["semantic_scholar_id"]
        arxiv_id = row.get("arxiv_id", "")

        # Already downloaded
        if row.get("pdf_path") and Path(row["pdf_path"]).exists():
            skipped += 1
            continue

        safe = "".join(c if c.isalnum() or c in " -_" else "" for c in title)
        safe = safe.strip().replace(" ", "_")[:60]
        filename = f"{ss_id[:8]}_{safe}.pdf"
        dest = ONEDRIVE_PDF_DIR / topic_folder / filename

        print(f"\n[{row['id']}] {title[:70]}")

        pdf_url = get_open_access_url(ss_id, arxiv_id)
        time.sleep(0.5)  # rate limit

        if not pdf_url:
            print("    [SKIP] No open-access PDF available - download manually")
            unavailable += 1
            continue

        print(f"    [URL]  {pdf_url[:80]}")

        if args.dry_run:
            print(f"    [DRY]  Would save to {dest}")
            downloaded += 1
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        if download_pdf(pdf_url, dest):
            row["pdf_path"] = str(dest)
            print(f"    [OK]   Saved → {dest.name}")
            downloaded += 1
        else:
            print("    [SKIP] Download failed - download manually")
            unavailable += 1

    if not args.dry_run:
        update_csv(rows)
        print(f"\nCSV updated with pdf_path.")

    print(f"\nDone.  Downloaded: {downloaded}  |  Already had: {skipped}  |  Not available: {unavailable}")


if __name__ == "__main__":
    main()
