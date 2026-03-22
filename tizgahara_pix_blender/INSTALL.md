# INSTALL (Blender Extension only)

この手順は Blender extension の build/validate/install のみを扱います。

## 1) Validate source
```bash
cd tizgahara_pix_blender
blender --command extension validate
```

## 2) Build distributable zip
```bash
cd tizgahara_pix_blender
mkdir -p dist
blender --command extension build --output-dir ./dist
```

## 3) Validate built zip
```bash
cd tizgahara_pix_blender
blender --command extension validate ./dist/tizgahara_pix_blender-0.1.0.zip
```

## 4) Install from Disk
Blender で `dist/tizgahara_pix_blender-0.1.0.zip` を Install from Disk します。

## 5) Runtime Preferences
- Workspace Root
- Aseprite Executable (任意)
- Auto Sync / Relay 設定 (`relay_inbox_path` など)

## External dependency
Aseprite 側 extension は別 repo `tizgahara-gif/aseprite_addon` を参照してください。
