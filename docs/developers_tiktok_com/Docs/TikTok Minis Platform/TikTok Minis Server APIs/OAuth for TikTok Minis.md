Docs
# OAuth for TikTok Minis
TikTok OAuth v2 flow manages the token life cycle, allowing you to integrate authentication flows directly in your TikTok Minis or mini game. A successful authorization flow grants you refreshable access tokens. Those tokens enable you to perform endpoint access with user permissions.
[Note: OAuth for TikTok Minis has the same structure as User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management), with the exception of omitting `redirect_uri` and `code_verifier` in the request body parameters for fetching an access token.
## Fetch an access token using an authorization code
Once the authorization code callback is handled, you can use the code to retrieve the user's access token.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/token/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| code | string | The authorization code from the web, iOS, Android or desktop authorization callback. The value should be URL decoded. |
| grant_type | string | A fixed value that should always be set as `authorization_code` |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize |
| access_token | string | The access token for future calls on behalf of the user |
| expires_in | int64 | The expiration of `access_token`in seconds. It is valid for 24 hours after initial issuance. |
| refresh_token | string | The token to refresh `access_token`. It is valid for 365 days after the initial issuance. |
| refresh_expires_in | int64 | The expiration time of `refresh_token`in seconds |
| token_type | string | A fixed value that should be set to `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'code=CODE' \
--data-urlencode 'grant_type=authorization_code' \
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "afd97af1-b87b-48b9-ac98-410aghda5344",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request is missing a required parameter.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## Refresh an access token using a refresh token
Although the fetched `access_token` expires within 24 hours, it can be refreshed without user consent. The developer's backend server can schedule background jobs to keep tokens up to date.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/token/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| grant_type | string | A fixed value that should always be set as `refresh_token` |
| refresh_token | string | The user's refresh token |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize |
| access_token | string | The new token for future calls on behalf of the user |
| expires_in | int64 | The expiration of the access token in seconds |
| refresh_token | string | The token to refresh a user's `access_token`. Note: The returned `refresh_token`may be different than the one passed in the payload. You must use the newly-returned token if the value is different than the previous one. |
| refresh_expires_in | int64 | The expiration for `refresh_token`in seconds. |
| token_type | string | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=REFRESH_TOKEN'
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "asdf-12345c-1a2s3d-ac98-asdf123as12as34",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## Revoke access
When a user wants to disconnect your application from TikTok, you can revoke their tokens so the user will no longer see your application on the **Manage apps **page of the TikTok for Developers website.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/revoke/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| token | string | The `access_token`that bears the authorization of the TikTok user |

### Response struct
If the request is successful, the response struct will be empty.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/revoke/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'token=ACCESS_TOKEN'
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
Was this document helpful?