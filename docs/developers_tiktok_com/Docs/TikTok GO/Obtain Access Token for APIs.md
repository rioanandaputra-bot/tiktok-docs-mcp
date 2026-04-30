Docs
# Obtain Access Token for APIs
To use TikTok's APIs, you will need to use an access token. Use the following reference tables to retrieve and refresh an access token.
## Get Access Token
For the first time, when developers receive notification that merchants have approved their request for certain scopes, they can send an HTTP request to get their access token bundle.
### Endpoint
`POST ``https://open.tiktokapis.com/merchant/oauth/token/`
### Authorization headers

| **Field** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |
| x-tt-target-idc | alisg |

### Request

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Unique identification key provisioned to the partner |
| client_secret | string | Unique identification secret provisioned to the partner |
| merchant_id | string | Unique identification of merchant that partner applied for |
| grant_type | string | Action type such as `access_token`to retrieve access token |

Example:
```
curl --location 'https://open.tiktokapis.com/merchant/oauth/token/' \
--header 'x-tt-target-idc: alisg' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=xxxxxxx' \
--data-urlencode 'client_secret=xxxxxxxx' \
--data-urlencode 'grant_type=access_token' \
--data-urlencode 'merchant_id=xxxxxx'
```
### Response

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| access_token | string | Access token used for API call self identification |
| expires_in | int64 | Unix timestamp indicating when the access token expires |
| refresh_token | string | Refresh token used to request a new access token when the current one expires |
| refresh_expires_in | int64 | Unix timestamp indicating when the refresh token expires |

Example:
```
{
    "access_token": "xxx",
    "expires_in": 1749368707,
    "refresh_expires_in": 1906616707,
    "refresh_token": "xxx"
}
```
## Refresh Access Token
Each access aoken usually has an expiration time of 120 hours (5 days). After they expire, developers should use refresh the access token.
Note that if there is a scope range change (for example, if merchants revoke or approve new scopes), the access token value will change.
### Endpoint
`POST ``https://open.tiktokapis.com/merchant/oauth/token/`
### Authorization headers

| **Field** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |
| x-tt-target-idc | alisg |

### Request Body

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Unique identification key provisioned to the partner |
| client_secret | string | Unique identification secret provisioned to the partner |
| merchant_id | string | Unique identification of the merchant that the partner applied for |
| grant_type | string | Action type such as `refresh_token`for refreshing the access token |
| refresh_token | string | Token previously issued to the client used to request a new access token without re authentication |

Example:
```
curl --location 'https://open.tiktokapis.com/merchant/oauth/token/' \
--header 'x-tt-target-idc: alisg' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=xxxxx' \
--data-urlencode 'client_secret=xxxxxx' \
--data-urlencode 'grant_type=access_token' \
--data-urlencode 'merchant_id=xxxxxxx' \
--data-urlencode 'refresh_token=mrt.xxxxxx.s1'
```
### Response

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| access_token | string | Access token used for API call self identification |
| expires_in | int64 | Access token expiration time Unix timestamp |
| refresh_token | string | Refresh token used to refresh an access token when it expires |
| refresh_expires_in | int64 | Refresh token expiration time Unix timestamp |

Example:
```
{
    "access_token": "xxx",
    "expires_in": 1749368707,
    "refresh_expires_in": 1906616707,
    "refresh_token": "xxx"
}
```
Was this document helpful?