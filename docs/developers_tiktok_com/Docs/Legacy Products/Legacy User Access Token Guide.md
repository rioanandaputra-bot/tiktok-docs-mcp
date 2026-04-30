Docs
# Manage Legacy User Access Tokens
[Legacy user access tokens using our OAuth v1 API are deprecated. View migration announcement](https://developers.tiktok.com/bulletin/migration-guidance-oauth-v1).
## Understanding the Basics
### OAuth
TikTok Login Kit manages the token lifecycle, allowing you to integrate login and authentication flows directly in your application. A successful authorization flow grants developers refreshable access tokens. Those tokens enable developers to perform endpoint access with user permissions.
### Authorization Scopes
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the rights to only agree to a subset of scopes you requested from them.
Here are some example scopes:
- **user.info****.basic** gives read-only access to a user's avatar and display name.
- **video.list** gives read-only access to a user's public TikTok videos.
[You can learn more about Scopes on our Scopes Overview page](https://developers.tiktok.com/doc/scopes-overview).
### Token Security
Tokens must be handled with extreme caution. We recommend storing and managing all tokens on the server side.
- Access token is a user authorization token that can be used to directly access user information in the Tiktok ecosystem.
- Refresh token is used to renew the access token.
## Endpoints
### 1. Fetch Access Token Using Authorization Code
Once the authorization code callback is handled, you can use the code to retrieve the user's access token.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/access_token/`
#### Request Query Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| client_secret | string | The unique identification secret provisioned to the partner. |
| code | string | Authorization code from Web/iOS/Android authorization callback. |
| grant_type | string | Its value should always be set as _authorization_code_. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier. |
| scope | string | The scopes user has agreed to authorize, separated by comma (,). |
| access_token | string | The access token for future calls on behalf of the user. |
| expires_in | int64 | Expiration for the `access_token`in seconds. **It is valid for 24 hours after initial issuance**. |
| refresh_token | string | The token for refresh the `access_token`. **It is valid for 365 days after initial issuance**. |
| refresh_expires_in | int64 | Expiration for the `refresh_token`in seconds. |

Make sure to store these values in your backend as they will be needed to persist access.
#### Code Example
```
app.get('/redirect', (req, res) => {
    const { code, state } = req.query;
    const { csrfState } = req.cookies;

    if (state !== csrfState) {
        res.status(422).send('Invalid state');
        return;
    }

    let url_access_token = 'https://open-api.tiktok.com/oauth/access_token/';
    url_access_token += '?client_key=' + CLIENT_KEY;
    url_access_token += '&client_secret=' + CLIENT_SECRET;
    url_access_token += '&code=' + code;
    url_access_token += '&grant_type=authorization_code';

    fetch(url_access_token, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
If the request is not successful, the response will return the following error response body:
```
{
    "data": {
        "captcha": "",
        "desc_url": "",
        "description": "Parameter error",
        "error_code": 10002
    },
    "message": "error"
}
```
### 2. Refresh Access Token Using Refresh Token
Although the fetched `access_token` expires within 24 hours, it can be refreshed without user consent. The developer's backend server can schedule background jobs to keep tokens up to date.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/refresh_token/`
#### Request Query Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| grant_type | string | Its value should always be set as _refresh_token_. |
| refresh_token | string | The user's `refresh_token`received from `/oauth/access_token/`endpoint. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The partner-facing user id. |
| scope | string | The scopes user has agreed to authorize, separated by comma (,). |
| access_token | string | New token for future calls on behalf of the user. |
| expires_in | int64 | Expiration for the access token in seconds. |
| refresh_token | string | The token for refresh an user's `access_token`. Note that the returned refresh_token may be different than the one passed in the payload. **Developers must use the newly-returned token should the value is different than the previous one.** |
| refresh_expires_in | int64 | Expiration for the `refresh_token`in seconds. |

Make sure to store these values in your backend as they will be needed to persist access.
#### Code Example
```
app.get('/refresh_token/', (req, res) => {
    const refresh_token = req.query.refresh_token;

    let url_refresh_token = 'https://open-api.tiktok.com/oauth/refresh_token/';
    url_refresh_token += '?client_key=' + CLIENT_KEY;
    url_refresh_token += '&grant_type=refresh_token';
    url_refresh_token += '&refresh_token=' + refresh_token;

    fetch(url_refresh_token, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
If the request is not successful, the response will return the following error response body:
```
{
    "data": {
        "captcha": "",
        "desc_url": "",
        "description": "Parameter error",
        "error_code": 10002
    },
    "message": "error"
}
```
### 3. Revoke Access
When users want to disconnect the connection between your application and TikTok, you can revoke their `access_tokens` so the users will no longer see your application show up on the **Manage app permissions** page within TikTok.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/revoke/`
#### Request Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier; obtained through `/oauth/access_token/`the user's unique token. |
| access_token | string | The token that bears the authorization of the TikTok user, `/oauth/access_token/`. This token requires user authorization. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| error_code | int64 | Error code. |
| description | string | Error code description. |

#### Code Example
```
app.get('/revoke', (req, res) => {
    const { open_id, access_token } = req.query;

    let url_revoke = 'https://open-api.tiktok.com/oauth/revoke/';
    url_revoke += '?open_id=' + open_id;
    url_revoke += '&access_token=' + access_token;

    fetch(url_revoke, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
Was this document helpful?