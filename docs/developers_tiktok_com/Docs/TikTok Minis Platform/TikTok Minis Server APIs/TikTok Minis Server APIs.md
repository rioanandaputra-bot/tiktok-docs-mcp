Docs
**TikTok Minis Server APIs **(open.tiktokapis.com) is a secure, backend-only suite of endpoints that manages identity and commerce for TikTok Minis (mini apps and mini games) via OAuth v2 and scope-based permissions. It provides OAuth token retrieval, scope-gated user info retrieval, order creation and management, and pricing. Your backend stores and manages tokens and trade orders.
TikTok Minis Server API serves both mini apps (such as mini dramas) and mini games use cases.

| **Category** | **Function** | **Description** |
| --- | --- | --- |
| [OAuth for TikTok Minis](https://developers.tiktok.com/doc/minis-oauth) | Fetch an access token using an authorization code | Exchanges the temporary `code`(received from the client-side `.login()`or `.authorize()`calls) for the permanent user tokens |
| Refresh an access token using a refresh token | Obtain a new `access_token`when the current one expires (after 24 hours), without requiring the user to log in again |
| Revoke access | Disconnects your application from a user's TikTok account |
| [TikTok User Data API](https://developers.tiktok.com/doc/minis-user-data) | Get user info | Retrieve basic profile information for an authorized TikTok user |
| [Payment APIs](https://developers.tiktok.com/doc/minis-payment-apis) | Get recharge tiers | Query the details and pricing of available BEANS recharge packages (tiers) offered by TikTok |
| Create an order | Register an upcoming payment order in your system with the TikTok server to generate a secure `trade_order_id`for the transaction |
| Query an order | Track the status of a specific payment order created on the TikTok server |
| Check redeem amounts | Verify if a list of requested Beans amounts (prices) for their products complies with TikTok's current pricing policy and restrictions |

Was this document helpful?