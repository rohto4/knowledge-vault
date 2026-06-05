# Backup Script

`backup-vault.ps1` は `G:\knowledge-vault` を日付付き snapshot として `H:\bk\knowledge-vault-snapshots\` へコピーする。

## 実行

```powershell
G:\knowledge-vault\scripts\backup\backup-vault.ps1
```

## 方針

- vault 本体は初期 GitHub repo 化しない。
- backup は世代 snapshot として残す。
- `.obsidian/cache`, `.trash`, `*.tmp` は除外する。

## 確認

実行後、出力された backup 先に `AGENTS.md`, `PROJECT.md`, `memory/`, `knowledge/`, `tasks/` があることを確認する。

