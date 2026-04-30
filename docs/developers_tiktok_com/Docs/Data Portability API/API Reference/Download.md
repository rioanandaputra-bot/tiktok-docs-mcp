Docs
# Download
Use POST request to download the requested data. The response is streamed as an HTTP data zip file.

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/download/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API. | 123123123123 | Yes |

## Response
The response is streamed as HTTP zip file, and must be converted to a zip file to get the correct data.
This Python script can be used to POST a successful request and get data in a readable format
```
import requests
import json

url = "https://open.tiktokapis.com/v2/user/data/download/"

# The request_id returned from the `Add Data Request` API
request_id = <REQUEST ID>

# Request JSON structure
payload = json.dumps({
  "request_id": request_id
})

# Necessary headers
# Authorization must have the token obtained from the /v2/oauth/token/ API
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'AUTHORIZATION_TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

zip_file_path = f'./{request_id}.zip'

# Open the zip file in write-binary mode
with open(zip_file_path, 'wb') as zip_file:
    # Write the content of the response to the zip file
    zip_file.write(response.content)
```
### Success Example
`.zip` must be added to streamed data to make it a zip file. The data itself, viewed as unicode will not be human-readable.
### Failure Example
In case a Download Request is unsuccessful, the following response will be returned
```
{
    "data": {},
    "error": {
        "code": "invalid_params",
        "http_status_code": 400,
        "log_id": "20240125230933D4C4606E87F0A61BE502",
        "message": "Incorrect `request_id`. Please validate the request."
    }
}
```
Was this document helpful?