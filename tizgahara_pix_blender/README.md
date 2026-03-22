# Tizgahara Pix Blender (Blender Extension)

Blender companion add-on + localhost relay 方式で、Aseprite export を Blender に自動反映します。

## Relay 方式概要
- Relay server は外部 localhost プロセス（Blender/Aseprite 本体外）
- Aseprite は relay へ通知（WebSocket client 想定）
- Blender は relay inbox(JSONL) を `bpy.app.timers` で poll
- Blender 側での `Image.reload()` は main thread timer callback のみで実行

## Job JSON schema（Aseprite互換 + backward compatible）
- top-level (`schema`, `revision`, `asset`, `task`) を維持
- `data` ラッパ配下にも同等情報を出力（Aseprite parser 向け）
- 重要フィールド:
  - `data.task.source_path`
  - `data.task.export_path`
  - `data.task.guides.uv_guide_path`
  - `data.task.width` / `height` / `color_mode`

## Auto Sync (Relay) 設定
Preferences:
- `auto_sync_enabled`
- `relay_enabled`
- `relay_poll_interval`
- `relay_inbox_path`
- `relay_endpoint` (optional metadata)
- `reload_settle_delay`
- `debug_sync_logging`

N-panel:
- `Auto Sync (Relay) > Enabled`
- 状態表示 `Relay/Targets/Queue`

## Relay event format
```json
{
  "event_id": "uuid-or-monotonic-id",
  "type": "texture_exported",
  "export_path": "C:/path/to/export.png",
  "revision": 1,
  "asset_name": "Cube",
  "map_type": "EMISSION",
  "timestamp": "2026-03-22T12:00:00Z"
}
```

## 導入手順（Blender 側）
1. Extension build/validate を実行
2. Blender へ `dist/*.zip` を Install from Disk
3. Preferences で `relay_inbox_path` を設定
4. Job 生成後、Aseprite 側が `texture_exported` を relay へ送る
5. Relay が inbox にイベントを書き込むと Blender が自動 reload

## 手動 reload との違い
- 手動: `Reload Exported Image` ボタンで即時 reload
- Auto Sync: relay 通知 + settle delay 後に自動 reload

## 既知制約
- relay inbox は JSONL（1行1イベント）前提
- relay server 本体は別プロセスとして用意が必要
- Aseprite 側 WebSocket 実装は MVP スケルトン
