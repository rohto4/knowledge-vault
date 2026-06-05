---
title: "Vault Bootstrap"
type: task
status: active
topic: [vault, memory]
source:
  - "G:\\devwork\\obsidian-set\\docs\\imp\\task-a-session-handoff.md"
created: 2026-04-18
updated: 2026-04-27
confidence: medium
review_after:
tags: [task, bootstrap]
---

# Vault Bootstrap

## Purpose

- `G:\knowledge-vault` を本運用 vault として初期作成する。
- ユーザ用ナレッジと LLM 長期記憶階層を同じ vault 内で両立させる。

## Work Done

- 初期ディレクトリを作成。
- `AGENTS.md`, `PROJECT.md`, `README.md` を作成。
- `memory/`, `knowledge/`, `tasks/`, `sources/`, `prompts/`, `inbox/` の役割を定義。
- note template を作成。
- 2026-04-19: Dataview plugin を設置。
- 2026-04-19: `knowledge/dashboards/vault-dashboard.md` を作成。
- 2026-04-19: SQLite indexer を作成し、`data/vault.sqlite` を生成。
- 2026-04-19: `tech-stack.md` を root に作成し、参照URLを集約。
- 2026-04-19: Local REST API plugin を設置。
- 2026-04-19: Obsidian registry に `G:\knowledge-vault` を登録。
- 2026-04-27: memory L2-L4 のREADMEを作成。
- 2026-04-27: Dataview dashboard に入口、最近のtask、knowledge、template一覧を追加。
- 2026-04-27: backup script のREADMEを作成。
- 2026-04-27: SQLite indexer を実行し、28 notes を `data/vault.sqlite` に反映。
- 2026-04-27: backup script を実行し、`H:\bk\knowledge-vault-snapshots\2026-04-27_172129` を作成。
- 2026-04-27: 他PJの `AGENTS.md` 向け vault 参照テンプレートを作成。

## Decisions

- vault 本体は初期状態では GitHub repo 化しない。
- ローカル正本 + 別ドライブ世代 snapshot backup を基本にする。
- `memory/` は正本ではなく、LLM 用の想起・圧縮レイヤーにする。
- Web Clipper は見送り。
- P1で Dataview と SQLite を採用する。
- Local REST API plugin は導入する。

## Waiting

- backup 先は `H:\bk\knowledge-vault-snapshots\`。
- L2, L3, L4 の粒度はREADMEで初期定義済み。実運用で調整する。

## Next Actions

- P0設計を `obsidian-set` 側の `task-a-vault-structure-plan.md` に反映する。
- Obsidianで Local REST API plugin を有効化し、API key確認後に疎通確認する。
