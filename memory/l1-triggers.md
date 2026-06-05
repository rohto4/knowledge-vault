---
title: "L1 Triggers"
type: memory
status: active
topic: [memory]
source: []
created: 2026-04-18
updated: 2026-04-27
confidence: medium
review_after:
tags: [memory, l1]
---

# L1 Triggers

LLM が最初に読む想起用メモ。詳細本文は書かず、キーワードとリンクだけを置く。

## Vault

- vault構成: `knowledge / memory / tasks / sources / prompts / inbox` に分離。
- memory方針: L1はトリガー、L2は未確定モデル、L3は実施概要、L4は詳細入口。
- backup方針: vault本体は初期GitHub repo化しない。別ドライブ世代snapshotを優先。
- 回答方針: 通常回答は短く、詳細化は `expand-answer` 相当の依頼時に行う。
- dashboard: `knowledge/dashboards/vault-dashboard.md` を最初の一覧入口にする。
- SQLite: `scripts/index-vault/index_vault.py` で `data/vault.sqlite` を再生成する。
- backup: `scripts/backup/backup-vault.ps1` で `H:\bk\knowledge-vault-snapshots\` へsnapshotする。
