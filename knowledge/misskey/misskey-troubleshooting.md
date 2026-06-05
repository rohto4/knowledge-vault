---
title: "Misskey troubleshooting"
type: knowledge
status: active
topic: [misskey]
source: ["G:\\devwork\\misskey-plan"]
created: 2026-06-05
updated: 2026-06-05
confidence: medium
tags: [misskey, troubleshooting]
---

# Misskey Troubleshooting

## Docker / WSL

- Docker Desktop の WSL integration が無効だと Ubuntu 側で `docker` が使えない。
- `docker --version` と `docker compose version` が最初の確認ポイント。
- Docker Desktop 側の再起動、`wsl --shutdown`、WSL Integration のオンオフが復旧候補。

## Disk / BuildKit

- 容量不足時、BuildKit が `SIGBUS` や `Bus error` で落ちることがある。
- Cドライブと WSL root の空き容量を確認する。

## Upload EACCES

画像アップロードで `EACCES: permission denied, copyfile ... -> /misskey/files/...` が出る場合、ホスト側 `files` ディレクトリの所有者が原因になりやすい。

確認・修正例:

```bash
cd ~/src/misskey-custom
ls -ld files
sudo chown -R 991:991 files
sudo chmod -R u+rwX,g+rwX files
docker compose restart web
```
