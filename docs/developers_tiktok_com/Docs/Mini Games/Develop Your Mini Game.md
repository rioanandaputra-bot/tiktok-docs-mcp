Docs
# Develop Your Mini Game
Develop a mini game that integrates with capabilities from TikTok.
**Info**: TikTok supports two runtime types for mini games:
- **HTML**: Web-based build that runs in a webview using HTML/CSS/JavaScript. Fast to ship and broadly portable, but bounded by browser performance and system memory limits.
- **Native**: Compiled mini‑game that runs on TikTok’s native runtime. Optimized performance with smoother gameplay, fast loading, and unified access to system capabilities.
This guide explains how to develop a mini game using **Native **runtime. Overall, mini games that rely on native runtime have better performance, controllability, and user experience. Development broadly happens in two stages:
- Develop your mini game locally using a third-party game engine
- Export mini game directory
- Integrate with TikTok APIs for mandatory client-side capabilities
## Develop your mini game locally
Use a third-party game engine and integrated development environment (IDE) to build your mini game. After you've finished developing your mini game, export your project's code package.
## Export mini game directory
After you've completed development, export your mini game directory from the game engine. When selecting export options in the game engine, choose a compatible platform game type for export, and then continue with subsequent debugging.
## Integrate APIs for TikTok capabilities
TikTok provides a number of open capabilities through two complementary API bundles:
- **Mini Games SDK (TTMinis.game)**: A client-side JavaScript SDK that runs inside the TikTok app. It provides in-app capabilities like login and authorization, payments, UI triggers, rewarded ads, lifecycle hooks, networking, and capability detection.
- **TikTok Minis Server APIs (****open.tiktokapis.com****)**: A secure, backend-only suite of endpoints that manages identity and commerce for mini games via OAuth v2 and scope-based permissions. It provides OAuth token retrieval, scope-gated user info retrieval, order creation and management, and pricing. Your backend stores and manages tokens and trade orders.
The open capabilities offered through these APIs allow your mini game to integrate seamlessly with the TikTok in-app experience and access TikTok's client-side functionalities.
**Important**: You are required to integrate several of these capabilities for your mini game to run correctly on TikTok. Such capabilities are listed below.

