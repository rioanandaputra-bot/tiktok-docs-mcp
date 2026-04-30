Docs
# Query User Info
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | profile | Yes |
| condition_groups | object | Specifications for what data should be returned and processed | `condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": [ "test user" ] } ] } ]` | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | username, bio_description, avatar_uri, is_verified, following_count, follower_count, video_count, likes_count, bio_url | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |
| bio_url | string | The user's bio url | EQ IN |  |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query Condition Fields and Operators

| Field | Description | Type | Allowed Operator |
| --- | --- | --- | --- |
| username | The unique user name on TikTok | string | EQ IN |
| bio_description | The user's bio description | string | EQ IN |
| avatar_uri | The url to a user's profile picture | string | EQ IN |
| is_verified | The user's verified status. True if verified, false if not | int64 | EQ |
| following_count | The number of people the user is following | int64 | EQ IN GT GTE LT LTE |
| follower_count | The number of followers the user has | int64 | EQ IN GT GTE LT LTE |
| video_count | The number of videos the user has posted | int64 | EQ IN GT GTE LT LTE |
| likes_count | The total number of likes the user has accumulated | int64 | EQ IN GT GTE LT LTE |

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
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | username, bio_description, avatar_uri, is_verified, following_count, follower_count, video_count, likes_count |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Profile Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs

category = 'profile'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "username",
                "operator": "eq",
                "field_values": ["test user"]
            }
        ]
    }
]

fields = 'username, bio_description, avatar_uri, is_verified, following_count, follower_count'
limit = 1000
client = rqs.RQSClient()
data = client.query(category=category, condition_groups=condition_groups, fields=fields, limit=limit)
```
Was this document helpful?