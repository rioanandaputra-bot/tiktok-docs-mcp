Docs
# Liked Videos
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/liked_videos/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query Parameters

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Video Object below for a full list of values. | Complete list: id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names, is_stem_verified, favourites_count, video_duration,hashtag_info_list, sticker_info_list, effect_info_list, ,video_mention_list,video_label,video_tag | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of liked videos in a single response. Default is 20, max is 100. It is possible that the API returns fewer videos than the max count due to content moderation outcomes, videos being deleted, marked as private by users, or more. | 20 | No |
| cursor | int64 | Videos created on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/user/liked_videos/?fields=id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.testtemp123testtemp123' \
--data '{
    "username": "test_username",
    "max_count": 1,
    "cursor" : 1706457540000,
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserLikedVideosData | The returned list of liked video objects |
| error | ErrorStructV2 | Error object |

### UserLikedVideosData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_liked_videos | list<Video> | A list of video objects that match the query |
| cursor | int64 | Retrieve liked videos starting from the specified Unix timestamp in UTC seconds |
| has_more | bool | Whether there are more liked videos or not |

### Video Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | The unique identifier of the TikTok video |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The username as the unique identifier of the video creator |
| "region_code" | string | A two digit code for the country where the video creator registered their account. |
| "video_description" | string | The description of the liked video |
| "music_id" | int64 | The music ID used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of views the video has received |
| "hashtag_names" | list<string> | The list of hashtags used in the video |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists. |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_URI". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video |
| "video_label" | Struct | Returns any information and labels associated with a video. |
| "video_duration" | int64 | The duration of the video, in seconds. |
| "is_stem_verified" | bool | Whether the video has been verified as being high quality STEM content. |
| "favorites_count" | int64 | The number of favorites that a video receives. |
| video_tag | Struct | "video_tag_type" and "video_tag_number" returned here Definitions: "video_tag_number" = 2, and "video_tag_type" = AIGC Type indicates "Creator Labelled as AI-Generated" "video_tag_number" = 1, and "video_tag_type" = AIGC Type indicates "AI-Generated" "video_tag_number" = 7, and "video_tag_type" = Branded Type indicates "Creator Earns Commission" "video_tag_number" = 1, and "video_tag_type" = Branded Type indicates "Paid Partnership" |

### Example
```
{
    "data": {
        "cursor": 1706457371000,
        "has_more": true,
        "user_liked_videos": [
            {
                "share_count": 1,
                "view_count": 1586,
                "comment_count": 6,
                "hashtag_names": [
                    "song",
                    "Viral"
                ],
                "id": 123123123123123123123,
                "music_id": 454545454545454545
            },
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "20240299999999999993FCB68B8B13"
    }
}
```
Was this document helpful?