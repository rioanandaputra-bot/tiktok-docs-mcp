Docs
# List Videos
[There is a new version of this API available in TikTok API v2: List Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)
## Overview
The `video/list/` endpoint can return a paginated list of given user's **public** TikTok video posts, sorted by `create_time` in descending order.

| **HTTP URL** | https://open-api.tiktok.com/video/list/ |
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
| fields | set<string> | The set of optional video fields **Choose fields from: VideoObject's fields** | ["embed_link"] | Yes |
| cursor | int64 | Cursor for pagination. If `response.has_more`is true, pass in the `response.cursor`to the next request will yield the results for the next page. _Note: the cursor value is a __UTC__Unix timestamp in milli-seconds. You can pass in a customized timestamp to fetch the user's videos posted before the provided timestamp._ | 0 | No |
| max_count | int32 | The maximum number of videos that will be returned from each page. Default is 10. Maximum is 20. _Note: due our trust and safety policies, it is possible that the endpoint returns less than max_count number of videos even if __response.data.has_more__is __true__._ | 10 | No |

### Example
```
curl -L -X POST 'https://open-api.tiktok.com/video/list/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "access_token": "act.example12345Example12345Example",
    "fields": ["id", "embed_link", "title"]
}'
```
## Response

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | map<string, object> | video_list: list<VideoObject> cursor: int64 has_more: bool err_code:int64 error_code:int64 |
| extra | map<string, object> | error_detail: string logid: string |

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
        "cursor":1652986389000,
        "err_code":0,
        "error_code":0,
        "has_more":false,
        "video_list":[
            {
                "id":"7099522475452681474",
                "embed_link":"https://www.tiktok.com/static/profile-video?id=7099522475452681474&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
                "title":"video 1"
            }
        ]
    },
    "extra":{
        "error_detail":"",
        "logid":"202205200320140101131341351D46C27E"
    }
}
```
Was this document helpful?