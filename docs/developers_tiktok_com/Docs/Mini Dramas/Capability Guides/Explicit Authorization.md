Docs
# Explicit Authorization
Explicit authorization is a targeted process utilizing the `TTMinis.authorize` interface that prompts a user with a pop-up dialog to grant specific permissions (defined by a scope), enabling your app to access additional details beyond a basic silent login.
You should only trigger this flow when a specific business scenario strictly requires extra information, such as accessing a user's profile data or binding a phone number.
## Prerequsities
Before using explicit authorization, make sure you meet these preconditions:
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
- You have already configured silent login, and your backend is ready to save a user's `open_id`
- Your backend already has the following capabilities:
- Save`access_token`
- Call the TikTok user profile API
- Persistently store user avatars and nicknames
## Applicable scenarios
It is recommended that developers integrate and display authorization in the following scenarios:
- When a user clicks on "Profile", the avatar and nickname need to be displayed
- User profile needs to be displayed when the user enters the "Leaderboard"
- When a user enters the "Edit Profile" page, they need to retrieve basic information
Not recommended:
- The authorization box pops up immediately as soon as the page is opened
- Forcefully interrupt the experience when the user has not yet clearly defined the scenario requirements
## Best practices
Consult the best practices for implementing explicit authorization:
- **Avoid immediate pop-ups:** Do not launch an authorization dialog as soon as your Mini starts, as this significantly increases user churn and friction.
- **Prioritize silent login:** Establish basic user identity first using silent login (`TTMinis.login`) to seamlessly retrieve the `open_id`.
- **Request contextually:** Only ask for explicit permissions (`TTMinis.authorize`) when a specific business scenario strictly requires extra information, such as accessing a profile or binding a phone number.
- **Use user-initiated triggers:** Initiate the authorization flow via a direct user action, like clicking a button, so the request feels natural and expected.
- **Secure token management:** Always manage and store the resulting `access_token` and `refresh_token` securely on your backend server. Never expose them to the frontend.
- **Avoid local caching:** Do not cache retrieved user data locally on the frontend to ensure the information you are using and displaying remains accurate and up-to-date.
## Technical integration workflow
We don't recommend calling TTMinis.authorize to pop up an authorization box as soon as Minis starts, as it may easily lead to users refusing and affect conversion. It is suggested to first complete the basic login (get open_id), and then request users to authorize more permissions (such as obtaining user information, phone numbers, etc.) when necessary, and trigger authorization through buttons to avoid users' resentment.
If your platform needs to obtain additional user information such as username and avatar, use explicit authorization. This method necessitates user consent via an authorization screen.
### Step 1: Ensure silent login has already been configured
It is recommended to first establish user identity through `TTMinis.login()` and have the developer's backend exchange for it:
- `open_id`
- `access_token`
- `refresh_token`
This way, when the user clicks to authorize later, the backend already has the precondition to continue pulling data.
### Step 2: Trigger when authorization is required
When the user actively enters scenarios such as Profile or Leaderboard, let the frontend call `TTMinis.game.authorize` , specifying the desired level of user data via the scope parameter.
- Define scope: The scope `user.info``.basic` tells the TikTok platform exactly what information you are requesting (in this case, basic user profile info like username and avatar). This triggers the user-facing pop-up.
**Warning: **Do not call this immediately when the user enters the game. Users may reject the request, and you will lose the chance to get their OpenID. Call this function only when the feature requiring the data (for example, a personalized leaderboard) is needed.
### Step 3: User confirms authorization
After the user sees the authorization pop-up window within the TikTok container, they may allow or reject it:
- Allow: The frontend obtains the authorization result and authorization code
- Reject: The frontend receives a failure result or an error object
This step is explicit authorization, different from silent login, where users have a clear perception.
### Step 4: Your frontend sends the authorization result to backend
Success callback: If successful, the game receives an encrypted code, which is a temporary authorization code used for the next step. Your frontend will send this content to your backend:
- `authResponse.code`
- `authResponse.grantedScopes` (if returned)
### Step 5: Your backend retrieves user profiles
Your backend uses the already held `access_token` to call the TikTok user profile API:
- `GET ``https://open.tiktokapis.com/v2/user/info/`
- `Authorization: Bearer {access_token}`
The backend can obtain the following based on this:
- User nickname
- User avatar address
### Step 6: Return data to the frontend
Recommendations for your backend:
- Use `open_id` as the user primary key
- Persist basic information such as avatar and nickname to the database
- Return the current data to the frontend for display
Example code:
```
TTMinis.authorize({
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
## Backend instructions to obtain user profile
Under the current TikTok system, the frontend does not provide an interface like `getUserInfo` that directly returns the nickname and avatar.
The developer backend should obtain user profiles through open API:
- `GET https://open.tiktokapis.com/v2/user/info/`
- `Authorization: Bearer {access_token}`
Recommendations for the developer backend:
- Only pull data after the user has explicitly authorized it
- Store in the database with `open_id` as the primary key
- Implement local caching to avoid re-fetching data every time the page is accessed
## Debugging suggestions
We recommend conducting joint debugging in the following order:
- First, ensure that the silent login link is available
- Confirmation page completed `TTMinis.init({ clientKey })`
- Do not immediately pop up the authorization dialog during the page initialization phase
- Trigger <a i=1> `TTMinis.authorize()`  when the user clicks the explicit entry point `</a>`
- Backend verifies whether it can successfully obtain and save the avatar and nickname
## Frequently Asked Questions
**Why is there no front-end ****getUserInfo**** interface**
This is one of the core differences in TikTok's authorization system. TikTok does not provide an interface for direct front-end reading of nicknames and avatars; user profiles must be obtained by the developer's backend through the Open API.
**What if the user refuses to authorize?**
You should avoid blocking the main process. Authorization can be downgraded, for example:
- Show default avatar
- Display the default nickname, such as `TikTok Player`
**Why is it not recommended to pop up the authorization box as soon as the page is entered?**
It will disrupt the user experience. The more recommended mode is:
- First, perform silent login to obtain identity
- In scenarios where data is clearly needed, trigger the display of authorization as needed
**Since silent login has already been performed, why is authorization still required?**
Silent login is mainly used to obtain:
- `open_id`
- Login state-related tokens
If developers still need information such as nicknames and avatars, they still have to go through the explicit authorization process separately.
## TikTok Minis toolchain explanation
- In the current TikTok Minis SDK, for `authorize` the default scope is `user.info``.basic`
- Currently `minis dev` will strongly verify whether SDK initialization and `clientKey` consistency are completed in HTML before startup
- The process of this article strictly refers to the mini game authorize access solution, only replacing the front end JSAPI with Minis's `TTMinis.authorize()`
Was this document helpful?