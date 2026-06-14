#!/usr/bin/env python3
"""Merge configured RSS/Atom feeds with approved BreastScreening-AI milestones."""

from __future__ import annotations

import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "assets/data/news-feeds.json"
MANUAL_PATH = ROOT / "assets/data/news-manual.json"
OUTPUT_PATH = ROOT / "assets/data/news.json"


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def clean_text(value: str | None, maximum: int = 280) -> str:
    parser = TextExtractor()
    parser.feed(html.unescape(value or ""))
    text = re.sub(r"\s+", " ", " ".join(parser.parts)).strip()
    if len(text) <= maximum:
        return text
    return text[: maximum - 1].rsplit(" ", 1)[0] + "..."


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, *names: str) -> str:
    wanted = {name.lower() for name in names}
    for child in element:
        if local_name(child.tag) in wanted and child.text:
            return child.text.strip()
    return ""


def entry_link(element: ET.Element) -> str:
    direct = child_text(element, "link")
    if direct:
        return direct
    for child in element:
        if local_name(child.tag) == "link":
            href = child.attrib.get("href", "")
            rel = child.attrib.get("rel", "alternate")
            if href and rel in ("alternate", ""):
                return href
    return ""


def iso_date(value: str) -> str:
    if not value:
        return datetime.now(timezone.utc).date().isoformat()
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        return parsed.date().isoformat()
    except (TypeError, ValueError):
        pass
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return datetime.now(timezone.utc).date().isoformat()


def parse_feed(xml_bytes: bytes, source: dict[str, object]) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes)
    entries = [element for element in root.iter() if local_name(element.tag) in ("item", "entry")]
    items: list[dict[str, str]] = []

    for entry in entries:
        title = clean_text(child_text(entry, "title"), 180)
        url = entry_link(entry)
        if not title or not url:
            continue
        description = child_text(entry, "description", "summary", "content", "encoded")
        date = child_text(entry, "pubdate", "published", "updated", "date")
        items.append(
            {
                "date": iso_date(date),
                "type": str(source.get("type", "News")),
                "title": title,
                "summary": clean_text(description) or "Read the complete update at the original source.",
                "url": url,
                "linkLabel": "Read the update",
                "source": str(source.get("name", "RSS feed")),
            }
        )
    return items


def fetch_feed(source: dict[str, object]) -> list[dict[str, str]]:
    request = urllib.request.Request(
        str(source["url"]),
        headers={"User-Agent": "BreastScreening-AI-News/1.0 (+https://breastscreeningai.github.io/)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return parse_feed(response.read(), source)


def excluded(item: dict[str, str], patterns: list[str]) -> bool:
    title = item.get("title", "")
    return any(re.search(pattern, title, flags=re.IGNORECASE) for pattern in patterns)


def deduplicate(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    output: list[dict[str, str]] = []
    for item in sorted(items, key=lambda record: record.get("date", ""), reverse=True):
        key = item.get("url", "").rstrip("/").lower() or item.get("title", "").lower()
        if not key or key in seen:
            continue
        seen.add(key)
        output.append(item)
    return output


def main() -> int:
    config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    manual = json.loads(MANUAL_PATH.read_text(encoding="utf-8"))
    feed_items: list[dict[str, str]] = []
    failures: list[str] = []

    for source in config.get("feeds", []):
        if not source.get("enabled"):
            continue
        try:
            feed_items.extend(fetch_feed(source))
        except Exception as error:  # Preserve approved content when an external feed is unavailable.
            failures.append(f"{source.get('name', 'RSS feed')}: {error}")

    maximum = int(config.get("maximumFeedItems", 20))
    patterns = [str(pattern) for pattern in config.get("excludeTitlePatterns", [])]
    accepted_feed_items = [item for item in feed_items if not excluded(item, patterns)][:maximum]
    merged = deduplicate(manual + accepted_feed_items)
    OUTPUT_PATH.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {len(merged)} news items ({len(manual)} approved, {len(accepted_feed_items)} from feeds).")
    if failures:
        print("Feed warnings: " + "; ".join(failures), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
