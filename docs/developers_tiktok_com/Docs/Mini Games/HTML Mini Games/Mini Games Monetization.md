Docs
# Mini Games Monetization
Follow the mini game login authorization process and business verification on the Developer Portal before accessing monetization features like In-App Ads (IAA) and In-App Purchases (IAP).
## Access monetization for mini games
On your mini game's app page, go to the **Monetize** section. Complete business verification when prompted, if you haven't done so already.
## Complete third-party authorization for mini games
[To configure monetization for mini games, you will need to have first completed third-party authorization for mini games, as outlined in the development stage guide](https://developers.tiktok.com/doc/minis-development-stage#integrate-with-tiktok-login). Refer to the following code:
```
TTMinis.game.login({
  success: (result) => {
  // The user has logged in and authorized the application
  // You can get the code and send it to the backend in exchange for open_id, access_token, and more
   let code = result.code;
  },
  fail: (error) => {
  // Other errors or deauthorization code is null
  },
  complete: () => {
   //  Both success and failure will trigger this callback
  }
});
```
The authorization process follows these basic steps.
- Retrieve the code and send it back to the third party server
- Server calls `https://open.tiktokapis.com/v2/oauth/token/` to obtain the `open_id` and `access_token`
- Server calls `https://open.tiktokapis.com/v2/user/info/` to get the logged-in user's information
## In-App Ads (IAA)
[First call `TTMinis.game.createRewardedVideoAd](https://developers.tiktok.com/doc/mini-games-sdk-iaa#createRewardedVideoAd(opts))` to create a rewarded video ad, which will return an instance of the rewarded video ad. The ad instance provides `onError` ,`onClose` and `show` methods.
- `onError` is used to monitor errors during the playback of an ad video. If an error occurs when the ad component fetches ad materials or in other situations, the error event will be triggered.
- `onClose` is used to monitor the closing of an ad video. When a user taps the close button on a video ad, or the ad automatically closes due to a playback error, the close event will be triggered.
- `show` is used to display incentive video ads.
Notes:
- Call `show` for ad display. After the ad is displayed, if the video retrieval or playback fails, the ad will automatically close.
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
})

rewardedVideoAd.show().then(() => {
  console.log('ad displayed');
}).catch(() => {
  console.log('ad failed to display');
})
```
[See the full list of JavaScript APIs for IAA](https://developers.tiktok.com/doc/mini-games-sdk-iaa).
## In-App Purchase (IAP)
Note: This flow requires users to complete the login process.
In Sandbox, the IAP process currently allows payment operations to be carried out even if there is no balance. If the account has a Beans balance, it will not be deducted either. After the payment is successful, you will normally receive a webhook and a TikTok in-app message.
If you need to display the number of Beans consumed in the game, you can use the following image as the icon for Beans.
### Create an order
The server creates a payment order through OPENAPI and obtains the order's `trade_order_id`:
[_POST_ `https://open.tiktokapis.com/v2/minis/trade_order/create/](https://developers.tiktok.com/doc/minis-payment-apis#create-an-order)`
```
curl --location 'https://open.tiktokapis.com/v2/minis/trade_order/create' \
--header 'Authorization: Bearer {access token}' \
--header 'Content-Type: application/json' \
--data '{
    "token_type": "BEANS",
    "token_amount": 100,
    "order_info": {
        "order_id": "external_order_id_003",
        "product_name": "Wake up dad! wedding time",
        "product_id": "external_product_id",
        "order_url": "/profile/order_history/external_product_id",
        "quantity": 1,
        "quantity_unit": "episode",
        "iamge_url": "https//your.domain/pics/wake_up_dad.jpg"
    }
}'

response:
{
    "data": {
        "trade_order_id": "xxxx"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
[Call the Mini Games SDK payment endpoint](https://developers.tiktok.com/doc/mini-games-sdk-payment#pay(opts)) to complete the payment operation:
```
TTMinis.game.pay({
  trade_order_id: "{your_trade_order_id}",
  success: () => {
  // do something when succeeded
  },
  fail: (error) => {
  // do something when failed
  },
  complete: () => {
  // do something when completed
  }
})
```
### Webhook integration
Provide a webhook URL to TikTok, and after the order is successfully paid, the result will be sent through a webhook postback.
[If you need to verify the source of webhooks, refer to the webhook verification documentation](https://developers.tiktok.com/doc/webhooks-verification).
**Example payload**

| minis.trade_order.redeem.success | The order payment has been successfully completed |
| --- | --- |
| minis.trade_order.redeem.refund_traceback | The user initiated a refund in the store, resulting in the order amount being partially recovered. The refund_amount value is the amount that was recovered. |

**Example payload**
```
{
    "client_key": "your_client_key",
    "event": "minis.trade_order.redeem.success",
    "create_time": 1615338610,
    "user_openid": "",
    "content": "{\"trade_order_id\":\"TOID667700996\",\"order_id\":\"order_id_as_in_your_system\"}"
}

{
  "client_key": "your_client_key",
  "event": "minis.trade_order.redeem.refund_traceback",
  "create_time": 1744946518,
  "user_openid": "",
  "content": "{\"trade_order_id\":\"TOID2157c5ba03\",\"order_id\":\"order_id_as_in_your_system\",\"is_sandbox\":true,\"refund_amount\":80}"
}
```
[[For more information, refer to the Mini Games SDK payment functions](https://developers.tiktok.com/doc/mini-games-sdk-payment) or Open Payment APIs from TikTok Minis](https://developers.tiktok.com/doc/minis-payment-apis).
Was this document helpful?