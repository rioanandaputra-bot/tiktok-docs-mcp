Docs
# Websocket
Note: Websocket JavaScript APIs are supported starting from SDK version 0.4.0. Lower versions must be adjusted for compatibility.
## .connectSocket
Create a Websocket connection.
### Parameters
**Object**

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| url | string | Developer Server WSS Interface Address | Yes |
| header | Object | HTTP Header, Referer cannot be set in the Header | No |
| protocols | Array.<string> | Subprotocol Array | No |
| timeout | number | Timeout, in milliseconds | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

### Return Value
`SocketTask`
### Example
```
TTMinis.game.connectSocket({
  url: 'wss://example.qq.com',
  header:{
    'content-type': 'application/json'
  }
})
```
## SocketTask
### .close
Close WebSocket connection .
#### Parameters
**Object**

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| code | number | A numeric value representing the status number of a closed connection, indicating the reason for the connection being closed. Default value is 1000 (indicating normal connection closure). | No |
| reason | string | A readable string indicating the reason for the connection closure. This string must be UTF-8 text (not characters) no longer than 123 bytes. | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

### .onOpen
Listen for WebSocket connection open event .
#### Parameter
Listener function for WebSocket connection open event.
**Object response**

| Field | Type | Description |
| --- | --- | --- |
| header | object | HTTP response headers for a successful connection |
| profile | Object | Some debugging information during the network request process |

### .onMessage
Listen for the event of receiving messages from the server via WebSocket.
#### Parameter
The listener function for the WebSocket message event received from the server.
**Object response**

| Field | Type | Description |
| --- | --- | --- |
| data | string/ArrayBuffer | Message returned by the server |

### .onClose
Listen for WebSocket connection close event.
#### Parameter
Listener function for WebSocket connection close event
**Object response**

| Field | Type | Description |
| --- | --- | --- |
| code | number | A numeric value representing the status number of a closed connection, indicating the reason for the connection being closed. |
| reason | string | A readable string indicating the reason for the connection being closed. |

### .onError
Listen for WebSocket error events.
#### Parameters
Listener function for WebSocket error events.
**Object response**

| Field | Type | Description |
| --- | --- | --- |
| errCode | number | Error Code |
| errMsg | string | Error Message |

### .send
Send data via WebSocket connection.
#### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| data | string/ArrayBuffer | Content to be sent | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

Was this document helpful?