Docs
# In-App Purchases
Generate revenue with in-app purchases (IAP) which allow users to buy digital goods and virtual currency within your application. There are two IAP methods that you can set up:
- **TikTok Beans**: Virtual currency used for one-time, non-subscription purchases
- **Subscriptions**: Recurring charges for packages within your mini drama
Your frontend re-engages the payment panel through a TikTok Minis SDK JavaScript API. The real payment closed loop additionally includes the following:
- Silent login to obtain user identity
- Your backend creates a pre-payment order
- Your frontend initiates payment based on the trade order ID
- TikTok's server asynchronously calls back the payment result
- Your backend completes signature verification, idempotence, and delivery
## Prerequisites
Before setting up in-app ads for your mini game or mini drama, you must have completed the following:
- [Enabled in-app purchases](https://developers.tiktok.com/doc/enable-monetization-features) for your mini game or mini drama
- [Configured silent login](https://developers.tiktok.com/doc/tiktok-minis-silent-login) for your mini drama
- [Configured the payment webhook callback](https://developers.tiktok.com/doc/set-up-development-configuration#) address on your app page
Make sure you also meet the following technical preconditions:
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
- The project root directory contains `minis.config.json`
- Your backend already has the following capabilities:
- Complete silent login to replace token
- Create a pre-payment order via `open_id` and `access_token`
- Receive and verify the payment success webhook
- Perform idempotent shipment based on the order
## Applicable scenarios
You should integrate rewarded ads in the following scenarios:
- Unlock a story chapter
- Purchase virtual currency, items, and gift packs
- Purchase any digital rights that require a Beans deduction
## Backend requirements
Your  backend must implement these capabilities at minimum:
### Create a prepayment order
- Use `open_id` and `access_token`, create `trade_order_id`
- Do not trust the frontend price, always follow the backend product configuration
### Persistent order mapping
We recommend to saving the following information together:
- `order_id`
- `trade_order_id`
- `open_id`
- Product information
- Amount information
- Current payment status
### Receive webhooks
After the payment is successful, your backend needs to process the TikTok callback and perform the final shipment based on the callback content.
### Polling query interface
To enable the frontend to perceive the final shipping status, we recommend that your backend provide an order query interface for the front end to perform polling.
## Best practices
- First complete silent login, then proceed with payment
- Product prices shall be subject to backend configuration only
- Your frontend re-engages payment, while your backend confirms payment and ships the product
- [Always perform webhook signature verification](https://developers.tiktok.com/doc/webhooks-verification) and idempotence control
- Your frontend uses polling to query results instead of directly treating the payment callback as the arrival signal
## Virtual currency and pricing tiers
### TikTok Beans
Beans are in-app virtual credits that can be used to unlock or access content within your mini app. Beans can be converted into any virtual currency that's exclusively used within your mini app.
If you need to display the number of Beans consumed in the game, you can use the following image as the icon for Beans.
### Pricing tiers
[TikTok Beans exist in fixed pricing tiers. Refer to this pricing tiers chart](https://developers.tiktok.com/doc/tiktok-beans-pricing-tiers) for more information on the packages available.
## IAP setup for TikTok Beans
This flow allows users to make purchases within your mini game using Beans, the virtual currency of TikTok. This requires users to complete the login process first.
[**Note**: Silent login](https://developers.tiktok.com/doc/silent-login) is required for in-game payment operations.
### Step 1: Create an order
First, create an order by calling TikTok's Payment API. When making a request, it is necessary to include:
- `Authorization: Bearer {access_token}`
- `Content-Type: application/json`
`POST`_ _`https://open.tiktokapis.com/v2/minis/trade_order/create/`
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
        "image_url": "https//your.domain/pics/wake_up_dad.jpg"
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
### Step 2: Your backend returns the trade order ID
Your backend must return the `trade_order_id` value to the frontend, and store the associated mapping of the following fields in your own database:
- `trade_order_id`
- Your internal business `order_id`
- `open_id`
### Step 3: Call the TikTok Minis SDK payment endpoint
[[Your frontend should call the TikTok Minis](https://developers.tiktok.com/doc/minis-sdk-payment#)SDK payment endpoint](https://developers.tiktok.com/doc/minis-sdk-payment#) with the `trade_order_id` to initiate the payment process:
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
### Step 4: Receive webhook event for payment completion
After the order is successfully paid, the result will be sent through a webhook postback asynchronously pushed by the TikTok server. Typical events include the following:

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
### Step 5: Your backend completes signature verification, idempotence, and delivery
After receiving the webhook, your backend must execute signature verification, idempotence, and delivery:
- Verify Signature
- Check if the order has been processed
- Issue virtual rights and interests to users based on `open_id`.
- Update local order status
**Warning**: It is strictly prohibited to rely solely on frontend callbacks as the final basis for shipping.
### Step 6: Frontend polls the payment result
After the payment panel is closed, the frontend is recommended to poll your backend order status every 1 to 2 seconds until it is confirmed that the backend has completed processing.
If a timeout occurs, the user can be prompted:
- Order processing
- Please check your balance/items later
- Provide customer service entry
[[For more information, refer to the TikTok Minis SDK IAP APIs](https://developers.tiktok.com/doc/minis-sdk-payment) or Payment APIs from TikTok Minis](https://developers.tiktok.com/doc/minis-payment-apis).
## IAP setup for subscriptions
Configuring subscriptions for your mini drama requires you to use methods from both TikTok Minis SDK and TikTok Minis Server API. You can complete two methods:
- Create a new subscription
- Renew an existing subscription
### Create a new subscription
To create a new subscription, you must first query whether or not the user has a subscription. Subsequently, your platform will display a subscription tier list and then create a subscription order according to the package the user chooses. Optionally, you can provide coupons to first-time subscribers.
Note: Each user may have no more than one active subscription within your app.
#### Step 1: Query user's subscription status
Call `https://open.tiktokapis.com/v2/minis/subscription/get_active_list/` to retrieve the user's subscription status.
- If the return value is empty, then the user has no valid subscription. Proceed to step two.
- If the return value is not empty, this indicates that the user has a subscription.
If a user has a subscription, their status may be `active`, `cancel`, or `onhold`. Two key fields that determine the subscription's state:
- `is_subscription_rights_valid`: Whether the user currently has active subscription benefits.
- `is_renewal_normal`: Whether auto-renewal is active and functioning normally.

| **Status** | **Has benefits?** | **Auto-renewing?** | **Allowed actions** | **Description** |
| --- | --- | --- | --- | --- |
| **Active** | Yes ✅ | Yes ✅ | Change | The user is actively subscribed and paying. If needed, you can offer them options to upgrade to a longer billing period. |
| **Cancel** | Yes ✅ | No ❌ | Reactivate | The user canceled, but their paid time hasn't run out yet. They keep their benefits until the expiration date. During this time, they can only reactivate their subscription. |
| **OnHold** | No ❌ | No ❌ | None | The user's automatic payment failed. This status lasts 1-2 months. During this time, they must update their payment info in the Apple or Google Store. They cannot create a new subscription while on hold. |

When a subscription payment fails, TikTok sends a `minis.subscription.onhold` webhook. This `onhold` status lasts 1-2 months.
During this time, the following rules apply:
- User action required: Users cannot create a new subscription. Use a toast notification to remind them to resolve their current subscription (either renew or cancel) in the Apple or Google Store.
- Active benefits: An `onhold` status does not mean the user's benefits have expired, because auto-renewals are attempted one day before expiration. To verify if benefits are still active, check the expiration date or the `is_subscription_rights_valid` field.
- Resolution webhooks: Once the status is resolved, TikTok will send `minis.subscription.renew` (if successfully renewed) or `minis.subscription.expire` (if the subscription becomes entirely inactive).
#### Step 2: Show surface coupon
To offer introductory discounts to first-time subscribers, use `showSurfaceCoupon` to display the promotion to the user before they view your products.
#### Step 3: Show tier list
Display your product page with the available subscription tier list on your frontend. Your promotion from the surface coupon will be displayed as a banner at the top of the screen.
Let the user choose their target tier then subsequently create the subscription order.
Note: When the user leaves your product page, ensure you close the promotional banner by calling `hideRibbon`.
#### Step 4: Create subscription order
To create a subscription for a user:
- Your server calls the subscription creation API to generate a `trade_order_id`.
- Your client calls `TTMinis.createSubscription` with the `trade_order_id` to open the payment screen.
- After the user completes payment, TikTok sends a `minis.subscription.create` webhook to your server to confirm activation.
### Reactivate subscription
Note: A subscription can be reactivated ONLY when `is_renew_normal=false`.
#### Step 1: Query user's subscription status
Call `https://open.tiktokapis.com/v2/minis/subscription/get_active_list/` to retrieve the user's subscription status.
If a user has a subscription, their status may be `active`, `cancel`, or `onhold`. Two key fields that determine the subscription's state:
- `is_subscription_rights_valid`: Whether the user currently has active subscription benefits.
- `is_renewal_normal`: Whether auto-renewal is active and functioning normally. Subscriptions can only be reactivated if this value is false.

| **Status** | **Has benefits?** | **Auto-renewing?** | **Allowed actions** | **Description** |
| --- | --- | --- | --- | --- |
| **Active** | Yes ✅ | Yes ✅ | Change | The user is actively subscribed and paying. If needed, you can offer them options to upgrade to a longer billing period. |
| **Cancel** | Yes ✅ | No ❌ | Reactivate | The user canceled, but their paid time hasn't run out yet. They keep their benefits until the expiration date. During this time, they can only reactivate their subscription. |
| **OnHold** | No ❌ | No ❌ | None | The user's automatic payment failed. This status lasts 1-2 months. During this time, they must update their payment info in the Apple or Google Store. They cannot create a new subscription while on hold. |

When a subscription payment fails, TikTok sends a `minis.subscription.onhold` webhook. This `onhold` status lasts 1-2 months.
During this time, the following rules apply:
- User action required: Users cannot create a new subscription. Use a toast notification to remind them to resolve their current subscription (either renew or cancel) in the Apple or Google Store.
- Active benefits: An `onhold` status does not mean the user's benefits have expired, because auto-renewals are attempted one day before expiration. To verify if benefits are still active, check the expiration date or the `is_subscription_rights_valid` field.
- Resolution webhooks: Once the status is resolved, TikTok will send `minis.subscription.renew` (if successfully renewed) or `minis.subscription.expire` (if the subscription becomes entirely inactive).
#### Step 2: Allow user to reactivate subscription
A user can reactivate their subscription only if they don't already have an active subscription.
#### Step 3: Reactivate subscription
To create a subscription for a user:
- Your server calls the subscription reactivation API to generate a `trade_order_id`.
- Your client calls `TTMinis.reactivateSubscription` with the `trade_order_id` to open the payment screen.
- After the user completes payment, TikTok sends a `minis.subscription.reactivate` webhook to your server to confirm activation.
### Test subscriptions with sandbox
Before going live, test your subscription integration using the provided sandbox tier IDs. The following concepts apply when testing integrations with sandbox tier IDs:
- No real payments: Sandbox subscriptions will not trigger the payment panel. We assure you that you will receive notifications and webhooks just like in the production environment
- Automatic renewals: Subscriptions renew every 5 minutes (12 times total). After 12 renewals or cancellation, an expiry event will be triggered.
- Same webhooks: You'll receive the same notifications as production.
- Blocked reactivations: You may not reactivate within 2 minutes of renewal. In production, this period is typically one day.
- In the sandbox, these actions can be executed: `create`, `change`, `cancel`, `reactivate`, `onhold`, `onhold recover`.
#### Sandbox tier IDs
When calling subscription APIs, use the following tier IDs in your request body parameters. This will automatically trigger sandbox mode:

| Tier ID | Description |
| --- | --- |
| `sandbox_499_1M` | $4.99 per month |
| `sandbox_1347_3M` | $13.47 per quarter |
| `sandbox_699_1M` | $6.99 per month |
| `sandbox_1887_3M` | $18.87 per quarter |

## Debugging recommendations
After configuring IAPs, we recommend conducting joint debugging in the following order:
- First, ensure that the silent login link is available
- Confirm that the backend can create `trade_order_id`
- The front end successfully launched `TTMinis.pay()`
- Confirm that the backend has received the webhook
- Confirm that the backend shipment was successful
- Confirm that the frontend polling status update was successful
If you need to speed up joint debugging, you can enable payment Mock and identify `is_sandbox` in the backend.
## Frequently Asked Questions
**Must explicit authorization be performed first before accessing payment?**
No, it's not necessary. The core of the payment process relies on user identity, which is obtained through silent login:
- `open_id`
- `access_token`
Users are not required to authorize their avatar and nickname first.
**Frontend callback succeeded. Can we ship the product immediately?**
No, it cannot. The only reliable basis should be:
- The developer backend receives a payment success webhook
- Complete signature verification and idempotence check
**Can the same **`trade_order_id` ** be paid repeatedly?**
No, it cannot. If the payment for this order fails or the user cancels, a new ` trade_order_id ` should be recreated when initiating payment again.
**How to prevent duplicate shipments**
The developer backend must be based on:
- `trade_order_id`or business ` order_id `
Perform an idempotence check.
**Why does the payment panel display "An error occurred, please try again later"? **
Common causes include:
- Payment is not supported in the current region
- Store account location does not match
- IP/device environment does not meet the requirements
- The platform's payment capability has not yet been truly activated
Was this document helpful?