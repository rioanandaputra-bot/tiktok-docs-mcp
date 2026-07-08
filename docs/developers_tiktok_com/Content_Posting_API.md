# Content Posting API

> Consolidated from 8 source files.



---
## SOURCE: Content Posting API/Content Posting API.md

Docs
[**Tip**: You can enable email notifications](https://developers.tiktok.com/settings/#notification-setting) to get our latest product updates.
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post#)!
# Get Started
This guide demonstrates how to use the Content Posting API to post content directly to TikTok.
## Prerequisites
To successfully complete this tutorial, you will need the following:
- A valid video if you want to post videos:
- [Ensure you have a video file in one of the supported formats](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#video_restrictions), such as MP4 + H.264, stored on your local machine.
- [Alternatively, you can provide the URL of a video from your verified domain or URL prefix. Learn how to verify your domain or URL prefix](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url).
- [Learn more about video restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#video_restrictions).
- A valid photo if you want to post photos:
- [You must provide a URL of a photo from your verified domain or URL prefix. Learn how to verify your domain or URL prefix](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url).
- [Learn more about photo restrictions.](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#image_restrictions)
- [A registered app](https://developers.tiktok.com/doc/getting-started-create-an-app) on the TikTok for Developers website.
- Add the Content Posting API product to your app as shown below.
- To enable the direct posting of content on authorized users' profiles, you need to enable the Direct Post configuration for the Content Posting API in your app, as shown below.
- [Get approval and authorization of the `video.publish` scope. Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
- Your app must be approved for the `video.publish` scope.
- The target TikTok user must have authorized your app for the `video.publish` scope.
- [The access token and open ID of the TikTok user who authorized your app. Learn how to obtain the access token and open ID](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens).
[[**Note:** All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
## Post directly to TikTok
This section demonstrates how to successfully post a video or photo to a creator's TikTok account.
### Query Creator Info
[To initiate a direct post to a creator's account, you must first use the Query Creator Info endpoint to get the target creator's latest information. For more information about why creator information is necessary, refer to these UX guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines#).
Request:
```
curl --location --request POST 'https://open.tiktokapis.com/v2/post/publish/creator_info/query/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8'
```
Response:
```
200 OK

{
   "data":{
      "creator_avatar_url": "https://lf16-tt4d.tiktokcdn.com/obj/tiktok-open-platform/8d5740ac3844be417beeacd0df75aef1",
      "creator_username": "tiktok",
      "creator_nickname": "TikTok Official",
      "privacy_level_options": ["PUBLIC_TO_EVERYONE", "MUTUAL_FOLLOW_FRIENDS", "SELF_ONLY"] 
      "comment_disabled": false,
      "duet_disabled": false,
      "stitch_disabled": true,
      "max_video_post_duration_sec": 300
   },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
```
### Post a video
[To initiate video upload on TikTok's server, you must invoke the Direct Post Video](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post) endpoint. You have the following two options:
- If you have the video file locally, set the source parameter to `FILE_UPLOAD` in your request.
- If the video is hosted on a URL, set the source parameter to `PULL_FROM_URL`.
#### Example
Example using `source=FILE_UPLOAD`:
Request:
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
Response:
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
Example using `source=PULL_FROM_URL`:
Request:
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
      "source": "PULL_FROM_URL",
      "video_url": "https://example.verified.domain.com/example_video.mp4"
  }
}'
```
Response:
```
200 OK

{
    "data": {
        "publish_id": "v_pub_url~v2.123456789"  
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F4"
     }
}
```
If you are using `source=FILE_UPLOAD`
- Extract the `upload_url` and `publish_id` from the response data.
- [Send the video](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post#)from your local filesystem to the extracted `upload_url` using a PUT request. The video processing will occur asynchronously once the upload is complete.
```
curl --location --request PUT 'https://open-upload.tiktokapis.com/upload/?upload_id=67890&upload_token=Xza123' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Type: video/mp4' \
--data '@/path/to/file/example.mp4'
```
[With the `publish_id` returned earlier, check for status updates using the Get Post Status](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status)endpoint.
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/status/fetch/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data '{
    "publish_id": "v_pub_url~v2.123456789"
}'
```
### Post photos
[To initiate photo upload on TikTok's server, you must invoke the Content Posting API endpoint.](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)
Note:
There are differences between the photo post endpoint and the existing video post endpoint.
- Use /v2/post/publish/content/init/ to upload photos instead of /v2/post/publish/inbox/video/init/
- The `post_mode` and `media_type` is required in request.body
#### Example
Request:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photo on your @tiktok #fyp",
        "disable_comment": true,
        "privacy_level": "PUBLIC_TO_EVERYONE",
        "auto_add_music": true
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "DIRECT_POST",
    "media_type": "PHOTO"
}'
```
Response:
```
200 OK

{
    "data": {
        "publish_id": "p_pub_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
Was this document helpful?


---
## SOURCE: Content Posting API/Get Started - Upload.md

Docs
[**Tip**: You can enable email notifications](https://developers.tiktok.com/settings/#notification-setting) to get our latest product updates.
[**New: **Content Posting API now supports sending photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post#upload_)!
# Get Started
This guide shows you how to use the Content Posting API to upload content to TikTok.
## Prerequisites
To successfully complete this tutorial, you will need the following:
- A valid video if you want to upload videos:
- [Ensure you have a video file in one of the supported formats](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#video_restrictions), such as MP4 + H.264, stored on your local machine.
- [Alternatively, you can provide a URL of a video from your verified domain or URL prefix. Learn how to verify your domain or URL prefix](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url).
- [Learn more about video restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#video_restrictions).
- A valid photo if you want to upload photos:
- [You need to provide a URL of a photo from your verified domain or URL prefix. Learn how to verify your domain or URL prefix](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url).
- [Learn more about photo restrictions.](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#image_restrictions)
- [A registered app](https://developers.tiktok.com/doc/getting-started-create-an-app) on the TikTok for Developers website.
- Add the content posting API product to your app as shown below.
- [Get approval and authorization of the `video.upload` scope. Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
- Your app must be approved for the `video.upload` scope.
- The target TikTok user must have authorized your app for the `video.upload` scope.
- [The access token and open ID of the TikTok user who authorized your app. Learn how to obtain the access token and open ID](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens).
## Upload draft to TikTok
This section demonstrates how to successfully upload videos or photos to TikTok for the user to review and post.
You should inform users that they must click on inbox notifications to continue the editing flow in TikTok and complete the post.

| _User notified of video upload_ | _User reviews and posts video_ |
| --- | --- |

### Upload a video
[To initiate video upload on TikTok's servers, you must invoke the Content Posting API - Video Upload](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video) endpoint. You have the following two options:
- If you have the video file locally, set the source parameter to `FILE_UPLOAD` in your request.
- if the video is hosted on a URL, set the source parameter to `PULL_FROM_URL`.
#### Example
Example using `source=FILE_UPLOAD`:
Request:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data '{
    "source_info": {
        "source": "FILE_UPLOAD",
        "video_size": exampleVideoSize,
        "chunk_size" : exampleVideoSize,
        "total_chunk_count": 1
    }
}'
```
Response:
```
200 OK

{
    "data": {
        "publish_id": "v_inbox_file~v2.123456789",
        "upload_url": "https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123"    
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
Example using `source=PULL_FROM_URL`:
Request:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data '{
    "source_info": {
        "source": "PULL_FROM_URL",
        "video_url": "https://example.verified.domain.com/example_video.mp4",
    }
}'
```
Response:
```
200 OK

{
    "data": {
        "publish_id": "v_inbox_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F4"
     }
}
```
If you are using `source=FILE_UPLOAD`:
- Extract the `upload_url` and `publish_id` from the response data.
- [Send the video](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video#) from your local filesystem to the extracted `upload_url` using a PUT request. The video processing will occur asynchronously once the upload is complete.
```
curl --location --request PUT 'https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Type: video/mp4' \
--data '@/path/to/file/example.mp4'
```
[With the `publish_id` returned earlier, check for status updates using the Get Post Status](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status) endpoint.
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/status/fetch/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8' \
--data '{
    "publish_id": "v_inbox_file~v2.123456789"
}'
```
### Upload photos
[To initiate photo upload on TikTok's server, you must invoke the Content Posting API endpoint.](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)
Note:
There are differences between the photo post endpoint and the existing video post endpoint.
- Use /v2/post/publish/content/init/ to upload photos instead of /v2/post/publish/inbox/video/init/
- The `post_mode` and `media_type` are required parameters in request.body
- There are additional parameters supported, such as title and description.
#### Example
Request:
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photo on your @tiktok #fyp"
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "MEDIA_UPLOAD",
    "media_type": "PHOTO"
}'
```
Response:
```
200 OK

{
    "data": {
        "publish_id": "p_pub_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
Was this document helpful?


---
## SOURCE: Content Posting API/Media Transfer Guide.md

Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# Media Transfer Guide
This guide explains the process of transferring media files to TikTok servers when using the Content Posting API.
## File upload
[Using this method, you can transfer your media to TikTok using HTTP. Upon initializing your video upload](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video#initialize_video_upload) with `source=FILE_UPLOAD`, an `upload_url` will be returned. You must send the media binary to this URL.
[[To learn how to send videos to TikTok servers and for details on the HTTP request (endpoint, request and response schema, and headers), see the API reference for the Upload Video endpoint](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video) or the Direct Post endpoint](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post).
### Work with chunks
#### Chunk restrictions
- The value of `total_chunk_count` should be equal to `video_size` divided by `chunk_size`, rounded down to the nearest integer.
- Each chunk must be at least 5 MB but no greater than 64 MB, except for the final chunk, which can be greater than `chunk_size` (up to 128 MB) to accommodate any trailing bytes.
- Videos with a total size less than 5 MB must be uploaded as a whole, with `chunk_size` equal to the entire video's byte size. Videos with a total size greater than 64 MB must be uploaded in multiple chunks.
- There must be a minimum of 1 chunk and a maximum of 1000 chunks.
- File chunks must be uploaded sequentially.
#### Media transfer HTTP schema
```
PUT {UPLOAD_URL} HTTP /1.1
Content-Type: {MIME_TYPE}
Content-Length: {BYTE_SIZE_OF_THIS_CHUNK}
Content-Range: bytes {FIRST_BYTE}-{LAST_BYTE}/{TOTAL_BYTE_LENGTH}

BINARY_FILE_DATA
```
#### Examples
##### Chunk upload
In this example, there is a file with a size of 50,000,123 bytes. The chunk size is specified to be 10,000,000 bytes. The trailing 123 bytes is merged into the 10,000,000-byte chunk to meet the restriction that each chunk must be greater than 5 MB.
Example _UPLOAD_URL=_`https://upload.us.tiktokapis.com/video/?upload_id=67890&upload_token=chunkexample` will be shared across all chunks.

| **Variable** | **1st Request** | **2nd Request** | **3rd Request** | **4th Request** | **5th Request** |
| --- | --- | --- | --- | --- | --- |
| _MIME_TYPE_ | video/mp4 | video/mp4 | video/mp4 | video/mp4 | video/mp4 |
| _TOTAL_BYTE_LENGTH_ | 50,000,123 | 50,000,123 | 50,000,123 | 50,000,123 | 50,000,123 |
| _BYTE_SIZE_OF_THIS_CHUNK_ | 10,000,000 | 10,000,000 | 10,000,000 | 10,000,000 | 10,000,123 |
| _FIRST_BYTE_ | 0 | 10,000,000 | 20,000,000 | 30,000,000 | 40,000,000 |
| _LAST_BYTE_ | 9,999,999 | 19,999,999 | 29,999,999 | 39,999,999 | 50,000,122 |
| _BINARY_FILE_DATA_ | BINARY1 | BINARY2 | BINARY3 | BINARY4 | BINARY5 |
| response HTTP status | 206 | 206 | 206 | 206 | 201 |

[The following is the corresponding `source_info` for initializing video upload](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video#initialize_video_upload).
```
"source_info": {
      "source": "FILE_UPLOAD",
      "video_size": 50000123
      "chunk_size":  10000000
      "total_chunk_count": 5
  }
```
##### Whole upload
In this example, the media file is 4 MB, which must be uploaded as a whole in one request.

| **Variable** | **Single Request** |
| --- | --- |
| _UPLOAD_URL_ | https://open-upload.tiktokapis.com/video/?upload_id=123&upload_token=wholeexample |
| _MIME_TYPE_ | video/mp4 |
| _TOTAL_BYTE_LENGTH_ | 4,194,304 |
| _BYTE_SIZE_OF_THIS_CHUNK_ | 4,194,304 |
| _FIRST_BYTE_ | 0 |
| _LAST_BYTE_ | 4,194,303 |
| _BINARY_FILE_DATA_ | BINARY1 |
| response status code | 201 |

[The following is the corresponding `source_info` for initializing video upload](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video#initialize_video_upload).
```
"source_info": {
      "source": "FILE_UPLOAD",
      "video_size": 4194304
      "chunk_size":  4194304
      "total_chunk_count": 1
  }
```
#### Response

| **HTTP Code** | **Status** | **Description** |
| --- | --- | --- |
| 201 | Created | All parts are uploaded. TikTok will start the posting process. |
| 206 | PartialContent | The current chunk has been successfully processed. There are additional chunks yet to be uploaded. |
| 400 | BadRequest | Malformated request headers, or _BYTE_SIZE_OF_THIS_CHUNK_****does not reflect the true byte size of the binary in the request body. |
| 403 | Forbidden | The `upload_url`has expired. |
| 404 | NotFound | TikTok cannot find a valid upload task given the `upload_url`. |
| 416 | RequestedRangeNotSatisfiable | `Content-Range`does not reflect the actual upload progress. |
| 5xx | InternalServerError | Gateway connection error or TikTok Internal error. You should retry submitting this chunk. |

The response header includes the following key-value pair indicating the number of bytes uploaded:
`Content-Range:bytes 0-{UPLOADED_BYTES}/{TOTAL_BYTE_LENGTH}`.
## Pull from URL
[By initializing your content post using /init endpoints with `source=PULL_FROM_URL`, the TikTok server starts to download the media resource using the URL you provide. Learn more about getting post status.](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status)
TikTok server's ingress bandwidth for file downloads can reach 100 Mbps.
### Prerequisites
- [Ensure that the media URL you provided belongs to a path that you own. To confirm ownership, log into the TikTok for Developers website](https://developers.tiktok.com/) and add your Domain or URL Prefix property to your application in the URL properties widget as shown below. You must have manage or write access to the property.
- The media URL must use "https" and should not redirect to another URL.
- The URL must remain accessible for the entire duration of the download process, which times out one hour after the download task is initiated.
[**Note: **To conveniently test the Pull from URL feature, you can try this](https://sf16-va.tiktokcdn.com/obj/eden-va2/uvpapzpbxjH-aulauvJ-WV[[/ljhwZthlaukjlkulzlp/3min.mp4) URL without any verification.
### Ownership verification rules
#### Domain
##### Definition
A domain can be a base domain (for example, example.com) or a subdomain (for example, subdomain.example.com).
##### Verification
To verify domain ownership, it is recommended that you add a signature string to the domain's DNS records.
Once the ownership of a domain is verified, all paths under that domain or its subdomains are considered owned by the developer application.
For example, if you have verified the domain `static.example.com`, then URLs like `https://video.static.example.com/tiktok/example.mp4` are considered verified, while URLs like `https://example.com/videos/example.mp4` are still considered unverified.
#### URL Prefix
##### Definition
A URL prefix consists of: https:// + host + path + /.
The host must be a domain and should not be an IP address.
Redirections are not followed. URLs that return HTTP 3xx are considered invalid.
##### Verification
Once a URL prefix's ownership is verified, all URLs with the exact prefix are considered owned by the developer application.
For example, if you have already verified the domain `https://example.com/videos/user/`, then URLs like `https://example.com/videos/user/123/example.mp4` are considered verified, while URLs like `https://example.com/videos/2023/user/123/example.mp4` are still considered unverified.
## Cancel ongoing pull from URL tasks
The API can cancel downloads for both Direct Post and Content Upload endpoints on a _best-effort_ basis.
While it is possible to cancel ongoing slow downloads, it is not feasible to cancel downloads that are nearing completion or already in the file processing state.
## Request
```
POST /v2/post/publish/cancel/ HTTP /1.1
Host: open.tiktokapis.com
Authorization: Bearer {{AccessToken}}
Content-Type: application/json; charset=UTF-8

{
    "publish_id": {PUBLISH_ID}
}
```
## Response
```
200 OK

{
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
**response.error.code specification**

| **HTTP Status** | **error.code** | **Description** |
| --- | --- | --- |
| 200 | ok | The request was successful |
| 400 | invalid_publish_id | The `publish_id`does not exist |
| token_not_authorized_for_specified_publish_id | The `access_token`does not have authorization to cancel the publish |
| publish_not_cancellable | The task associated with this `publish_id`is already in a final state and can't be cancelled |
| 403 | url_ownership_unverified | To use `PULL_FROM_URL`as the media transfer method, developer must verify the ownership of the URL prefix or domain |
| 401 | access_token_invalid | The access_token is invalid or has expired |
| scope_not_authorized | The access_token does not bear user's grant on `video.upload`or `video.publish` |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit |
| 5xx | internal_error | TikTok server or network error. Try again later. |

## Video restrictions

| Supported media formats | MP4 (recommended) WebM MOV |
| --- | --- |
| Supported codecs | H.264 (recommended) H.265 VP8 VP9 |
| Framerate restrictions | Minimum of 23 FPS Maximum of 60 FPS |
| Picture size restrictions | Minimum of 360 pixels for both height and width Maximum of 4096 pixels for both height and width |
| Duration restrictions | [All TikTok creators can post 3-minute videos, while some have access to post 5-minute or 10-minute videos. The longest video a developer can send via the initialize Upload Video](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video) endpoint is 10 minutes. TikTok users may trim developer-sent videos inside the TikTok app to fit their accounts' actual maximum publish durations. |
| Size restrictions | Maximum of 4GB |

## Image restrictions

| Supported media formats | WebP JPEG |
| --- | --- |
| Picture size restrictions | Maximum 1080p |
| Size restrictions | Maximum of 20MB for each image |

Was this document helpful?


---
## SOURCE: Content Posting API/API Reference/API Reference.md

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


---
## SOURCE: Content Posting API/API Reference/Get Post Status.md

Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# Get Post Status
For content uploaded with the Content Posting API, two mechanisms are provided for developers to check the status of the post by the TikTok user:
- Fetch Status endpoint: An API endpoint for polling the status of the post.
- Content Posting webhooks: Events that notify your registered endpoint of the final outcome of the post.
## Content Status Overview
Content uploaded to TikTok undergoes several stages before it is published. This process can be visualized with the following diagram:
- Direct Post:
- Content Upload
The time taken in any given stage can vary by use cases and a time limit is not guaranteed for the content posting process. The following are some helpful details:
- The average processing times for content processing vary by content size:
- 512 MB: Less than half a minute
- 1 GB: About one minute
- 4 GB: More than two minutes
- If the post was created for **public** viewership, it must undergo TikTok's moderation process. Based on TikTok's policies, developers are not provided with the `post_id` until this process is complete.
- Moderation usually finishes within one minute.
- In some cases, moderation may take a few hours.
## Fetch Status endpoint

| HTTP URL | /v2/post/publish/status/fetch/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.upload/video.publish |

### Request
**Note**: Each user access_token is limited to 30 requests per minute.
```
POST /v2/post/publish/status/fetch/ HTTP /1.1
Host: open.tiktokapis.com
Authorization: Bearer {{AccessToken}}
Content-Type: application/json; charset=UTF-8

{
    "publish_id": {PUBLISH_ID}
}
```
## Response
```
200 OK

{
    "data": {
        "status": "FAILED",
        "fail_reason": "picture_size_check_failed",
        "publicaly_available_post_id": [],
        "uploaded_bytes": 10000
    },
    
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
### Nested data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| status | string | [[The following are the available statuses: `PROCESSING_UPLOAD`: Only available for `FILE_UPLOAD`. Indicates that the upload is in process. `PROCESSING_DOWNLOAD`: Only available for `PULL_FROM_URL`. Indicates that the download from the URL is in process. `SEND_TO_USER_INBOX`: Only available when you choose to upload content](https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content). Indicates that a notification has been sent to creator's inbox to complete the draft post using TikTok's editing flow. `PUBLISH_COMPLETE`: For the Direct Post](https://developers.tiktok.com/doc/content-posting-api-get-started), it indicates that the content has been posted. For the Upload Content, it indicates that the user has clicked on the inbox notification and has successfully posted the media using TikTok editing flow. `FAILED`: Indicates that an error has occurred and the entire process has failed. |
| fail_reason | string | Refer to the fail_reason table to see whether the issue is with the developer, the TikTok creator, or TikTok APIs |
| publicaly_available_post_id | list<int64> | `post_id`is returned only if the post is published for public viewership and has been approved by the TikTok moderation process. Creators may use the uploaded content draft to create multiple pieces of content. |
| uploaded_bytes | int64 | The number of bytes uploaded (1-indexed) for `FILE_UPLOAD` |
| downloaded_bytes | int64 | The number of bytes downloaded (1-indexed) for `PULL_FROM_URL` |

### Nested error struct

| **HTTP Status** | **error.code** | **Description** |
| --- | --- | --- |
| 200 | ok | The request was successful |
| 400 | invalid_publish_id | The `publish_id`does not exist |
| 400 | token_not_authorized_for_specified_publish_id | The `access_token`does not have authorization to cancel the publish |
| 401 | access_token_invalid | The access_token is invalid or has expired |
| scope_not_authorized | The access_token does not bear user's grant on `video.upload`or `video.publish` |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit |
| 5xx | internal_error | TikTok server or network error. Try again later. |

# Content Posting webhooks
These events will be sent to your registered server when you have a webhook URL configured for your app in the TikTok for Developers website.

| **Event Name** | **Event Values** | **Description** |
| --- | --- | --- |
| post.publish.failed | publish_id reason publish_type | The publishing action is not successful. The failure reason is sent as an enum string. `publish_type`should be `INBOX_SHARE`when using Upload endpoint (for users to review, edit and post in TikTok once they click inbox notification). |
| post.publish.complete | publish_id publish_type | When uploading content, the event indicates that the TikTok user has created a post from the content you sent. It's possible for the user to make multiple posts from the content associated with one `publish_id`. |
| post.publish.inbox_delivered | publish_id publish_type | Indicates that a notification has been sent to the creator's inbox to complete the draft post using TikTok's editing flow. `publish_type`can only be `INBOX_SHARE`when using upload endpoints. |
| post.publish.publicly_available | publish_id post_id publish_type | This event is sent when a post associated with the `publish_id`has become publicly viewable on TikTok. Non-public posts will not trigger this event unless the user makes them public later. |
| post.publish.no_longer_publicaly_available | publish_id post_id publish_type | The event is sent when a post associated with the `publish_id`has ceased to be publicly viewable. |

# Fail reasons
The following is a list of `fail_reason` that may be returned by the HTTP endpoint or webhook events.

| **fail_reason ** | **Guidance** |
| --- | --- |
| file_format_check_failed | [[Unsupported media format. See Video Restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#) and Photo Restrictions.](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#image_restrictions) |
| duration_check_failed | [Video does not meet our duration restrictions. See Video Restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). |
| frame_rate_check_failed | [Unsupported frame rate. See Video Restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). |
| picture_size_check_failed | [Upsupported picture size. See Video Restrictions](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#) and Photo Restrictions. |
| internal | Some parts of the TikTok server may currently be unavailable. This is a retryable error. |
| video_pull_failed | The TikTok server encountered a connection error while downloading the specified video resource, or the download is terminated since it can not be completed within the one-hour timeout. Check if the supplied URL is publicly accessible or bandwidth-limited. If developers are certain that the URL is valid, a retry is recommended. |
| photo_pull_failed | The TikTok server encountered a connection error while downloading the specified photo resource, or the download is terminated since it can not be completed within the one-hour timeout. Check if the supplied URL is publicly accessible or bandwidth-limited. If developers are certain that the URL is valid, a retry is recommended. |
| publish_cancelled | Developers can cancel an ongoing download. After a successful cancellation, developers will receive a webhook containing this error reason. |
| auth_removed | This TikTok creator has removed the developer's access while the download/uploading is being processed, so the publishing effort must be terminated. Retry should not be done. |
| spam_risk_too_many_posts | This TikTok creator has created too many posts within the last 24 hours via OpenAPI. Try to post the videos from the TikTok Mobile App. |
| spam_risk_user_banned_from_posting | TikTok TnS team has banned the creator from making new posts. Retry should not be done. |
| spam_risk_text | TikTok TnS team determines that the description text has risky or spammy contents, so the publishing attempt is terminated. Retry should not be done. |
| spam_risk | TikTok TnS team determines the publishing request is risky, so the publishing attempt is terminated Retry should not be done. |

Was this document helpful?


---
## SOURCE: Content Posting API/API Reference/Photo.md

Docs
# Photo
## Overview
The `/v2/post/publish/content/init/` endpoint allows you to post directly or upload photos to TikTok.

| HTTP URL | /v2/post/publish/content/init/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.publish or video.upload |

To directly post photos to users' TikTok accounts, you must query creator information to render the UI elements to be displayed on the export page of your app before you call this Content Posting API.
- [Learn more about the UX guidelines.](https://developers.tiktok.com/doc/content-sharing-guidelines#)
- [Learn more about the creator_info/query API](https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info).
## Request
**Note**: Each user access_token is limited to six requests per minute.
### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Authorization | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/ | Bearer {$UserAccessToken} | true |
| Content-Type | The content format of the body of this HTTP request | application/json; charset=UTF-8 | true |

### Body

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| media_type | string | Currently only `PHOTO`is allowed | true |
| post_mode | string | Enum of: `DIRECT POST`: Directly post the content to TikTok user's account. `MEDIA_UPLOAD`: Upload content to TikTok for users to complete the post using TikTok's editing flow. Users will receive an inbox notification. | true |
| post_info | [Post Info Object](#eK35Sd) | The post information | true |
| source_info | [Source Info Object](#D9SdTz) | The media source information | true |

#### Post Info Object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| title | string | The post title. The maximum length for photo posts is 90 in UTF-16 runes. | false |
| description | string | The post description. The maximum length for photo posts is 4000 in UTF-16 runes. | false |
| privacy_level | string | Enum of: `PUBLIC_TO_EVERYONE` `MUTUAL_FOLLOW_FRIENDS` `FOLLOWER_OF_CREATOR` `SELF_ONLY` The provided value must match one of the `privacy_level_options`returned in the `/creator_info/query/`API. | Required for `DIRECT POST` |
| disable_comment | bool | Only works for post_mode = `DIRECT POST`. If set to `true`, other TikTok users will not be allowed to make comments on this post. | false |
| auto_add_music | bool | Only works for post_mode = `DIRECT POST`. If set to `true`, recommended music will be automatically added to photos, and users can later choose to change the post's music in TikTok if they prefer other music. | false |
| brand_content_toggle | bool | Only works for post_mode = `DIRECT POST`. Set to `true`if the content is a paid partnership to promote a third-party business. | true |
| brand_organic_toggle | bool | Only works for post_mode = `DIRECT POST`. Set to `true`if this content is promoting the creator's own business. | true |

#### Source Info Object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| source | string | Only `PULL_FROM_URL`is allowed | true |
| photo_images | list<string> | [An array containing up to 35 photo content URLs. The URLs must be publicly accessible and verified by your app. Learn more about pulling from URLs](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url). | true |
| photo_cover_index | int | Indicates the index (starting from 0) of the photo to be used as the cover | true |

### Example
#### Direct Post
**Note**: To use Direct Post, the target TikTok user must have authorized your app for the `video.publish` scope.
[[All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photomode on your @tiktok #fyp",
        "disable_comment": true,
        "privacy_level": "PUBLIC_TO_EVERYONE",
        "auto_add_music": true
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "DIRECT_POST",
    "media_type": "PHOTO"
}'
```
#### Upload
After uploading from your app, you should inform users that they must click on inbox notifications to continue the editing flow in TikTok and complete the post. Title and description parameters are now supported with sending photos.
**Note**: To use upload method, the target TikTok user must have authorized your app for the `video.upload` scope.
We now support sending title and description in this method and it will be reflected in the editing flow once user clicks on the inbox notification.
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photomode on your @tiktok #fyp"
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "MEDIA_UPLOAD",
    "media_type": "PHOTO"
}'
```
## Response

| **Field Name** | **Nested Field** | **Type** | **Description** |
| --- | --- | --- | --- |
| data | publish_id | string | An identifier to track the posting action, which you can use to check status. The maximum length of this field is 64. |
| error | code | string | [You can decide whether the request is successful based on the error code. Any code other than `ok`indicates the request did not succeed. Learn more about error codes](#DU14lm). |
| message | string | A human-readable description of the error |
| logid | string | A unique identifier for the execution of this request |

### Example
```
200 OK
{
    "data": {
        "publish_id": "p_pub_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
### Error codes

| **HTTP Status** | **error.code** | **Description** |
| --- | --- | --- |
| 400 | invalid_param | Check error message for details |
| app_version_check_failed | To use `MEDIA_UPLOAD`post_mode, users' TikTok APP version must not be less than 31.8 |
| 403 | spam_risk_too_many_posts | The daily post cap from API is reached for the current user |
| spam_risk_user_banned_from_posting | The user is banned from making new posts |
| spam_risk_too_many_pending_share | The daily upload cap from the API is reached for the current user. To reduce spamming, TikTok limits the number of videos that can be uploaded via API that are not pending approval and posting by the creator. There may be at most 5 pending shares within any 24-hour period. |
| reached_active_user_cap | The daily quota for active publishing users from your client is reached |
| unaudited_client_can_only_post_to_private_accounts | Unaudited clients can only post to private account. The publish attempt will be blocked when calling `/publish/content/init/`. |
| url_ownership_unverified | [To use `PULL_FROM_URL`as the content transfer method, developer must verify the ownership of the URL prefix or domain. Learn more about content transfer](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). |
| privacy_level_option_mismatch | `privacy_level`is either unspecified or not among the options from the `privacy_level_options`returned in /publish/creator_info/query/ API. All clients are required to correctly display the creator account's privacy level options and honor the users' choice. Occurances of this error for product-use applications suggest violations to TikTok's product-use guidance. |
| 401 | access_token_invalid | The access_token is invalid or has expired |
| scope_not_authorized | The access_token does not bear user's grant on `video.publish`or `video.upload`scope |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit |
| 5xx | internal_error | TikTok server or network error. Try again later. |

Was this document helpful?


---
## SOURCE: Content Posting API/API Reference/Query Creator Info.md

Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# Query Creator Info
## Overview
This API returns profile and permission information of the current user.
When rendering the Export to TikTok page, your app must invoke the API and use the latest creator information returned to display the account's available privacy level options and video/photo interaction settings.

| HTTP URL | /v2/post/publish/creator_info/query/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.publish |

## Request
**Note**: Each user access_token is limited to 20 requests per minute.
### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Authorization | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer {$UserAccessToken} | true |
| Content-Type | The content format of the body of this HTTP request. | application/json; charset=UTF-8 | true |

### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/post/publish/creator_info/query/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json; charset=UTF-8'
```
## Response

| **Field Name** | **Nested Field** | **Type** | **Description** |
| --- | --- | --- | --- |
| data | creator_avatar_url | string | The URL of the TikTok creator's avatar with a TTL of 2 hours. |
| creator_username | string | The unique ID of the TikTok creator. |
| creator_nickname | string | The nickname of the TikTok creator. |
| privacy_level_options | list<string> | If the TikTok creator account is public, the available options are: `PUBLIC_TO_EVERYONE` `MUTUAL_FOLLOW_FRIENDS` `SELF_ONLY` If the TikTok creator account is private, the available options are: `FOLLOWER_OF_CREATOR` `MUTUAL_FOLLOW_FRIENDS` `SELF_ONLY` |
| comment_disabled | boolean | Returns`true`if the creator sets the comment interaction to "No one" in their privacy setting. |
| duet_disabled | boolean | Returns`true`if the creator account is private or they set the Duet interaction to "No one" in their privacy setting. **IGNORE **if your client only sends photo media through this API. |
| stitch_disabled | boolean | Returns`true`if the creator account is private or they set the Stitch interaction to "No one" in their privacy setting. **IGNORE **if your client only sends photo media through this API. |
| max_video_post_duration_sec | int32 | The longest video duration in seconds that the TikTok creator can post. Different users have different maximum video-duration privileges. Developers should use this field to stop video posts that are too long. **IGNORE **if your client only sends photo media through this API. |
| error | code | string | [You can decide whether the request is successful based on the error code. Any code other than `ok`indicates the request did not succeed. Learn more about error codes](#lATfV6). |
| message | string | A human readable description of the error. |
| logid | string | A unique identifier for the execution of this request. |

[**Note**: Your app needs to use fields returned in the respose.data to render your export screen. This will indicate the TikTok account to which the post will be published and provide creators with the available privacy settings they can choose from. Learn more about the UX guidelines here](https://developers.tiktok.com/doc/content-sharing-guidelines#).
### Example
```
200 OK

{
   "data":{
      "creator_avatar_url": "https://lf16-tt4d.tiktokcdn.com/obj/tiktok-open-platform/8d5740ac3844be417beeacd0df75aef1",
      "creator_username": "tiktok",
      "creator_nickname": "TikTok Official",
      "privacy_level_options": ["PUBLIC_TO_EVERYONE", "MUTUAL_FOLLOW_FRIENDS", "SELF_ONLY"] 
      "comment_disabled": false,
      "duet_disabled": false,
      "stitch_disabled": true,
      "max_video_post_duration_sec": 300
   },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
### Error Codes

| **HTTP Status** | **Error code** | **Description** |
| --- | --- | --- |
| 200 | ok |  |
| 200 (intentional) | spam_risk_too_many_posts | The daily post cap from the API is reached for the current user. |
| spam_risk_user_banned_from_posting | The user is banned from making new posts. |
| reached_active_user_cap | The daily quota for active publishing users from your client is reached. |
| 401 | access_token_invalid | The access_token is invalid or has expired. |
| scope_not_authorized | The access_token does not bear user's grant on `video.publish`scope. |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit. |
| 5xx |  | TikTok server or network error. Try again later. |

Was this document helpful?


---
## SOURCE: Content Posting API/API Reference/Upload.md

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
