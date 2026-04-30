Docs
# In-App Ads
In-App Ads (IAA) are a form of advertising that allows developers to display video ads. Currently, rewarded ads are supported for TikTok Minis:
- Rewarded ads: Grant in-app rewards to users after they watch the ad (required)
Note: Please be aware that there are version limitations associated with IAAs.
- **TikTok version**: The IAA feature requires the TikTok app version to be no lower than 44.2.0.** **Please use `canIUse`** **to determine whether the current TikTok app version supports IAA before using the IAA API.
- **TikTok Pro Android**: Currently does not support the short drama IAA feature. During development, please check whether an error code is thrown by the TikTok Pro Android Client.
## Prerequisites
Before setting up in-app ads for your mini app, you must have completed the following:
- [Enabled in-app ads](https://developers.tiktok.com/doc/enable-monetization-features) for your mini app
Make sure your code package also meets the following preconditions:
- Your app has completed integration with the TikTok Minis SDK
- SDK initialization has been correctly completed in HTML
```
<head>
  <script src="https://connect.tiktok-minis.com/drama/sdk.js"></script>
  <script>
    TTMinis.init({
      clientKey: 'your_client_key',
    });
  </script>
</head>
```
- The current project can be successfully launched locally and meets the following basic requirements:
- The project root directory exists `package.json`
- `package.json` must provide at least `dev` or `start` startup script
- The project root directory exists `minis.config.json`
## Applicable scenarios
You should integrate rewarded ads in the following scenarios:
- Watch an ad to unlock a story chapter
- Watch ads to claim rewards such as gold coins, stamina, and items
- Use ad view completion as an explicit incentive behavior
## Best practices
- Perform `canIUse` detection before ad display
- Activate the ad slot immediately after creation
- Use a new ad instance for each display
- Awards are only given when ` isEnded === true `
- When strict risk control is required, developers can record reward distribution logs on the backend
## Rewarded ad integration process
### Step 1: Add an ad placement
Before you start integrating with TikTok's JavaScript APIs for IAAs, you must first add ad placements on your app page.
- Go to your app's **Monetization** page under the **Operation** tab.
- Go to the **In-App Ads (IAAs)** tab, then click the **Ad placements** toggle.
- Click the **Add ad placement **button.
- Enter the name of your ad, select the ad type, then click the **Add** button.
- Rewarded ad
- Interstitial ad
- Switch the ad's status toggle to **Active**.
**Note**: Ad placements are inactive by default and must be switched to **Active** to be used.
- Obtain the **Placement ID **of the ad you want to introduce as an incentive ad.
### Step 1: Your frontend creates an incentive ad instance
To introduce the ad into your app's code, do the following:
- Call the In-App Ads API from the TikTok Minis SDK to create an ad instance. This instance provides methods for displaying and managing the ad.
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});
```
### Step 2: Frontend registers callback
You should register at least two types of callbacks:
- `onError` is used to monitor errors during the playback of an ad video. If an error occurs when the ad component fetches ad materials or in other situations, the error event will be triggered.
- `onClose` is used to monitor the closing of an ad video. When a user taps the close button on a video ad, or the ad automatically closes due to a playback error, the close event will be triggered.
[See the full list of JavaScript APIs for IAA](https://developers.tiktok.com/doc/mini-games-sdk-iaa).
### Step 3: Frontend launches the ad
Display the ad in the corresponding scene of the app and distribute rewards upon completion.
Your frontend calls `show` to display the ad. After the ad is displayed, if the video retrieval or playback fails, the ad will automatically close.
```
rewardedVideoAd.show()
```
Each instance of an incentive ad `rewardedVideoAd` can only be shown once. After displaying, the instance is released, and you will need to recreate the ad instance.
```
const rewardedVideoAd = TTMinis.createRewardedVideoAd({
  adUnitId: 'xxx';
});
rewardedVideoAd.onError(() => {
  console.log('ad display error')
});
rewardedVideoAd.onClose(() => {
  console.log('ad closed')
});
rewardedVideoAd.show().then(() => {
  console.log('ad displayed');
}).catch(() => {
  console.log('ad failed to display');
});
```
### Step 4: Grant reward
Decide whether to grant the reward based on the results of the `onClose` callback:
- `res.isEnded === true`: The ad has been fully played, and reward can be distributed.
- `res.isEnded!== true`: The ad was not fully played, so reward should not be distributed.
### Step 5: Business side updates the reward results
You can do the following after the ad finishes playing:
- Frontend state rewards are directly issued by the frontend
- Alternatively, notify the developer that the backend has recorded the result of the reward collection
- Alternatively, perform both frontend display and server-side persistence simultaneously
## Debugging recommendations
We recommend conducting joint debugging in the following order:
- First, confirm that the ad slot has been created and activated
- Start `minis dev`
- Use the developer options in the debug page to enable ad mock
- Connect to the TikTok app by scanning the QR code
- Trigger ad display on the business page
- Verify separately:
- Full playback
- Closed midway
- Pulling failed / Playing failed
## Frequently Asked Questions
**The ad slot has been created, but why is it still not displaying?**
First, check whether the ad slot has truly been switched to the "activated" state.
**Why does ****show()**** fail?**
Common causes include:
- The current environment does not support this capability
- Ad slot ID is invalid
- Failed to retrieve ad creatives
- An exception occurred during playback
**Can an ad instance repeatedly ****show()****?**
This is not recommended. The current recommended practice is to recreate a new ad instance before each display.
**How to quickly debug the reward link locally**
We recommend enabling IAA mock through the developer tools, so that you can simulate without actually watching ads:
- Playback completed
- Playback failed
- User cancelled
Was this document helpful?