Docs
# Device
## disableCapture(cb)
Disable screen recording to prevent end users from stealing copyrights by recording short drama videos.
### Parameters
```
/**
 * Disable user screen recording privileges
 * @param {disableCaptureCallback} cb - callback function, see params below
 */
TTMinis.disableCapture(cb);
```
Callback Response
```
{
  isSuccess: true // Call JavaScript API success
}
```
### Example
```
TTMinis.disableCapture((response) => {
    if (response.isSuccess === true) {
        
    }
))
```
## enableCapture(cb)
Enable screen recording.
### Parameters
```
/**
 * Enable user screen recording privileges
 * @param {enableCaptureCallback} cb - callback function, see params below
 */
TTMinis.enableCapture(cb);
```
### Callback response
```
{
  isSuccess: true // Call JavaScript API success
}
```
### Example
```
TTMinis.enableCapture((response) => {
    if (response.isSuccess === true) {
        
    }
))
```
## getDeviceInfo()
Get user's device information.
### Parameters
```
/**
 * Get user device information
 */
TTMinis.getDeviceInfo();
```
### Response
```
{
  data: {
    bottomHeight: '34',  // Device bottom height setting.
  }
}
```
### Example
```
const { data } = TTMinis.getDeviceInfo();

if (data) {
  const { bottomHeight } = data;
  // use the device info for your program
}
```
Was this document helpful?