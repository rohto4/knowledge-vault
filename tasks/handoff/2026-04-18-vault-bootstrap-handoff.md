---
title: "Vault Bootstrap Handoff"
type: task
status: active
topic: [vault, handoff]
source:
  - "G:\\devwork\\obsidian-set"
created: 2026-04-18
updated: 2026-04-27
confidence: medium
review_after:
tags: [handoff]
---

# Vault Bootstrap Handoff

## Current State

- `G:\knowledge-vault` を作成済み。
- 初期構成は `knowledge + memory + tasks + sources + prompts + inbox` の分離。
- `memory/` は LLM 長期記憶用の圧縮・想起レイヤー。
- `knowledge/`, `tasks/`, `sources/` が詳細正本。
- P1で Dataview plugin 設置済み。
- P1で SQLite indexer 作成済み。DBは `G:\knowledge-vault\data\vault.sqlite`。
- `tech-stack.md` 作成済み。参照URLはここへ集約。
- Local REST API plugin 設置済み。
- Obsidian registry に `G:\knowledge-vault` 登録済み。
- memory L2-L4 のREADME作成済み。
- Dataview dashboard は入口、task、knowledge、template のビューを追加済み。
- backup script は実行済み。snapshot: `H:\bk\knowledge-vault-snapshots\2026-04-27_172129`
- SQLite indexer は実行済み。28 notes を index 済み。
- 他PJ向け `AGENTS.md` 参照テンプレート作成済み: `templates/project-agent-vault-reference.md`

## Read First

1. `G:\knowledge-vault\AGENTS.md`
2. `G:\knowledge-vault\PROJECT.md`
3. `G:\knowledge-vault\memory\README.md`
4. `G:\knowledge-vault\memory\l1-triggers.md`
5. `G:\knowledge-vault\tasks\active\2026-04-18-vault-bootstrap.md`
6. `G:\knowledge-vault\knowledge\dashboards\vault-dashboard.md`
7. `G:\knowledge-vault\scripts\index-vault\index_vault.py`
8. `G:\knowledge-vault\tech-stack.md`

## Open Decisions

- backup 世代数。
- Local REST API plugin のAPI key確認と疎通確認。
