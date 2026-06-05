---
title: "Dataview Adoption"
type: decision
status: decided
topic: [obsidian, dataview, query]
source:
  - "https://github.com/blacksmithgu/obsidian-dataview"
created: 2026-04-19
updated: 2026-04-19
confidence: high
review_after: 2026-07-19
tags: [decision, dataview]
---

# Dataview Adoption

## Decision

- P1で Dataview を採用する。
- P1で SQLite index も作り、SQLでも検索できる状態にする。
- Web Clipper は見送り。

## Reason

- Obsidian内で frontmatter 付き note を一覧化できる。
- SQLite index と併用すれば、Obsidian UI と SQL の両方で確認できる。
- 外部MCP導入前に、vault内の構造崩れを早く検出できる。

## Boundary

- Dataview は Obsidian内 dashboard 用。
- SQLite は Codex / CLI / 再現可能検索用。
- Markdown note が正本。Dataview結果と SQLite DB は派生物。

