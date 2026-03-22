# INSTALL (Blender Extension)

## 前提
- Blender 4.2 以上
- extension ルートに `blender_manifest.toml` が存在すること

## 1) Validate
`blender_manifest.toml` とパッケージ構成を検証します。

```bash
cd tizgahara_pix_blender
blender --command extension validate
```

## 2) Build
配布用 ZIP は手動 zip ではなく、公式 build コマンドで生成します。

```bash
cd tizgahara_pix_blender
blender --command extension build
```

## 3) Install from Disk
1. Blender を起動
2. Extensions 画面で **Install from Disk**
3. build で生成された ZIP を選択

## 4) Optional: ZIP validate

```bash
cd tizgahara_pix_blender
blender --command extension validate ./tizgahara_pix_blender-0.1.0.zip
```
