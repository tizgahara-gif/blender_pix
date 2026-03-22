# Tizgahara Pix Blender

**This repository contains only the Blender add-on / Blender extension.**

Aseprite extension の実装・配布・導入手順はこの repo には含めません。Aseprite 側は別 repo `tizgahara-gif/aseprite_addon` を参照してください。

## Scope (責務)
この repo の責務は Blender 側のみです。
- Generate Aseprite Job による job JSON 出力
- source/export/guide path 生成
- relay inbox(JSONL) poll による `Image.reload()` 自動反映

## Requirements
- Blender 4.2+

## Blender Add-on 機能
- **Generate Aseprite Job**: revision 付き job JSON を生成
- **Export UV Guide**: UV guide PNG を出力
- **Reload Exported Image**: export PNG を手動再読込
- **Auto Sync (Relay)**: relay inbox 通知から自動再読込

## Job JSON contract (external consumer 向け)
Blender は以下を含む JSON を出力します（top-level + `data` ラッパ両方）。
- `data.task.source_path`
- `data.task.export_path`
- `data.task.guides.uv_guide_path`
- `data.task.width`
- `data.task.height`
- `data.task.color_mode`

詳細な consumer 実装（Aseprite UI/command/package 構造）は `tizgahara-gif/aseprite_addon` 側で管理します。

## Auto Sync (Relay) 設定
Add-on Preferences:
- `auto_sync_enabled`
- `relay_enabled`
- `relay_poll_interval`
- `relay_inbox_path`
- `relay_endpoint` (optional metadata)
- `reload_settle_delay`
- `debug_sync_logging`

N-panel:
- `Auto Sync (Relay)` ON/OFF
- `Relay/Targets/Queue` 状態表示

## 出力場所
- jobs: `<workspace>/aseprite_jobs/*.json`
- source: `<workspace>/sources/*.png`
- export: `<workspace>/exports/*.png`

## relay_inbox_path
- relay server は外部 localhost プロセス前提
- Blender は `relay_inbox_path` の JSONL を timer polling
- 各行は `texture_exported` イベント（`event_id` を含む）を想定

## Known limitations
- Packed image 非対応
- relay server 本体はこの repo に含まれない
- relay inbox は JSONL（1行1イベント）前提
