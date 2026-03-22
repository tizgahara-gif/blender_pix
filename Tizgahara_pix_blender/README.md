# Tizgahara_pix_blender Add-on

Blender 内の PixelArt 向けテクスチャ編集を Aseprite extension と連携するための companion add-on です。

## MVP 機能
- Active object/material から編集対象 image datablock を解決
- revision 管理付き job JSON の生成
- source/export/job のパス管理
- UV guide (UV Layout PNG) の出力
- Aseprite 起動補助
- export PNG の Blender image への再読込
- recent jobs 管理

## 主要フォルダ
- `addon/`: add-on 実装
- `tests/fixtures/`: サンプル JSON / パス構造