| **Function** | **APIs** | **Description** | **Required** |
| --- | --- | --- | --- |
| [Silent login](https://developers.tiktok.com/doc/silent-login) | `TTMinis.game.login` `https://open.tiktokapis.com/v2/oauth/token/` | Obtain the users' OpenID and access token without explicit authorization | Yes |
| [Explicit authorization](#share-W2rGdm9SNoy1zyxp6riu8iZLsym) | `TTMinis.game.authorize` `https://open.tiktokapis.com/v2/oauth/token/` `https://open.tiktokapis.com/v2/user/info/` | Obtain additional user data like username and avatar, requires user consent through an authorization screen | No |
| [In-app ads](https://developers.tiktok.com/doc/in-app-ads) (rewarded ads) | `TTMinis.game.createRewardedVideoAd` | Insert rewarded video ads into your mini game; IAA must be enabled to configure | Yes |
| [In-app purchases](https://developers.tiktok.com/doc/in-app-purchases) | `https://open.tiktokapis.com/v2/minis/trade_order/create/` `TTMinis.game.pay` | Allow purchases to be made within your mini game; IAP must be enabled to configure | No |
| [Home screen shortcut](https://developers.tiktok.com/doc/home-screen-shortcut) | `TTMinis.game.addShortcut` `TTMinis.game.getShortcutMissionReward` | Grant the user a reward when they add a shortcut to their home screen | Yes |
| [Revisit from profile](https://developers.tiktok.com/doc/revisit-from-profile) | `TTMinis.game.startEntranceMission` `TTMinis.game.getEntranceMissionReward` | Guide the user out of the game and to the relevant section of the TikTok app that promotes repeat visits and grant a reward in return | Yes |

### Login and authorization methods
You must choose and configure a login method for your mini game. Different levels of data require different methods for user login:
- **No data needed:** No login required.
- **Basic data:** To retrieve basic data like OpenID and access token, use **Silent login**, which logs the user in without an authorization screen.
- **Profile data:** To retrieve profile data like username and avatar in addition to basic data, use **Explicit authorization, **which opens an authorization screen and requires the user to confirm.
**Note**: If you need to obtain more sensitive user data like email address or mobile phone number, you must reach out to your TikTok operations representative to undergo an extra compliance process.
To choose and and configure a login method, do the following:
- Choose a login method depending on your data requirements.

| **Scenario** | **JavaScript API ** | **Backend API** | **User interaction** | **Data acquired** |
| --- | --- | --- | --- | --- |
| **No user data needed** | Do nothing | None | None | None |
| **Only OpenID and access token needed (for IAP)** | `TTMinis.game.login()` | `https://open.tiktokapis.com/v2/oauth/token/` | Silent login: the user has no immediate perception, and no authorization screen appears. | OpenID, access token |
| **Additional user info needed (such as username, avatar)** | `TTMinis.game.authorize()` | `https://open.tiktokapis.com/v2/oauth/token/` `h``ttps://``open.tiktokapis.com/v2/user/info/` | Explicit authorization: the user sees an authorization screen and must consent to authorization. | OpenID, access token, profile data |

- Configure your login method by calling the relevant JavaScript and backend APIs. The setup methods are listed:
- Silent login
- Explicit authorization
- Take note that access tokens are temporary: they can expire, or the user can manually revoke your game's authorization. Take the following precautionary steps for error handling and fallback.
- **Error handling**: Your server should be designed to handle 401 (Unauthorized) errors from TikTok's open APIs. When a 401 is received, the server should prompt the frontend to re-initiate the login (`.login`) or authorization (`.authorize`) process.
- **Fallback**: If the explicit `.authorize` call fails (perhaps the user denied the pop-up), the frontend should immediately use the `.login` method as a fallback to ensure you at least obtain the basic OpenID (silent login) and avoid losing the player entirely.
#### Silent login
If your platform only needs to obtain the user's OpenID without requiring additional user information, use silent login. This is the recommended default for basic functionalities like In-App Purchases (IAP), as it doesn't interrupt the user.
- Call the JavaScript API: Let the frontend call `TTMinis.game.login` to trigger the silent OAuth process in the background.
- Success callback: If successful, the game receives an encrypted code, which is a temporary authorization code used for the next step.
- Backend step (exchange code): The frontend must pass the obtained code to your server, so the server is able to exchange `open_id` and `access_token` by calling `https://open.tiktokapis.com/v2/oauth/token/`_._
Example code:
```
TTMinis.game.login({
  success: (result) => {
    // The user has logged in and authorized the application
    // You can get the code and send it to the backend to exchange for open_id, access_token, and more
    let code = result.code;
  },
  fail: (error) => {
    // Other errors or the user did not authorize; code will be null
  },
  complete: () => {
    // This callback is triggered regardless of success or failure
  }
});
```
#### Explicit authorization
If your platform needs to obtain additional user information such as username and avatar, use explicit authorization. This method necessitates user consent via an authorization screen.
- Call the JavaScript API: Let the frontend call `TTMinis.game.authorize` , specifying the desired level of user data via the scope parameter.
- Define scope: The scope `user.info``.basic` tells the TikTok platform exactly what information you are requesting (in this case, basic user profile info like username and avatar). This triggers the user-facing pop-up.
**Warning: **Do not call this immediately when the user enters the game. Users may reject the request, and you will lose the chance to get their OpenID. Call this function only when the feature requiring the data (for example, a personalized leaderboard) is needed.
- Success callback: If successful, the game receives an encrypted code, which is a temporary authorization code used for the next step.
- Backend step (exchange code): The frontend must pass the obtained code to your server, so the server is able to exchange `open_id` and `access_token` by calling `https://open.tiktokapis.com/v2/oauth/token/`_._
- Backend step (get user data): After acquiring the access token, the server makes a second call to `https://open.tiktokapis.com/v2/user/info/` to fetch the actual profile data (username, avatar) that the user explicitly authorized.
Example code:
```
TTMinis.game.authorize({
  // If you require other user permissions, please refer to https://developers.tiktok.com/doc/tiktok-api-scopes
  scope: "user.info.basic",
  success: (result) => {
    // The user has logged in and authorized the application
    // You can get the code, and send it to the backend to exchange for open_id, access_token
    let code = result.code;
  },
  fail: (error) => {
    // Other errors or unauthorized (user did not grant permission); code will be null
  },
  complete: () => {
    // This callback is triggered regardless of success or failure
  }
});
```
[Learn more about TikTok's login and authorization JavaScript APIs](https://developers.tiktok.com/doc/mini-games-sdk-login).
### Monetization features
If you plan on monetizing your mini game, you first enable monetization features in the Developer Portal to gain access to TikTok's monetization capabilities.
- [Review the monetization overview and process](https://developers.tiktok.com/doc/monetization-overview) for mini games.
- [Enable your desired monetization features](https://developers.tiktok.com/doc/enable-monetization-features) in the Developer Portal. This step can only be performed by an organizational admin.
- Configure monetization features for your mini game:
- In-app ads
- In-app purchases
#### In-app ads (IAA)
To configure in-app ads for your mini game, IAA must be enabled for your mini game. Rewarded ads specifically are required for mini games.
[Learn more about how to configure IAA for your mini game](https://developers.tiktok.com/doc/in-app-ads).
#### In-app purchases (IAA)
To configure in-app purchases for your mini game, IAP must be enabled for your mini game.
[Learn more about how to configure IAP for your mini game](https://developers.tiktok.com/doc/in-app-purchases).
### User engagement
Incentivize engagement by granting rewards to users after they add a home screen shortcut or complete an entrance mission.
**Note**: These APIs require TikTok app version ≥ 41.0.0. Always gate with `canIUse` before calling, and ensure the user is logged in (silent login is fine).
#### Home screen shortcut
This flow allows users to receive a reward after adding a shortcut to their mini game on their home screen:
- Before calling the API, check if the function is available in the current TikTok version with `canIUse`.
```
if (TTMinis.game.canIUse("addShortcut")) {
    // Proceed to call the API
}
```
- Execute the `addShortcut` function. This will typically trigger a system-level prompt asking the user for permission to add the icon.
```
TTMinis.game.addShortcut({
  success: () => {
    // Log or handle the success (User confirmed and shortcut was added)
    console.log("Shortcut successfully added to home screen");
  },
  fail: (error) => {
    // Log or handle the failure (User declined or an error occurred)
    console.log("Failed to add shortcut", error);
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
- After the shortcut has been added, the game can check and award the user.
- Check reward status: Call the `getShortcutMissionReward` API. This API checks the user's status for the "add-to-home-screen" mission.
- Handle success: The success callback should check the returned boolean value, `canReceiveReward`, to determine the next action.
```
TTMinis.game.getShortcutMissionReward({
  success: ({ canReceiveReward }) => {
    if (canReceiveReward) {
      // If true, grant the reward (coins, items, etc.) in your game logic
      console.log("User is eligible for the shortcut mission reward");
    } else {
      console.log("User is not currently eligible for the reward");
    }
  },
  fail: (error) => {
    // Handle failure to check status
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
#### Revisit from profile
This process encourages users to revisit the game by guiding them to the TikTok profile sidebar, where the mini game is featured:
- Before calling the API, check if the function is available in the current TikTok version with `canIUse`.
```
if (TTMinis.game.canIUse("startEntranceMission")) {
    // Proceed to call the API
}
```
- Execute the `startEntranceMission` function. This navigates the user to the TikTok profile sidebar, effectively completing the follow-up education task.
```
TTMinis.game.startEntranceMission({
  success: () => {
    // Log or handle the successful navigation to the sidebar
    console.log("Successfully jumped to the sidebar of the home page");
  },
  fail: () => {
    // Handle failure to jump
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
- After the user has completed the entrance/sidebar mission (usually by visiting the sidebar via Step 1), the game can award them.
- Check reward status: Call the `getEntranceMissionReward` API. This checks the user's eligibility for the reward associated with the sidebar revisit mission.
- Handle success: Check the `canReceiveReward` boolean in the success callback.
```
TTMinis.game.getEntranceMissionReward({
  success: ({ canReceiveReward }) => {
    if (canReceiveReward) {
      // If true, grant the reward (coins, items, etc.) in your game logic
      console.log("User is eligible for the entrance mission reward");
    } else {
      console.log("User is not currently eligible for the reward");
    }
  },
  fail: () => {
    // Handle failure to check status
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
## Next step: Debug your mini game
[Learn how to debug your native runtime mini game](https://developers.tiktok.com/doc/debug-your-mini-game).
Was this document helpful?