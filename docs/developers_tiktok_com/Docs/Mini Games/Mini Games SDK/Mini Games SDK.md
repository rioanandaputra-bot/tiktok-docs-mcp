Docs
**Mini Games SDK **is a client-side JavaScript SDK that runs inside the TikTok app. It provides in-app capabilities like login and authorization, payments, UI triggers, rewarded ads, lifecycle hooks, networking, and capability detection. JavaScript APIs contained within the Mini Games SDK contain the prefix **TTMinis.game**.
TikTok supports two runtime types for your mini game: **HTML** and **Native**. As the Mini Games SDK is already preloaded into the TikTok app, you only need to initialize the SDK if your mini game uses HTML runtime.
- [**HTML**: Web-based build that runs in a webview using HTML/CSS/JavaScript, fast to ship but limited performance. Requires you to initialize Mini Games SDK in your HTML](https://developers.tiktok.com/doc/mini-games-sdk-get-started) before calling JavaScript APIs.
- **Native**: Compiled mini‑game that runs on TikTok’s native runtime, with optimized performance and smoother gameplay. No initialization required, you can call JavaScript APIs directly.
Here is a list of the JavaScript APIs contained within the Mini Games SDK:

| **Category** | **Function** | **Description** |
| --- | --- | --- |
| Basic Utility | `canIUse(schema)` | Checks if a JSAPI feature is available in the current client version |
| `env.USER_DATA_PATH` | Provides the local file system path to the user's data directory |
| `request()` | Initiates an HTTPS network request |
| `RequestTask.abort()` | Cancels an ongoing network request |
| Data Caching | `setStorage()` | Asynchronously saves a key-value pair to local cache |
| `setStorageSync()` | Synchronously saves a key-value pair to local cache |
| `getStorage()` | Asynchronously retrieves a value from local cache |
| `getStorageSync()` | Synchronously retrieves a value from local cache |
| `removeStorage()` | Asynchronously removes a key-value pair from local cache |
| `removeStorageSync()` | Synchronously removes a key-value pair from local cache |
| `clearStorage()` | Asynchronously clears all data from the mini-game's cache |
| `clearStorageSync()` | Synchronously clears all data from the mini-game's cache |
| `.getStorageInfo()` | Asynchronously obtain relevant information about the current storage |
| `.getStorageInfoSync()` | Synchronously obtain relevant information about the current storage |
| Device and Network | `showKeyboard()` | Shows the keyboard for text input with customizable types and buttons |
| `updateKeyboard()` | Updates the content of the keyboard input box while it is active |
| `hideKeyboard()` | Manually hides the active keyboard |
| `onKeyboardInput(listener)` | Registers a listener for real-time keyboard input events |
| `offKeyboardInput(listener)` | Removes a listener for keyboard input events |
| `onKeyboardHeightChange(listener)` | Registers a listener for changes in the keyboard's height |
| `offKeyboardHeightChange(listener)` | Removes a listener for keyboard height change events |
| `onKeyboardConfirm(listener)` | Registers a listener for when the user clicks the "Confirm" button |
| `offKeyboardConfirm(listener)` | Removes a listener for the keyboard "Confirm" button event |
| `onKeyboardComplete(listener)` | Registers a listener for the event of the keyboard being retracted |
| `offKeyboardComplete(listener)` | Removes a listener for the keyboard retraction event |
| `getNetworkType()` | Gets the user's current network type (such as 'wifi', '4g') |
| `onTouchStart(listener)` | Registers a listener for the start of a touch event |
| `onTouchMove(listener)` | Registers a listener for movement during a touch event |
| `onTouchEnd(listener)` | Registers a listener for the end of a touch event |
| `onTouchCancel(listener)` | Registers a listener for when a touch event is interrupted |
| `offTouchStart(listener)` | Removes a listener for the `onTouchStart` event |
| `offTouchMove(listener)` | Removes a listener for the `onTouchMove` event |
| `offTouchEnd(listener)` | Removes a listener for the `onTouchEnd` event |
| `offTouchCancel(listener)` | Removes a listener for the `onTouchCancel` event |
| `.vibrateShort` | Make the phone vibrate for 15ms |
| `.vibrateLong` | Make the phone vibrate for 400 ms |
| Event | `onShow(cb)` | Registers a callback for when the mini-game returns to the foreground |
| `offShow(cb)` | Unregisters a callback for the `onShow` event |
| `onHide(cb)` | Registers a callback for when the mini-game is sent to the background |
| `offHide(cb)` | Unregisters a callback for the `onHide` event |
| `getLaunchOptionsSync()` | Gets query parameters from the mini-game's initial cold start |
| `getEnterOptionsSync()` | Gets query parameters from the most recent time the user opened the mini game |
| File | `getFileSystemManager()` | Returns the global manager for performing file system operations |
| `readFile()` | Asynchronously reads the content of a local file |
| `readFileSync()` | Synchronously reads the content of a local file |
| `access()` | Asynchronously checks if a file or directory exists |
| `accessSync()` | Synchronously checks if a file or directory exists |
| `writeFile()` | Asynchronously writes data to a local file |
| `writeFileSync()` | Synchronously writes data to a local file |
| `mkdir()` | Asynchronously creates a new directory |
| `mkdirSync()` | Synchronously creates a new directory |
| `copyFile()` | Asynchronously copies a file to a new location |
| `copyFileSync()` | Synchronously copies a file to a new location |
|  | `unzip()` | Unzips the file |
| In-App-Ads | `createRewardedVideoAd()` | Creates a rewarded video ad instance using an ad unit ID |
| `rewardedVideoAd.show()` | Displays the loaded rewarded video ad |
| `rewardedVideoAd.onClose()` | Registers a listener for when the rewarded ad is closed |
| `rewardedVideoAd.offClose()` | Unregisters a listener for the rewarded ad close event |
| `rewardedVideoAd.onError()` | Registers a listener for errors during ad playback |
| `rewardedVideoAd.offError()` | Unregisters a listener for ad playback errors |
| `createInterstitialAd()` | Creates an interstitial ad instance using an ad unit ID |
| `interstitialAd.show()` | Displays the loaded interstitial ad |
| `interstitialAd.onClose()` | Registers a listener for when the interstitial ad is closed |
| `interstitialAd.offClose()` | Unregisters a listener for the interstitial ad close event |
| `interstitialAd.onError()` | Registers a listener for errors during ad playback |
| `interstitialAd.offError()` | Unregisters a listener for ad playback errors |
| In-App Purchases | `checkBalance()` | Checks if the user's BEANS balance is sufficient for a specified amount |
| `recharge()` | Initiates the client-side recharge flow for a given tier ID |
| `pay()` | Triggers the client payment sheet using a `trade_order_id` |
| `navigateToBalance()` | Directs the user to their BEANS balance page within TikTok |
| Login and Authorization | `login()` | Starts the silent login flow to get an authorization code |
| `authorize()` | Prompts the user to grant permissions for specific scopes |
| Media | `createInnerAudioContext()` | Creates an instance for straightforward audio playback |
| `createWebAudioContext()` | Creates an instance for advanced audio synthesis and processing |
| `play()`/ `pause()`/ `stop()` | Controls for starting, pausing, or stopping audio playback |
| `seek(position)` | Jumps to a specific time position (in seconds) |
| `destroy()` | Destroys the audio instance and releases resources |
| `onPlay()`/ `offPlay()` | Manages listeners for the start/resume playback event |
| `onPause()`/ `offPause()` | Manages listeners for the audio pause event |
| `onStop()`/ `offStop()` | Manages listeners for the audio stop event |
| `onEnded()`/ `offEnded()` | Manages listeners for when playback completes naturally |
| `onCanplay()`/ `offCanplay()` | Manages listeners for when audio is buffered enough to play |
| `onTimeUpdate()`/ `offTimeUpdate()` | Manages listeners for playback progress updates |
| `onSeeking()`/ `onSeeked()` | Manages listeners for the start and end of seek operations |
| `onWaiting()`/ `offWaiting()` | Manages listeners for playback stalls due to buffering |
| `onError()`/ `offError()` | Manages listeners for errors (returns `errMsg`and `errorCode`) |
| `decodeAudioData()` | Asynchronously decodes an `ArrayBuffer`into an `AudioBuffer` |
| `resume()`/ `suspend()` | Resumes or pauses the entire audio context (returns Promise) |
| `close()` | Closes the context and immediately releases all resources |
| `createBuffer()` | Creates an empty `AudioBuffer`with specified channels and length |
| `createBufferSource()` | Creates a node to play data from an `AudioBuffer` |
| `createGain()` | Creates a node to control audio volume |
| `createOscillator()` | Creates a node to generate periodic waveforms |
| `createDelay(maxTime)` | Creates a node to delay the incoming audio signal |
| `createBiquadFilter()` | Creates a node for frequency filtering (low-pass, high-pass, etc.) |
| `createAnalyser()` | Creates a node for real-time time and frequency analysis |
| `createPanner()` | Creates a node for spatializing audio in 3D space |
| `createDynamicsCompressor()` | Creates a node for signal compression (threshold, knee, etc.) |
| `createWaveShaper()` | Creates a node for non-linear distortion effects |
| `createChannelMerger()` | Combines multiple input streams into a single output |
| `createChannelSplitter()` | Separates an input stream into individual channel outputs |
| `createScriptProcessor()` | Creates a node for custom JavaScript-based audio processing |
| Render and Canvas | `createCanvas()` | Creates a canvas element for drawing (first call creates the on-screen canvas) |
| `createImage()` | Creates an image object for loading and rendering image sources |
| `Canvas.getContext()` | Retrieves the drawing context ('2d' or 'webgl') from a canvas object |
| `Canvas.toDataURL()` | Exports the canvas content as a base64-encoded data URI string |
| `setPreferredFramesPerSecond` | Modify the rendering frame rate |
| `loadFont()` | Loads a custom font file for use in rendering |
| Revisit Incentives | `startEntranceMission()` | Guides the user to add the mini-game to their TikTok Profile sidebar |
| `getEntranceMissionReward()` | Checks if the user is eligible for the reward for completing the profile entrance task |
| `addShortcut()` | Prompts the user to add a shortcut to their device's home screen |
| `getShortcutMissionReward()` | Checks if the user can claim the reward for adding the shortcut |
| Sharing | `shareToStory` | Shares the Minis content directly to the user's TikTok Story |
| `shareAppMessage` | Triggers the contact selection interface to send a DM |
| `onCopyUrl` | Listens for the "Copy Link" action to inject custom metadata |
| `offCopyUrl` | Removes listeners for the "Copy Link" event |
| Subpackage Loading | `preDownloadSubpackage()` | Downloads a subpackage in the background without executing it |
| `loadSubpackage()` | Downloads and immediately executes the code within a subpackage |
| `LoadSubpackageTask.onProgressUpdate()` | Listens for progress updates on a subpackage download task |
| `PreDownloadSubpackageTask` | Registers a listener for subpackage download progress changes, receiving an object with progress percentage |
| System | `getSystemInfoSync()` | Synchronously retrieves device and system information |
| `getSystemInfo()` | Asynchronously retrieves device and system information |
| `getWindowInfo` | Returns an object with current device and window metrics |
| UI | `getMenuButtonBoundingClientRect()` | **(HTML mini games only)**Get the layout position information of the menu button (capsule button in the upper right corner) |
| Websocket | `connectSocket` | Creates a WebSocket connection to the specified WSS URL with optional headers, protocols, and timeout, returning a SocketTask. |
| `SocketTask.close` | Closes the WebSocket connection, optionally providing a close code and reason, with success/fail/complete callbacks. |
| `onOpen` | Registers a listener for when the WebSocket connection opens, receiving response headers and debugging profile info. |
| `onMessage` | Registers a listener for incoming WebSocket messages, receiving the server’s data as a string or ArrayBuffer. |
| `onClose` | Registers a listener for the WebSocket close event, receiving the close status code and reason. |
| `onError` | Registers a listener for WebSocket errors, receiving an error code and message. |
| `send` | Sends string or ArrayBuffer data over the WebSocket with optional success/fail/complete callbacks. |

Was this document helpful?