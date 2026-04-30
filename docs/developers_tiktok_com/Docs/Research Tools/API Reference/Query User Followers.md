Docs
# Query User Followers
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/followers/ |
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
| max_count | int64 | The maximum number of followers that can be returned in this response. Default is 20; max is 100. | 100 | No |
| cursor | int64 | Followers followed on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://platform.tiktokapis.com/v2/research/user/followers/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.test123test123test123' \
--data '{
    "username": "test_user",
    "max_count":3,
    "cursor": 12347764
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserFollowerData | The list of the followers of the user |
| error | ErrorStructV2 | Error object |

### UserFollowerData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_followers | list<UserInfo> | A list of user info objects that match the query |
| cursor | int64 | Followers that followed this user on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. |
| has_more | bool | Whether this user has more followers or not |

### User Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "display_name" | string | The profile name of the follower of this user |
| "username" | string | The username of the follower of this user |

### Example
```
{
    "data": {
        "cursor": 1706837834,
        "has_more": true,
        "user_followers": [
            {
                "display_name": "test user",
                "username": "test_username"
            },
            {
                "username": "test user 2",
                "display_name": "test_username2"
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "123499999999999999999999999999"
    }
}
```
Was this document helpful?