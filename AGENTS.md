# knowledge-vault Agent Instructions

## 最優先ルール

1. 日本語で対応する。
2. UTF-8 で読み書きする。
3. この vault は横断ナレッジと LLM 記憶階層の本運用 vault として扱う。
4. vault 本体は初期状態では GitHub repo 化しない。
5. API key、token、private URL、個人情報は保存しない。
6. 同じ事実セットの正本を複数作らない。
7. `memory/` は正本ではなく、LLM が思い出すための索引・圧縮レイヤーとして扱う。
8. 参照URLは原則 `tech-stack.md` に集約する。

## 役割

| Path | 役割 |
|---|---|
| `knowledge/` | 人間が読む整理済みナレッジ |
| `memory/` | LLM 用の想起・圧縮レイヤー |
| `tasks/` | タスク単位の作業記録、引き継ぎ、実施概要 |
| `sources/` | 根拠資料の要約と出典 |
| `prompts/` | ユーザプロンプト全文と AI 回答要約 |
| `inbox/` | 未整理情報の一時置き場 |
| `templates/` | note 作成用テンプレート |
| `attachments/` | 画像、PDF、添付ファイル |
| `tech-stack.md` | PJ全体の参照URL集約 |

## 書き込み判断

1. 実施した作業は `tasks/` に保存する。
2. 再利用できる知識は `knowledge/` に昇格する。
3. 外部情報や根拠は `sources/` に保存する。
4. LLM が常時または優先的に読む手がかりは `memory/` に短く置く。
5. 保存先に迷う情報は `inbox/` に置き、後で整理する。

## 他PJからの利用

各開発PJの `AGENTS.md` には、この vault の場所だけを書く。

```text
横断ナレッジ vault: G:\knowledge-vault
```

PJ固有の実装状態は各PJ内に置き、横断的に再利用できる知識だけこの vault に保存する。
