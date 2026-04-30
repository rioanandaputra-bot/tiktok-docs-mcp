Docs
# Silent Login
Silent login is a capability that allows your app platform to securely retrieve the user's open ID and access token, thereby logging the user in without the need for explicit authorization.
In the explicit authorization scheme, the app must pass a `scope` when calling `TTMinis.login`. This requires an authorization screen to appear within the app during the initial call. The app can only obtain the code after the user manually confirms authorization; this code is then used by the backend to exchange for an `open_id` and `access_token` to retrieve user information.
Using silent login, the transition away from the "pop-up on first launch" and "mandatory authorization to get a code" approach avoids unnecessary authorization prompts. Improving the initial login experience and app-open rates with silent login this helps reduce user churn.
**Note**: Integration with this capability is mandatory for mini dramas.
## Prerequsities
Before using silent login, make sure you meet these preconditions:
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
- Your backend can securely store:
- `client_key`
- `client_secret`
- Your backend already has the ability to call the TikTok OAuth token API
## Applicable scenarios
It is recommended that developers integrate silent login in the following scenarios:
- Establish identity when the user first enters the application
- When it is necessary to bind viewing progress, assets, and subscription status to the user
- Unified precondition steps for subsequent capabilities such as payment, subscription, and user profile authorization
Silent login itself does not directly pop up the data authorization box, and users usually complete it without awareness.
## Best practices
- The front end is only responsible for retrieving `code`, and should not directly replace tokens on the frontend
- `client_secret` can only be stored in your backend
- Your backend uses `open_id` as the user primary key
- Unified management of your backend`access_token`/`refresh_token`
- Even if only `open_id` is currently needed, it is still recommended to fully go through the code-to-token process once
## Technical integration process
[If your platform only needs to obtain the user's OpenID without requiring additional user information, use silent login. This is the recommended default for basic functionalities like In-App Purchases (IAP), as it doesn't interrupt the user. For more details, see the login and authorization JavaScript APIs](https://developers.tiktok.com/doc/mini-games-sdk-login).
### Step 1: Frontend Initializes SDK
The front-end page first executes:
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
If initialization is not completed, silent login should not enter the formal access process.
### Step 2: Frontend calls login endpoint
Frontend calls:
```
window.TTMinis.login(
```
- After the call is successful, the TikTok container will return a one-time, short-lived `AuthorizationCode`
Note:
- `code` is not the final login state
- It is just a temporary ticket for the developer backend to exchange for official credentials.
- this `code` has a very short validity period. It is recommended to handle it as valid for 5 minutes and usable only once.
### Step 3: Your frontend immediately sends code to your backend
After receiving the `code`, your frontend should immediately send it to your backend via HTTPS.
Not recommended:
- Cache in the front end`code`
- Resubmit the same `code`
- Submit after the user has completed other operations
### Step 4: Your backend exchanges for a token with the TikTok server
Backend call:
- `POST https://open.tiktokapis.com/v2/oauth/token/`
- `grant_type=authorization_code`
Request headers:
- `Content-Type: application/x-www-form-urlencoded`
Request parameters:

| **Key** | **Description** | **Required** |
| --- | --- | --- |
| `client_key` | Currently applied client key | Yes |
| `client_secret` | Currently applied client secret | Yes |
| `code` | Frontend `TTMinis.login() `Returned authorization code | Yes |
| `grant_type` | Fixed value`authorization_code` | Yes |

After success, it will return:
- `open_id`
- `access_token`
- `refresh_token`
- `expires_in`
- `refresh_expires_in`
- `scope`
- `token_type`
### Step 5: Your backend stores identity and token
It is recommended that your backend use `open_id` as the unique primary key for TikTok users under the current application and persistently save it:
- `open_id`
- `access_token`
- `refresh_token`
- `access_token_expire_time`
- `refresh_token_expire_time`
- `scope`
- `token_type`
If your current business only requires user identity and does not need to immediately access protected resources, then at least the `open_id` should be persistently saved.
### Step 6: Your backend usesaccess token and open ID in subsequent business operations
If subsequent business operations require calling protected interfaces such as user information, payment, and subscription, it is recommended that they be uniformly executed by your backend.
The typical pattern is:
- The front end initiates a business request
- The backend uses the saved `access_token` and `open_id` to call the TikTok server
- The backend returns the results to the frontend
### Step 7: The developer backend refreshes the token before it expires
`access_token` is not long-term valid. According to the current information, it should be designed with the following constraints:
- `access_token` Typical validity period: 24 hours
- `refresh_token` Typical validity period: 365 days
It is recommended that the developer backend perform silent refresh 10 to 30 minutes before expiration.
The refresh interface remains:
- `POST https://open.tiktokapis.com/v2/oauth/token/`
- `grant_type=refresh_token`
After the refresh is successful, the backend should immediately overwrite and update:
- New `access_token`
- New `refresh_token`
- New expiration time
If the refresh fails and returns ` invalid_grant `, it usually indicates that the ` refresh_token ` has expired, and the front-end login should be re-triggered at this time.
## Process summary
From the developer's perspective, silent login can be understood as the following complete link:
- Frontend `TTMinis.init({ clientKey })`
- Frontend `TTMinis.login()`
- Frontend obtains `AuthorizationCode`
- Frontend sends `code` to the backend
- Backend calls`/v2/oauth/token/` to exchange for `open_id`, `access_token`, `refresh_token`
- Backend persistent storage
- The backend refreshes the token just before it expires
## Frequently Asked Questions
**client_key**** does not match ****client_secret**
Phenomenon:
- When the backend changes the token, it returns `invalid_client` or authentication fails.
Troubleshooting suggestions:
- Make sure you are using the same TikTok `client_key `and `client_secret`
- Do not mix configurations from other platforms
**Terms of Service and Privacy Policy are not configured**
Phenomenon:
- Frontend call `TTMinis.login()` directly fails
- Similar ` errorCode: 102102  may occur`
Troubleshooting suggestions:
- Complete the links to the Terms of Service and Privacy Policy in the developer backend
- If the official link is not yet ready, you can fill in a temporary placeholder link first
**code**** has expired or been reused**
Phenomenon:
- When the backend exchanges tokens, it returns ` invalid_grant `
Troubleshooting suggestions:
- `code` Use immediately after acquisition
- Do not resubmit the same `code`
- Avoid caching for too long in the front end
**Token interface request format error**
Phenomenon:
- Backend returns `invalid_request`
Troubleshooting Suggestions:
- Check` Content-Type ` to see if it is ` application/x-www-form-urlencoded `
- Check if `grant_type` is `authorization_code`
**access_token**** has expired**
Phenomenon:
- Subsequent protected interface calls return 401
Troubleshooting Suggestions:
- Backend implementation ` refresh_token ` refresh mechanism
- Proactively refresh before it is about to expire, rather than waiting until it has completely expired before handling it
## TikTok Minis toolchain explanation
- The current JSSDK requires `login` to be called after `init`
- Currently`minis dev` will perform a strong verification before startup to check if there is a valid `TTMinis.init({ clientKey })`
- This article strictly follows the silent login process of mini apps, only replacing the front-end JSAPI with Minis' `TTMinis.login()`
Was this document helpful?