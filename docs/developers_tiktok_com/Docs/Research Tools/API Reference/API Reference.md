Docs
# Query Videos
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/video/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | Indicate the original media type of the resource. | "application/json" | Yes |
| Authorization | string | The client access token which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields. Choose from the Video Object's fields. | Complete list: id,video_description,create_time, region_code,share_count,view_count,like_count,comment_count, music_id,hashtag_names, username,effect_ids,playlist_id,voice_to_text, is_stem_verified, favorites_count, video_duration,hashtag_info_list, sticker_info_list, effect_info_list, video_mention_list,video_label,video_tag | Yes |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| query | Query object (See the definition below) | A JSON object that contains three types of children: `and`, `or`, and `not`, each of which is a list of conditions. An valid query must contain at least one non-empty `and`, `or`or `not`condition lists | { "and":[ { "operation":"IN", "field_name":"region_code", "field_values":[ "JP", "US" ] }, { "operation":"EQ", "field_name":"keyword", "field_values":["animal"] } ], "not":[ { "operation":"LT", "field_name":"create_date", "field_values":["20230101"] } ] } | Yes |
| start_date | string | The lower bound of video creation time in UTC | "20210102" | Yes |
| end_date | string | The upper bound of video creation time in UTC The end_date must be no more than 30 days after the start_date | "20210123" | Yes |
| max_count | int64 | The number of videos in response. Default is 20, max is 100. It is possible that the API returns less videos than the max count due to reasons such as videos deleted/marked as private by users etc. | 20 | No |
| cursor | int64 | Retrieve video results starting from the specified index | 100 | No |
| search_id | string | The unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "7201388525814961198" | No |
| is_random | bool | The flag that indicates whether to return results in a random order. If set to true, then the API returns 1 - 100 videos in random order that matches the query. If set to false or not set with any value, then the API returns results in the decreasing order of video IDs. | true | No |

##### Query

| **Key** | **Type** | **Description ** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

##### Condition

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| field_name | string | The name of the field this condition is restricting One of: ["create_date", "username", "region_code", "video_id", "hashtag_name", "keyword", "music_id", "effect_id", "video_length", "view_count", "comment_count"] |
| operation | string | One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" |
| field_values | list<string> | A list of restriction values |

##### Condition fields

| **Field Name** | **Description ** | **Example** |
| --- | --- | --- |
| create_date | The video creation date in UTC, presented in the format YYYYMMDD | "20220910" |
| username | The username of the video creator | "cookie_love_122" |
| region_code | A two digit code for the country where the video creator registered their account | "FR", "TH", "MM", "BD", "IT", "NP", "IQ", "BR", "US", "KW", "VN", "AR", "KZ", "GB", "UA", "TR", "ID", "PK", "NG", "KH", "PH", "EG", "QA", "MY", "ES", "JO", "MA", "SA", "TW", "AF", "EC", "MX", "BW", "JP", "LT", "TN", "RO", "LY", "IL", "DZ", "CG", "GH", "DE", "BJ", "SN", "SK", "BY", "NL", "LA", "BE", "DO", "TZ", "LK", "NI", "LB", "IE", "RS", "HU", "PT", "GP", "CM", "HN", "FI", "GA", "BN", "SG", "BO", "GM", "BG", "SD", "TT", "OM", "FO", "MZ", "ML", "UG", "RE", "PY", "GT", "CI", "SR", "AO", "AZ", "LR", "CD", "HR", "SV", "MV", "GY", "BH", "TG", "SL", "MK", "KE", "MT", "MG", "MR", "PA", "IS", "LU", "HT", "TM", "ZM", "CR", "NO", "AL", "ET", "GW", "AU", "KR", "UY", "JM", "DK", "AE", "MD", "SE", "MU", "SO", "CO", "AT", "GR", "UZ", "CL", "GE", "PL", "CA", "CZ", "ZA", "AI", "VE", "KG", "PE", "CH", "LV", "PR", "NZ", "TL", "BT", "MN", "FJ", "SZ", "VU", "BF", "TJ", "BA", "AM", "TD", "SI", "CY", "MW", "EE", "XK", "ME", "KY", "YE", "LS", "ZW", "MC", "GN", "BS", "PF", "NA", "VI", "BB", "BZ", "CW", "PS", "FM", "PG", "BI", "AD", "TV", "GL", "KM", "AW", "TC", "CV", "MO", "VC", "NE", "WS", "MP", "DJ", "RW", "AG", "GI", "GQ", "AS", "AX", "TO", "KN", "LC", "NC", "LI", "SS", "IR", "SY", "IM", "SC", "VG", "SB", "DM", "KI", "UM", "SX", "GD", "MH", "BQ", "YT", "ST", "CF", "BM", "SM", "PW", "GU", "HK", "IN", "CK", "AQ", "WF", "JE", "MQ", "CN", "GF", "MS", "GG", "TK", "FK", "PM", "NU", "MF", "ER", "NF", "VA", "IO", "SH", "BL", "CU", "NR", "TP", "BV", "EH", "PN", "TF", "RU" |
| video_id | The unique identifier of the video | 6978662169214864645 |
| hashtag_name | The hashtag associated with the video | "arianagrande", "celebrity" |
| keyword | The keyword in the video description | "tiktok" |
| music_id | The music ID of the video. | "8978345345214861235" |
| effect_id | The effect ID of the video. | "3957392342148643476" |
| video_length | The duration of the video SHORT: <15s MID: 15 ~60s LONG: 1~5min EXTRA_LONG: >5min | "SHORT", "MID", "LONG", "EXTRA_LONG" |
| view_count | The number of video views the video has received | 10 |
| comment_count | The number of comments the video has received | 10 |

