Docs
# Query VideoComments
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | comment | Yes |
| condition_groups | list | Specifications for what data should be returned and processed | condition_groups = [ { "operator": "and", "conditions": [ { "field": "id", "operator": "eq", "field_values": ["7347705421577563079"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, video_id, text, parent_comment_id, like_count, reply_count, create_time, display_name | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query  Condition Fields and Operators

| **Field** | **Description** | **Type** | **Allowed Operator** |  |
| --- | --- | --- | --- | --- |
| id | The unique ID for the comment | string | EQ IN |  |
| text | The text within the comment | string | EQ IN |  |
| video_id | The ID of the video or item that the comment is under | string | EQ IN |  |
| parent_comment_id | The ID of the comment's parent comment, if any | string | EQ IN |  |
| like_count | The number of likes a comment has | string | EQ IN GT GTE LT LTE |  |
| reply_count | The number of replies a comment has | string | EQ IN GT GTE LT LTE |  |
| create_time | The unix timestamp that the comment was created on | string | EQ IN GT GTE LT LTE |  |
| display_name | User's display name who post the comment | string | EQ IN |  |

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
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | No |

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
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, video_id, text, parent_comment_id, like_count, reply_count, create_time |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Video Comment Data from Tiktok via SDK
Example code
```
from pyrqs import rqs

category = 'comment'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "video_id",
                "operator": "eq",
                "field_values": ["7347705421577563079"]
            }
        ]
    }
]

fields = 'id, video_id, text, parent_comment_id, like_count, reply_count, create_time'
limit = 100
client = rqs.RQSClient()
task_id = client.create_query_task(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
status = client.check_query_task_status(task_id)
```
Was this document helpful?