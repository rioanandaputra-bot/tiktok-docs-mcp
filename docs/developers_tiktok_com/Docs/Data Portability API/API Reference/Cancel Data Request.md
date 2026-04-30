Docs
# Cancel Data Request
Use POST request to cancel the data download request

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/cancel/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | string | The requested fields: request_id | request_id | Yes |

### Request Example
```
curl --location 'https://open.tiktokapis.com/v2/user/data/cancel/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemp123.e1' \
--data '{
    "request_id": 123451234512345
}'
```
## Response
A successful cancellation request will return an "ok" message in the error response. In case of failure, a verbose error message will be returned

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| error | ErrorStructV2 | See the response example below |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string | ok |
| message | string | The detailed error description |  |
| log_id | string | The unique ID associated with every request for debugging | 1010xyz10101asdf1010101010100a12abc24 |

### Response Example
```
{
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "2023242526272829300000000000001111"
    }
}
```
Was this document helpful?