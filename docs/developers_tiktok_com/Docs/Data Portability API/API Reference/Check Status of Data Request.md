Docs
# Check Status of Data Request
Use POST request to check the status of a data download request

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/check/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: request_id apply_time collect_time status data_format category_selection_list | request_id,status,apply_time | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API. | "text" | Yes |

### Request Example
```
curl --location 'https://open-platform.tiktokapis.com/v2/user/data/check/?fields=request_id,status,apply_time,collect_time,data_format,category_selection_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemo123!5328.e2' \
--data '{
    "request_id": 123451234512345
}'
```
## Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | GetUserDataResponseData | See the response example below |
| error | ErrorStructV2 | See the response example below |

### GetUserDataResponseData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The `request_id`for which the status is requested | 123451234512345 |
| apply_time | int64 | UTC Unix timestamp at which the data collection was requested | 1703186989 |
| collect_time | int64 | UTC Unix timestamp at which the data collection was started | 1703187862 |
| status | string | Current status of the data which was requested to be collected. Valid values are: pending : Indicates the data is still being collected and not yet ready for download. downloading : Indicated the data is ready for download. expired : The Download User Data API can no longer fetch this information as it is expired. Request expires within 4 days from when it was ready to be downloaded. cancelled : The caller cancelled this request using the Cancel User Data API | "downloading" |
| data_format | string | Format requested in the initial Add Data Request API. Valid values are: json text | "text" |
| category_selection_list | list<string> | Type of data that was requested in the initial Add Request API. Valid values are: all_data profile activity video direct_message | ["profile", "activity"] |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string | ok |
| message | string | The detailed error description |  |
| log_id | string | The unique ID associated with every request for debugging | 1010xyz10101asdf1010101010100a12abc24 |

### Response Example
```
{
    "data": {
        "apply_time": 1703186989,
        "category_selection_list": [
            "profile",
            "video",
            "direct_messages"
        ],
        "collect_time": 1703187862,
        "data_format": "text",
        "request_id": 123451234512345,
        "status": "downloading"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "2023242526272829300000000000001111"
    }
}
```
Was this document helpful?