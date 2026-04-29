# Paper Tracker

A research paper tracking system that automatically fetches new papers from [Semantic Scholar](https://www.semanticscholar.org/), organizes them by topic, and provides a local search tool.

---

## For Students: How to Use

### Step 1 — Install Python (one time only)

Download and install Python 3.8 or later from https://www.python.org/downloads/

Check it works:
```bash
python --version
```

### Step 2 — Clone this repository (one time only)

```bash
git clone https://github.com/shanlu-nagoya/paper-tracker.git
cd paper-tracker
```

### Step 3 — Search for papers

Open a terminal in the `paper-tracker` folder and run:

```bash
# Single keyword
python scripts/search_papers.py "VLC"

# Multiple keywords — AND logic (must match all)
python scripts/search_papers.py "VLC" "RIS"

# Multiple keywords — OR logic (match any)
python scripts/search_papers.py "VLC" "LiFi" --any

# Filter by topic
python scripts/search_papers.py --topic 03_vlc_isc

# Filter by year
python scripts/search_papers.py "VLC" --year 2026

# Filter by author
python scripts/search_papers.py --author "Wang"

# Combine filters
python scripts/search_papers.py "VLC" "RIS" --year 2026
```

No `pip install` needed — the search tool uses only Python built-in libraries.

### Step 4 — Read the summary

The search result shows a `Summary` path like:

```
[03_vlc_isc] Adaptive partitioning for reconfigurable intelligent surface... (2026)
  Authors : Mert Ilgüy, Berna Özbek
  Venue   : Physical Communication
  Added   : 2026-04-29
  Summary : paper_summaries/03_vlc_isc/368a9bec_Adaptive_partitioning_...md
```

Open that `.md` file to read the abstract, metadata, and notes.

### Step 5 — Read the full PDF

Open the shared OneDrive folder and find the PDF under `pdfs/<topic>/`.
Papers that are open-access (e.g., arXiv) are downloaded automatically.
Others need to be accessed via the journal website.

### Step 6 — Sync new papers (run weekly)

When new papers are added to the database, just run:

```bash
git pull
```

---

## Research Topics

| Folder | Topic |
|--------|-------|
| `01_intent_communication` | Intent-Aware / Semantic Communication |
| `02_v2x_safety`           | V2X Safety Communication |
| `03_vlc_isc`              | VLC and Optical Wireless / ISC |
| `04_mission_reliability`  | Mission-Critical Reliability |
| `05_non_ergodic_channels` | Non-Ergodic Channels |
| `06_importance_aware_coding` | Importance-Aware Source Coding |
| `07_ai_for_comm_design`   | AI for Communication System Design |

---

## For the Lab Manager: Updating the Database

### Fetch new papers (run weekly)

```bash
pip install -r requirements.txt   # first time only
python paper_tracker.py
```

This will:
1. Search Semantic Scholar for papers published in the last 8 days
2. Add new papers to `papers_index.csv`
3. Generate a markdown summary for each paper in `paper_summaries/<topic>/`
4. Auto-download open-access PDFs to OneDrive
5. Generate a weekly report in `weekly_reports/`

### Download PDFs for existing papers

```bash
python scripts/download_pdfs.py
```

### Commit and push updates to GitHub

```bash
git add papers_index.csv paper_summaries/ weekly_reports/
git commit -m "Weekly paper update $(date +%Y-%m-%d)"
git push
```

Students can then sync with `git pull`.
