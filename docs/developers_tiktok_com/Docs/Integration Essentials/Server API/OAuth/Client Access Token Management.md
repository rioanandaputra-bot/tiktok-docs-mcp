Docs
# Client Access Token Management
[[Client access token is a type of access token that does not need user authorization. This is typically used by clients to access resources about themselves or a TikTok application, rather than to access a user's resources. The use cases are to access Research API](https://developers.tiktok.com/products/research-api/) and Commercial Content API](https://developers.tiktok.com/products/commercial-content-api/).
### Endpoint
_POST_ https://open.tiktokapis.com/v2/oauth/token/
### Headers

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | String | The unique identification key provisioned to the partner. |
| client_secret | String | The unique identification secret provisioned to the partner. |
| grant_type | String | Its value should always be set as `client_credentials`. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| access_token | String | The generated client access token. |
| expires_in | Int64 | The expiration for the `access_token`in seconds. **It****is valid for 2 hours after the initial issuance**. |
| token_type | String | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'grant_type=client_credentials'
```
If the request is successful, the response will look like the following:
```
{
    "access_token": "clt.example12345Example12345Example",
    "expires_in": 7200,
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following:
```
{
    "error": "invalid_request",
    "error_description": "Client secret is missed in request.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
[[At the time of this writing, this guide is applicable to Research API](https://developers.tiktok.com/doc/research-api-get-started) and Commercial Content API](https://developers.tiktok.com/doc/commercial-content-api-getting-started).
Was this document helpful?