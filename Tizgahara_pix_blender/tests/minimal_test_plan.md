# Minimal Test Plan

1. Blender で add-on 有効化
2. Preferences で Workspace Root を設定
3. テクスチャ付き mesh object を active にする
4. Validate Asset が成功すること
5. Generate Aseprite Job 実行
   - `aseprite_jobs/*.json` 生成
   - `sources/*.png` コピー生成
   - UV guide 有効時 `*_uv.png` 生成
6. export_path に PNG を配置して Reload Exported Image
7. Blender image が更新されること
