#!/usr/bin/env python3
"""Fetch Google Scholar citation stats and update google-scholar-stats/*.json.

Runs inside GitHub Actions (see .github/workflows/google_scholar_crawler.yml).
The site's JS (fetch_google_scholar_stats.html) reads google-scholar-stats/gs_data.json
from the main branch, so this script commits updates back to main.

Data source priority:
  1. Scrapingdog Google Scholar Author API (stable, CAPTCHA handled server-side)
     when the SCRAPINGDOG_API_KEY env var is set.
  2. scholarly library (unreliable fallback; direct requests get CAPTCHA-blocked
     after a handful of calls).
"""

import json
import os
import signal
import sys
import time
from datetime import date

import requests

from scholarly import scholarly

# Disable scholarly's built-in free-proxy pool: those proxies frequently hang
# for many minutes on GitHub runners. Direct connections fail fast instead.
scholarly.use_proxy = False

# Scholar author ID; falls back to the default if the secret is unset.
AUTHOR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "edyJPQQAAAAJ")

# Manual citation overrides: full paper id ("author_id:pub_id") -> citation count.
# These win over whatever the crawler returns. Only for cases that really cannot
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

# Version-split papers whose other version (the one with the real citations) is
# NOT returned by the author API. We look it up through the Scholar *search* API
# to get its real citation count on every run (no hardcoded numbers).
# display_key -> (search_query, [keywords to match the result item])
SEARCH_LOOKUPS = {
    "edyJPQQAAAAJ:W7OEmFMy1HYC": (
        "Can Generated Images Serve as a Viable Modality for Text-Centric Multimodal Learning",
        ["Generated Images Serve as a Viable Modality"],
    ),
}

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "google-scholar-stats",
)
GS_DATA_PATH = os.path.join(DATA_PATH, "gs_data.json")
SHIELDSIO_PATH = os.path.join(DATA_PATH, "gs_data_shieldsio.json")


def _parse_cites_per_year(payload) -> dict:
    """Pull {year: count} from scholarly / Scrapingdog author payloads."""
    if not isinstance(payload, dict):
        return {}
    out = {}

    def _ingest_map(raw):
        if not isinstance(raw, dict):
            return
        for key, value in raw.items():
            try:
                out[str(int(key))] = int(str(value).replace(",", ""))
            except (TypeError, ValueError):
                continue

    def _ingest_graph(graph):
        if not isinstance(graph, list):
            return
        for item in graph:
            if not isinstance(item, dict):
                continue
            year = item.get("year") or item.get("label")
            cites = item.get("citations")
            if cites is None:
                cites = item.get("value", item.get("cited"))
            try:
                out[str(int(year))] = int(str(cites).replace(",", ""))
            except (TypeError, ValueError):
                continue

    _ingest_map(payload.get("cites_per_year"))
    for key in ("graph", "cited_by_graph", "citation_graph"):
        _ingest_graph(payload.get(key))

    cited_by = payload.get("cited_by")
    if isinstance(cited_by, dict):
        _ingest_map(cited_by.get("cites_per_year"))
        _ingest_graph(cited_by.get("graph"))
        _ingest_graph(cited_by.get("table"))

    author = payload.get("author")
    if isinstance(author, dict):
        _ingest_map(author.get("cites_per_year"))
        author_cited = author.get("cited_by")
        if isinstance(author_cited, dict):
            _ingest_map(author_cited.get("cites_per_year"))
            _ingest_graph(author_cited.get("graph"))

    return out


def _parse_int(value):
    if value is None:
        return None
    if isinstance(value, dict):
        value = value.get("all") or value.get("value") or value.get("total")
    try:
        return int(str(value).replace(",", ""))
    except (TypeError, ValueError):
        return None


def _since_value(value):
    if not isinstance(value, dict):
        return None
    for key, raw in value.items():
        if str(key).startswith("since"):
            return _parse_int(raw)
    return None


