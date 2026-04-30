Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# Upload
## Overview
To upload a video without posting it, you must invoke the Content Posting API to do the following:
- Initialize the video upload.
- Send the video to TikTok servers (not needed if transfer method is `PULL_FROM_URL`).
This guide provides the API details including the endpoint, request, and response schema.
You should inform users that they must click on inbox notifications to continue the editing flow in TikTok and complete the post.
## Initialize Video Upload
To upload a video to a TikTok user's account, the first step is to initialize the upload.

| HTTP URL | /v2/post/publish/inbox/video/init/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.upload |

### Request
**Restriction**: Each user access_token is limited to 6 requests per minute.
#### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Authorization | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer {$UserAccessToken} | true |
| Content-Type | The content format of the body of this HTTP request. | application/json; charset=UTF-8 | true |

#### Body

| **Field Name** | **Nested Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- | --- |
| source_info | source | string | The mechanism by which you will provide the video. You can choose from `FILE_UPLOAD`and `PULL_FROM_URL`. | true |
| video_size | int64 | The size of the video to be uploaded in bytes. | true for `FILE_UPLOAD` |
| chunk_size | int64 | The size of the chunk in bytes. | true for `FILE_UPLOAD` |
| total_chunk_count | int64 | The total number of chunks. | true for `FILE_UPLOAD` |
| video_url | string | [The URL of the video to be uploaded. The domain or URL prefix of the video_url should already be verified. Learn more about verifying the URL prefix](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). | true for `PULL_FROM_URL` |

#### Examples
Example with `source=FILE_UPLOAD`:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8'
--data '{
    "source_info": {
        "source": "FILE_UPLOAD",
        "video_size": exampleVideoSize,
        "chunk_size" : exampleChunkSize,
        "total_chunk_count": exampleTotalChunkCount
    }
}'
```
Example with`source=PULL_FROM_URL`:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data '{
    "source_info": {
        "source": "PULL_FROM_URL",
        "video_url": "https://example.verified.domain.com/example_video.mp4"
    }
}'
```
### Response

| **Field Name** | **Nested Field** | **Type** | **Description** |
| --- | --- | --- | --- |
| data | publish_id | string | An identifier to track the posting action, which you can use to check the status. The maximum length of this field is 64. |
| upload_url | string | The URL provided by TikTok where the video file can be uploaded. The maximum length of this field is 256. This field is only for `source=FILE_UPLOAD`. |
| error | code | string | [You can decide whether the request is successful based on the error code. Any code other than `ok`indicates the request did not succeed. Learn more about error codes](#_error_codes). |
| message | string | A human readable description of the error. |
| logid | string | A unique identifier for the execution of this request. |

**Note**: The `upload_url` is valid for one hour after issuance. The upload must be completed in this time range.
#### Example
```
200 OK
{
    "data": {
        "publish_id": "v_inbox_file~v2.123456789",
        "upload_url": "https://open-upload.tiktokapis.com/video/?upload_id=12345&upload_token=Xza123"    
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
#### Error codes

| **HTTP status code** | **Error code** | **Descrption** |
| --- | --- | --- |
| 400 | invalid_param | Check error message for details. |
| 403 | spam_risk_too_many_pending_share | The daily upload cap from the API is reached for the current user. To reduce spamming, TikTok limits the number of videos that can be uploaded via API that are not pending approval and posting by the creator. There may be at most 5 pending shares within any 24-hour period. |
| spam_risk_user_banned_from_posting | The user is banned from making new posts. |
| url_ownership_unverified | [To use `PULL_FROM_URL`as the video transfer method, the developer must verify the ownership of the URL prefix or domain. Refer to this doc](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#) for more details. |
| 401 | access_token_invalid | The access_token for the TikTok user is invalid or has expired. |
| scope_not_authorized | The access_token does not bear user's grant on `video.upload`scope. |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit. |
| 5xx |  | TikTok server or network error. Try again later. |

## Send Video to TikTok Servers
**Note**: If you used the `source=PULL_FROM_URL` to initialize the video upload, you can skip this part. The TikTok server will handle the video uploading process for you.
[Once you have initialized the video upload and received an `upload_url`, you must send the video file to TikTok for processing. Many video formats are supported and chunking is provided for larger files. Learn more about media transmission](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide).

| HTTP URL | Returned in `upload_url` |
| --- | --- |
| HTTP Method | PUT |

**Important**: Use the entire URL returned as the `upload_url` including the returned query parameters.
### Request
#### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Content-Type | The content format of the body of this HTTP request. | Select from: video/mp4 video/quicktime video/webm | true |
| Content-Length | Byte size of this chunk. | {BYTE_SIZE_OF_THIS_CHUNK} | true |
| Content-Range | Metadata describing the portion of the overall file contained in this chunk. | bytes {FIRST_BYTE}-{LAST_BYTE}/{TOTAL_BYTE_LENGTH} | true |

#### Body
The binary file data.
#### Example
```
curl --location --request PUT 'https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Length: 30567100'\
--header 'Content-Type: video/mp4' \
--data '@/path/to/file/example.mp4'
```
Was this document helpful?