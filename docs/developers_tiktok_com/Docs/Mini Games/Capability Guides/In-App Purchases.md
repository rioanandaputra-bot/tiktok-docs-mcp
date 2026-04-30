Docs
# In-App Purchases
Generate revenue with in-app purchases (IAP) which allow users to buy digital goods and virtual currency within your application.
## Prerequisites
Before setting up in-app ads for your mini game, you must have completed the following:
- [Enabled in-app purchases](https://developers.tiktok.com/doc/enable-monetization-features) for your mini game
## Virtual currency and pricing tiers
### TikTok Beans
Beans are in-app virtual credits that can be used to unlock or access content within your mini app. Beans can be converted into any virtual currency that's exclusively used within your mini app.
If you need to display the number of Beans consumed in the game, you can use the following image as the icon for Beans.
### Pricing tiers
[TikTok Beans exist in fixed pricing tiers. Refer to this pricing tiers chart](https://developers.tiktok.com/doc/tiktok-beans-pricing-tiers) for more information on the packages available.
## IAP setup for mini games
This flow allows users to make purchases within your mini game using Beans, the virtual currency of TikTok. This requires users to complete the login process first.
[**Note**: Silent login](https://developers.tiktok.com/doc/silent-login) is required for in-game payment operations.
### Step 1: Create an order
First, create an order by calling TikTok's Payment API:
_POST _`https://open.tiktokapis.com/v2/minis/trade_order/create/`
```
POST https://open.tiktokapis.com/v2/minis/trade_order/create/
curl --location 'https://open.tiktokapis.com/v2/minis/trade_order/create' \
--header 'Authorization: Bearer {access token}' \
--header 'Content-Type: application/json' \
--data '{
    "token_type": "BEANS", // Required
    "token_amount": 100, // Required
    "order_info": {
        "order_id": "external_order_id_003", // Required
        "product_name": "Wake up dad! wedding time", // Required; displayed on the user's order list page

        "order_url": "/profile/order_history/external_product_id",
        "quantity": 1,
        "quantity_unit": "relive", // Pass the unit of the item being sold as appropriate; e.g., "episode" is the unit for a series
        "iamge_url": "https//your.domain/pics/wake_up_dad.jpg"
    }
}'
```
The server creates a payment order through the open API and obtains the order's `trade_order_id`:
```
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
### Step 2: Call the Mini Games SDK payment endpoint
[Call the Mini Games SDK payment endpoint](https://developers.tiktok.com/doc/mini-games-sdk-payment#pay(opts)) to initiate the payment process:
```
TTMinis.game.pay({
  trade_order_id: "{your_trade_order_id}",
  success: () => {
  // Do something if succeeded
  },
  fail: (error) => {
  // Do something if failed
  },
  complete: () => {
  // Do something if completed
  }
})
```
### Step 3: Register a callback URL for payment completion
Register a webhook URL in the Developer Portal so that after the order is successfully paid, the result will be sent through a webhook postback.
[If you need to verify the source of webhooks, refer to the webhook verification documentation](https://developers.tiktok.com/doc/webhooks-verification).

| **Event** | **Description** |
| --- | --- |
| minis.trade_order.redeem.success | Order payment successful |
| minis.trade_order.redeem.refund_success | Order refund successful (currently unavailable) |
| minis.trade_order.redeem.refund_fail | Order refund failed (currently unavailable) |
| minis.trade_order.redeem.refund_traceback | The order amount partially recovered due to the user initiating a refund in the store, with the value of refund_amount being the recovered amount |

```
{
    "client_key": "your_client_key",
    "event": "minis.trade_order.redeem.success",
    "create_time": 1615338610,
    "user_openid": "",
    "content": "{\"trade_order_id\":\"TOID667700996\",\"order_id\":\"order_id_as_in_your_system\",\"is_sandbox\":true}"
}

{
  "client_key": "your_client_key",
  "event": "minis.trade_order.redeem.refund_traceback",
  "create_time": 1744946518,
  "user_openid": "",
  "content": "{\"trade_order_id\":\"TOID2157c5ba03\",\"order_id\":\"order_id_as_in_your_system\",\"is_sandbox\":true,\"refund_amount\":80}"
}
```
[[For more information, refer to the Mini Games SDK IAP APIs](https://developers.tiktok.com/doc/mini-games-sdk-payment) or Payment APIs from TikTok Minis](https://developers.tiktok.com/doc/minis-payment-apis).
Was this document helpful?