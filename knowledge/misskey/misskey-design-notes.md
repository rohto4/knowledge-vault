---
title: "Misskey design notes"
type: knowledge
status: active
topic: [misskey]
source: ["G:\\devwork\\misskey-plan"]
created: 2026-06-05
updated: 2026-06-05
confidence: medium
tags: [misskey, design]
---

# Misskey Design Notes

## Current Direction

- 本流調査と独自改修を分離する。
- 独自改修は `misskey-custom` に集約する。
- 本流との差分は小さく保ち、追随しやすくする。
- 大きな改修は `G:\devwork\misskey-plan\commands\prp-plan.md` の型で計画化する。

## Notes To Expand Later

- 独自アップデートのテーマ一覧。
- backend / frontend / migration の変更ルール。
- CHANGELOG と Misskey 本体 `AGENTS.md` の運用。
- 本流取り込み時の差分確認手順。
