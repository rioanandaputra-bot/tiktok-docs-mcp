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