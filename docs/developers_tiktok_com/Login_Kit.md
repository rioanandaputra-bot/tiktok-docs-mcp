# Login Kit

> Consolidated from 7 source files.



---
## SOURCE: Login Kit/Android.md

Docs
# Login Kit for Android
[This guide explains how to integrate with Login Kit for Android using Kotlin. Once authenticated users authorize your app, you can access their basic TikTok profile data, including their display name and avatar. Additional data access may require approval for additional scopes. Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
## Prerequisites
[Before proceeding, make sure you complete all of the steps in the Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart).
[Obtain the `client_key` and `client_secret` located in the **Credentials** section of your app page on the TikTok for Developers website](https://developers.tiktok.com/). Navigate to the **Products** section of your app page and click **Add products**. Then add **Login Kit**.
## Android integration
### Create an authorization request
- Create an instance of `AuthApi`.
- Create an `AuthRequest` instance and set the following required parameters:
- `clientKey = your_client_key`: Use the client key that you obtain on the TikTok for Developers website.
- `scope = ``user.info``.basic`: If you are approved for additional scopes, include them using a comma-separated list.
- `redirectUri = your_redirectUri`: Redirect URI determines how TikTok sends back the response to your app. The value must match one of the authorized redirect URIs that you provide for your Android Login Kit and follow an `https` scheme.
- `codeVerifier = your_codeverifier`: Generate a code verifier with `PKCEUtils`.
- Call the `authorize()` method on your instance of `AuthApi` .
```
// STEP 1: Create an instance of AuthApi
val authApi = AuthApi(
    activity = [your_activity]
)

// STEP 2: Create an AuthRequest and set parameters
val request = AuthRequest(
    clientKey = clientKey,
    scope = "user.info.basic",
    redirectUri = redirectUri, 
    codeVerifier = codeVerifier
)

// STEP 3: Invoke the authorize method
authApi.authorize(
    request = request,
    authMethod = AuthMethod.TikTokApp / AuthMethod.ChromeTab
);
```
After successful authorization, the user will be brought back to your app via the activity associated with `redirectUri`.
### Receive callbacks
```
// the actvity which will receive the authorization response from TikTok
<activity>
    ...
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        // Note that VIEW action, and DEFAULT & BROWSAbLE categories are necessary.
        <data android:scheme="your_redirect_uri_scheme" />
        <data android:host="your_redirect_uri_host"/>
    </intent-filter>
</activity>
```
Parse the AuthResponse from intent with `authApi.getAuthResponseFromIntent`. Refer to `MainActivity` in the `demo-auth` package as an example.
```

authApi.getAuthResponseFromIntent(intent, [your_redirect_uri])?.let { 
    val authCode = it.authCode // The auth code will be used to obtain access token
    val grantedPermissions = it.grantedPermissions // Granted scopes
            
    // Please refer to the Handling Errors for more detail.
    val authError = it.authError
    val authErrorDescription = it.authErrorDescription
    ...
}
```
### Obtain an access token
[Upload the `code` returned in the callback and your `code_verifier` to your server-side and obtain a user access token. See User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management) for more information.
### Handling errors
[See Error Handling](https://developers.tiktok.com/doc/oauth-error-handling) for more information.
Was this document helpful?


---
## SOURCE: Login Kit/Desktop.md

Docs
# Login Kit for Desktop
This guide details how to enable authentication from your desktop app to TikTok. After successfully completing authentication with TikTok, developers can obtain an `access_token` for the TikTok user.
## Prerequisites
### Register your app
[[Register your app following these steps](https://developers.tiktok.com/doc/getting-started-create-an-app/). Then obtain a **Client key** and **Client secret** from the TikTok for Developers website](https://developers.tiktok.com/) by clicking your profile icon in the navigation bar, clicking **Manage apps**, and then selecting the relevant app.
### Configure Redirect URI
Redirect URI is required for desktop apps. After the user completes authorization with Login Kit on the desktop, they will be redirected to the URI that you provide. This redirect URI must be registered in the Login Kit product configuration for your app.
The following are restrictions for registering redirect URIs.
- A maximum of 10 URIs is supported.
- The length of each URI must be fewer than 512 characters.
- URIs must be absolute and begin with `https` or `http`.
- URIs must be static. Parameters or fragment CANNOT be appended to the URI.
- Only `localhost` or loopback IP `127.0.0.1` are allowed host names in URI.
- URIs must have a port number, and wildcard port number (*) is supported. Wildcard config is recommended if your redirect URI uses a random port number.
- The following are some examples of valid redirect URIs:
- `http://localhost:3455/callback/`
- `http://127.0.0.1:*/callback/`
- `https://127.0.0.1:3455/callback/`
## Integration Guide
### Implement the front-end code
Get started by connecting your front-end login button to the server endpoint. The following is an example in HTML:
```
<a href='{SERVER_ENDPOINT_OAUTH}'>Continue with TikTok</a>
```
### Implement the server code to handle authorization grant flow
The server code must be responsible for the following:
- Ensuring that the client secret and refresh token are stored securely.
- Ensuring that the security for each user is protected by preventing request forgery attacks.
- Handling the refresh flow before access token expiry.
- Managing the access token request flow for each user.
#### Redirect request to TikTok's authorization server
##### Create an anti-forgery state token
You must prevent request forgery attacks to protect the security of your users. The first step before making the redirect request to TikTok's authorization server is to create a unique session token to maintain the state between the request and callback.
You will later match this unique session token with the authentication response to verify that the user is making the request and is not a malicious attacker.
One of the simple approaches to a state token is a randomly generated alphanumeric string constructed using a random-number generator, like the following example.
```
let array = new Uint8Array(30); 
const csrfState = window.crypto.getRandomValues(array);
```
##### Generate a code verifier and code challenge
[TikTok requires the Proof Key for Code Exchange](https://tools.ietf.org/html/rfc7636) (PKCE) protocol for desktop apps to make the authorization flow more secure. You are required to generate a code verifier and code challenge pair for desktop authorization. Please note the following:
- You should generate a new code verifier every time you initialize an authorization request.
- You must use hex encoding of SHA256 to generate the code challenge from the code verifier.
Here's how to generate a code verifier and code challenge:
- **code_verifier**
Generate a high-entropy cryptographic random string using the unreserved characters [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~" , with a minimum length of 43 characters and a maximum length of 128 characters.
```
function generateRandomString(length) {
  var result = '';
  var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~';
  var charactersLength = characters.length;
  for (var i = 0; i < length; i++) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}
```
- **code_challenge**
Create the code challenge by hashing the code verifier using hex encoding of SHA256. Since we only support S256 as `code_challenge_method`, use `code_challenge = SHA256(code_verifier)`.
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.min.js"></script>
// CryptoJS required
code_challenge = CryptoJS.SHA256(code_verifier).toString(CryptoJS.enc.Hex);
```
##### Initial redirect to TikTok's authorization page
To make the initial redirect request to TikTok's authorization server, the following query parameters below must be added to the Authorization Page URL using the `application/x-www-form-urlencoded` format.
[For example, you can use an online URL encoder](https://www.urlencoder.org/) to encode parameters. Select **UTF-8** as the destination character set.

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| `client_key` | string | The unique identification key provisioned to the partner |
| `scope` | string | A comma (,) separated string of authorization scope(s). These scope(s) are assigned to your application on the TikTok for Developers website. They handle what content your application can and cannot access. If a scope is toggleable, the user can deny access to one scope while granting access to others. |
| `redirect_uri` | string | The redirect URI that you requested for your application. It must match one of the redirect URIs you registered for the app. |
| `state` | string | The state is used to maintain the state of your request and callback. This value will be included when redirecting the user back to the client. Check if the state returned in the callback matches what you sent earlier to prevent cross-site request forgery. The state can also include customized parameters that you want TikTok service to return. |
| `response_type` | string | This value should always be set to `code` |
| `code_challenge` | string | SHA256 hash of `code_verifier`that will be used as a server-side challenge during authorization code exchange |
| `code_challenge_method` | string | This value should always be set to `S256` |

Redirect your users to the authorization page URL and supply the necessary query parameters. Note that the page can only be accessed through HTTPS.

| **Type** | **Description** |
| --- | --- |
| URL | `https://www.tiktok.com/v2/auth/authorize/` |
| Query parameters | `client_key=<client_key>&response_type=code&scope=<scope>&redirect_uri=<redirect_uri>&state=<state>&code_challenge=<code_challenge>&code_challenge_method=S256` |

The following is an example using Node, Express, and JavaScript:
```
const express = require('express');
const app = express();
const fetch = require('node-fetch');
const cookieParser = require('cookie-parser');
const cors = require('cors');

app.use(cookieParser());
app.use(cors());
app.listen(process.env.PORT || 5000).

const CLIENT_KEY = 'your_client_key' // this value can be found in app's developer portal
const SERVER_ENDPOINT_REDIRECT = 'your_redirect_uri' // redirect URI should be registered in developer portal
const CODE_VERIFIER = 'your_unique_code_verifier'
const CODE_CHALLENGE = 'SHA256_hash_of_code_verifier'

app.get('/oauth', (req, res) => {
    const csrfState = Math.random().toString(36).substring(2);
    res.cookie('csrfState', csrfState, { maxAge: 60000 });

    let url = 'https://www.tiktok.com/v2/auth/authorize/';

    // the following params need to be in `application/x-www-form-urlencoded` format.
    url += '?client_key={CLIENT_KEY}';
    url += '&scope=user.info.basic';
    url += '&response_type=code';
    url += '&redirect_uri={SERVER_ENDPOINT_REDIRECT}';
    url += '&state=' + csrfState;
    url += '&code_challenge={CODE_VERIFIER}';
    url += '&code_challenge_method=S256'

    res.redirect(url);
})
```
#### TikTok prompts a users to log in or sign up
The authorization page takes the user to the TikTok website if the user is not logged in. They are then prompted to log in or sign up for TikTok.
#### TikTok prompts a user for consent
After logging in or signing up, an authorization page asks the user for consent to allow your application to access your requested permissions.
#### Manage authorization response
If the user authorizes access, they will be redirected to `redirect_uri` with the following query parameters appended using `application/x-www-form-urlencoded` format:

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| `code` | string | Authorization code that is used in getting an access token |
| `scopes` | string | A comma-separated (,) string of authorization scope(s), which the user has granted |
| `state` | string | A unique, non-guessable string when making the initial authorization request. This value allows you to prevent CSRF attacks by confirming that the value coming from the response matches the one you sent. |
| `error` | string | If this field is set, the current user is not eligible for using third-party login or authorization. The partner is responsible for handling the error gracefully. |
| `error_description` | string | If this field is set, it will be a human-readable description about the error |

#### Manage access token
Using the `code` appended to your `redirect_uri`, you can obtain `access_token` for the user, which completes the flow for logging in with TikTok.
[For related endpoints, refer to this guide on managing user access tokens](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens/).
Was this document helpful?


---
## SOURCE: Login Kit/Login Kit.md

Docs
# Login Kit
[[[[[Integrating with our Login Kit enables users to quickly and securely sign into your app with their TikTok account. LoginKit is available on iOS](https://developers.tiktok.com/doc/login-kit-ios-quickstart), Android](https://developers.tiktok.com/doc/login-kit-android-quickstart-v2), Desktop](https://developers.tiktok.com/doc/login-kit-desktop/) and Web](https://developers.tiktok.com/doc/login-kit-web). Login Kit is based on OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749) for user authorization and API authentication.
After successfully completing authentication with TikTok, your application will be able to request access to basic user data such as display name and avatar. For requesting access to additional data from users, pre-approval will be required in your TikTok app on developers.tiktok.com.
[Once users have approved your access, you can view basic user data with our Display APIs. Learn more here](https://developers.tiktok.com/doc/display-api-get-started).
Was this document helpful?


---
## SOURCE: Login Kit/Manage User Access Tokens.md

Docs
# Manage User Access Tokens with OAuth v2
TikTok Login Kit manages the token life cycle, allowing you to integrate login and authentication flows directly in your application. A successful authorization flow grants you refreshable access tokens. Those tokens enable you to perform endpoint access with user permissions.
## Authorization scopes
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the rights to only agree to a subset of scopes you requested from them.
The following are some example scopes:
- **user.info****.basic** gives read-only access to a user's avatar and display name.
- **video.list** gives read-only access to a user's public TikTok videos.
[Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
## Token security
Tokens must be handled with caution. It is recommended that you store and manage all tokens on the server side.
- Access token is a user authorization token that can be used to directly access user information in the TikTok ecosystem.
- Refresh token is used to renew the access token.
## Endpoints for web
[If you have already registered a redirect URI for your web app and use `https://www.tiktok.com/v2/auth/authorize/` to authorize, please refer to the new generation user access token management API guide](https://developers.tiktok.com/doc/oauth-user-access-token-management).
[[If you are an existing client, have not registered a redirect URI for your web app and use `https://www.tiktok.com/auth/authorize/` to authorize, please refer to the legacy user access token management API guide](https://developers.tiktok.com/doc/legacy-user-access-guide). To register a redirect URI, go to the Manage apps](https://developers.tiktok.com/apps/) page of the TikTok for Developers website and migrate to the new endpoints as soon as possible.
## Endpoints for mobile
[[[**Preferred: **If you are using the new Android](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart) or iOS](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart) TikTok OpenSDK, please refer to the new user access token management guide](https://developers.tiktok.com/doc/oauth-user-access-token-management).
[[[**Legacy: **If you are using the old Android](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart) or iOS](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart) TikTok OpenSDK, please refer to the legacy user access token management guide](https://developers.tiktok.com/doc/legacy-user-access-guide).
## Endpoints for desktop
[You must register a redirect URI for your desktop app and use `https://www.tiktok.com/v2/auth/authorize/` to authorize. Please refer to the new generation user access token management API guide](https://developers.tiktok.com/doc/oauth-user-access-token-management) to manage the user access token.
Was this document helpful?


---
## SOURCE: Login Kit/QR Code Authorization.md

Docs
# Login Kit with QR Code
[If you are using our deprecated v1 endpoint for QR code authorizations, please migrate to our v2 endpoint immediately. Learn more](https://developers.tiktok.com/bulletin/migration-guidance-qr-code-authorization-v2).
## Overview
[This guide will explain how to integrate with the Login Kit to facilitate user authorization via QR code login. Once an authenticated user authorizes your app, you can access their basic TikTok profile data such as their display name and avatar. Additional data access may require approval for additional scopes. Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
## Prerequisites
[Obtain a client key and client secret by logging into the TikTok for Developers website](https://developers.tiktok.com/). Then go to the **Manage apps** page and select your app.
### Security advisory: Verifying integrity using client_ticket
The `client_ticket` mentioned throughout this guide enables you to verify the data integrity of the response. While your app may still function even if you don't validate the `client_ticket`, doing so introduces security risks. Therefore, it is highly recommended that you always verify that the `client_ticket` matches the one generated by you, and reject any response where this validation fails as it may have been compromised by a malicious attacker.
#### Generating a client_ticket
Your `client_ticket` can be any series of characters, letters, or symbols, as long as it is URL safe and the URL-encoded version is under 512 characters. The generation method is at your discretion as there are no complexity requirements. You may reuse the same `client_ticket`, but some randomness is recommended for security. You should persist the ticket for the entirety of the QR code process as it will be needed when checking the validity of the QR status.
## Integration
Your web app must implement the following functionality on the server side:
- Generate a QR code.
- Request a QR code URL (see the below sections for API guidance).
- Generate a `client_ticket`.
- Insert the client ticket into the QR code URL.
- Render the URL.
- Display it to the user.
- Repeatedly check the QR code status and refresh or disable it accordingly (see the below sections for API guidance).
- Parse the response for the provided authorization code once the QR code status is changed to `confirmed`.
- Request an access token and refresh token from TikTok using the authorization code and client key.
- Notify the user of authorization success or failure.
- Use the access token to fetch authorized user data, and use the refresh token to extend the access token's expiration time.
[For more information on access and refresh tokens, see Manage User Access Tokens](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens).
## Get QR Code
_POST_ `https://open.tiktokapis.com/v2/oauth/get_qrcode/`
### Description
Request a QR code from TikTok.
### Header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner | aw7nk86b7czitwc9 | true |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize | user.info.basic,video.list | true |
| state | string | The state is used to maintain the state of your request and callback. This value will be included when redirecting the user back to the client. Check if the state returned in the callback matches what you sent earlier to prevent cross-site request forgery. The state can also include customized parameters that you want TikTok service to return. | key%3Dabc%26key2%3Ddef | false |

### Example request
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/get_qrcode/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=aw7nk86b7czitwc9' \
--data-urlencode 'scope=user.info.basic,user.info.username' \
--data-urlencode 'state=key%3Dabc%26key2%3Ddef'
```
### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| scan_qrcode_url | string | QR code url which is returned when the call is successful | aweme://authorize?authType=100&client_key=abcd1234&client_ticket=tobefilled&... |
| token | string | Token used to check QR code status, returned when the call is successful | VJ5JCKGJGRSWNMFWHQH4W5NKY943Q97D |
| error | string | If this field is set, it means that the current user is not eligible for using third-party login or authorization. The partner is responsible for handling the error . | invalid_request |
| error_description | string | If this field is set, it will be a human-readable description about the error | The request parameters are malformed. |
| log_id | string | If this field is set, it will be a log ID for troubleshooting | 202206221854370101130062072500FFA2 |

A successful response will include the `scan_qrcode_url` and `token` fields. Once obtained, please perform the following steps:
- Extract the `scan_qrcode_url`.
- Generate a unique ticket using your preferred approach, such as an alphanumeric string such as `2ncv7awq`. Persist this ticket alongside your service.
- In the previously extracted `scan_qrcode_url`, replace the value of the `client_ticket` query parameter with your ticket. For example, `scan_qrcode_url=...&client_ticket=tobefilled&...` should be replaced by `scan_qrcode_url=...&client_ticket=your_ticket&...`.
- Use the modified `scan_qrcode_url` to generate a QR code.
- Display the QR code to your user.
### Example response
#### Success
```
{
    "scan_qrcode_url": "aweme://authorize?authType=100&client_key=abcd1234&client_ticket=tobefilled&...",
    "token": "VJ5JCKGJGRSWNMFWHQH4W5NKY943Q97D..."
}
```
#### Failure
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## Check QR code status
_POST_ `https://open.tiktokapis.com/v2/oauth/check_qrcode/`
### Description
Check the QR code status. Call with polling after the `get_qrcode` endpoint has been successfully called.
### Header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner | aw7nk86b7czitwc9 | true |
| client_secret | string | The unique identification secret provisioned to the partner | 123fnaoif12n3ij | true |
| token | string | Token obtained along with QR code | VJ5JCKGJGRSWNMFWHQH4W5NKY943Q97D | true |

### Example request
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/check_qrcode/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=aw7nk86b7czitwc9' \
--data-urlencode 'token=VJ5JCKGJGRSWNMFWHQH4W5NKY943Q97D' \
--data-urlencode 'client_secret=123fnaoif12n3ij'
```
### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| client_ticket | string | A string, which is generate in user's service. This is returned when the call is successful. | client_ticket="A23SDWEGsdasd" |
| status | string | QR code status | new | expired | scanned | confirmed |
| code | string | Authorization code, returned when the status is confirmed | https://callback.example.com?code=HOXbXtnAok4qojdOmsHjucm1V1KJrOjYuMnV |
| state | string | The "state" parameter which is sent in /v2/oauth/get_qrcode/. It is returned when the status is confirmed. | key%3D123 |
| error | string | If this field is set, it means that the current user is not eligible for using third-party login or authorization. The partner is responsible for handling the error gracefully. | invalid_request |
| error_description | string | If this field is set, it will be a human-readable description about the error | The request parameters are malformed. |
| log_id | string | If this field is set, it will be a log ID for trouble shooting | 202206221854370101130062072500FFA2 |

When the call succeeds, please perform the following steps:
- Validate the `client_ticket` to make sure it matches what you provided in your generated ticket for the request. If they do not match, ignore the response as its integrity may be compromised.
- Check that the status is `confirmed` and that the authorization code is appended in the `redirect_uri`.
- If the status is not `confirmed`, continue polling if the status is not `expired`. If it is `expired`, then re-invoke the `get_qrcode` API.
### Example response
#### Success
```
// A new generate QR code
{
    "client_ticket": "",
    "status": "new"
}
// A QR code scaned by the user
{
    "client_ticket": "your_ticket_string",
    "status": "scanned"
}
// A QR code confirmed by the user
{
    "client_ticket": "your_ticket_string",
    "redirect_uri": "https://example.com?code=example_code",
    "status": "confirmed"
}
// An expired QR code
{
    "client_ticket": "",
    "status": "expired"
}
// A QR Code after auth code returned
{
    "client_ticket": "your_ticket_string",
    "status": "utilised"
}
```
#### Failure
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
Was this document helpful?


---
## SOURCE: Login Kit/Web.md

Docs
# Login Kit for Web
This guide details how to enable authentication from your web app to TikTok. After successfully completing authentication with TikTok, developers can obtain an `access_token` for the TikTok user.
## Prerequisites
### Register your app
[[Register your app following these steps](https://developers.tiktok.com/doc/getting-started-create-an-app). Then obtain a client key and secret from the developer portal on https://developers.tiktok.com](https://developers.tiktok.com/) under **Manage apps**.
### Configure redirect URI
Redirect URI is required for web apps. After the user completes authorization with Login Kit on the web, they will be redirected to a URI provided by you. This redirect URI must be registered in the Login Kit product configuration for your app.
The following are restrictions for registering redirect URIs.
- A maximum of 10 URIs is supported.
- The length of each URI must be less than 512 characters.
- URIs must be absolute and begin with `https`. For example:
- Correct: `https://dev.example.com/auth/callback/`
- Incorrect: `dev.example.com/auth/callback/`
- URIs must be static. Parameters will be denied. For example:
- Correct: `https://dev.example.com/auth/callback/`
- Incorrect: `https://dev.example.com/auth/callback/?id=1`
- URIs cannot include a fragment, or hash character (#):
- Correct: `https://dev.example.com/auth/callback/`
- Incorrect: `https://dev.example.com/auth/callback/#100`
## Integration Guide
### Implement the front-end code
Get started by connecting your front-end login button to the server endpoint. The following is an example in HTML:
```
<a href='{SERVER_ENDPOINT_OAUTH}'>Continue with TikTok</a>
```
### Implement the server code to handle authorization grant flow
The server code must be responsible for the following:
- Ensuring that the client secret and refresh token are stored securely.
- Ensuring that the security for each user is protected by preventing request forgery attacks.
- Handling the refresh flow before access token expiry.
- Managing the access token request flow for each user.
#### Redirect request to TikTok's authorization server
##### Create an anti-forgery state token
You must prevent request forgery attacks to protect the security of your users. The first step before making the redirect request to TikTok's authorization server is to create a unique session token to maintain the state between the request and callback.
You will later match this unique session token with the authentication response to verify that the user is making the request and not a malicious attacker.
One of the simple approaches to a state token is a randomly generated alphanumeric string constructed using a random-number generator. For example:
```
let array = new Uint8Array(30); 
const csrfState = window.crypto.getRandomValues(array);
```
##### Initial redirect to TikTok's authorization page
To make the initial redirect request to TikTok's authorization server, the following query parameters below must be added to the Authorization Page URL using the `application/x-www-form-urlencoded` format.
[For example, you can use an online URL encoder](https://www.urlencoder.org/) to encode parameters. Select **UTF-8** as the destination character set.

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| `client_key` | String | The unique identification key provisioned to the partner. |
| `scope` | String | A comma (,) separated string of authorization scope(s). These scope(s) are assigned to your application on the TikTok for Developers website. They handle what content your application can and cannot access. If a scope is toggleable, the user can deny access to one scope while granting access to others. |
| `redirect_uri` | String | The redirect URI that you requested for your application. It must match one of the redirect URIs you registered for the app. |
| `state` | String | The state is used to maintain the state of your request and callback. This value will be included when redirecting the user back to the client. Check if the state returned in the callback matches what you sent earlier to prevent cross-site request forgery. The state can also include customized parameters that you want TikTok service to return. |
| `response_type` | String | This value should always be set to `code`. |
| `disable_auto_auth` | int | Controls whether the authorization page is automatically presented to users. When set to 0, skips the authorization page for valid sessions. When set to 1, always displays the authorization page. |

Redirect your users to the authorization page URL and supply the necessary query parameters. Note that the page can only be accessed through HTTPS.

| **Type** | **Description** |
| --- | --- |
| URL | `https://www.tiktok.com/v2/auth/authorize/` |
| Query parameters | `client_key=<client_key>&response_type=code&scope=<scope>&redirect_uri=<redirect_uri>&state=<state>` |

[Note: If you are an existing client and use `https://www.tiktok.com/auth/authorize/` as the authorization page URL, please register a redirect URI](https://developers.tiktok.com/apps/) for your app and migrate to the new URL mentioned above.
The following is an example using Node, Express, and JavaScript:
```
const express = require('express');
const app = express();
const fetch = require('node-fetch');
const cookieParser = require('cookie-parser');
const cors = require('cors');

app.use(cookieParser());
app.use(cors());
app.listen(process.env.PORT || 5000).

const CLIENT_KEY = 'your_client_key' // this value can be found in app's developer portal

app.get('/oauth', (req, res) => {
    const csrfState = Math.random().toString(36).substring(2);
    res.cookie('csrfState', csrfState, { maxAge: 60000 });

    let url = 'https://www.tiktok.com/v2/auth/authorize/';

    // the following params need to be in `application/x-www-form-urlencoded` format.
    url += '?client_key={CLIENT_KEY}';
    url += '&scope=user.info.basic';
    url += '&response_type=code';
    url += '&redirect_uri={SERVER_ENDPOINT_REDIRECT}';
    url += '&state=' + csrfState;

    res.redirect(url);
})
```
#### TikTok prompts a users to log in or sign up
The authorization page takes the user to the TikTok website if the user is not logged in. They are then prompted to log in or sign up for TikTok.
#### TikTok prompts a user for consent
After logging in or signing up, an authorization page asks the user for consent to allow your application to access your requested permissions.
#### Manage authorization response
If the user authorizes access, they will be redirected to `redirect_uri` with the following query parameters appended using `application/x-www-form-urlencoded` format:

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| `code` | String | Authorization code that is used in getting an access token. |
| `scopes` | String | A comma-separated (,) string of authorization scope(s), which the user has granted. |
| `state` | String | A unique, non-guessable string when making the initial authorization request. This value allows you to prevent CSRF attacks by confirming that the value coming from the response matches the one you sent. |
| `error` | String | If this field is set, it means that the current user is not eligible for using third-party login or authorization. The partner is responsible for handling the error gracefully. |
| `error_description` | String | If this field is set, it will be a human-readable description about the error. |

#### Manage access token
Using the `code` appended to your `redirect_uri`, you can obtain `access_token` for the user, which completes the flow for logging in with TikTok.
[See Manage User Access Tokens](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens) for related endpoints.
Was this document helpful?


---
## SOURCE: Login Kit/iOS.md

Docs
# Login Kit for iOS
This guide explains how to integrate your app with Login Kit for iOS. After successful user authentication with TikTok, your app can access basic user data, such as display name and avatar. Access to additional user data requires approval from TikTok for Developers website.
## Prerequisites
[Before proceeding, make sure you complete all of the steps in the iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart).
[Obtain the `client_key` and `client_secret` located in the **Credentials** section of your app page on the TikTok for Developers website](https://developers.tiktok.com/). Navigate to the **Products** section of your app page and click **Add products**. Then add **Login Kit**.
[[You must also register a redirect URI on the TikTok for Developers website. This redirect URI is used to verify your application, as well as to callback to your application with an authorization response. This redirect URI must be a universal link](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc) with an `https` scheme and your app must support associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains?language=objc).
## iOS integration
### Create an authorization request and handle responses
For the following steps, your app is required to maintain a strong reference to the request to receive the response callback. You can discard it once you have handled the response.
- Import the `TikTokOpenAuthSDK` module and create an authorization request, as shown in the code snippet below. In the authorization request init method, set the following parameters.
- `scopes`: The set of scopes you are requesting from the user.
- `redirectURI`: Universal link that's used to callback to your application
- Start the login by calling the `send(_:)` method on the authorization request object.
- After the user finishes authorizing, you will receive a response callback in the closure. In the authorization response object, you can find whether the authorization request succeeded or failed.
```
/* Step 1 */
import TikTokOpenAuthSDK

let authRequest = TikTokAuthRequest(scopes: ["user.info.basic",...], 
                                    redirectURI: "https://www.example.com/path")
/* Step 2 */
authRequest.send { response in
    /* Step 3 */
    let authResponse = response as? TikTokAuthResponse else { return }
    if authResponse.errorCode == .noError {
        print("Auth code: \(authResponse.code)")
    } else {
        print("Authorization Failed! 
              Error: \(authResponse.error ?? "") 
              Error Description: \(authResponse.errorDescription ?? "")")
    }
}
```
Alternatively, you can pass in a `nil` completion handler to the authorization request and create a `TikTokAuthResponse` directly from the URL sent back by TikTok in the `application(_:continue:restorationHandler:)` AppDelegate function. In this case, you do not have to maintain a strong reference to the authorization request.
### Obtain an access token
[Upload the `TikTokAuthResponse.code` returned in the callback and the `TikTokAuthRequest.pkce.codeVerifier` to your server-side and obtain a user access token. See User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management) for more information.
### Handling errors
[See Error Handling](https://developers.tiktok.com/doc/oauth-error-handling) for more information.
Was this document helpful?
