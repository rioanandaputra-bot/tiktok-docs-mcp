Docs
# Share Video
[**Important**: This Share Video API is now deprecated and will sunset on **September 10th, 2023**. Please migrate to our Content Posting API immediately. To simplify your migration experience, we have published a migration guide](https://developers.tiktok.com/bulletin/migration-notice-share-video-api/).
## Overview
Share Video API allows users to share videos from your Web or Desktop app into TikTok. Videos will be sent into users' inboxes where they can then be edited and published through the TikTok app.
### Authorization Scopes
- **video.upload** gives developers permissions to upload a video on behalf of the TikTok user.
## Endpoint Documentation
### Endpoint
_POST_ `https://open-api.tiktok.com/share/video/upload/`
### Request
#### Query Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier, which is obtained through `/oauth/access_token/`. |
| access_token | string | The token that bears the authorization of the TikTok user, which is obtained through `/oauth/access_token/`. |

#### Body
Content-Type: multipart/form-data

| **Part** | **Type** | **Description** |
| --- | --- | --- |
| video | MP4 | The video file being uploaded. |

### Response
#### Response.data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| share_id | string | A unique identifier for the shared video. |
| error_code | int64 | Error code. |
| error_msg | string | Error description. If the request is not successful, then this field will be returned. |

#### Response.extra Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| error_detail | string | Detailed information on the error. |
| logid | string | Unique identifier to identify the request. |

### Constraints
To make sure the video can be shared successfully, the developer is responsible for uploading video files that meet the following expectations:
- The size of the uploaded video file must be less than or equal to 50 MB.
- The duration of the video file must be at least 3 seconds and at most 60 seconds.
- The supported video file format is _MP4_.
- The video resolution is at least 540p.
### Webhook
TikTok uses webhooks to notify your application when an event happens to the shared video.
[For more information about how to set up a webhook subscription, see Webhooks Overview](https://developers.tiktok.com/doc/webhooks-overview).
## Example Flow
- Make sure your users have authorized `video.upload` permissions to your application. This should be shown under the authorization page as a bullet that reads "Publish videos to TikTok".
- Send a POST request to the share/video/upload endpoint.
Example Request
```
curl --location --request POST 'https://open-api.tiktok.com/share/video/upload/?access_token=<ACCESS_TOKEN>&open_id=<OPEN_ID>' \
--form 'video=@"/Users/tiktok/Downloads/video.mp4"'
```
- Check to make sure you have received a successful response. With a successful response, you should see a notification show up in your inbox saying that your video has been sent to TikTok.
Example Successful Response
```
{
    "data": {
        "err_code": 0,
        "error_code": 0,
        "share_id": "v_inbox.<ID>"
    },
    "extra": {
        "error_detail": "",
        "logid": "<LOG_ID>"
    }
}
```
Example Failed Response
```
{
    "data": {
        "err_code": 20002,
        "error_code": 20002,
        "error_msg": "The user did not authorize the scope required for completing this request."
    },
    "extra": {
        "error_detail": "",
        "logid": "<LOG_ID>"
    }
}
```
Notification in inbox
- After some time, another notification will appear in your inbox saying: "Your video from <APP> is ready: Edit your video before sharing to TikTok." Click this notification to proceed to edit and publish your video to TikTok. You may instead get another notification explaining that your video upload has failed. If this occurs, please check that your video meets the constraints outlined in the "Constraints" section above in this documentation and try uploading your video again.
Successful Upload Notification
Unsuccessful Upload Notification
Was this document helpful?