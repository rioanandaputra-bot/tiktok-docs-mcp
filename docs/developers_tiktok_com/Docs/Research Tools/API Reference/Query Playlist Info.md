Docs
# Query Playlists
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/playlist/info/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Request Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| playlist_id | int64 | The unique ID of the playlist | 1234569763387255595 | Yes |
| cursor | int64 | Retrieve video results starting from the specified index | 15 | No |
| max_count | int64 | Max number of videos can be returned in one playlist | 10 | No |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/playlist/info/?fields=playlist_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefghijklmn' \
--data '{
   "playlist_id": 12345677654321,
    "max_count":100,
    "cursor":0
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | PlayListInfoObject | The returned playlist info data |
| error | ErrorStructV2 | Error object |

### PlayListInfoObject

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| playlist_id | int64 | The unique ID of the playlist |
| playlist_item_total | int64 | Provides the total number of items in a playlist |
| playlist_last_updated | int64 | Provides info on when the playlist was last updated |
| playlist_name | string | The name of the playlist |
| playlist_video_ids | list<i64> | Provides a list of all video IDs in a playlist |
| has_more | bool | Whether there are more videos in the playlist or not |
| cursor | int64 | Next available videos start index |

### Example
```
{
    "data": {
        "playlist_item_total": 10,
        "playlist_last_updated": 12345678,
        "playlist_name": "example name",
        "playlist_video_ids": [
            12345678910,
            10987654321
        ],
        "cursor": 10,
        "has_more": true,
        "playlist_id": 12345678910
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "12345678899abcdefg"
    }
}
```
Was this document helpful?