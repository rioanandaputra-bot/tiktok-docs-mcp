Docs
# Query User Info
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/user/info/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See User Info Object below for a full list of values. | **Complete list**: display_name, bio_description, avatar_url, is_verified, follower_count, following_count, likes_count, video_count,bio_url | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| username | string | username as the unique identifier | "joe11235" |

### Example
```
curl -L 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type:application/json' \
-d '{"username": "joe123456"}'
```
# Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | User Info Object | The returned user info data |
| error | ErrorStructV2 | Error object |

User Info Object

| Field name | Type | Description |
| --- | --- | --- |
| "display_name" | string | The user's display name / nickname |
| "bio_description" | string | The user's bio description |
| "avatar_url" | string | The url to a user's profile picture |
| "is_verified" | bool | The user's verified status. True if verified, false if not |
| "following_count" | int | The number of people the user is following |
| "follower_count" | int | The number of followers the user has |
| "video_count" | int | The number of videos the user has posted |
| "likes_count" | int | The total number of likes the user has accumulated |
| "bio_url" | string | The url in user's bio when shared |

### Example
```
{
    "data": {
        "bio_description": "my_bio",
        "is_verified": false,
        "likes_count": 27155089,
        "video_count": 44,
        "avatar_url": "https://some_cdn.com/my_avatar",
        "follower_count": 232,
        "following_count": 45,
        "display_name": "my nick name"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202207280326050102231031430C7E754E",
    }
}
```
Was this document helpful?