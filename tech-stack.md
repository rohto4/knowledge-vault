# Tech Stack and Reference URLs

作成日: 2026-04-19

## 位置づけ

`G:\knowledge-vault` 全体の参照URL集約ファイル。
PJ内で使う技術、plugin、docs、候補リンクはまずここに登録する。

## Root

| 項目 | 値 |
|---|---|
| Vault root | `G:\knowledge-vault` |
| Obsidian app | `G:\IDE\Obsidian\Obsidian.exe` |
| Obsidian version | `1.12.7` |
| Backup root | `H:\bk\knowledge-vault-snapshots\` |

## Core

| 項目 | 状態 | URL |
|---|---|---|
| Obsidian | adopted | https://obsidian.md/ |
| Obsidian Help | reference | https://help.obsidian.md/ |
| Obsidian Developer Docs | reference | https://docs.obsidian.md/ |
| Git docs | reference | https://git-scm.com/docs |
| ECC | reference | https://github.com/affaan-m/everything-claude-code |
| MCP overview | future | https://modelcontextprotocol.io/ |
| MCP spec | future | https://modelcontextprotocol.io/specification/2025-11-25 |

## Obsidian Plugins

| Plugin | 状態 | URL |
|---|---|---|
| Dataview | installed | https://github.com/blacksmithgu/obsidian-dataview |
| Dataview plugin stats | reference | https://www.obsidianstats.com/plugins/dataview |
| Local REST API | installed | https://github.com/coddingtonbear/obsidian-local-rest-api |
| Local REST API docs | reference | https://coddingtonbear.github.io/obsidian-local-rest-api/ |
| Query All The Things | candidate | https://www.obsidianstats.com/plugins/qatt |

## Obsidian MCP Candidates

| Candidate | 状態 | URL |
|---|---|---|
| cyanheads/obsidian-mcp-server | candidate | https://github.com/cyanheads/obsidian-mcp-server |
| newtype-01/obsidian-mcp | candidate | https://github.com/newtype-01/obsidian-mcp |
| PublikPrinciple/obsidian-mcp-rest | candidate | https://github.com/PublikPrinciple/obsidian-mcp-rest |

## Agent / Client Docs

| 項目 | URL |
|---|---|
| VS Code MCP | https://code.visualstudio.com/docs/copilot/chat/mcp-servers |
| Claude Code MCP | https://docs.anthropic.com/en/docs/claude-code/mcp |
| Gemini CLI MCP | https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md |

## SQL / Search

| 項目 | 状態 | URL |
|---|---|---|
| SQLite FTS5 | P1 | https://www.sqlite.org/fts5.html |
| DuckDB FTS | future | https://duckdb.org/docs/stable/core_extensions/full_text_search.html |

## VS Code / Markdown Candidates

| 項目 | 状態 | URL |
|---|---|---|
| markdownlint | candidate | https://github.com/DavidAnson/markdownlint |
| markdownlint VS Code | candidate | https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint |
| Markdown All in One | optional | https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one |
| Foam | candidate | https://github.com/foambubble/foam |

## Practical Obsidian References

| 項目 | URL |
|---|---|
| Daily notes workflow | https://parazettel.com/articles/obsidian-daily-workflows/ |
| AI productivity daily notes | https://aiproductivity.ai/guides/obsidian-daily-notes-workflow/ |
| Zettelkasten Obsidian | https://desktopcommander.app/blog/zettelkasten-obsidian/ |
| VS Code as notes | https://www.xda-developers.com/tried-using-vs-code-obsidian-notes/ |

## Rules

- 新しい参照URLはまずここへ追加。
- 個別noteには直接必要なURLだけ残す。
- API key、private URL、credential は書かない。

## Misskey / Codex Reference URLs (2026-06-06)

### Codex CLI

| Item | URL |
|---|---|
| OpenAI Codex CLI Help Center | https://help.openai.com/en/collections/13193998-codex-cli |
| OpenAI Codex CLI Getting Started | https://help.openai.com/en/articles/11096431 |
| OpenAI Codex GitHub | https://github.com/openai/codex |
| Codex Slash Commands | https://github.com/openai/codex/blob/main/docs/slash_commands.md |
| Codex Config | https://github.com/openai/codex/blob/main/docs/config.md |
| Codex Changelog | https://developers.openai.com/codex/changelog/ |
| Codex `/status` related issue | https://github.com/openai/codex/issues/10233 |

### Misskey

| Item | URL |
|---|---|
| MisskeyHub | https://misskey-hub.net/ |
| MisskeyHub Docker install guide | https://misskey-hub.net/docs/for-admin/install/guides/docker/ |
| misskey-dev/misskey | https://github.com/misskey-dev/misskey |
| Misskey repository README | https://github.com/misskey-dev/misskey/blob/master/README.md |
| Misskey compose example | https://github.com/misskey-dev/misskey/blob/master/compose_example.yml |
| Misskey Dockerfile | https://github.com/misskey-dev/misskey/blob/master/Dockerfile |

### Docker / Compose

| Item | URL |
|---|---|
| Docker Docs | https://docs.docker.com/ |
| Docker Desktop WSL | https://docs.docker.com/desktop/features/wsl/ |
| Docker Compose | https://docs.docker.com/compose/ |
| Compose file reference | https://docs.docker.com/reference/compose-file/ |
| Dockerfile reference | https://docs.docker.com/reference/dockerfile/ |
| BuildKit | https://docs.docker.com/build/buildkit/ |
| Docker Hub Node image | https://hub.docker.com/_/node |
| Docker Hub PostgreSQL image | https://hub.docker.com/_/postgres |
| Docker Hub Redis image | https://hub.docker.com/_/redis |
| Docker Hub Meilisearch image | https://hub.docker.com/r/getmeili/meilisearch |

### Runtime / Services From Misskey Compose And Dockerfile

| Item | URL |
|---|---|
| Node.js docs | https://nodejs.org/docs/latest/api/ |
| pnpm docs | https://pnpm.io/ |
| PostgreSQL docs | https://www.postgresql.org/docs/ |
| Redis docs | https://redis.io/docs/latest/ |
| Meilisearch docs | https://www.meilisearch.com/docs/ |
| Meilisearch Docker install | https://www.meilisearch.com/docs/learn/self_hosted/install_meilisearch_with_docker |
| mCaptcha GitHub | https://github.com/mCaptcha/mCaptcha |
| Tini GitHub | https://github.com/krallin/tini |
| FFmpeg documentation | https://ffmpeg.org/documentation.html |
| jemalloc | https://jemalloc.net/ |
| Debian documentation | https://www.debian.org/doc/ |
