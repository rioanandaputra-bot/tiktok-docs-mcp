Docs
These APIs promote user retention by integrating missions related to the TikTok interface and home screen shortcuts.
**Note:** All APIs in this section require **TikTok version 41.0.0** or higher. Always use `canIUse()` first.

| **API** | **Description** | **Context** |
| --- | --- | --- |
| **addShortcut(opts)** | Prompts the user to Add the game icon to their desktop/home screen. | Triggers the system-level prompt for shortcut creation. |
| **getShortcutMissionReward(opts)** | Checks if the user is eligible to claim the reward for adding the desktop shortcut. | Returns `canReceiveReward: boolean`in the success callback. |
| **startEntranceMission(options)** | Jumps the user to the sidebar of the TikTok Profile to complete a "follow-up education" task, guiding them to the game's entry point for repeat visits. | Navigates the user outside of the game and into the host app's interface. |
| **getEntranceMissionReward(options)** | Checks if the user is eligible to claim the reward for completing the sidebar revisit task. | Returns `canReceiveReward: boolean`in the success callback. |

## .canIUse(schema)
[Determine whether the APIs, callbacks, and parameters](https://developers.tiktok.com/doc/mini-games-sdk-basic-utility#)of the mini-game are available in the current version.
### Parameter
```
type schema = string

Use ${api}.${method}.${param}.${option} to call

- api: API name
- method: call mode, valid values are return, object, callback
- params: parameter or return value
- options: valid values of parameters or attributes of return values
```
### Example
```
if (TTMinis.game.canIUse("startEntranceMission")) {
  TTMinis.startEntranceMission({
    success: () => {
      console.log("success");
    },
    fail: () => {
      console.log("fail");
    },
    complete: () => {
      sonsole.log("complete");
    }
  })
}
```
## .startEntranceMission(opts)
Jump to the TikTok Profile sidebar to guide repeat visits.
### Parameters
**success**: Callback for successful execution
```
type success = () => void;
```
**fail**: Callback for execution failure
```
type fail = () => void;
```
**complete**: Callback for execution completion (including success and failure)
```
type complete = () => void;
```
### Example
```
TTMinis.startEntranceMission({
  success: () => {
    console.log("success");
  },
  fail: () => {
    console.log("fail");
  },
  complete: () => {
    sonsole.log("complete");
  }
})
```
## .getEntranceMissionReward(opts)
Determine whether the user can claim the reward for completing the follow-up education task.
### Parameters
**success**: Callback for successful execution
```
type success = (res: {
  canReceiveReward: boolean;
}) => void;
```
**fail**: Callback for execution failure
```
type fail = () => void;
```
**complete**: Callback for execution completion (including success and failure)
```
type complete = () => void;
```
### Example
```
TTMinis.getEntranceMissionReward({
  success: ({ canReceiveReward }) => {
    console.log("success", canReceiveReward);
  },
  fail: () => {
    console.log("fail");
  },
  complete: () => {
    sonsole.log("complete");
  }
})
```
## .addShortcut(opts)
Add mini game to home screen.
### Parameters
**success**: Callback for successful execution
```
type success = () => void;
```
**fail**: Callback for execution failure
```
type fail = (error: {
  error_code: number;
  error_msg: string;
}) => void;
```
**complete**: Callback for execution completion (including success and failure)
```
type complete = () => void;
```
### Example
```
TTMinis.game.addShortcut({
  success: () => {
    console.log("success");
  },
  fail: (error) => {
    console.log("fail", error);
  },
  complete: () => {
    sonsole.log("complete");
  }
})
```
## .getShortcutMissionReward(opts)
Determine whether the user can claim the add-to-home-screen reward.
### Parameters
**success**: Callback for successful execution
```
type success = () => void;
```
**fail**: Callback for execution failure
```
type fail = (error: {
  error_code: number;
  error_msg: string;
}) => void;
```
**complete**: Callback for execution completion (including success and failure)
```
type complete = () => void;
```
### Example
```
TTMinis.getShortcutMissionReward({
  success: ({ canReceiveReward }) => {
    console.log("success", canReceiveReward);
  },
  fail: (error) => {
    console.log("fail", error);
  },
  complete: () => {
    sonsole.log("complete");
  }
})
```
Was this document helpful?