# USER GUIDE (Blender side)

## 事前準備
- Active object に material と image texture node を設定
- packed image は非対応
- generated image（filepath空）は source PNG 生成で対応

## 基本フロー
1. `Validate Asset`
2. `Generate Aseprite Job`
3. 必要に応じて `Export UV Guide`
4. Aseprite 側（別 repo）で編集・export
5. `Reload Exported Image` または Auto Sync で反映

## Auto Sync (Relay)
1. Preferences で `auto_sync_enabled` / `relay_enabled` を ON
2. `relay_inbox_path` を設定
3. relay inbox(JSONL)へ `texture_exported` イベントが入ると、自動で `Image.reload()`

## Job JSON
- 本 add-on は external consumer 向けに `data.task.*` を含む JSON を生成
- 詳細 parser 実装は `tizgahara-gif/aseprite_addon` を参照
