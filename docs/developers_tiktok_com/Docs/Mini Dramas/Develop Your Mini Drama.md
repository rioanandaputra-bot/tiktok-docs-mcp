Docs
# Develop Your Mini Drama
During this stage, you will locally develop your mini drama app and integrate with necessary APIs. This guide explains how to develop a mini drama based on **H5 **runtime.
## What are TikTok Minis?
Unlike traditional mini-program runtime environments, TikTok Minis are lightweight web applications that run within the TikTok app's WebView. This architecture combines standard web development practices with TikTok-native client capabilities, offering developers a familiar workflow while accessing platform features. Key characteristics include:
- Minis are built as standard web projects with core files like `index.html`, frontend framework code, and compiled build artifacts
- TikTok client-side capabilities are exposed via the global `window.TTMinis` interface, rather than being implemented directly in your web code
- Local development relies on three interconnected layers: your local business page, the Playground debug page, and the TikTok mobile app
- Before uploading to the Developer Platform, you first build your web project independently, then run the `minis build` command to validate and package your artifacts according to platform requirements
**Note**: If you have experience developing mini apps or mini programs for other platforms, avoid mapping traditional mini program concepts directly to TikTok Minis. The most accurate way to conceptualize this framework is **Web App + Client-side JSAPI + CLI toolchain**.
## Complete app setup on Developer Platform
### Set up basic information
Ensure all required project fields (including app information, Privacy Policy URL, Terms of Service URL) are populated in the Developer Portal. Empty or incomplete configuration will cause login and authorization errors. Use temporary placeholder links if your production resources are not yet available.
[Learn more about configuring your app's basic information](https://developers.tiktok.com/doc/tiktok-minis-basic-information-specifications).
### Configure request domains
Add all domains that your mini app will communicate with to the allowlist in the Developer Portal. Cross-origin requests from non-whitelisted domains will be blocked by the TikTok client.
[Learn more about configuring trusted domains](https://developers.tiktok.com/doc/set-up-development-configuration).
### Enable monetization capabilities
TikTok Minis support two primary monetization models: In-App Ads (IAAs) and In-App Purchases (IAPs). Ensure you've completed monetization enablement, signed all necessary contracts, and received approval from TikTok before integrating monetization features into your app project.
- [Review the monetization overview and process](https://developers.tiktok.com/doc/monetization-overview) for mini apps.
- [Enable your desired monetization features](https://developers.tiktok.com/doc/enable-monetization-features) in the Developer Portal. This step can only be performed by an organizational admin.
- After approval, configure monetization features for your mini app on the Developer Portal.
- IAAs: Create and configure your ad units to get unique identifiers for rewarded ads, interstitial ads, and other supported formats.
- [IAPs: Configure your payment callback URL for webhooks](https://developers.tiktok.com/doc/set-up-development-configuration#set_up_webhooks) to receive transaction updates from TikTok's servers.
## Install developer tools
**Note**: Before setting up the CLI, ensure your environment meets the following requirements:
- An existing H5 project that represents your mini app (the CLI integrates Minis framework capabilities into your standard web application).
- Node.js and npm installed on your machine.
### Install TikTok Minis command line interface tool
After completing development of your H5 mini app, install the command-line interface (CLI) tool to generate config files and debug.
```
npm install tiktok-minis-cli -g --registry=https://registry.npmjs.org/
```
Verify your installation by checking the CLI version:
```
minis -v
# Expected output: 0.0.4
```
### Install TikTok Client for testing
[For local testing with Android devices, you must use a test client version of TikTok. Reach out to your operations representative at TikTok or submit a support ticket](https://developers.tiktok.com/portal/support) for more information.
For local testing on iOS devices, you can test your TikTok Minis by uploading the packaged artifact to the Developer Platform and scanning the generated QR code to preview on your device.
## Develop your mini app
Since TikTok Minis run in a standard WebView, you can develop most UI and non-client-dependent functionality using standard browser-based development workflows. Features that require TikTok client access (including login, authorization, ads, payments, and subscriptions) must be tested using the local debugging workflow outlined below.
### Initialize TikTok Minis SDK
First, you must initialize the TikTok Minis SDK to access all of TikTok's client-side JavaScript APIs.
To use TikTok Minis SDK, include a piece of JavaScript code in your HTML to asynchronously load the SDK into your pages. This will not block other elements from loading on your page. TikTok Minis SDK does not require standalone files or downloads.
Add the TikTok Minis SDK to your `index.html` file and initialize it with your project's unique client key:
```
<!-- index.html -->
<head>
  <script src="https://connect.tiktok-minis.com/drama/sdk.js"></script>
  <script>
    TTMinis.init({
      clientKey: "your_client_key_here",
    });
  </script>
</head>
```
### Integrate with core capabilities
TikTok provides a number of open capabilities through two complementary API bundles:
- **TikTok Minis SDK (TTMinis)**: A client-side JavaScript SDK that runs inside the TikTok app. It provides in-app capabilities like login and authorization, payments, UI triggers, rewarded ads, lifecycle hooks, networking, and capability detection.
- **TikTok Minis Server APIs (****open.tiktokapis.com****)**: A secure, backend-only suite of endpoints that manages identity and commerce for mini apps via OAuth v2 and scope-based permissions. It provides OAuth token retrieval, scope-gated user info retrieval, order creation and management, and pricing. Your backend stores and manages tokens and trade orders.
The open capabilities offered through these APIs allow your mini app to integrate seamlessly with the TikTok in-app experience and access TikTok's client-side functionalities.
**Important**: You are required to integrate several of these capabilities for your mini app to run correctly on TikTok. Such capabilities are listed below.

| **Function** | **APIs** | **Description** | **Required** |
| --- | --- | --- | --- |
| Silent Login | `TTMinis.login` `https://open.tiktokapis.com/v2/oauth/token/` | Obtain the users' OpenID and access token without explicit authorization | Yes |
| Explicit Authorization | `TTMinis.authorize` `https://open.tiktokapis.com/v2/oauth/token/` `https://open.tiktokapis.com/v2/user/info/` | Obtain additional user data like username and avatar, requires user consent through an authorization screen | No |
| In-App Ads: Rewarded ads | `TTMinis.createRewardedVideoAd` | Insert rewarded video ads into your mini app; IAA must be enabled to configure | Yes |
| In-App Ads: Interstitial ads | `TTMinis.createInterstitialAd` | Insert interstitial ads into your mini app; IAA must be enabled to configure | Yes |
| In-App Purchases: Beans (one-time payment) | `https://open.tiktokapis.com/v2/minis/trade_order/create/` `TTMinis.pay` | Allow one-time purchases with Beans to be made within your mini app; IAP must be enabled to configure | Yes |
| In-App Purchases: Subscriptions | `https://open.tiktokapis.com/v2/minis/subscription/create/` `TTMinis.createSubscription` | Allow subscriptions to be purchased within your mini app; IAP must be enabled to configure | Yes |
| Navigation bar | `TTMinis.setNavigationBarColor` `TTMinis.getMenuButtonBoundingClientRect` | Set up and customize a navigation bar in your mini game | Yes |

#### Silent Login
The silent login flow allows you to authenticate users without additional user interaction, enabling seamless account creation and session management.
- [Silent Login implementation guide](https://developers.tiktok.com/doc/tiktok-minis-silent-login)
- [Silent Login JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-login#)
- [Server API OAuth reference](https://developers.tiktok.com/doc/minis-oauth)
#### Explicit Authorization
For permissions that require explicit user approval, use the `TTMinis.authorize()` method to launch the TikTok permission request flow.
- [Explicit Authorization implementation guide](https://developers.tiktok.com/doc/tiktok-minis-explicit-authorization)
- [[Explicit Authorization](https://developers.tiktok.com/doc/minis-sdk-login#) JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-login#)
- [OAuth Server API reference](https://developers.tiktok.com/doc/minis-oauth)
#### In-App Ads (IAAs)
To configure in-app ads for your mini app, IAA must be enabled for your mini app. There are two types of IAAs: rewarded ads and interstitial ads.
- [In-App Ads configuration guide](https://developers.tiktok.com/doc/tiktok-minis-in-app-ads)
- [[In-App Ads](https://developers.tiktok.com/doc/minis-sdk-in-app-ads) JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-in-app-ads)
#### In-App Purchases (IAPs)
To configure in-app purchases for your mini app, IAP must be enabled for your mini app. There are two types of IAPs: one-time purchases with TikTok Beans and subscriptions.
- [In-App Purchases configuration guide](https://developers.tiktok.com/doc/tiktok-minis-in-app-purchases)
- [[In-App Purchases](https://developers.tiktok.com/doc/minis-sdk-payment) JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-payment)
- [Subscriptions JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-subscriptions)
- [Payment Server API reference](https://developers.tiktok.com/doc/minis-payment-apis)
- [Subscriptions Server API reference](https://developers.tiktok.com/doc/minis-subscription-apis)
#### Navigation Bar
Configure a navigation bar in your mini app that adapts to the user's device.
- [Navigation Bar configuration guide](https://developers.tiktok.com/doc/tiktok-minis-navigation-bar)
- [[UI](https://developers.tiktok.com/doc/minis-sdk-ui)JavaScript API reference](https://developers.tiktok.com/doc/minis-sdk-ui)
Was this document helpful?