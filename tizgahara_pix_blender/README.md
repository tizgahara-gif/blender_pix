# Tizgahara Pix Blender (Blender Extension)

`Tizgahara Pix Blender` は Blender 4.2+ の **Extension Package** です。

## 重要: source tree と配布 artifact は分離する
- **source tree**: `tizgahara_pix_blender/`
- **install artifact (配布物)**: `tizgahara_pix_blender/dist/*.zip`

Blender へ入れるのは `dist/` の build 成果物のみです。source tree や `addon.zip` を直接配布/導入しません。

## Extension Package 要件
extension ルート (`tizgahara_pix_blender/`) に以下を配置します。
- `blender_manifest.toml`
- `__init__.py`
- `addon/`

`Missing manifest from ... addon.zip` は、公式 build 以外の ZIP を使った時に起きる典型的なエラーです。

---

## 公式 build/validate フロー（推奨: scripts 経由）

### A) スクリプト実行（推奨）
```bash
cd tizgahara_pix_blender
./scripts/build_extension.sh
./scripts/validate_extension.sh
./scripts/inspect_zip.sh
```

### B) 手動実行（公式 CLI）
```bash
cd tizgahara_pix_blender
blender --command extension validate
mkdir -p dist
blender --command extension build --output-dir ./dist
blender --command extension validate ./dist/tizgahara_pix_blender-0.1.0.zip
unzip -l ./dist/tizgahara_pix_blender-0.1.0.zip
```

`unzip -l` で ZIP 内に `blender_manifest.toml` と `__init__.py` があることを確認してください。

---

## Blender に Install from Disk する対象
- `tizgahara_pix_blender/dist/tizgahara_pix_blender-0.1.0.zip`

> `addon.zip` 等の独自 zip は使用しないこと。

---

## 既知制約
- `bl_info` は legacy 互換のため残していますが、配布/導入は `blender_manifest.toml` + extension build を優先します。
- `build` / `validate` 実行には Blender CLI が必要です。
