# USER GUIDE

## 事前準備
- Active object に material と image texture node を設定
- 対象 image は外部保存済み (packed image 非対応)

## 基本フロー
1. `Validate Asset`
2. `Generate Aseprite Job`
3. 必要に応じて `Launch Aseprite`
4. Aseprite extension が `export_path` へ PNG 出力
5. `Reload Exported Image`

## 運用注意
- `export_path` 未生成時の reload はエラー停止
- revision は `*_rNNN.json` で採番
- source は revision ごとにコピー保存され、元画像を直接上書きしない
