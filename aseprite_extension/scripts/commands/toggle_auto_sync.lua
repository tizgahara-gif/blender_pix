return {
  title = "Toggle Auto Sync",
  run = function(plugin)
    plugin.preferences.auto_sync_default = not plugin.preferences.auto_sync_default
    app.alert("Auto Sync: " .. tostring(plugin.preferences.auto_sync_default))
  end,
}
