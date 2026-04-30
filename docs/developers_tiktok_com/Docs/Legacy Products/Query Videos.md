Docs
# Query Videos
[There is a new version of this API available in TikTok API v2: Query Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)
## Overview
The `video/query/` endpoint, given a user and a list of video ids, can check if the videos belong to the requesting user and fetch the data of videos belonging to the user. It can be used to refresh the given videos' cover image url TTL. Number of video ids should not be larger than 20 at a time.

| **HTTP URL** | https://open-api.tiktok.com/video/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | video.list |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | "application/json" | "application/json" | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| access_token | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | act.example12345Example12345Example | Yes |
| filters | object | Fields: video_ids: set<string> | { "video_ids": ["1234565570247476230"] } | Yes |
| fields | set<string> | The set of optional video fields **Choose fields from: VideoObject's fields** | ["embed_link"] | Yes |

### Request Example
```
curl -L -X POST 'https://open-api.tiktok.com/video/query/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "access_token": "act.example12345Example12345Example",
    "filters": {
        "video_ids": ["1234568030997662933", "1234580793298373833"]
    },
    "fields": ["id", "title"]
}'
```
## Response

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| data | map<string, list<VideoObject>> | videos: list<video object> | Yes |
| error | Object | Error object | Yes |

### VideoObject

| **Field** | **Type** | **Description** | **Scope** |
| --- | --- | --- | --- |
| id | string | Unique identifier for the TikTok video. Also called "item_id" | video.list |
| create_time | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. | video.list |
| cover_image_url | string | A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a **TTL****of 6 hours.** | video.list |
| share_url | string | A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices. | video.list |
| video_description | string | The description that the creator has set for the TikTok video. Max length: 150 | video.list |
| duration | int32 | The duration of the TikTok video in seconds. | video.list |
| height | int32 | The height of the TikTok video. | video.list |
| width | int32 | The width of the TikTok video. | video.list |
| title | string | The video title. Max length: 150 | video.list |
| embed_html | string | HTML code for embedded video | video.list |
| embed_link | string | Video embed link of tiktok.com | video.list |
| like_count | int32 | Number of likes of the video. Included when requested in the fields. | video.list |
| comment_count | int32 | Number of comments of the video. Included when requested in the fields. | video.list |
| share_count | int32 | Number of shares of the video. Included when requested in the fields. | video.list |
| view_count | int64 | Number of views of the video. Included when requested in the fields. | video.list |

### Example
```
{
    "data":{
        "videos":[
            {
                "id":"1234568030997662933",
                "title":"Test Video 32"
            },
            {
                "id":"1234580793298373833",
                "title":"Test Video 22"
            }
        ]
    },
    "error":{
        "code":0,
        "message":""
    }
}
```
Was this document helpful?