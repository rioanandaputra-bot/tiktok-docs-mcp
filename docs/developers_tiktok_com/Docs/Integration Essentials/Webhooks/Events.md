Docs
# Webhook Events
[Webhooks let you subscribe to events and receive notice when an event occurs. For more information about how to set up a webhook subscription, see Webhooks Overview](https://developers.tiktok.com/doc/webhooks-overview).
By default, you are subscribed to all events when a callback URL is configured in the TikTok Developer Portal.
## Webhook Structure
### Request Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| event | string | Event name. |
| create_time | int64 | The time in which the event occurred. UTC epoch time is in seconds. |
| user_openid | string | The TikTok user's unique identifier; obtained through `/oauth/access_token/`. |
| content | string | A serialized JSON string of event information. |

## Event types
### authorization.removed
Fired when the user's account deauthorized from your application.
The `access_token` for the user will have been already revoked when you receive the disconnect callback message. Developers can persist this information for clean-up purposes.

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| reason | int | 0 = Unknown 1 = User disconnects from TikTok app 2 = User's account got deleted 3 = User's age changed 4 = User's account got banned 5 = Developer revoke authorization |

#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "authorization.removed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content": "{\"reason\": 1 }"
}
```
### video.upload.failed
[Fired when the video uploaded from Video Kit](https://developers.tiktok.com/doc/web-video-kit-with-web) fails to upload in TikTok.
#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "video.upload.failed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content":"{\"share_id\":\"video.6974245311675353080.VDCxrcMJ\"}"
}
```
### video.publish.completed
[Fired when the video uploaded from Video Kit](https://developers.tiktok.com/doc/web-video-kit-with-web) has been published by the user in TikTok.
#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "video.publish.completed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content":"{\"share_id\":\"video.6974245311675353080.VDCxrcMJ\"}"
}
```
## portability.download.ready
[Fired when data requested via from the Data Portability API](https://developers.tiktok.com/products/data-portability-api/) is in the `downloading` state.
Example payload:
```
{
    "client_key": "developer_client_key",
    "event": "portability.download.ready",
    "create_time": 1615338610,
    "content":"{\"request_id\":123123123123123}"
}
```
Note: `content` is a JSON object marshalled as a string
```
{
    "request_id": 123123123123123
}
```
### Payload content

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API | 123123123123 |

Was this document helpful?