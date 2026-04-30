Docs
# Query video_wi
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | video_wi | Yes |
| condition_groups | object | Specifications for what data should be returned and processed | condition_groups = [ { "operator": "and", "conditions": [ { "field": "like_count", "operator": "gte", "field_values": ["1000"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | display_name, country_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_date, duration_type, favorites_count, stem_verified, hashtag_info_list, effect_info_list, sticker_text,video_label,video_mention_list,video_tags | Yes |
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

## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, text, parent_comment_id, like_count, reply_count, create_time |

## Query Video Comment Data from Tiktok via SDK
Example code
```
from pyrqs import rqs

category = 'video_wi'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "like_count",
                "operator": "gte",
                "field_values": ["1000"]
            }
        ]
    }
]

fields = 'video_description'
limit = 10
client = rqs.RQSClient()
data = client.query(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
Was this document helpful?