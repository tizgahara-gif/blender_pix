local RelayClient = dofile("scripts/core/relay_client.lua")

local SyncManager = {}

local active_sync = {}

local function build_event(job)
  return {
    event_id = tostring(app.fs.fileTitle(job.task.export_path)) .. "-" .. tostring(os.time()),
    type = "texture_exported",
    export_path = job.task.export_path,
    revision = job.revision,
    asset_name = job.asset.object_name,
    map_type = job.task.map_type,
    timestamp = os.date("!%Y-%m-%dT%H:%M:%SZ"),
  }
end

function SyncManager.attach_sprite_sync(sprite, job, plugin)
  local prefs = plugin.preferences
  local relay = RelayClient.new({ relay_url = prefs.relay_url })
  relay:connect()

  local timer = Timer {
    interval = math.max(0.1, prefs.debounce_seconds or 0.5),
    ontick = function()
      if prefs.auto_validate_before_export and not job.task.export_path then
        return
      end
      local ok, err = pcall(function()
        sprite:saveCopyAs(job.task.export_path)
      end)
      if ok then
        relay:send_texture_exported(build_event(job))
      else
        print("[sync_manager] saveCopyAs failed: " .. tostring(err))
      end
      timer:stop()
    end,
  }

  local listener = function()
    timer:stop()
    timer:start()
  end

  sprite.events:on("change", listener)
  active_sync[sprite] = { timer = timer, relay = relay, listener = listener }
end

function SyncManager.detach_sprite_sync(sprite)
  local state = active_sync[sprite]
  if not state then return end
  pcall(function() state.timer:stop() end)
  pcall(function() sprite.events:off("change", state.listener) end)
  pcall(function() state.relay:close() end)
  active_sync[sprite] = nil
end

function SyncManager.sync_now(sprite, job, plugin)
  local ok, err = pcall(function() sprite:saveCopyAs(job.task.export_path) end)
  if not ok then
    print("[sync_manager] sync_now failed: " .. tostring(err))
  end
end

return SyncManager
