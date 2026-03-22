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


## Auto Sync (Relay)
- Preferences で `relay_enabled` を ON にすると relay inbox を常時 poll
- relay の `texture_exported` 通知を受けると、対応 export path に紐づく image を queue へ積む
- `reload_settle_delay` 後に `Image.reload()` を実行してビューポートへ反映
- blend 再読込後は linked export path から registry を復元
