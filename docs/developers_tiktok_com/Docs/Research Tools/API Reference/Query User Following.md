Docs
# Query User Following
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/following/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of accounts the user follows returned in a single response. Default is 20, max is 100. | 100 | No |
| cursor | int64 | Accounts the user started following on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://open-platform.tiktokapis.com/v2/research/user/following/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.test123temp123test123test123' \
--data '{
    "username": "test_user",
    "max_count":3,
    "cursor": 1685544251
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserFollowingData | The list of the accounts this user is following |
| error | ErrorStructV2 | Error object |

### UserFollowingData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_following | list<UserInfo> | A list of user info objects that match the query |
| cursor | int64 | Accounts the user started following on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. |
| has_more | bool | Whether there are more accounts this user is following or not |

### User Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "display_name" | string | The profile name of the account that the user is following |
| "username" | string | The username of the account that the user is following |

### Example
```
{
    "data": {
        "has_more": true,
        "user_following": [
            {
                "display_name": "test user",
                "username": "test_username"
            },
            {
                "display_name": "test user 2",
                "username": "test_username2"
            },
            {
                "display_name": "test user 3",
                "username": "test_username3"
            }
        ],
        "cursor": 1650642422
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "202499999999999999999999999999999"
    }
}
```
Was this document helpful?