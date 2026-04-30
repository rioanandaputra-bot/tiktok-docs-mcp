Docs
# Event
## on(event,cb)
Listen to the TikTok Minis lifecycle-related events to handle business logic.
### Parameters
```
/**
 * Listen to TikTok Minis life cycle events
 * @param {string} event - TikTok Minis life cycle events 'minis.hide'、'minis.show'
 * @param {onCallback} cb - callback function, see params below
 */
TTMinis.on(event, cb);
```
### Response
```
callbackId: string
```
### Example
```
type Callback = () => void;

const callbackId = TTMinis.On('minis.show', callback: Callback)
```
## off(event, cb)
Remove the listener to the TikTok Minis lifecycle events.
### Parameters
```
/**
 * Unlisten to the minis lifecycle
 * @param {string} event - minis life cycle events 'minis.hide'、'minis.show'
 * @param {string} callbackId - callbackId
 */
TTMinis.off(event, callbackId);
```
### Example
```
TTMinis.off('minis.show', callbackId)
```
Was this document helpful?