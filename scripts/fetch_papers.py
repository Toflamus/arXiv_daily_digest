"""Daily paper fetcher: arXiv + Nature/Science RSS, score and write top 30 to raw/papers_YYYY-MM-DD.json."""
import json
import os
import re
import sys
import traceback
from datetime import datetime, timedelta, timezone

import arxiv
import feedparser

ARXIV_CATEGORIES = [
    "cs.LG", "cs.AI", "cs.CL", "cs.RO",
    "q-bio.BM", "cond-mat.mtrl-sci", "physics.chem-ph",
]
ARXIV_LOOKBACK_HOURS = 48
ARXIV_MAX_RESULTS = 500
JOURNAL_LOOKBACK_DAYS = 7

JOURNALS = {
    "Nature": ("https://www.nature.com/nature.rss", 5),
    "Science": ("https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science", 5),
    "Science Advances": ("https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=sciadv", 3),
    "Nature Machine Intelligence": ("https://www.nature.com/natmachintell.rss", 3),
    "Nature Computational Science": ("https://www.nature.com/natcomputsci.rss", 3),
    "Nature Methods": ("https://www.nature.com/nmeth.rss", 3),
    "Nature Materials": ("https://www.nature.com/nmat.rss", 3),
    "Nature Chemistry": ("https://www.nature.com/nchem.rss", 3),
    "Nature Chemical Engineering": ("https://www.nature.com/natchemeng.rss", 3),
    "Nature Biomedical Engineering": ("https://www.nature.com/natbiomedeng.rss", 3),
}

KW_LLM = [
    "large language model", "llm", "foundation model", "agent", "multi-agent", "rag",
    "reasoning", "chain-of-thought", "alignment", "rlhf", "fine-tuning",
    "in-context learning", "long context", "mixture of experts",
]
KW_LAB = [
    "self-driving lab", "autonomous experiment", "robotic chemistry",
    "closed-loop optimization", "lab automation", "bayesian experimental design",
    "autonomous discovery",
]
KW_AI4S = [
    "ai for science", "materials discovery", "protein structure", "drug discovery",
    "molecular dynamics", "scientific discovery", "equivariant",
    "geometric deep learning", "simulation",
]
KW_INST = [
    "deepmind", "google research", "openai", "anthropic", "meta ai", "fair",
    "microsoft research", "mit", "stanford", "berkeley", "cmu", "tsinghua",
    "peking university", "eth",
]
ALL_KW = KW_LLM + KW_LAB + KW_AI4S


def fetch_arxiv():
    query = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
    search = arxiv.Search(
        query=query,
        max_results=ARXIV_MAX_RESULTS,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    cutoff = datetime.now(timezone.utc) - timedelta(hours=ARXIV_LOOKBACK_HOURS)
    out = []
    fetched = 0
    for r in arxiv.Client(page_size=100, delay_seconds=3, num_retries=3).results(search):
        fetched += 1
        if r.published < cutoff:
            continue
        out.append({
            "id": r.entry_id.rsplit("/", 1)[-1],
            "title": r.title.strip(),
            "authors": [a.name for a in r.authors],
            "abstract": r.summary.strip(),
            "categories": r.categories,
            "submitted": r.published.isoformat(),
            "source": "arXiv",
            "link": r.entry_id,
            "journal_boost": 0,
        })
    return out, fetched


def fetch_journal(name, url, boost):
    cutoff = datetime.now(timezone.utc) - timedelta(days=JOURNAL_LOOKBACK_DAYS)
    feed = feedparser.parse(url)
    out = []
    for e in feed.entries:
        try:
            pub = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
        except (TypeError, AttributeError):
            pub = cutoff
        if pub < cutoff:
            continue
        link = getattr(e, "link", "")
        doi_match = re.search(r"10\.\d{4,9}/[^\s\"<>?#]+", link)
        abstract = re.sub(r"<[^>]+>", "", getattr(e, "summary", "")).strip()
        out.append({
            "id": doi_match.group(0) if doi_match else (getattr(e, "id", link) or link),
            "title": e.title.strip(),
            "authors": [],
            "abstract": abstract[:3000],
            "submitted": pub.isoformat(),
            "source": name,
            "link": link,
            "journal_boost": boost,
        })
    return out


def score(p):
    t = p["title"].lower()
    a = p["abstract"].lower()
    authors = " ".join(p.get("authors", [])).lower()
    s = 0
    for kw in ALL_KW:
        s += 2 * t.count(kw) + a.count(kw)
    s += sum(1 for inst in KW_INST if inst in authors)
    s += p["journal_boost"]
    return s


def main():
    arxiv_papers = []
    arxiv_error = None
    try:
        print("Fetching arXiv...", flush=True)
        arxiv_papers, fetched_total = fetch_arxiv()
        print(f"  arXiv: API returned {fetched_total} results, {len(arxiv_papers)} within {ARXIV_LOOKBACK_HOURS}h cutoff", flush=True)
    except Exception as e:
        arxiv_error = f"{type(e).__name__}: {e}"
        traceback.print_exc()

    journal_papers = []
    journal_status = {}
    for name, (url, boost) in JOURNALS.items():
        try:
            print(f"Fetching {name}...", flush=True)
            ps = fetch_journal(name, url, boost)
            journal_papers.extend(ps)
            journal_status[name] = len(ps)
        except Exception as e:
            journal_status[name] = f"error: {type(e).__name__}: {e}"
            print(f"  ERROR {name}: {e}", flush=True)

    seen = set()
    deduped = []
    for p in arxiv_papers + journal_papers:
        if p["id"] in seen:
            continue
        seen.add(p["id"])
        p["score"] = score(p)
        deduped.append(p)
    deduped.sort(key=lambda p: p["score"], reverse=True)
    top30 = deduped[:30]

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs("raw", exist_ok=True)
    out_path = f"raw/papers_{date_str}.json"
    payload = {
        "date": date_str,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "arxiv_count": len(arxiv_papers),
            "arxiv_error": arxiv_error,
            "journal_counts": journal_status,
            "total_after_dedup": len(deduped),
            "top_n": len(top30),
        },
        "top30": top30,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out_path} ({len(top30)} top / {len(deduped)} dedup)", flush=True)

    if not deduped:
        print("WARNING: no papers fetched from any source", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
