Docs
# Device and Network
## Keyboard
Note: Keyboard JavaScript APIs are supported starting from SDK version 0.6.0. Lower versions must be adjusted for compatibility.
### .showKeyboard
Shows the keyboard for text input.
#### Parameters
`Object` object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| defaultValue | string | Default value displayed in the keyboard input box | Yes |
| maxLength | number | Maximum length of text in the keyboard | Yes |
| multiple | boolean | Is it a multi-line input? | Yes |
| confirmHold | boolean | Whether the keyboard remains visible when the "Done" button is clicked | Yes |
| confirmType | string | The type of the confirm button in the lower right corner | Yes |
| keyboardType | string | Keyboard type (text, or numeric on Client 8.0.57 and above) | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call | No |

### .updateKeyboard
Update the content of the keyboard input box. It will only take effect when the keyboard is in the pulled-up state.
#### Parameters
`Object` object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| value | string | Current value of the keyboard input box | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call | No |

### .hideKeyboard
Hides the active keyboard.
#### Parameters
`Object` object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call | No |

## Keyboard events
Note: Keyboard event JavaScript APIs are supported starting from SDK version 0.6.0. Lower versions must be adjusted for compatibility.
Listeners for keyboard interactions. Each listener receives a `res` object.
- **onKeyboardInput(listener) / offKeyboardInput(listener):** Listen for or remove a listener for keyboard input events.
- **onKeyboardHeightChange(listener) / offKeyboardHeightChange(listener):** Listen for or remove a listener for keyboard height changes.
- **onKeyboardConfirm(listener) / offKeyboardConfirm(listener):** Listen for or remove a listener for the Confirm button click.
- **onKeyboardComplete(listener) / offKeyboardComplete(listener):** Listen for or remove a listener for the keyboard being retracted.
### .onKeyboardInput
Listen for keyboard input events
#### Parameter
`res` object

| Attribute | Type | Description |
| --- | --- | --- |
| value | string | Current value of keyboard input |

### .onKeyboardHeightChange
Listen for keyboard height change events.
#### Parameter
`res` object

| Attribute | Type | Description |
| --- | --- | --- |
| height | number | Keyboard Height |

### .onKeyboardConfirm
Listen for the event when the user clicks the Confirm button on the keyboard.
#### Parameter
`res` object

| Attribute | Type | Description |
| --- | --- | --- |
| value | string | Current value of keyboard input |

### .onKeyboardComplete
Listen for the event of the keyboard collapse event.
#### Parameter
`res` object

| Attribute | Type | Description |
| --- | --- | --- |
| value | string | Current value of keyboard input |

### .offKeyboardInput
Remove the listener function for keyboard input events.
#### Example
```
const
```
### .offKeyboardHeightChange
Remove the listener function for the keyboard height change event.
#### Example
```
const
```
### .offKeyboardConfirm
Remove the event listener function when the user clicks the Confirm button on the keyboard.
#### Example
```
const
```
### .offKeyboardComplete
Remove the listener function for keyboard input events.
#### Example
```
const
```
## Network
### .getNetworkType
Reports current network type and basic connection quality indicators.
#### Parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

Response object (success callback)

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| networkType | string | Network Type |
| signalStrength | Number | Signal strength, unit: dbm |
| hasSystemProxy | Boolean | Does the device use a network proxy? |
| weakNet | Boolean | Is it in a weak connection environment? |

