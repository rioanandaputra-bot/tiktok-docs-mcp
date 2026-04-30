Docs
# Query Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | video | Yes |
| condition_groups | list<Condition> | Specifications for what data should be returned and processed | `condition_groups = [ { "operator": "and", "conditions": [ { "field": "like_count", "operator": "gte", "field_values": ["1000"] } ] } ]` | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_time, duration_type, favorites_count, stem_verified, hashtag_info_list, effect_info_list, sticker_text, video_label, video_mention_list, video_tags | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query Condition Fields and Operators

| **Field** | **Description** | **Type** | **Allowed Operator** |
| --- | --- | --- | --- |
| id | Unique identifier for the TikTok video. Also called "item_id" or "video_id" | string | EQ IN |
| create_time | UTC Unix epoch (in seconds) of when the TikTok video was posted. (Inherited field from TNS research API) | string | EQ IN GT GTE LT LTE |
| username | The video creator's username | string | EQ IN |
| region_code | A two digit code for the country the video was posted in | string | EQ IN |
| video_description | The description of the video, also known as the title | string | EQ IN LIKE |
| music_id | The music_id used in the video | int64 | EQ IN |
| like_count | The number of likes the video has received. | string | EQ IN GT GTE LT LTE |
| comment_count | The number of comments the video has received. | string | EQ IN GT GTE LT LTE |
| share_count | The number of shares the video has received. | string | EQ IN GT GTE LT LTE |
| view_count | The number of video views the video has received. | int64 | EQ IN GT GTE LT LTE |
| effect_ids | The list of effect ids applied on the video | list<string> | CONTAINS |
| hashtag_names | The list of hashtag names that the video participates in | list<string> | CONTAINs |
| playlist_id | The ID of playlist that the video belongs to | string | EQ IN |
| voice_to_text | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) | string | EQ IN |
| duration_type | The duration of the video, in seconds. | int | EQ IN GT GTE LT LTE |
| hashtag_id | Hash tag id which is associated with the video. | string | EQ IN |
| hashtag_name | Hash tag name which is associated with the video. | string | EQ IN |
| hashtag_description | Hashtag description which is associated with the video. | string | EQ IN |
| effect_id | Effect ID that the video used | string | EQ IN |
| effect_name | Effect name that the video used | string | EQ IN |
| effect_photo_url | Effect photo url that the video used | string | EQ IN |
| sticker_text | Sticker text that the video has | string | EQ IN |
| video_label | Video label that the video contains | list<string> | CONTAINs |
| video_mention_list | People who are mentioned in the video | list<string> | CONTAINs |
| video_tags | Video tags that the video contains | list<string> | CONTAINs |

#### Create Query Task Sample Code
This interface will create a query task at TikTok, and it will return a task id. Users can use this id to check the status, get the result and cancel the result in the future.
#### Example
```
from pyrqs import rqs

category = 'video'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "region_code",
                "operator": "eq",
                "field_values": ["NL"]
            }
        ]
    }
]

fields = 'username,region_code,video_description,music_id,like_count'
limit = 1000
client = rqs.RQSClient()
task_id = client.create_query_task(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
```
#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Result Code Sample
#### Example
```
data = client.get_query_task_result(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

#### Get_query_task_result_example
##### Example
```
data = client.get_query_task_result(task_id)
```
### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_time, duration_type, favorites_count, and stem_verified. |

## Query Video Data from Tiktok via SDK
Example code
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json

category = 'video'
fields = 'username,like_count,hashtag_info_list,video_sticker_id,video_mention_list,video_label'
limit = 100
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "video_description",
                    "operator": "LIKE",
                    "field_values": ["%tiktok%"]
                },
                {
                    "field": "hashtag_names",
                    "operator": "CONTAINS",
                    "field_values": ["tiktok"]
                }
            ]
        }
]
data = client.query(category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
Was this document helpful?