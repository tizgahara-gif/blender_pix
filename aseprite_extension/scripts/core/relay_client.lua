local RelayClient = {}
RelayClient.__index = RelayClient

function RelayClient.new(opts)
  local self = setmetatable({}, RelayClient)
  self.url = opts.relay_url or "ws://127.0.0.1:8765"
  self.connected = false
  self.ws = nil
  return self
end

function RelayClient:connect()
  -- MVP placeholder: integrate Aseprite WebSocket API / host bridge in production.
  self.connected = false
  return self.connected
end

function RelayClient:send_texture_exported(payload)
  if not self.connected then
    return false, "relay not connected"
  end
  local text = json.encode(payload)
  self.ws:sendText(text)
  return true
end

function RelayClient:close()
  if self.ws then
    pcall(function() self.ws:close() end)
  end
  self.ws = nil
  self.connected = false
end

return RelayClient
