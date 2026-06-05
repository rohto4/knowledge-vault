from __future__ import annotations

import argparse
import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


@dataclass
class Note:
    path: str
    title: str
    type: str
    status: str
    topic: str
    tags: str
    source: str
    created: str
    updated: str
    confidence: str
    review_after: str
    body: str
    mtime: str


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip('"').strip("'") for part in inner.split(",")]
    return value.strip('"').strip("'")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end() :]
    data: dict[str, Any] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(line[4:].strip().strip('"').strip("'"))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(value)

    return data, body


def as_json(value: Any) -> str:
    if value in (None, ""):
        return ""
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def read_note(vault: Path, path: Path) -> Note:
    text = path.read_text(encoding="utf-8-sig")
    fm, body = parse_frontmatter(text)
    rel = path.relative_to(vault).as_posix()
    return Note(
        path=rel,
        title=str(fm.get("title") or path.stem),
        type=str(fm.get("type") or ""),
        status=str(fm.get("status") or ""),
        topic=as_json(fm.get("topic")),
        tags=as_json(fm.get("tags")),
        source=as_json(fm.get("source")),
        created=str(fm.get("created") or ""),
        updated=str(fm.get("updated") or ""),
        confidence=str(fm.get("confidence") or ""),
        review_after=str(fm.get("review_after") or ""),
        body=body.strip(),
        mtime=str(int(path.stat().st_mtime)),
    )


def iter_notes(vault: Path) -> list[Note]:
    ignored = {".obsidian", ".trash", "data", "attachments"}
    notes: list[Note] = []
    for path in vault.rglob("*.md"):
        if any(part in ignored for part in path.relative_to(vault).parts):
            continue
        notes.append(read_note(vault, path))
    return notes


def rebuild(db_path: Path, notes: list[Note]) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as conn:
        conn.executescript(
            """
            DROP TABLE IF EXISTS notes_fts;
            DROP TABLE IF EXISTS notes;

            CREATE TABLE notes (
              path TEXT PRIMARY KEY,
              title TEXT,
              type TEXT,
              status TEXT,
              topic TEXT,
              tags TEXT,
              source TEXT,
              created TEXT,
              updated TEXT,
              confidence TEXT,
              review_after TEXT,
              body TEXT,
              mtime TEXT
            );

            CREATE VIRTUAL TABLE notes_fts
            USING fts5(path UNINDEXED, title, body, topic, tags);
            """
        )
        conn.executemany(
            """
            INSERT INTO notes (
              path, title, type, status, topic, tags, source, created, updated,
              confidence, review_after, body, mtime
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [tuple(note.__dict__.values()) for note in notes],
        )
        conn.executemany(
            "INSERT INTO notes_fts (path, title, body, topic, tags) VALUES (?, ?, ?, ?, ?)",
            [(note.path, note.title, note.body, note.topic, note.tags) for note in notes],
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", default=r"G:\knowledge-vault")
    parser.add_argument("--db", default=r"G:\knowledge-vault\data\vault.sqlite")
    args = parser.parse_args()

    vault = Path(args.vault)
    db_path = Path(args.db)
    notes = iter_notes(vault)
    rebuild(db_path, notes)
    print(f"indexed {len(notes)} notes -> {db_path}")


if __name__ == "__main__":
    main()