def _parse_indices(payload) -> dict:
    """Pull h-index / i10-index / 5-year citation totals from an author payload."""
    out = {}
    if not isinstance(payload, dict):
        return out

    def take(key, raw, since_key=None, since_raw=None):
        parsed = _parse_int(raw)
        if parsed is not None:
            out[key] = parsed
        if since_key:
            parsed_since = _parse_int(since_raw)
            if parsed_since is not None:
                out[since_key] = parsed_since

    take("hindex", payload.get("hindex") or payload.get("h_index"))
    take("i10index", payload.get("i10index") or payload.get("i10_index"))
    take("citedby_5y", payload.get("citedby5y") or payload.get("citedby_5y"))

    tables = []
    cited_by = payload.get("cited_by")
    if isinstance(cited_by, dict) and isinstance(cited_by.get("table"), list):
        tables.extend(cited_by["table"])
    author = payload.get("author")
    if isinstance(author, dict):
        take("hindex", author.get("hindex") or author.get("h_index"))
        take("i10index", author.get("i10index") or author.get("i10_index"))
        take("citedby_5y", author.get("citedby5y") or author.get("citedby_5y"))
        author_cited = author.get("cited_by")
        if isinstance(author_cited, dict) and isinstance(author_cited.get("table"), list):
            tables.extend(author_cited["table"])

    for row in tables:
        if not isinstance(row, dict):
            continue
        for name, key, since_key in (
            ("citations", "citedby", "citedby_5y"),
            ("cited_by", "citedby", "citedby_5y"),
            ("h_index", "hindex", "hindex_5y"),
            ("hindex", "hindex", "hindex_5y"),
            ("i10_index", "i10index", "i10index_5y"),
            ("i10index", "i10index", "i10index_5y"),
        ):
            if name not in row:
                continue
            raw = row[name]
            # Year-graph rows look like {year, citations: 27}; skip those.
            if name in ("citations", "cited_by") and not isinstance(raw, dict):
                continue
            take(key, raw, since_key, _since_value(raw) if isinstance(raw, dict) else None)

    return out


def _parse_cited_by(value) -> int:
    """Extract an integer citation count from Scrapingdog's cited_by shapes
    (e.g. {"total": "Cited by 3031"} or {"value": "3031"} or a raw number)."""
    if isinstance(value, dict):
        value = value.get("total") or value.get("value") or 0
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return int(digits) if digits else 0


def fetch_via_scrapingdog() -> tuple[str, int, dict, dict, dict] | None:
    """Fetch the author profile via Scrapingdog's Google Scholar Author API.

    Returns (name, citedby, publications, cites_per_year, indices) or None when
    no API key is configured. citation_id values already have the
    "author_id:pub_id" format we store.
    """
    api_key = os.environ.get("SCRAPINGDOG_API_KEY", "")
    if not api_key:
        return None
    url = "https://api.scrapingdog.com/google_scholar/author"
    params = {"api_key": api_key, "author_id": AUTHOR_ID, "results": 100, "language": "en"}
    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    publications = {}
    print(f"Scrapingdog returned {len(data.get('articles', []))} article row(s):")
    for art in data.get("articles", []):
        cid = art.get("citation_id", "")
        if not cid:
            continue
        cited = art.get("cited_by", 0)
        if isinstance(cited, dict):
            cited = cited.get("value", 0)
        print(f"  - {cid} | cited_by={cited} | {art.get('title', '')[:70]}")
        try:
            num = int(str(cited).replace(",", ""))
        except (TypeError, ValueError):
            num = 0
        publications[cid] = {"num_citations": num, "title": art.get("title", "")}

    # Look up the missing version(s) of version-split papers via Scholar search,
    # so their merged total uses REAL citation numbers (no hardcoded values).
    for display_key, (search_query, match_kw) in SEARCH_LOOKUPS.items():
        try:
            sresp = requests.get(
                "https://api.scrapingdog.com/google_scholar",
                params={"api_key": api_key, "query": search_query, "language": "en", "results": 10},
                timeout=60,
            )
            sresp.raise_for_status()
            sdata = sresp.json()
        except Exception as exc:  # noqa: BLE001 - lookup is best-effort
            print(f"SEARCH_LOOKUPS: search failed for {display_key}: {exc!r}")
            continue
        best = None
        for item in sdata.get("scholar_results", []):
            title = item.get("title", "")
            if any(kw.lower() in title.lower() for kw in match_kw):
                best = item
                break
        if best is None:
            print(f"SEARCH_LOOKUPS: no matching result for {display_key}")
            continue
        pid = best.get("id", "")
        cited = _parse_cited_by(best.get("inline_links", {}).get("cited_by", {}))
        if pid:
            key = f"{AUTHOR_ID}:{pid}"
            publications[key] = {"num_citations": cited, "title": best.get("title", "")}
            print(f"SEARCH_LOOKUPS: {key} = {cited} citations (real value)")

    # Author-level total citations: look in several possible response fields.
    citedby = 0
    for cand in (
        data.get("cited_by"),
        data.get("citedby"),
        data.get("author", {}).get("cited_by"),
        data.get("author", {}).get("citations"),
    ):
        if cand is None:
            continue
        if isinstance(cand, dict):
            cand = cand.get("value", 0)
        try:
            citedby = int(str(cand).replace(",", ""))
            break
        except (TypeError, ValueError):
            continue
    if not citedby:
        citedby = sum(p["num_citations"] for p in publications.values())

    name = data.get("author", {}).get("name", "Unknown")
    return name, citedby, publications, _parse_cites_per_year(data), _parse_indices(data)