#### Example
```
TTMinis.game.getNetworkType({
  success (res) {
    const networkType = res.networkType
    const weakNet = res.weakNet
  }
})
```
## Touch events
APIs for handling touch input. Each listener callback receives a `res` object containing `touches` (all current points), `changedTouches` (points that triggered the event), and a `timeStamp`.
- **onTouchStart(listener) / offTouchStart(listener)**: Listen for or remove a listener for the start of a touch event.
- **onTouchMove(listener) / offTouchMove(listener)**: Listen for or remove a listener for movement during a touch event.
- **onTouchEnd(listener) / offTouchEnd(listener)**: Listen for or remove a listener for the end of a touch event.
- **onTouchCancel(listener) / offTouchCancel(listener)**: Listen for or remove a listener for when a touch event is interrupted.
A Touch object  (touch array) represents a touch point on a touch device. It typically refers to the action of a finger or stylus on a touchscreen device or touchpad.
- number identifier: The Touch object's unique identifier, a read-only property. This identifier remains unchanged throughout the entire movement of a touch action (referring to a finger's touch) on a plane. It can be used to determine whether the tracked action is the same touch event.
- number screenX: The X coordinate of the touch point relative to the left edge of the screen.
- number screenY: The Y coordinate of the touch point relative to the edge of the screen.
### .onTouchStart
Listens for the start of a touch interaction.
#### Parameters
`res` object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| touches | Array<object> | Touch array. List of all current touchpoints |
| changedTouches | Array<object> | Touch array. The list of touchpoints that triggered this event |
| timeStamp | number | Timestamp when the event is triggered |

### .onTouchMove
Listens for touch movement events.
#### Parameters
`res` object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| touches | Array<object> | Touch array. List of all current touchpoints |
| changedTouches | Array<object> | Touch array. The list of touchpoints that triggered this event |
| timeStamp | number | Timestamp when the event is triggered |

### .onTouchEnd
Listens for the end of a touch interaction.
#### Parameters
`res` object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| touches | Array<object> | Touch array. List of all current touchpoints |
| changedTouches | Array<object> | Touch array. The list of touchpoints that triggered this event |
| timeStamp | number | Timestamp when the event is triggered |

### .onTouchCancel
Listens for touch interruptions/cancellations.
#### Parameters
`res` object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| touches | Array<object> | Touch array. List of all current touchpoints |
| changedTouches | Array<object> | Touch array. The list of touchpoints that triggered this event |
| timeStamp | number | Timestamp when the event is triggered |

### .offTouchStart
Removes a start‑touch listener. The listener function passed to `onTouchStart`. If this parameter is not passed, all listener functions will be removed.
#### Example
```
const listener = function (res) { console.log(res) }

TTMinis.game.onTouchStart(listener)
TTMinis.game.offTouchStart(listener) // You must pass the same function object used for listening.
```
### .offTouchMove
Removes a move‑touch listener. The listener function passed to `onTouchMove`. If this parameter is not passed, all listener functions will be removed.
#### Example
```
const listener = function (res) { console.log(res) }

TTMinis.game.onTouchMove(listener)
TTMinis.game.offTouchMove(listener) // You must pass the same function object used for listening.
```
### .offTouchEnd
Removes an end‑touch listener. The listener function passed to `onTouchEnd`. If this parameter is not passed, all listener functions will be removed.
#### Example
```
const listener = function (res) { console.log(res) }

TTMinis.game.onTouchEnd(listener)
TTMinis.game.offTouchEnd(listener) // You must pass the same function object used for listening.
```
### .offTouchCancel
Removes a cancel‑touch listener. The listener function passed in by `onTouchCancel`. If this parameter is not passed, all listener functions will be removed.
#### Example
```
const listener = function (res) { console.log(res) }

TTMinis.game.onTouchCancel(listener)
TTMinis.game.offTouchCancel(listener) // You must pass the same function object used for listening.
```
## Vibrate
### .vibrateShort
Note: This API is supported starting from SDK version 0.10.0. Lower versions must be adjusted for compatibility.
Make the phone vibrate for 15ms.
#### Parameter
Object object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Vibration intensity type, valid values are: heavy, medium, light | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

### .vibrateLong
Note: This API is supported starting from SDK version 0.10.0. Lower versions must be adjusted for compatibility.
Make the phone vibrate for 400 ms.
#### Parameter
Object object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

Was this document helpful?