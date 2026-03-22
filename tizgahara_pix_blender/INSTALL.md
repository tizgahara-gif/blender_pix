# INSTALL

## Blender Extension
```bash
cd tizgahara_pix_blender
blender --command extension validate
mkdir -p dist
blender --command extension build --output-dir ./dist
blender --command extension validate ./dist/tizgahara_pix_blender-0.1.0.zip
```
Blender では `dist/tizgahara_pix_blender-0.1.0.zip` を Install from Disk してください。

## Relay 前提セットアップ
1. localhost relay server を起動（外部プロセス）
2. relay が JSONL inbox へイベントを書き出す設定にする
3. Blender Preferences で `relay_inbox_path` を同じファイルに設定

## Aseprite 側
- `aseprite_extension/` の scripts を extension 側へ組み込み
- `relay_url`, `debounce_seconds`, `auto_sync_default` 等を設定
- Open Blender Job 後に Auto Sync を有効化


## Job JSON compatibility check
- 生成JSONに `data.task.source_path` / `data.task.export_path` / `data.task.guides.uv_guide_path` / `data.task.width` / `height` / `color_mode` が含まれることを確認してください。