def fetch_via_scholarly() -> tuple[str, int, dict, dict, dict]:
    """Fallback: direct scholarly scrape (unreliable, CAPTCHA-prone)."""
    # scholarly >= 1.x renamed search_author_by_id -> search_author_id.
    search_author = getattr(scholarly, "search_author_id", None)
    if search_author is None:
        search_author = scholarly.search_author_by_id
    author = search_author(AUTHOR_ID)
    if author is None:
        sys.exit("Could not find author with id " + AUTHOR_ID)
    author = scholarly.fill(author, sections=["basics", "indices", "publications"])

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
    return name, citedby, publications, _parse_cites_per_year(author), _parse_indices(author)


def main() -> None:
    if os.environ.get("SCRAPINGDOG_API_KEY"):
        fetched = fetch_via_scrapingdog()
        if fetched is None:
            sys.exit("Scrapingdog fetch failed (empty response)")
        name, citedby, publications, cites_per_year, indices = fetched
        print(f"Fetched via Scrapingdog: {name}: {citedby} total citations, {len(publications)} publications")
    else:
        name, citedby, publications, cites_per_year, indices = fetch_via_scholarly()
        print(f"Fetched via scholarly: {name}: {citedby} total citations, {len(publications)} publications")
    if not cites_per_year:
        cites_per_year = {}
    if not indices:
        indices = {}

    # Keep manually-maintained entries (papers not yet indexed on Scholar).
    old = {}
    if os.path.exists(GS_DATA_PATH):
        with open(GS_DATA_PATH, encoding="utf-8") as f:
            old = json.load(f)
        for key, value in old.get("publications", {}).items():
            if key.startswith("manual:") and key not in publications:
                publications[key] = value
                print(f"Preserved manual entry: {key}")
        if not cites_per_year:
            cites_per_year = old.get("cites_per_year") or {}
            if cites_per_year:
                print("Kept previous cites_per_year (graph missing from this fetch)")
        for key in ("citedby_5y", "hindex", "hindex_5y", "i10index", "i10index_5y", "since_year"):
            if indices.get(key) is None and old.get(key) is not None:
                indices[key] = old[key]

    # Apply manual overrides (e.g. merged/duplicate Scholar rows summed by hand).
    for key, count in CITATION_OVERRIDES.items():
        if key in publications:
            publications[key]["num_citations"] = count
        else:
            publications[key] = {"num_citations": count, "title": ""}
        print(f"Applied manual citation override: {key} = {count}")

    # Merge Scholar rows that belong to the same paper into a single entry.
    # The citation counts of all matching rows are summed on every run, so the
    # total tracks Scholar whenever the rows are returned.
    for display_key, (fixed_title, keywords) in MERGE_RULES.items():
        keys = [
            k for k in publications
            if any(kw.lower() in publications[k].get("title", "").lower() for kw in keywords)
        ]
        if not keys:
            # If this paper is in SEARCH_LOOKUPS but the lookup failed, keep the
            # last real value instead of dropping the paper or showing 0.
            if display_key in SEARCH_LOOKUPS:
                prev = old.get("publications", {}).get(display_key, {}).get("num_citations", 0)
                if prev > 0:
                    publications[display_key] = {"num_citations": prev, "title": fixed_title}
                    print(f"Kept previous real value {prev} for {display_key} (lookup unavailable)")
                    continue
            print(f"MERGE_RULES: no Scholar rows matched {display_key}, leaving as-is")
            continue
        total = sum(publications[k]["num_citations"] for k in keys)
        # If the merged total is 0 for a paper whose other version is fetched via
        # SEARCH_LOOKUPS, the lookup likely failed: keep the last real value.
        if total == 0 and display_key in SEARCH_LOOKUPS:
            prev = old.get("publications", {}).get(display_key, {}).get("num_citations", 0)
            if prev > 0:
                total = prev
                print(f"Kept previous real value {prev} for {display_key} (lookup unavailable or zero)")
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
        "citedby_5y": indices.get("citedby_5y", citedby),
        "hindex": indices.get("hindex"),
        "hindex_5y": indices.get("hindex_5y", indices.get("hindex")),
        "i10index": indices.get("i10index"),
        "i10index_5y": indices.get("i10index_5y", indices.get("i10index")),
        "since_year": indices.get("since_year", date.today().year - 5),
        "updated": date.today().isoformat(),
        "cites_per_year": cites_per_year,
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
    # Hard per-attempt timeout: neither data source has a reliable built-in one.
    class FetchTimeout(Exception):
        pass

    def _timeout(signum, frame):
        raise FetchTimeout("Google Scholar fetch exceeded 300s")

    signal.signal(signal.SIGALRM, _timeout)

    # Retry a few times with backoff.
    for attempt in range(1, 4):
        signal.alarm(300)  # max 5 minutes per attempt
        try:
            main()
            signal.alarm(0)
            break
        except Exception as exc:  # noqa: BLE001 - surface any fetch failure
            signal.alarm(0)
            print(f"Attempt {attempt} failed: {exc!r}", file=sys.stderr)
            if attempt == 3:
                sys.exit("Google Scholar fetch failed after 3 attempts")
            time.sleep(30 * attempt)
