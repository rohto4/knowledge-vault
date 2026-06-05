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
## 2026-06-06: Image Upload INTERNAL_ERROR / EACCES

Symptom:

- Profile icon upload and note image attachment failed with `INTERNAL_ERROR`.
- Error ID shown in UI: `5d37dbcb-891e-41ca-a3d6-e690c97775ac`.

Server log:

```text
Error: EACCES: permission denied, copyfile '/tmp/tmp-*' -> '/misskey/files/<uuid>'
```

Cause:

- `compose.yml` mounts `./files:/misskey/files`.
- Host directory `/home/unibell4/src/misskey/files` was owned by `root:root` with mode `755`.
- Container user `misskey` cannot write there.

Fix applied:

```bash
cd /home/unibell4/src/misskey
docker compose exec -T -u root web chown -R 991:991 /misskey/files
docker compose exec -T -u root web chmod -R u+rwX,g+rwX /misskey/files
```

Verification:

```bash
docker compose exec -T -u 991 web touch /misskey/files/.write-test
docker compose exec -T -u 991 web rm -f /misskey/files/.write-test
ls -ld files
```

Expected `ls -ld files` after fix:

```text
drwxrwxr-x 2 991 ... files
```
