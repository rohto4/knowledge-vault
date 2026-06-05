---
title: "Misskey handoff"
type: task
status: active
topic: [misskey]
source: ["G:\\devwork\\misskey-plan"]
created: 2026-06-05
updated: 2026-06-05
confidence: high
tags: [misskey, handoff]
---

# Misskey Handoff

## Summary

Misskey 改修は WSL 側を正本にする方針で承認済み。次回は WSL に worktree 構成を作る段階。

## Approved

- J1: WSL 側を正本にする。
- J2: `misskey-repo`, `misskey-upstream`, `misskey-custom` の worktree 構成。
- J3: 通常起動は `misskey-custom`。
- J4: Windows 側 clone は当面残す。
- J5: Obsidian vault に系統別台帳とヒストリーを作る。
- J6: ECC / command / skill を導入する。

## Next Files To Read

1. `G:\devwork\misskey-plan\README.md`
2. `G:\devwork\misskey-plan\docs\imp\user-judge.md`
3. `G:\devwork\misskey-plan\docs\guide\wsl-worktree-operations.md`
4. `G:\devwork\misskey-plan\docs\imp\imp-tasks.md`

## Next Actions

- WSL 側の既存ディレクトリを確認する。
- 既存 `~/src/misskey` があれば退避する。
- worktree を作る。
- Docker 起動と画像アップロード権限を確認する。
