# USER GUIDE

## 事前準備
- Active object に material と image texture node を設定
- packed image は非対応（unpack もしくは外部保存が必要）
- generated image（`image.filepath` 空）も job 生成可能

## 基本フロー
1. `Validate Asset`
2. `Generate Aseprite Job`
3. 必要に応じて `Launch Aseprite`
4. Aseprite extension が `export_path` へ PNG 出力
5. `Reload Exported Image`

## generated image の扱い
- `image.filepath` が空の画像は、`sources/<asset>_<rev>.png` に PNG として書き出してから job 化
- job JSON の `task.source_path` は、この生成された source PNG を指す
- Blender 内の元 image datablock は破壊しない

## 運用注意
- `export_path` 未生成時の reload はエラー停止
- revision は `*_rNNN.json` で採番
- source は revision ごとにコピー/生成され、元画像を直接上書きしない


## Auto Sync
- Preferences で `auto_sync_enabled` を ON にすると export PNG を常時監視
- 監視は `sync_poll_interval` 間隔で行い、更新検知後 `reload_settle_delay` 待ってから reload
- blend 再読込後は linked export path から監視を復元
