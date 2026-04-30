Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# Direct Post
## Overview
To directly post a video to users' TikTok accounts, you must invoke the Content Posting API - Direct Post endpoint to perform the following actions:
- Query creator information to render the UI elements to be displayed on the Export page of your app.
- [Learn more about the UX guidelines here.](https://developers.tiktok.com/doc/content-sharing-guidelines#)
- [Learn more about the creator_info/query API here](https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info).
- Initialize the post request.
- Export the video to TikTok servers.
This guide contains comprehensive information about the API, including the endpoint, request schema, and response schema.
[[**Note:** All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restriction on content visibility, your API client must undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
## Initialize the posting request
[Once you have requested creator info](https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info), and users have provided the necessary metadata for their posts and given explicit consent to send their video to TikTok, the next step is to initialize the posting request.

| HTTP URL | /v2/post/publish/video/init/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.publish |

### Request
**Note**: Each user access_token is limited to 6 requests per minute.
#### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Authorization | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer {$UserAccessToken} | true |
| Content-Type | The content format of the body of this HTTP request. | application/json; charset=UTF-8 | true |

#### Body

| **Field Name** | **Nested Field Name** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- | --- |
| post_info | privacy_level | string | Enum of: `PUBLIC_TO_EVERYONE` `MUTUAL_FOLLOW_FRIENDS` `FOLLOWER_OF_CREATOR` `SELF_ONLY` The provided value must match one of the `privacy_level_options`returned in the `/creator_info/query/`API. | true |
| title | string | The video caption. Hashtags (#) and mentions (@) will be matched, or deliminated by spaces or new lines. The maximum length is 2200 in UTF-16 runes. If not specified, the ticket post will not have any captions. | false |
| disable_duet | bool | If set to `true`, other TikTok users will not be allowed to make Duets using this post. The TikTok server disables Duets for private accounts and those who set the Duet permission to "No one" in their privacy setting. |
| disable_stitch | bool | If set to `true`, other TikTok users will not be allowed to make Stitches using this post. The TikTok server disables Stitches for private accounts and those who set the Stitch permission to "No one" in their privacy setting. |
| disable_comment | bool | If set to `true`, other TikTok users will not be allowed to make comments on this post. The TikTok server disables comments for users who set the Comments permission to "No one" in their privacy setting. |
| video_cover_timestamp_ms | int32 | Specifies which frame (measured in milli-seconds) will be used as the video cover. If not set, or the specified value is invalid, the cover is set to the first frame of the uploaded video. |
| brand_content_toggle | bool | Set to `true`if the video is a paid partnership to promote a third-party business. | true |
| brand_organic_toggle | bool | Set to `true`if this video is promoting the creator's own business. |
| is_aigc | bool | Set to `true`if the video is AI generated content. If set, the video will be labelled with `Creator labeled as AI-generated`tag in video's description. | false |
| source_info | source | string | [Choose from: `PULL_FROM_URL` `FILE_UPLOAD` Learn about the limitations for these file transmission methods](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). | true |
| video_url | string | A public-accessible URL from which the TikTok server will pull to retrieve the video resource. | true for `PULL_FROM_URL` |
| video_size | int64 | The size of the to-be-uploaded video file in bytes. | true for`FILE_UPLOAD` |
| chunk_size | int64 | The size of the chunk in bytes. |
| total_chunk_count | int64 | The total number of chunks. |

#### Example
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data-raw '{
  "post_info": {
    "title": "this will be a funny #cat video on your @tiktok #fyp",
    "privacy_level": "MUTUAL_FOLLOW_FRIENDS",
    "disable_duet": false,
    "disable_comment": true,
    "disable_stitch": false,
    "video_cover_timestamp_ms": 1000
  },
  "source_info": {
      "source": "FILE_UPLOAD",
      "video_size": 50000123,
      "chunk_size":  10000000,
      "total_chunk_count": 5
  }
}'
```
### Response

| **Field Name** | **Nested Field** | **Type** | **Description** |
| --- | --- | --- | --- |
| data | publish_id | string | An identifier to track the posting action, which you can use to check the status. The maximum length of this field is 64. |
| upload_url | string | The URL provided by TikTok where the video file can be uploaded. The maximum length of this field is 256. This field is only for `source=FILE_UPLOAD`. |
| error | code | string | [You can decide whether the request is successful based on the error code. Any code other than `ok`indicates the request did not succeed. Learn more about error codes](#Mb9Via). |
| message | string | A human readable description of the error. |
| logid | string | A unique identifier for the execution of this request. |

**Note**: The `upload_url` is valid for one hour after issuance. The upload must be completed in this time range.
#### Example
```
200 OK
{
    "data": {
        "publish_id": "v_pub_file~v2-1.123456789",
        "upload_url": "https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123"    
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
#### Error codes

| **HTTP Status** | **error.code** | **Description** |
| --- | --- | --- |
| 400 | invalid_param | Check error message for details. |
| 403 | spam_risk_too_many_posts | The daily post cap from the API is reached for the current user. |
| spam_risk_user_banned_from_posting | The user is banned from making new posts. |
| reached_active_user_cap | The daily quota for active publishing users from your client is reached. |
| unaudited_client_can_only_post_to_private_accounts | Unaudited clients can only post to a private account. The publish attempt will be blocked when calling `/publish/video/init/`. |
| url_ownership_unverified | [To use `PULL_FROM_URL`as the video transfer method, the developer must verify the ownership of the URL prefix or domain. Refer to this doc](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#) for more details. |
| privacy_level_option_mismatch | `privacy_level`is not specified or not among the options from the `privacy_level_options`returned in /publish/creator_info/query/ API. _All clients are required to correctly display the creator account's privacy level options and honor the users' choice. Occurances of this error for product-use applications suggest violations to TikTok's product-use guidance._ |
| 401 | access_token_invalid | The access_token is invalid or has expired. |
| scope_not_authorized | The access_token does not bear user's grant on `video.publish`scope |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit. |
| 5xx |  | TikTok server or network error. Try again later. |

## Send Video to TikTok Servers
**Note**: If you used the `source=PULL_FROM_URL` to initialize the video export, you can skip this part. The TikTok server will handle the video uploading process for you.
[Once you have initialized the video export and received an `upload_url`, you must send the video file to TikTok for processing. We support many video formats and provide chunking for larger files. Learn more about media transmission](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#).

| HTTP URL | Returned in `upload_url` |
| --- | --- |
| HTTP Method | PUT |

**Note**: Use the entire URL returned as the `upload_url` , including the returned query parameters.
#### Request
[**Note**: This document provides schemas for the API request and response. Learn more about media upload formats and advanced capabilities](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#).
#### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Content-Type | The content format of the body of this HTTP request. | Select from: video/mp4 video/quicktime video/webm | true |
| Content-Length | Byte size of this chunk. | {BYTE_SIZE_OF_THIS_CHUNK} | true |
| Content-Range | The metadata describing the portion of the overall file contained in this chunk. | bytes {FIRST_BYTE}-{LAST_BYTE}/{TOTAL_BYTE_LENGTH} | true |

#### Body
The binary file data.
#### Example
```
curl --location --request PUT 'https://open-upload.tiktokapis.com/upload/?upload_id=67890&upload_token=Xza123' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Length: 30567100'\
--header 'Content-Type: video/mp4' \
--data '@/path/to/file/example.mp4'
```
Was this document helpful?