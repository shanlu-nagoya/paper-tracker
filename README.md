# Paper Tracker

A personal research paper tracking system that automatically fetches new papers from [Semantic Scholar](https://www.semanticscholar.org/), organizes them by topic, generates markdown summaries, and provides a local search tool.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Quick Start: Search Only (Another Computer)](#quick-start-search-only-another-computer)
- [Full Setup: Running the Tracker](#full-setup-running-the-tracker)
- [Search Tool Usage](#search-tool-usage)
- [Research Topics](#research-topics)
- [Output Files](#output-files)

---

## Project Structure

```
paper-tracker/
├── paper_tracker.py        # Main script — fetches papers from Semantic Scholar
├── papers_index.csv        # Central database (all papers)
├── scripts/
│   └── search_papers.py    # Local search tool
├── paper_summaries/        # Auto-generated markdown summaries, by topic
│   ├── 01_intent_communication/
│   ├── 02_v2x_safety/
│   ├── 03_vlc_isc/
│   ├── 04_mission_reliability/
│   ├── 05_non_ergodic_channels/
│   ├── 06_importance_aware_coding/
│   └── 07_ai_for_comm_design/
├── weekly_reports/         # Auto-generated weekly reports
├── templates/              # Markdown templates
└── pdfs/                   # (Manual) store PDF files here
```

---

## Quick Start: Search Only (Another Computer)

If you only want to **search the existing paper database** on a new machine, you do not need any API keys or a full setup. Follow these steps:

### Step 1 — Install Python

Make sure Python 3.8 or later is installed.

```bash
python --version
```

Download from https://www.python.org/downloads/ if needed.

### Step 2 — Get the project files

**Option A — Clone from GitHub (recommended):**

```bash
git clone <your-repo-url>
cd paper-tracker
```

**Option B — Copy files manually:**

Copy the following files/folders from the original machine to the new machine, preserving the folder structure:

```
paper-tracker/
├── papers_index.csv          ← required
├── scripts/search_papers.py  ← required
└── paper_summaries/          ← optional, for reading full summaries
```

### Step 3 — No installation needed

The search tool only uses Python's built-in libraries (`csv`, `argparse`, `pathlib`). No `pip install` required.

### Step 4 — Run a search

Open a terminal, navigate to the `paper-tracker` folder, and run:

```bash
python scripts/search_papers.py "VLC"
```

---

## Full Setup: Running the Tracker

Follow this if you want to **fetch new papers** from Semantic Scholar automatically.

### Step 1 — Clone the repository

```bash
git clone <your-repo-url>
cd paper-tracker
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

This installs `requests`, the only external dependency.

### Step 3 — Run the tracker

```bash
python paper_tracker.py
```

The script will:

1. Query Semantic Scholar for papers published in the last 8 days across all configured topics
2. Skip papers already in `papers_index.csv`
3. Append new papers to `papers_index.csv`
4. Generate a markdown summary for each new paper in `paper_summaries/<topic>/`
5. Generate a weekly report in `weekly_reports/`

> **Note:** The script respects Semantic Scholar's rate limit with a 1-second delay between API calls. No API key is required.

---

## Search Tool Usage

All searches are run from the `paper-tracker/` directory.

### Basic keyword search

```bash
python scripts/search_papers.py "VLC"
```

### Multiple keywords — AND logic (default)

Returns papers that contain **all** of the keywords:

```bash
python scripts/search_papers.py "VLC" "RIS"
python scripts/search_papers.py "VLC" "channel estimation" "deep learning"
```

### Multiple keywords — OR logic

Returns papers that contain **any** of the keywords:

```bash
python scripts/search_papers.py "VLC" "LiFi" --any
```

### Filter by topic folder

```bash
python scripts/search_papers.py --topic 03_vlc_isc
python scripts/search_papers.py "RIS" --topic 01_intent_communication
```

### Filter by year

```bash
python scripts/search_papers.py "VLC" --year 2025
python scripts/search_papers.py --year 2026
```

### Filter by author

```bash
python scripts/search_papers.py --author "Wang"
python scripts/search_papers.py "VLC" --author "Li"
```

### Combine filters

```bash
python scripts/search_papers.py "VLC" "RIS" --year 2026 --author "Zhang"
python scripts/search_papers.py --topic 03_vlc_isc --year 2025
```

### Example output

```
Found 3 paper(s):
------------------------------------------------------------
[03_vlc_isc] Adaptive partitioning for reconfigurable intelligent surface aided integrated sensing and communication (2026)
  Authors : Mert Ilgüy, Berna Özbek
  Venue   : Physical Communication
  Added   : 2026-04-29
  Summary : paper_summaries/03_vlc_isc/368a9bec_Adaptive_partitioning_for_reconfigurable_intelligent_surface.md
  PDF     : (Google Drive link if available)
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

## Output Files

| File / Folder | Description |
|---------------|-------------|
| `papers_index.csv` | Master database — one row per paper with title, authors, year, venue, topic, abstract snippet, links, and path to summary |
| `paper_summaries/<topic>/<id>_<title>.md` | Individual paper summary with metadata, abstract, and a notes section |
| `weekly_reports/<date>_weekly_report.md` | Weekly digest grouped by topic |

---

## Requirements

- Python 3.8+
- `requests>=2.31.0` (only needed for `paper_tracker.py`, not for search)
