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