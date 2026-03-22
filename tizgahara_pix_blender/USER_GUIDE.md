# USER GUIDE

## 基本
- Packed image は非対応
- generated image（filepath空）は source PNG を生成して job 化

## Blender Auto Sync (Relay)
1. Preferences で `auto_sync_enabled` と `relay_enabled` を ON
2. `relay_inbox_path` を設定
3. `Generate Aseprite Job` 実行
4. Aseprite 側が `job.task.export_path` に export
5. Relay が `texture_exported` を inbox へ追記
6. Blender がイベントを poll し、`reload_settle_delay` 後に `Image.reload()`

## Aseprite 側の使い方（概要）
- Open Blender Job 後、変更を debounce して `saveCopyAs(job.task.export_path)`
- Save/Save As と Blender export は分離
- relay 未接続時は notify 失敗しても extension は落とさない
- guide layer は export に含めない
