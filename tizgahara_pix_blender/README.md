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

## 使用方法（実運用フロー）

### 事前準備
1. テクスチャ画像は外部ファイルでも generated image（未保存）でも可（Packed Image は不可）
2. Mesh Object に Material + Image Texture Node を設定
3. 編集対象 Object を Active にする
4. 3D View > Sidebar > **PixelArt** > **Tizgahara Pix Blender** パネルを開く

### 基本ワークフロー
1. **Validate Asset** で対象解決とパス前提を確認
2. **Generate Aseprite Job** で revision 付き job/source/export を生成
3. 必要なら **Launch Aseprite** で外部起動
4. Aseprite 側で `export_path` に PNG を書き戻し
5. **Reload Exported Image** で Blender image を再読込

---

## パネル各操作の目的と動作

### 設定項目
- **Map Type**: 生成 job の `task.map_type` を指定
- **Export UV Guide**: ジョブ生成時に UV ガイド画像 (`*_uv.png`) を同時出力
- **Guide Size**: UV ガイド出力解像度

### オペレーター
- **Validate Asset**
  - 目的: 事故前検証
  - 動作: active object/material/image の解決、画像実在、job/source/export ディレクトリ前提をチェック

- **Generate Aseprite Job**
  - 目的: Aseprite 側編集の入力を確定
  - 動作: revision 採番、外部画像は source へコピー・generated image は source PNG を直接生成、必要に応じ UV ガイド出力、job JSON 生成、recent jobs/state 更新

- **Export UV Guide**
  - 目的: 単独で UV レイアウト画像を出力
  - 動作: active mesh の UV layout を PNG 書き出し

- **Launch Aseprite**
  - 目的: job 生成後の作業遷移短縮
  - 動作: Preferences で設定した Aseprite 実行ファイルに last job path を渡して起動

- **Reload Exported Image**
  - 目的: Aseprite 編集結果の安全反映
  - 動作: last export path の PNG を対象 image datablock に再読込（ファイル未存在ならエラー停止）

- **Sync Paths**
  - 目的: image 側の linked 情報から scene 側状態を復元
  - 動作: linked export/revision を scene state に同期

- **Print Recent Jobs**
  - 目的: 直近ジョブの確認
  - 動作: 保存済み recent jobs をオペレータレポートに表示

- **Open Job Folder**
  - 目的: 生成 job JSON への即時アクセス
  - 動作: job ディレクトリを OS ファイルブラウザで開く

### Last State 表示
- **Revision**: 最後に扱った revision
- **Job**: 最後に生成した job JSON path
- **Export**: 最後に書き戻し対象として扱う export PNG path

---

## 既知制約
- `bl_info` は legacy 互換のため残していますが、配布/導入は `blender_manifest.toml` + extension build を優先します。
- `build` / `validate` 実行には Blender CLI が必要です。
