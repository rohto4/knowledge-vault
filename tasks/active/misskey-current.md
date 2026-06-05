---
title: "Misskey current work"
type: task
status: active
topic: [misskey]
source: ["G:\\devwork\\misskey-plan"]
created: 2026-06-05
updated: 2026-06-05
confidence: high
tags: [misskey, task]
---

# Misskey Current Work

## Purpose

WSL 上で Misskey を安定運用し、本流調査と独自改修を分けて進めるための作業基盤を作る。

## Current Decisions

- WSL 側を Misskey ソースの正本にする。
- worktree 構成は `misskey-repo`, `misskey-upstream`, `misskey-custom` とする。
- 通常起動対象は `misskey-custom` とする。
- Windows 側 `G:\devwork\clone-dir\misskey` は当面残す。
- Obsidian vault には系統別台帳と時系列ヒストリーを置く。
- ECC / ecc-expand 由来 command と skill は `G:\devwork\misskey-plan` に導入済み。

## Current State

- 計画フォルダ: `G:\devwork\misskey-plan`
- WSL 作業予定 root: `/home/unibell4/src`
- WSL worktree はまだ作成前。
- 次回は WSL 側の現状確認後、worktree 作成へ進む。

## Next Actions

- WSL 側 `/home/unibell4/src` の既存 Misskey ディレクトリを確認する。
- 必要なら既存ディレクトリを退避する。
- `misskey-repo`, `misskey-upstream`, `misskey-custom` を作る。
- `misskey-custom` で Docker 起動確認を行う。

## Links

- Plan root: `G:\devwork\misskey-plan`
- Judge file: `G:\devwork\misskey-plan\docs\imp\user-judge.md`
- Worktree guide: `G:\devwork\misskey-plan\docs\guide\wsl-worktree-operations.md`
