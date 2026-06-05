# knowledge-vault Project Context

## 目的

この vault は、次の2つを両立するための本運用 knowledge base。

1. ユーザ自身が知識、判断、作業履歴をさかのぼれるようにする。
2. LLM が長期記憶として効率よく参照できる階層を作る。

## 保存方針

- ローカルファイルを正本にする。
- 初期状態では GitHub repo 化しない。
- バックアップは別ドライブへの日付付き snapshot を基本にする。
- GitHub は `G:\devwork` 配下の各開発PJの Issue / PR / 実装状態の正本として扱う。
- この vault は横断ナレッジ、作業要約、LLM記憶、根拠資料の保存先として扱う。

## 推奨バックアップ

初期は次のような世代 snapshot を想定する。

```text
G:\knowledge-vault
  -> H:\backup\knowledge-vault-snapshots\YYYY-MM-DD\
```

完全ミラーは削除も反映されるため、まずは日付付き snapshot を複数世代残す。

## 正本ルール

- 参照URL一覧は `tech-stack.md` を正本にする。
- `sources/` は根拠資料の正本。
- `tasks/` は実施履歴の正本。
- `knowledge/` は整理済み知識の正本。
- `memory/` は LLM 用の索引・要約であり、詳細正本ではない。
- `prompts/` はユーザプロンプト全文とAI回答要約の保存先。
- `inbox/` は未整理の一時置き場。

## 初期導入範囲

Obsidian Sync、MCP、Local REST API は初期導入しない。

P1で Dataview と SQLite index を導入した。

- Dataview: Obsidian内 dashboard 用。
- SQLite: CLI / SQL検索用。
- Markdown note が正本。Dataview結果と SQLite DB は派生物。
- DB: `data/vault.sqlite`
- indexer: `scripts/index-vault/index_vault.py`

## Obsidian Plugins

- Dataview: installed
- Local REST API: installed

Local REST API は plugin files 設置済み。
API key や接続確認は Obsidian 側で plugin を有効化した後に行う。
