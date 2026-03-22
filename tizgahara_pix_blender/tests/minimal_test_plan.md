# Minimal Test Plan

1. Blender で add-on 有効化
2. Preferences で `relay_inbox_path` を設定
3. テクスチャ付き object で `Generate Aseprite Job` 実行
4. `aseprite_jobs/*.json` が nested schema (`data.task.*`) で生成されること
   - `data.task.guides.uv_guide_path` が存在
   - `data.task.width` / `height` / `color_mode` が存在
5. Relay inbox に `texture_exported` イベント(JSONL)を追記
6. `reload_settle_delay` 後に Blender image が自動更新されること
7. blend 再読込後も同イベントで自動更新すること
8. relay 停止/不正JSON時も Blender が落ちないこと
