#!/usr/bin/env python3
"""Fetch Google Scholar citation stats and update google-scholar-stats/*.json.

Runs inside GitHub Actions (see .github/workflows/google_scholar_crawler.yml).
The site's JS (fetch_google_scholar_stats.html) reads google-scholar-stats/gs_data.json
from the main branch, so this script commits updates back to main.
"""

import json
import os
import sys
import time
from datetime import date

from scholarly import scholarly

# Scholar author ID; falls back to the default if the secret is unset.
AUTHOR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "edyJPQQAAAAJ")

# Manual citation overrides: full paper id ("author_id:pub_id") -> citation count.
# These win over whatever scholarly returns. Only for cases that really cannot
# be handled automatically (e.g. a number you want pinned forever).
CITATION_OVERRIDES = {}

# Scholar sometimes lists two versions of the same paper as separate rows.
# Merge them into ONE site entry: sum the citation counts, keep the newest title.
# display_key -> (fixed_title, [keywords that match all rows of this paper])
MERGE_RULES = {
    # arXiv v1/ICML title: "Can Generated Images Serve as a Viable Modality for
    # Text-Centric Multimodal Learning?"  |  v2 (newest): "Synthetic Perception: ..."
    "edyJPQQAAAAJ:W7OEmFMy1HYC": (
        "Synthetic Perception: Can Generated Images Unlock Latent Visual Prior for Text-Centric Reasoning?",
        ["Synthetic Perception", "Generated Images Serve as a Viable Modality"],
    ),
}

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "google-scholar-stats",
)
GS_DATA_PATH = os.path.join(DATA_PATH, "gs_data.json")
SHIELDSIO_PATH = os.path.join(DATA_PATH, "gs_data_shieldsio.json")


def main() -> None:
    author = scholarly.search_author_by_id(AUTHOR_ID)
    if author is None:
        sys.exit("Could not find author with id " + AUTHOR_ID)
    author = scholarly.fill(author, sections=["basics", "publications"])

    name = author.get("name", "Unknown")
    citedby = int(author.get("citedby", 0))
    publications = {}
    for pub in author.get("publications", []):
        pub_id = pub.get("author_pub_id")
        if not pub_id:
            continue
        publications[f"{AUTHOR_ID}:{pub_id}"] = {
            "num_citations": int(pub.get("num_citations", 0)),
            "title": pub.get("bib", {}).get("title", ""),
        }
    print(f"Fetched {name}: {citedby} total citations, {len(publications)} publications")

    # Keep manually-maintained entries (papers not yet indexed on Scholar).
    if os.path.exists(GS_DATA_PATH):
        with open(GS_DATA_PATH, encoding="utf-8") as f:
            old = json.load(f)
        for key, value in old.get("publications", {}).items():
            if key.startswith("manual:") and key not in publications:
                publications[key] = value
                print(f"Preserved manual entry: {key}")

    # Apply manual overrides (e.g. merged/duplicate Scholar rows summed by hand).
    for key, count in CITATION_OVERRIDES.items():
        if key in publications:
            publications[key]["num_citations"] = count
        else:
            publications[key] = {"num_citations": count, "title": ""}
        print(f"Applied manual citation override: {key} = {count}")

    # Merge Scholar rows that belong to the same paper into a single entry.
    # The citation counts of all matching rows are summed on every run, so the
    # total always tracks Scholar (nothing is hardcoded).
    for display_key, (fixed_title, keywords) in MERGE_RULES.items():
        keys = [
            k for k in publications
            if any(kw.lower() in publications[k].get("title", "").lower() for kw in keywords)
        ]
        if not keys:
            print(f"MERGE_RULES: no Scholar rows matched {display_key}, leaving as-is")
            continue
        total = sum(publications[k]["num_citations"] for k in keys)
        for k in keys:
            if k != display_key:
                del publications[k]
        publications[display_key] = {
            "num_citations": total,
            "title": fixed_title,
        }
        print(f"Merged {len(keys)} Scholar row(s) into {display_key}: total = {total}")

    data = {
        "name": name,
        "citedby": citedby,
        "updated": date.today().isoformat(),
        "publications": publications,
    }
    with open(GS_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    shieldsio = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citedby),
    }
    with open(SHIELDSIO_PATH, "w", encoding="utf-8") as f:
        json.dump(shieldsio, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("Updated google-scholar-stats/gs_data.json and gs_data_shieldsio.json")


if __name__ == "__main__":
    # Scholar is aggressive with rate limiting; retry a few times with backoff.
    for attempt in range(1, 4):
        try:
            main()
            break
        except Exception as exc:  # noqa: BLE001 - surface any fetch failure
            print(f"Attempt {attempt} failed: {exc!r}", file=sys.stderr)
            if attempt == 3:
                sys.exit("Google Scholar fetch failed after 3 attempts")
            time.sleep(30 * attempt)
