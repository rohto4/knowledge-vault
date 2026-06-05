param(
  [string]$Source = "G:\knowledge-vault",
  [string]$BackupRoot = "H:\bk\knowledge-vault-snapshots"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $Source)) {
  throw "Source not found: $Source"
}

if (-not (Test-Path (Split-Path $BackupRoot -Parent))) {
  throw "Backup drive/root not found: $BackupRoot"
}

$stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$dest = Join-Path $BackupRoot $stamp
New-Item -ItemType Directory -Force -Path $dest | Out-Null

robocopy $Source $dest /E /XD ".obsidian\cache" ".trash" /XF "*.tmp" | Out-Null

if ($LASTEXITCODE -gt 7) {
  throw "robocopy failed: $LASTEXITCODE"
}

Write-Output "Backup complete: $dest"

