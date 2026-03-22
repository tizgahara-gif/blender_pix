# Aseprite Extension (Relay Auto Sync MVP)

このフォルダは Blender companion と連携する Aseprite 側 MVP スケルトンです。

## 追加ファイル
- `scripts/core/relay_client.lua`: relay 送信クライアント
- `scripts/core/sync_manager.lua`: sprite change debounce / export / notify 管理
- `scripts/commands/toggle_auto_sync.lua`
- `scripts/commands/sync_now.lua`

## 想定 plugin.preferences
- `relay_url`
- `auto_sync_default`
- `debounce_seconds`
- `auto_validate_before_export`
- `show_sync_status`
- `write_log_file`
- `log_file_path`
- `deflate_enabled`

## Save と Export の分離
- 通常保存: sprite 本来の保存先
- Blender 向け同期: `job.task.export_path` に `saveCopyAs`

## relay 未接続時
- export は継続可能
- relay notify は警告ログのみで extension は停止しない
