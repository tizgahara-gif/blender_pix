# Minimal Test Plan (Blender side)

1. Blender で add-on 有効化
2. Preferences で `Workspace Root` と `relay_inbox_path` を設定
3. `Generate Aseprite Job` 実行
4. `aseprite_jobs/*.json` に `data.task.source_path/export_path/guides.uv_guide_path` が出ること
5. `Export UV Guide` 実行で guide PNG が生成されること
6. `Reload Exported Image` が成功すること
7. relay inbox に `texture_exported` を追加し自動 reload されること
8. blend 再読込後も Auto Sync 復元されること
