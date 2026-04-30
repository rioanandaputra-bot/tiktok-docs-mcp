Docs
# Query User Pinned Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | pinned_videos | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": ["test user"] } ] } ] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

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

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
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

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Pinned Videos Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'pinned_videos'
fields = 'id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names,is_stem_verified,favorites_count'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?