Docs
# Create a batch compliance task
## Request to create a batch compliance task

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/validation_task/create/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters
Need form-data in Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| file_data | File | A text file that contains video ids or comment ids. The max IDs users can submit is 10,000 per time. |  | Yes |
| category | Text | Category that the file contains. Video or comment. | video | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task/create/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefg' \
--form 'file_data=@"/****/****/****/test file.txt"' \
--form 'category="video"'
```
## Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | struct | The task id associated with the task. |
| error | ErrorStructV2 | Error object |

### Example
```
{
    "data": {
        "task_id": 12345678910987654321
    },
    "error": {
        "code": "ok",
        "http_status_code": 200,
        "log_id": "987654321",
        "message": "ok."
    }
}
```
# Get a batch compliance task status
## Request to get a batch compliance task status

| **HTTP URL** | https://open.tiktokapis.com/v2/research/validation_task_status/get/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Task id created by the create batch compliance api | 12345678910 | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task_status/get/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 1234567891011' \
--data '{
    "task_id":12345678910
}'
```
## Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | struct | Current task status. Completed/Processing/Failed |
| error | ErrorStructV2 | Error object |

### Example
```
{
    "data": {
        "task_status": "Completed"
    },
    "error": {
        "code": "ok",
        "http_status_code": 200,
        "log_id": "12345678910",
        "message": "ok."
    }
}
```
# Download a completed batch compliance task
## Request to download a batch compliance task

| **HTTP URL** | https://open.tiktokapis.com/v2/research/validation_task/download/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Task id created by the create batch compliance api | 12345678910 | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task_status/get/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 1234567891011' \
--data '{
    "task_id":12345678910
}'
```
## Response
Click Send and Download, a text file with valid IDs will be download automatically.
Was this document helpful?