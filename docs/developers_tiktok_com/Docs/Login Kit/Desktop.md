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