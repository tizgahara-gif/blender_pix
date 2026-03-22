local SyncManager = dofile("scripts/core/sync_manager.lua")

return {
  title = "Sync Now",
  run = function(plugin)
    local sprite = app.activeSprite
    if not sprite then
      app.alert("No active sprite")
      return
    end
    local job = sprite.data.blender_job
    if not job then
      app.alert("No Blender job attached")
      return
    end
    SyncManager.sync_now(sprite, job, plugin)
  end,
}
