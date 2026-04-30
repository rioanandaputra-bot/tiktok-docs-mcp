Docs
These APIs allow the game to listen to or retrieve information about its transition between the foreground and background states.

| **API** | **Description** | **Context** |
| --- | --- | --- |
| **.onShow(cb)** | Listener: Registers a callback when the Mini Game comes back to the foreground (becomes visible) from the background. | Useful for pausing/resuming game action and checking for parameters passed during re-entry. |
| **.offShow(cb)** | Cancels the `onShow`listener. | -- |
| **.onHide(cb)** | Listener: Registers a callback when the Mini Game is sent to the background (hidden). | Critical for saving game state and pausing resource consumption. |
| **.offHide(cb)** | Cancels the `onHide`listener. | -- |
| **.getLaunchOptionsSync** | Synchronous: Retrieves the parameters used when the Mini Game was cold-started (opened for the first time in the session). | Returns object containing scene (entry point) and query (URL parameters). |
| **.getEnterOptionsSync** | Synchronous: Retrieves the parameters used for any start (cold start or hot start/return from background). | Provides consistent entry parameters regardless of the starting state. |

## .onShow(cb)
Listen to the mini game and return to foreground.
### Parameters
```
type Callback = (result: { query: Record<string, string> }) => void;
```
### Example
```
TTMinis.game.onShow((result) => {
  let query = result.query;
  // Do something when mini game shows
});
```
## .offShow(cb)
Cancel the game monitoring and return to the foreground.
### Parameters
```
type Callback = () => void;
```
## .onHide(cb)
Listen for events when the mini game is hidden in the background
### Parameters
```
type Callback = () => void;
```
### Example
```
TTMinis.game.onHide(() => {
  // Do something when mini game hides
});
```
## .offHide(cb)
Cancel listening to the mini game when hidden in the background.
### Parameters
```
type Callback = () => void;
```
### Example
```
TTMinis.game.offHide(() => {
  // Do something when off hide listener
});
```
## .getLaunchOptionsSync
Get the parameters during the cold start of the mini game.
### Return value
```
interface LaunchOptions {
  scene: string;
  query: object;
}
```
### Example
```
const launchOptions = TTMinis.game.getLaunchOptionsSync()
```
## .getEnterOptionsSync
Get the parameters for opening the mini game, including cold start and warm start.
### Return value
```
interface EnterOptions {
  scene: string;
  query: object;
}
```
### Example
```
const enterOptions = TTMinis.game.getEnterOptionsSync()
```
Was this document helpful?