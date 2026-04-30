Docs
# Silent login
Silent login is a capability that allows your game platform to securely retrieve the user's open ID and access token, thereby logging the user in without the need for explicit authorization.
In the explicit authorization scheme, the game must pass a `scope` when calling `TTMinis.game.login`. This requires an authorization screen to appear within the game during the initial call. The game can only obtain the code after the user manually confirms authorization; this code is then used by the backend to exchange for an `open_id` and `access_token` to retrieve user information.
Using silent login, the transition away from the "pop-up on first launch" and "mandatory authorization to get a code" approach avoids unnecessary authorization prompts. Improving the initial login experience and game-open rates with silent login this helps reduce user churn.
**Note**: Integration with this capability is mandatory for mini games.
## Technical integration
[If your platform only needs to obtain the user's OpenID without requiring additional user information, use silent login. This is the recommended default for basic functionalities like In-App Purchases (IAP), as it doesn't interrupt the user. For more details, see the login and authorization JavaScript APIs](https://developers.tiktok.com/doc/mini-games-sdk-login).
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
Was this document helpful?