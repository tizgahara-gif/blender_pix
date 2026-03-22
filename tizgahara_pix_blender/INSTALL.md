# INSTALL (Blender 4.2+ Extension)

## 0. 前提
- Blender 4.2+
- source tree: `tizgahara_pix_blender/`
- install artifact: `tizgahara_pix_blender/dist/*.zip`

## 1. build（公式 extension build）
```bash
cd tizgahara_pix_blender
./scripts/build_extension.sh
```

## 2. validate（source + built zip）
```bash
cd tizgahara_pix_blender
./scripts/validate_extension.sh
```

## 3. zip 内容検査
```bash
cd tizgahara_pix_blender
./scripts/inspect_zip.sh
```

ZIP 内に `blender_manifest.toml` と `__init__.py` が含まれることを確認します。

## 4. Blender で Install from Disk
1. Blender を起動
2. Extensions > Install from Disk
3. `dist/tizgahara_pix_blender-0.1.0.zip` を選択

## 5. 禁止事項
- source tree を直接 zip 化して配布しない
- `addon.zip` 等の独自 zip を作らない
- `dist/` 以外の ZIP を Install from Disk に使わない
