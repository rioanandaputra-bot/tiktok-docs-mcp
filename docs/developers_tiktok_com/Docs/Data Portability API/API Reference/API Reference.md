Docs
# Add Data Request
Use POST request to create a data download request.

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/add/ |
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
| fields | string | The requested fields: request_id | request_id | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| data_format | string | Format in which the individual data files will be returned. Valid values are: text json | "text" | Yes |
| category_selection_list | list<string> | Type of data that is to be returned. See <Data Categories>. Valid values are: all_data video profile activity direct_message | ["profile", "activity"] | Yes |

#### Scopes required for categories

| **Data Categories** | **Required Scopes** |
| --- | --- |
| activity | portability.activity.single, portability.activity.ongoing |
| video, profile | portability.postsandprofile.single, portability.postsandprofile.ongoing |
| direct_message | portability.directmessages.single, portability.directmessages.ongoing |
| all_data, activity, video, profile, direct_message | portability.all.single, portability.all.ongoing |

Notes:
- If "all_data" is sent as a parameter in `category_selection_list`, it will take precedence over other categories.
- For any `portability.*.single` scope, **Add Data Request** can only be called once to create a new request.
- For cases where multiple `portability.*.single` scopes are authorized by the user:
Example:
If scopes `portability.all.single` and `portability.activity.single` are authorized by the user and a request with `"category_selection_list" : ["activity", "video"]` is made.
The only scope consumed will be `portability.all.single`, as it has access to all the categories.
After making the request, the current access token will contain the scope `portability.activity.single` and a new request for the category `activity` can be made after the current request is fulfilled without reauthorizing the access token from the user.
### Request Example
```
curl --location 'https://open.tiktokapis.com/v2/user/data/add/?fields=request_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemp123.e1' \
--data '{
    "data_format": "text",
    "category_selection_list": ["profile","direct_message"]
}'
```
## Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | AddUserDataResponseData | See the response example below |
| error | ErrorStructV2 | See the response example below |

### AddUserDataResponseData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This will be a required query parameter to get request status, cancel request, and download the data. | 123451234512345 |

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
        "request_id": 123451234512345
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "1010xyz10101asdf1010101010100a12abc24"
    }
}
```
Was this document helpful?