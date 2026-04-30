Docs
# In-App Ads
This API allows the mini app to integrate and manage in-app ads (rewarded video ads) for monetization.
## .createRewardedVideoAd(opts)
Creates an instance of a rewarded video ad object for later use.
### Parameters
- **adUnitId: **The unique identifier for the ad slot, defined in the Developer Portal
### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
})
```
## rewardedVideoAd
The rewarded video ad object.

| **Method** | **Description** | **Context** |
| --- | --- | --- |
| **.show()** | Displays the loaded rewarded video ad to the user. Returns a promise. | Must be called at an appropriate break point in the app where the user expects a reward. |
| **.onClose(cb)** | Listener: Registers a callback function triggered when the user closes the ad. | The callback receives a result.isEnded: boolean, which determines if the user watched the ad to completion (and thus earned the reward). |
| **.offClose(cb)** | Cancels the close listener. | Used for cleanup to prevent memory leaks or incorrect reward granting. |
| **.onError(cb)** | Listener: Registers a callback function triggered if the ad fails to load or play (e.g., due to network issues or no available inventory). | Used to handle errors gracefully, perhaps by giving the user the reward anyway or offering an alternative action. |
| **.offError(cb)** | Cancels the error listener. | Used for cleanup. |

### .show()
Displays the loaded rewarded video ad to the user. Returns a promise. Must be called at an appropriate break point in the app where the user expects a reward.
#### Parameters
None
#### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});

rewardedVideoAd.show().then(() => {
  console.log('Display video ad');
}).catch(() => {
  console.log('Display video ad failed');
})
```
### .onClose(cb)
Registers a callback function triggered when the user closes the ad. The callback receives a boolean result which determines if the user watched the ad to completion (and thus earned the reward).
#### Parameters
- **Callback: **The callback function when the ad is closed
```
type Callback = (result: { isEnded: boolean }) => void
```
#### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});

rewardedVideoAd.onClose(() => {
  console.log('Rewarded video ad closed')
})
```
### .offClose(cb)
Cancel listening when ads are closed. Used for cleanup to prevent memory leaks or incorrect reward granting.
#### Parameters
- **Callback: **Callback function when the ad is closed
```
type Callback = () => void
```
#### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

rewardedVideoAd.onClose(listener);
// When not needed
rewardedVideoAd.offClose(listener);
```
### .onError(cb)
Registers a callback function triggered if the ad fails to load or play (for example: due to network issues or no available inventory). Used to handle errors gracefully, perhaps by giving the user the reward anyway or offering an alternative action.
#### Parameters
- **Callback **: Callback when ad pull or play fails
```
type Callback = () => void
```
#### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

rewardedVideoAd.onError(listener);
```
### .offError(cb)
Cancel listening when ads are pulled or played incorrectly. Used for cleanup.
#### Parameters
- **Callback: **Callback function for ad pulling or playing error
```
type Callback = () => void
```
#### Example
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

rewardedVideoAd.onClose(listener);
// When not needed
rewardedVideoAd.offClose(listener);
```
## .createInterstitialAd
**Note**: This feature is supported starting from SDK version 0.3.0, compatibility handling is required for lower versions.
Create an interstitial ad component.
### Parameter
- `adUnitId`: (string) Ad Slot ID
### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
})
```
## interstitialAd
### .show
Show interstitial ad.
#### Return Value
Result of the interstitial ad display operation.
#### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
});

interstitialAd.show().then(() => {
  console.log('Interstitial ad display');
}).catch(() => {
  console.log('Interstitial ad display failed.');
})
```
### .onClose
Listen for the close event of the interstitial ad, which is triggered when the ad is closed.
#### Parameter
The event listener function for the user tapping the  "Close Ad"  button.
#### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
});

interstitialAd.onClose(() => {
  console.log('The interstitial ad has been closed.)
})
```
### .offClose
Remove the event listener function for the user when tapping the  "Close Ad" button.
#### Parameter
The listener function passed to `onClose`.
#### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

interstitialAd.onClose(listener);
// When it's not needed
interstitialAd.offClose(listener);
```
### .onError
Listen for the error event of interstitial ad display, which is triggered when interstitial ad display fails.
#### Parameter
**Object res**

| Field | Type | Description |
| --- | --- | --- |
| errMsg | string | Error Message |
| errorCode | number | Error Code |

#### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

interstitialAd.onError(listener);
```
### .offError
Cancel the listener when there is an error in ad retrieval or playback.
#### Parameter
The listener function passed to onError.
#### Example
```
const interstitialAd = TTMinis.createInterstitialAd({
  adUnitId: 'xxx';
});

function listener() {
  console.log('error emit')
}

interstitialAd.onClose(listener);
// When it's not needed
interstitialAd.offClose(listener);
```
## Error codes
### Create ad APIs

| Error code | Error message |
| --- | --- |
| 11001 | Ad slot ID is empty, invalid parameter |
| 20000 | Client request to backend failed |
| 50000 | System Error |
| 500 | Internal error in the Server system |
| 10001 | Ad slot verification parameter error |
| 20001 | Ad slot does not exist |
| 20002 | Ad slot does not match the requested MinisID |
| 20003 | Ad slot status is abnormal |
| 20007 | Ad slot type error |
| 30001 | Requests for the same ad slot are too frequent |

### Show ad APIs

| Error code | Sub error code | Error message |
| --- | --- | --- |
| 10001 | -- | The incoming advertisement instance ID parameter is empty, which is an invalid parameter |
| 11002 | -- | Ad instance ID does not match, corresponding ad instance not found |
| 11003 | -- | Ad instances have already been displayed and cannot be reused |
| 11004 | -- | The time interval since the last playback is insufficient, and interstitial ads are not allowed to be displayed |
| 11005 | -- | has exceeded the limit on the number of interstitial ad plays, and interstitial ads are not allowed to be displayed |
| 30001 | -- | User clicks to exit without finishing watching (no incentive received) |
| 50000 | -- | System Error |
| 50101 | Client network environment error |
| 50102-50107 | Server Error |

Was this document helpful?