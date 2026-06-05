---
title: "Misskey decisions"
type: decision
status: active
topic: [misskey]
source: ["G:\\devwork\\misskey-plan"]
created: 2026-06-05
updated: 2026-06-05
confidence: high
tags: [misskey, decision]
---

# Misskey Decisions

## 2026-06-05: WSL をソース正本にする

Decision:

- Misskey の実行・調査・改修は WSL 側を正本にする。

Reason:

- Docker / Node / pnpm / VSCode Remote - WSL の整合を取りやすい。
- Windows 側 clone と WSL 側 clone の二重編集を避ける。

## 2026-06-05: worktree で upstream と custom を分ける

Decision:

- `/home/unibell4/src/misskey-repo` を管理元にし、`misskey-upstream` と `misskey-custom` を worktree で分ける。

Reason:

- 本流調査と独自改修を混ぜない。
- clone 2個よりディスクとGit管理の重複が少ない。

## 2026-06-05: 通常起動は custom

Decision:

- Docker で通常起動する対象は `misskey-custom` にする。

Reason:

- 独自改修の動作確認を主目的にするため。
- upstream は本流調査用として扱うため。

## 2026-06-05: vault は台帳型で始める

Decision:

- Obsidian vault には、細かい事象ごとのノートではなく、系統別台帳と時系列ヒストリーを置く。

Reason:

- ノートが増えすぎると後から追いづらい。
- 初期段階は時系列で列挙した方が再開しやすい。
