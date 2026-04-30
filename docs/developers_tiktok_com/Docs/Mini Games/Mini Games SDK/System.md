Docs
# System
Retrieves device and system information, which is essential for creating responsive layouts, optimizing rendering, and tailoring user experiences. The API is available in both synchronous and asynchronous versions to suit different use cases.
## .getSystemInfoSync
Use during initialization (like when the game first loads) to get layout information immediately, but be aware that it can block the main thread.
### Return value

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| screenWidth | number | Screen width, unit: px |
| screenHeight | number | Screen height, unit: px |
| windowWidth | number | Available window width, unit: px |
| windowHeight | number | Available window height, unit: px |
| devicePixelRatio | number | Device pixel ratio |
| pixelRatio | number | Device pixel ratio |
| deviceOrientation | string | Device orientation |
| system | string | Operating system and version |
| platform | 'ios' | 'android' | Client platform |
| language | string | Language |
| safeArea | -- | Safe area in the positive direction of portrait mode |
| SDKVersion | string | -- |
| version | string | Client version number |

### Example
```
try {
  const res = TTMinis.game.getSystemInfoSync()
  console.log(res.pixelRatio)
  console.log(res.windowWidth)
  console.log(res.windowHeight)
  console.log(res.language)
  console.log(res.version)
  console.log(res.platform)
} catch (e) {
  // Do something when catch error
}
```
## .getSystemInfo
Use with callbacks for non-critical tasks or when information is needed after the initial render to avoid blocking UI updates.
### Return value
Success callback

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| screenWidth | number | Screen width, unit: px |
| screenHeight | number | Screen height, unit: px |
| windowWidth | number | Available window width, unit: px |
| windowHeight | number | Available window height, unit: px |
| devicePixelRatio | number | Device pixel ratio |
| pixelRatio | number | Device pixel ratio |
| deviceOrientation | string | Device orientation |
| system | string | Operating system and version |
| platform | 'ios' | 'android' | Client platform |
| language | string | Language |
| safeArea | -- | Safe area in the positive direction of portrait mode |
| SDKVersion | string | -- |
| version | string | Client version number |

### Example
```
TTMinis.game.getSystemInfo({
  success (res) {
    console.log(res.pixelRatio)
    console.log(res.windowWidth)
    console.log(res.windowHeight)
    console.log(res.language)
    console.log(res.version)
    console.log(res.platform)
  }
})
```
## .getWindowInfo
Returns an object with current device and window metrics.
Note: Supported starting from SDK version 0.2.0, compatibility handling is required for lower versions.
### Return Value

| Attribute | Type | Instructions |
| --- | --- | --- |
| pixelRatio | number | Device pixel ratio |
| screenWidth | number | Screen width, unit in pixels |
| screenHeight | number | Screen height, unit in pixels |
| windowWidth | number | Available window width, unit in pixels |
| windowHeight | number | Available window height, unit in pixels |
| statusBarHeight | number | Height of the status bar, unit in pixels |
| safeArea | Object | The safe area in the positive direction of portrait mode. Some devices do not have the concept of a safe area and will not return the `safeArea`field, so developers need to handle compatibility themselves. |
| screenTop | number | The y value of the upper edge of the window |

### Example
```
const windowInfo = TTMinis.game.getWindowInfo()

console.log(windowInfo.pixelRatio)
console.log(windowInfo.screenWidth)
console.log(windowInfo.screenHeight)
console.log(windowInfo.windowWidth)
console.log(windowInfo.windowHeight)
console.log(windowInfo.statusBarHeight)
console.log(windowInfo.safeArea)
console.log(windowInfo.screenTop)
```
Was this document helpful?