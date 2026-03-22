# Tizgahara Pix Blender (Blender Extension)

`Tizgahara Pix Blender` は Blender 4.2+ の **Extension Package** として配布する想定の add-on です。
Aseprite 連携用の job JSON 生成、UV guide 出力、編集後テクスチャ再読込を提供します。

## Extension としての構成
本パッケージは extension ルートに以下を持ちます。

- `blender_manifest.toml`
- `__init__.py`
- `addon/` (実装本体)
- ドキュメント/fixtures

> `blender_manifest.toml` が無い ZIP は Blender 4.2+ の Install from Disk で
> `Missing manifest` エラーになります。

## Build / Validate (公式フロー)
Extension ルート (`tizgahara_pix_blender/`) で実行します。

```bash
# manifest/構成の検証
blender --command extension validate

# extension zip を生成
blender --command extension build

# 生成済み zip の検証（任意）
blender --command extension validate ./tizgahara_pix_blender-0.1.0.zip
```

上記コマンドは Blender 公式マニュアルの Extensions command-line フロー準拠です。

## Blender への導入
1. `blender --command extension build` で生成した ZIP を使用
2. Blender 4.2+ で **Extensions > Install from Disk**
3. 生成 ZIP を選択してインストール

## MVP 機能
- Active object/material から編集対象 image datablock を解決
- revision 管理付き job JSON の生成
- source/export/job のパス管理
- UV guide (UV Layout PNG) の出力
- Aseprite 起動補助
- export PNG の Blender image への再読込
- recent jobs 管理

## 既知制約（extension 化に伴う注意）
- Blender 4.2+ の extension install を第一対象とし、legacy add-on の手動 zip 直詰め運用は非推奨。
- `bl_info` は互換のため残していますが、配布/導入フローは `blender_manifest.toml` ベースです。
- `blender --command extension validate` / `build` は Blender 実行環境が必要です。
