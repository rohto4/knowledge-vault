# knowledge-vault

横断ナレッジと LLM 長期記憶のための本運用 vault。

## 最初に見るファイル

1. `AGENTS.md`
2. `PROJECT.md`
3. `memory/l1-triggers.md`
4. `tasks/README.md`
5. `knowledge/README.md`
6. `tech-stack.md`

## 初期構成

```text
memory/      LLM用の想起・圧縮レイヤー
knowledge/   整理済みナレッジ
tasks/       タスク単位の作業記録
sources/     根拠資料
prompts/     ユーザプロンプト全文とAI回答要約
inbox/       未整理情報
templates/   noteテンプレート
attachments/ 添付ファイル
```

## P1 Query

- Dataview plugin: installed
- Dashboard: `knowledge/dashboards/vault-dashboard.md`
- SQLite DB: `data/vault.sqlite`
- SQLite indexer: `scripts/index-vault/index_vault.py`

## Plugins

- Dataview: installed
- Local REST API: installed

Rebuild:

```powershell
python G:\knowledge-vault\scripts\index-vault\index_vault.py
```