## Example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "query": {
        "and": [
            {
                "operation": "IN",
                "field_name": "region_code",
                "field_values": ["JP", "US"]
            },
            {
                "operation":"EQ",
                "field_name":"hashtag_name",
                "field_values":["animal"]
            }
        ],
        "not": [
          {
                "operation": "EQ",
                "field_name": "video_length",
                "field_values": ["SHORT"]
           }
        ]
    },
    "max_count": 100,
    "cursor": 0,
    "start_date": "20230101",
    "end_date": "20230115"
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | QueryVideoResponseData | { "videos": [...], "cursor": 100, "has_more": true, "search_id": "" } |
| error | ErrorStruct | Error object |

## Data Structures
### QueryVideoResponseData

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| videos | list<Video Object> | A list of video objects that match the query |
| cursor | int64 | Returns video results from the given index. |
| has_more | bool | Whether there are more videos or not. |
| search_id | string | A search_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. |

##### Video Object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | Unique identifier for the TikTok video. Also called "item_id" or "video_id" |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The video's author's username |
| "region_code" | string | A two digit code for the country where the video creator registered their account |
| "video_description" | string | The description of the video, also known as the title |
| "music_id" | int64 | The music_id used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of video views the video has received |
| "effect_ids" | list<string> | The list of effect ids applied on the video |
| "hashtag_names" | list<string> | The list of hashtag names that the video participates in |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists. |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_url". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video . |
| "video_label" | Struct | Returns any information and labels associated with a video. |
| "playlist_id" | int64 | The ID of playlist that the video belongs to |
| "voice_to_text" | string | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) |
| is_stem_verified | bool | Whether the video has been verified as being high quality STEM content. |
| video_duration | int64 | The duration of the video, in seconds. |
| favorites_count | int64 | The number of favorites that a video receives. |
| video_tag | Struct | "type" and "number" returned here Definitions: "number" = 1, and "type" = AIGC Type indicates "Creator Labelled as AI-Generated" "number" = 2, and "type" = AIGC Type indicates "AI-Generated" "number" = 1, and "type" = Branded Type indicates "Paid Partnership" "number" = 7, and "type" = Branded Type indicates "Creator Earns Commission" |

## Example
```
{
    "data": {
        "videos": [
            {
                "hashtag_names": [
                    "avengers",
                    "pov"
                ],
                "region_code": "CA",
                "create_time": 1633823999,
                "effect_ids": [
                    "0"
                ],
                "video_id": 702874395068494965,
                "music_id": 703847506349838790,
                "video_description": "lol #pov #avengers",
                "view_count": 1050,
                "comment_count": 2
            },
            ...
        ],
        "cursor": 100,
        "search_id": "7201388525814961198",
        "has_more": true
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20230113024658F0D7C5D6CA3A9B79C5B9"
    }
}
```
Was this document helpful?