Docs
# In-App Ads
In-App Ads (IAA) are a form of advertising that allows developers to display video ads. There are two types:
- Rewarded ads: Grant in-game rewards to users after they watch the ad (required)
- Interstitial ads: Ad that appears during natural breaks in the gameplay
## Prerequisites
Before setting up in-app ads for your mini game, you must have completed the following:
- [Enabled in-app ads](https://developers.tiktok.com/doc/enable-monetization-features) for your mini game
## Add an ad placement
Before you start integrating with TikTok's JavaScript APIs for IAAs, you must first add ad placements on your mini game's app page.
- Go to your app's **Monetization** page under the **Operation** tab.
- Go to the **In-App Ads (IAAs)** tab, then click the **Ad placements** toggle.
- Click the **Add ad placement **button.
- Enter the name of your ad, select the ad type, then click the **Add** button.
- Rewarded ad
- Interstitial ad
- Switch the ad's status toggle to **Active**.
**Note**: Ad placements are inactive by default and must be switched to **Active** to be used.
- Obtain the **Placement ID **of the ad you want to introduce as an incentive ad.
## Rewarded ad setup for mini games
**Note**: This setup flow is for rewarded ads, which is a required capability for mini games.
To set up an incentived ad that grants users in-game rewards after they watch it, follow these steps:
First, obtain the Placement ID of the rewarded ad you want to use in your mini game. Make sure the status of the ad is switched to **Active**.
Next, to introduce the ad into your game's code, do the following:
- Call the In-App Ads API from the Mini Games SDK to create an ad instance. This instance provides methods for displaying and managing the ad.
```
const rewardedVideoAd = TTMinis.game.createRewardedVideoAd({
  adUnitId: 'xxx';
});
```
- Display the ad in the corresponding scene of the game and distribute rewards upon completion.
- Call `show` to display the ad. After the ad is displayed, if the video retrieval or playback fails, the ad will automatically close.
- `onError` is used to monitor errors during the playback of an ad video. If an error occurs when the ad component fetches ad materials or in other situations, the error event will be triggered.
- `onClose` is used to monitor the closing of an ad video. When a user taps the close button on a video ad, or the ad automatically closes due to a playback error, the close event will be triggered.
- Each instance of an incentive ad `rewardedVideoAd` can only be shown once. After displaying, the instance is released, and you will need to recreate the ad instance.
```
const rewardedVideoAd = TTMinis.game.createRewardedVideoAd({
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
[See the full list of JavaScript APIs for IAA](https://developers.tiktok.com/doc/mini-games-sdk-iaa).
## Interstitial ad setup for mini games
[To set up interstitial ads for your mini games, follow the same process as above, using the interstitial ad JavaScript APIs instead](https://developers.tiktok.com/doc/mini-games-sdk-iaa#).
Was this document helpful?