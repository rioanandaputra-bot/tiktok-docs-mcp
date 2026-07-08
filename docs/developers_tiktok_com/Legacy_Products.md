# Legacy Products

> Consolidated from 20 source files.



---
## SOURCE: Legacy Products/Legacy Products.md

Docs
# Migrating to our new API
Created based on feedback from our partners, our new API follows industry standards including OAuth 2.0 and provides an improved integration experience.
Our new API is hosted at `open.tiktokapis.com`. Learn more about our new API endpoints:
- [Get User Info](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)
- [List Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)
- [Query Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)
# What's New
## New Request and Response Format
### Authentication
Users need to pass the access token returned from the authorization step to successfully call our  APIs. The access token must be put into `Authorization` header with `Bearer` type. We no longer require `open_id` for request authentication.
### Request Parameters
`GET` requests may have query parameters but no request body is allowed.
For `POST` requests, `fields` should be provided as a query parameter. All other parameters should be placed in the request body in JSON format.
Please refer to the documentation for each individual API for detailed information about the request format.
### Error Handling
[[[New APIs will return different `4xx` and `5xx` HTTP status in the response, with the name of the error and an error message in the response body. For a complete list of HTTP status and error names, please refer to our new](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling)API Error Handling document](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling)ation](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling).
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy User Access Token Guide.md

Docs
# Manage Legacy User Access Tokens
[Legacy user access tokens using our OAuth v1 API are deprecated. View migration announcement](https://developers.tiktok.com/bulletin/migration-guidance-oauth-v1).
## Understanding the Basics
### OAuth
TikTok Login Kit manages the token lifecycle, allowing you to integrate login and authentication flows directly in your application. A successful authorization flow grants developers refreshable access tokens. Those tokens enable developers to perform endpoint access with user permissions.
### Authorization Scopes
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the rights to only agree to a subset of scopes you requested from them.
Here are some example scopes:
- **user.info****.basic** gives read-only access to a user's avatar and display name.
- **video.list** gives read-only access to a user's public TikTok videos.
[You can learn more about Scopes on our Scopes Overview page](https://developers.tiktok.com/doc/scopes-overview).
### Token Security
Tokens must be handled with extreme caution. We recommend storing and managing all tokens on the server side.
- Access token is a user authorization token that can be used to directly access user information in the Tiktok ecosystem.
- Refresh token is used to renew the access token.
## Endpoints
### 1. Fetch Access Token Using Authorization Code
Once the authorization code callback is handled, you can use the code to retrieve the user's access token.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/access_token/`
#### Request Query Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| client_secret | string | The unique identification secret provisioned to the partner. |
| code | string | Authorization code from Web/iOS/Android authorization callback. |
| grant_type | string | Its value should always be set as _authorization_code_. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier. |
| scope | string | The scopes user has agreed to authorize, separated by comma (,). |
| access_token | string | The access token for future calls on behalf of the user. |
| expires_in | int64 | Expiration for the `access_token`in seconds. **It is valid for 24 hours after initial issuance**. |
| refresh_token | string | The token for refresh the `access_token`. **It is valid for 365 days after initial issuance**. |
| refresh_expires_in | int64 | Expiration for the `refresh_token`in seconds. |

Make sure to store these values in your backend as they will be needed to persist access.
#### Code Example
```
app.get('/redirect', (req, res) => {
    const { code, state } = req.query;
    const { csrfState } = req.cookies;

    if (state !== csrfState) {
        res.status(422).send('Invalid state');
        return;
    }

    let url_access_token = 'https://open-api.tiktok.com/oauth/access_token/';
    url_access_token += '?client_key=' + CLIENT_KEY;
    url_access_token += '&client_secret=' + CLIENT_SECRET;
    url_access_token += '&code=' + code;
    url_access_token += '&grant_type=authorization_code';

    fetch(url_access_token, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
If the request is not successful, the response will return the following error response body:
```
{
    "data": {
        "captcha": "",
        "desc_url": "",
        "description": "Parameter error",
        "error_code": 10002
    },
    "message": "error"
}
```
### 2. Refresh Access Token Using Refresh Token
Although the fetched `access_token` expires within 24 hours, it can be refreshed without user consent. The developer's backend server can schedule background jobs to keep tokens up to date.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/refresh_token/`
#### Request Query Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| grant_type | string | Its value should always be set as _refresh_token_. |
| refresh_token | string | The user's `refresh_token`received from `/oauth/access_token/`endpoint. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The partner-facing user id. |
| scope | string | The scopes user has agreed to authorize, separated by comma (,). |
| access_token | string | New token for future calls on behalf of the user. |
| expires_in | int64 | Expiration for the access token in seconds. |
| refresh_token | string | The token for refresh an user's `access_token`. Note that the returned refresh_token may be different than the one passed in the payload. **Developers must use the newly-returned token should the value is different than the previous one.** |
| refresh_expires_in | int64 | Expiration for the `refresh_token`in seconds. |

Make sure to store these values in your backend as they will be needed to persist access.
#### Code Example
```
app.get('/refresh_token/', (req, res) => {
    const refresh_token = req.query.refresh_token;

    let url_refresh_token = 'https://open-api.tiktok.com/oauth/refresh_token/';
    url_refresh_token += '?client_key=' + CLIENT_KEY;
    url_refresh_token += '&grant_type=refresh_token';
    url_refresh_token += '&refresh_token=' + refresh_token;

    fetch(url_refresh_token, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
If the request is not successful, the response will return the following error response body:
```
{
    "data": {
        "captcha": "",
        "desc_url": "",
        "description": "Parameter error",
        "error_code": 10002
    },
    "message": "error"
}
```
### 3. Revoke Access
When users want to disconnect the connection between your application and TikTok, you can revoke their `access_tokens` so the users will no longer see your application show up on the **Manage app permissions** page within TikTok.
#### Endpoint
_POST_ `https://open-api.tiktok.com/oauth/revoke/`
#### Request Parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier; obtained through `/oauth/access_token/`the user's unique token. |
| access_token | string | The token that bears the authorization of the TikTok user, `/oauth/access_token/`. This token requires user authorization. |

#### Response.Data Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| error_code | int64 | Error code. |
| description | string | Error code description. |

#### Code Example
```
app.get('/revoke', (req, res) => {
    const { open_id, access_token } = req.query;

    let url_revoke = 'https://open-api.tiktok.com/oauth/revoke/';
    url_revoke += '?open_id=' + open_id;
    url_revoke += '&access_token=' + access_token;

    fetch(url_revoke, {method: 'post'})
        .then(res => res.json())
        .then(json => {
            res.send(json);
        });
})
```
Was this document helpful?


---
## SOURCE: Legacy Products/List Videos.md

Docs
# List Videos
[There is a new version of this API available in TikTok API v2: List Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)
## Overview
The `video/list/` endpoint can return a paginated list of given user's **public** TikTok video posts, sorted by `create_time` in descending order.

| **HTTP URL** | https://open-api.tiktok.com/video/list/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | video.list |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | "application/json" | "application/json" | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| access_token | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | act.example12345Example12345Example | Yes |
| fields | set<string> | The set of optional video fields **Choose fields from: VideoObject's fields** | ["embed_link"] | Yes |
| cursor | int64 | Cursor for pagination. If `response.has_more`is true, pass in the `response.cursor`to the next request will yield the results for the next page. _Note: the cursor value is a __UTC__Unix timestamp in milli-seconds. You can pass in a customized timestamp to fetch the user's videos posted before the provided timestamp._ | 0 | No |
| max_count | int32 | The maximum number of videos that will be returned from each page. Default is 10. Maximum is 20. _Note: due our trust and safety policies, it is possible that the endpoint returns less than max_count number of videos even if __response.data.has_more__is __true__._ | 10 | No |

### Example
```
curl -L -X POST 'https://open-api.tiktok.com/video/list/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "access_token": "act.example12345Example12345Example",
    "fields": ["id", "embed_link", "title"]
}'
```
## Response

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | map<string, object> | video_list: list<VideoObject> cursor: int64 has_more: bool err_code:int64 error_code:int64 |
| extra | map<string, object> | error_detail: string logid: string |

### VideoObject

| **Field** | **Type** | **Description** | **Scope** |
| --- | --- | --- | --- |
| id | string | Unique identifier for the TikTok video. Also called "item_id" | video.list |
| create_time | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. | video.list |
| cover_image_url | string | A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a **TTL****of 6 hours.** | video.list |
| share_url | string | A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices. | video.list |
| video_description | string | The description that the creator has set for the TikTok video. Max length: 150 | video.list |
| duration | int32 | The duration of the TikTok video in seconds. | video.list |
| height | int32 | The height of the TikTok video. | video.list |
| width | int32 | The width of the TikTok video. | video.list |
| title | string | The video title. Max length: 150 | video.list |
| embed_html | string | HTML code for embedded video | video.list |
| embed_link | string | Video embed link of tiktok.com | video.list |
| like_count | int32 | Number of likes of the video. Included when requested in the fields. | video.list |
| comment_count | int32 | Number of comments of the video. Included when requested in the fields. | video.list |
| share_count | int32 | Number of shares of the video. Included when requested in the fields. | video.list |
| view_count | int64 | Number of views of the video. Included when requested in the fields. | video.list |

### Example
```
{
    "data":{
        "cursor":1652986389000,
        "err_code":0,
        "error_code":0,
        "has_more":false,
        "video_list":[
            {
                "id":"7099522475452681474",
                "embed_link":"https://www.tiktok.com/static/profile-video?id=7099522475452681474&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
                "title":"video 1"
            }
        ]
    },
    "extra":{
        "error_detail":"",
        "logid":"202205200320140101131341351D46C27E"
    }
}
```
Was this document helpful?


---
## SOURCE: Legacy Products/Query Videos.md

Docs
# Query Videos
[There is a new version of this API available in TikTok API v2: Query Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)
## Overview
The `video/query/` endpoint, given a user and a list of video ids, can check if the videos belong to the requesting user and fetch the data of videos belonging to the user. It can be used to refresh the given videos' cover image url TTL. Number of video ids should not be larger than 20 at a time.

| **HTTP URL** | https://open-api.tiktok.com/video/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | video.list |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | "application/json" | "application/json" | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| access_token | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | act.example12345Example12345Example | Yes |
| filters | object | Fields: video_ids: set<string> | { "video_ids": ["1234565570247476230"] } | Yes |
| fields | set<string> | The set of optional video fields **Choose fields from: VideoObject's fields** | ["embed_link"] | Yes |

### Request Example
```
curl -L -X POST 'https://open-api.tiktok.com/video/query/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "access_token": "act.example12345Example12345Example",
    "filters": {
        "video_ids": ["1234568030997662933", "1234580793298373833"]
    },
    "fields": ["id", "title"]
}'
```
## Response

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| data | map<string, list<VideoObject>> | videos: list<video object> | Yes |
| error | Object | Error object | Yes |

### VideoObject

| **Field** | **Type** | **Description** | **Scope** |
| --- | --- | --- | --- |
| id | string | Unique identifier for the TikTok video. Also called "item_id" | video.list |
| create_time | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. | video.list |
| cover_image_url | string | A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a **TTL****of 6 hours.** | video.list |
| share_url | string | A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices. | video.list |
| video_description | string | The description that the creator has set for the TikTok video. Max length: 150 | video.list |
| duration | int32 | The duration of the TikTok video in seconds. | video.list |
| height | int32 | The height of the TikTok video. | video.list |
| width | int32 | The width of the TikTok video. | video.list |
| title | string | The video title. Max length: 150 | video.list |
| embed_html | string | HTML code for embedded video | video.list |
| embed_link | string | Video embed link of tiktok.com | video.list |
| like_count | int32 | Number of likes of the video. Included when requested in the fields. | video.list |
| comment_count | int32 | Number of comments of the video. Included when requested in the fields. | video.list |
| share_count | int32 | Number of shares of the video. Included when requested in the fields. | video.list |
| view_count | int64 | Number of views of the video. Included when requested in the fields. | video.list |

### Example
```
{
    "data":{
        "videos":[
            {
                "id":"1234568030997662933",
                "title":"Test Video 32"
            },
            {
                "id":"1234580793298373833",
                "title":"Test Video 22"
            }
        ]
    },
    "error":{
        "code":0,
        "message":""
    }
}
```
Was this document helpful?


---
## SOURCE: Legacy Products/Share Video API.md

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


---
## SOURCE: Legacy Products/User Info.md

Docs
# Get User Profile Information
[There is a new version of this API available in TikTok API v2: Get User Info](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)
[There is a migration plan related to this API. Learn more here](https://developers.tiktok.com/bulletin/user-info-scope-migration).
## Overview
The `user/info/` endpoint returns some basic information of a given TikTok user.

| **HTTP ****URL** | https://open-api.tiktok.com/user/info/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | [Needs relevant scopes](#user_object) to be authorized by the TikTok user through the authorization flow. |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | "application/json" | "application/json" | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| access_token | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | act.example12345Example12345Example | Yes |
| fields | set<string> | **Choose fields from: UserObject's fields** | ["open_id", "avatar_url"] | Yes |

### Example
```
curl -L -X POST 'https://open-api.tiktok.com/user/info/' \
-H 'Content-Type: application/json' \
--data-raw '{
    "access_token": "act.example12345Example12345Example",
    "fields": ["open_id", "union_id", "avatar_url"]
}'
```
## Response

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | map<string, UserObject> | Contains user object |
| error | object | Contains error code and error message |

### User Object

| **Field** | **Type** | **Description** | **Authorized ****Scope** |
| --- | --- | --- | --- |
| open_id | string | The unique identification of the user in the current application.Open id for the client | user.info.basic |
| union_id | string | The unique identification of the user across different apps for the same developer. For example, if a partner has X number of clients, it will get X number of open_id for the same TikTok user, but one persistent union_id for the particular user | user.info.basic |
| avatar_url | string | User's profile image | user.info.basic |
| avatar_url_100 | string | User`s profile image in 100x100 size | user.info.basic |
| avatar_large_url | string | User's profile image with higher resolution | user.info.basic |
| display_name | string | User's profile name | user.info.basic |
| bio_description | string | User's bio description if there is a valid one | user.info.profile |
| profile_deep_link | string | The link to user's TikTok profile page | user.info.profile |
| is_verified | boolean | Whether TikTok has provided a verified badge to the account after confirming that it belongs to the user it represents | user.info.profile |
| username | string | User's username. | user.info.profile |
| follower_count | int64 | User's followers count | user.info.stats |
| following_count | int64 | The number of accounts that the user is following | user.info.stats |
| likes_count | int64 | The total number of likes received by the user across all of their videos | user.info.stats |
| video_count | int64 | The total number of publicly posted videos by the user | user.info.stats |

### Example
```
{
    "data":{
        "user":{
            "avatar_url":"https://p19-sign.tiktokcdn-us.com/tos-avt-0068-tx/b17f0e4b3a4f4a50993cf72cda8b88b8~c5_168x168.jpeg",
            "open_id":"723f24d7-e717-40f8-a2b6-cb8463333b4",
            "union_id":"c9c60f44-a68e-4f5d-84dd-ce22fddb0ba1"
        }
    },
    "error":{
        "code":0,
        "message":""
    }
}
```
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Download.md

Docs
# Download
[There is a new version of this SDK: iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart)
## TikTokOpenSDK
[Click Download TikTokOpenSDK](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/TikTokOpenSDK.xcframework-5.0.15.zip).
## Demo
A complete access sample demo project, you can visually view the access method and API usage through Demo, test Demo uses the test Client Key for reference only.
[Click to download - iOS Demo](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/TikTokOpenSDKDemo-5.0.15.zip)
#### Change Bundle ID with yours
#### Change Info.plist ClientKey with yours
Run the project and you're all set.
## SDK Version History
---
Version : v5.0.15
Date : 2022-07-14
Info :
- Release Green Screen Kit
---
Version : v5.0.14
Date : 2022-05-10
Info :
- Change TikTokOpenSDK from framework to xcframework.
- Include support for bitcode
---
Version : v5.0.13
Date : 2022-03-30
Info :
- Fix web view navigation bar
---
Version : v5.0.0
Date : 2021-05-25
Info :
- Support share sound and login features
---
Version : v4.0.1
Date : 2020-08-06
Info :
- Optimize translation
---
Version : v4.0.0
Date : 2020-07-20
Info :
- Support share feature for TikTok 16.6.5 or later
---
Version : v3.0.0
Date : 2020-02-24
Info :
- Optimize API
- Support Bitcode
---
Version : v2.0.5
Date : 2019-09-17
Info :
- Fix sharing params are not passed to TikTok
---
Version : v2.0.4
Date : 2019-09-08
Info :
- Fix web authorization without callback BUG
- Handling iOS 13 compatibility issues
- Handling localization string compatibility issues
- Authorization to increase package name verification
---
Version : v2.0.1
Date : 2019-08-26
Info :
- Authorize the API to join the ClientKey check
- Authorization web page title adjustment
---
Version : v2.0.0
Date : 2019-08-07
Info :
- SDK is provided through Framework
- Some API usability adjustments
---
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Handling Errors.md

Docs
# Handling iOS Errors
When any error happens, the response will have an error code with the following mapping:

| **TikTokShareResponseErrorCode** | **Error Code** |
| --- | --- |
| Success | 0 |
| Common Error | -1 |
| User Canceled | -2 |
| Share failed | -3 |
| Share denied | -4 |
| Unsupported | -5 |

If the error code does not make it easy for you to locate a specific error, you can use 'respond.shareState` for detail message. SDK version need 2.0.8 or higher.
The following map defines the Sharing state and specific issues.

| **TikTokOpenSDKShareRespState** | **value** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKShareRespStateSuccess | 20000 | Success. |
| TikTokOpenSDKShareRespStateUnknownError | 20001 | Unknown or current SDK version unclassified error. |
| TikTokOpenSDKShareRespStateParamValidError | 20002 | Params parsing error. |
| TikTokOpenSDKShareRespStateSharePermissionDenied | 20003 | Not enough permissions to operation. |
| TikTokOpenSDKShareRespStateUserNotLogin | 20004 | User not logged in. |
| TikTokOpenSDKShareRespStateNotHavePhotoLibraryPermission | 20005 | TikTok has no album permissions. |
| TikTokOpenSDKShareRespStateNetworkError | 20006 | TikTok Network error. |
| TikTokOpenSDKShareRespStateVideoTimeLimitError | 20007 | Video length doesn't meet requirements. |
| TikTokOpenSDKShareRespStatePhotoResolutionError | 20008 | Photo doesn't meet requirements. |
| TikTokOpenSDKShareRespTimeStampError | 20009 | Timestamp check failed. |
| TikTokOpenSDKShareRespStateHandleMediaError | 20010 | Processing photo resources failed. |
| TikTokOpenSDKShareRespStateVideoResolutionError | 20011 | Video resolution doesn't meet requirements. |
| TikTokOpenSDKShareRespStateVideoFormatError | 20012 | Video format is not supported. |
| TikTokOpenSDKShareRespStateCancel | 20013 | Sharing canceled. |
| TikTokOpenSDKShareRespStateHaveUploadingTask | 20014 | Another video is currently uploading. |
| TikTokOpenSDKShareRespStateSaveAsDraft | 20015 | Users store shared content for draft or user accounts are not allowed to post videos. |
| TikTokOpenSDKShareRespStatePublishFailed | 20016 | Post share content failed. |
| TikTokOpenSDKShareRespStateMediaInIcloudError | 21001 | Downloading from iCloud failed. |
| TikTokOpenSDKShareRespStateParamsParsingError | 21002 | Internal params parsing error. |
| TikTokOpenSDKShareRespStateGetMediaError | 21003 | Media resources do not exist. |

Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Legacy Mobile SDK.md

Docs
# iOS Quickstart Objective C
[There is a new version of this SDK: iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart)
Integrating our open SDK can help you leverage TikTok's open platform capabilities, such as Login Kit, Sound Kit, sharing videos to TikTok, and more coming soon. We hope to help you enhance your app's discovery and engagement, as well as provide another location for your users to share their favorite content for the world to see.
## Getting Started with the TikTok SDK for iOS
### Requirements
TikTok iOS SDK requires iOS 9.3 and Xcode 4.5 or later.
### Step 1: Configure TikTok App Settings for iOS
Go to TikTok Developer App Registration Page to create your app. After approval, you will get the Client Key and Client Secret.
### Step 2: Install the SDK
#### Via Cocoapods (Recommend)
Add the pod to your Podfile:
```
pod 'TikTokOpenSDK', '~> 5.0.15'
```
And then run:
```
pod install --repo-update
```
#### Via Manual Install
[Download TikTokOpenSDK](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/TikTokOpenSDK.xcframework-5.0.15.zip), unzip the zip files, and you will find the SDK called TikTokOpenSDK.xcframework.
Link Framework
- **Copy** or **Drag** the SDKs into your Xcode Project.
Select your Project in Project Navigator. Click "+" in `TARGETS -> Build Phases -> Link Binary With Libraries`, and then select `TikTokOpenSDK.``xc``framework` in your Project folder to add it.
- Add `WebKit.framework` and `Security.framework`.
- `WebKit.framework` - It is used to gain authorization through web-view when TikTok is not installed.
- `Security.framework` - Encryption and decryption library. We use this framework to ensure that communications are securely transmitted.
- Add Link Flag `-ObjC` in `TARGETS->Build Settings->Other Linker Flags`. Make sure the letter 'O' and 'C' are capitalized.
The correct configuration is shown below:
### Step 3: Configure Xcode Project
#### Configure Info.plist
- In Xcode, right-click your project's Info.plist file and select Open As -> Source Code.
- Here are 3 keys need to configuration:
- **LSApplicationQueriesSchemes: Use to Open TikTop App**
- **TikTokAppID: Use to config TikTok OpenSDK**
- **CFBundleURLTypes : Use TikTok App callback your App**
Insert the following XML snippet into the body of your file just before the final `</dict>` element.
```
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>tiktokopensdk</string>
    <string>tiktoksharesdk</string>
    <string>snssdk1180</string>
    <string>snssdk1233</string>
</array>
<key>TikTokAppID</key>
<string>$TikTokAppID</string>
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>$TikTokAppID</string>
    </array>
  </dict>
</array>
```
- Replace `$TikTokAppID` with your **App's Client Key**
Note:
- `tiktokopensdk` is used for logging in.
- `tiktoksharesdk` is used for sharing.
- `snssdk1233`, `snssdk1180` are used to check if the TikTok application is installed.
- The TikTok Open SDK auto-registers your Client Key when your App launches.
#### Make sure your app has access to Photo Library
Sharing pictures requires Photo Library access. Make sure a proper Privacy - Photo Library Usage Description is added in your Info.plist.
After the configuration, your Info.plist will look like the following.
### Step 4: Connect App Delegate and/or Scene Delegate
You need to connect your `AppDelegate` class to the `TikTokOpenSDKApplicationDelegate.h`. To do this, add the following code to your `AppDelegate.m` file.
```
#import <TikTokOpenSDK/TikTokOpenSDKApplicationDelegate.h>
@implementation AppDelegate
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    [[TikTokOpenSDKApplicationDelegate sharedInstance] application:application didFinishLaunchingWithOptions:launchOptions];
    return YES;
}

- (BOOL)application:(UIApplication *)application openURL:(nonnull NSURL *)url options:(nonnull NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {

    if ([[TikTokOpenSDKApplicationDelegate sharedInstance] application:application openURL:url sourceApplication:options[UIApplicationOpenURLOptionsSourceApplicationKey] annotation:options[UIApplicationOpenURLOptionsAnnotationKey]]
        ) {
        return YES;
    }
    return NO;
}

- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation
{
    if ([[TikTokOpenSDKApplicationDelegate sharedInstance] application:application openURL:url sourceApplication:sourceApplication annotation:annotation]) {
        return YES;
    }
    return NO;
}

- (BOOL)application:(UIApplication *)application handleOpenURL:(NSURL *)url
{
    if ([[TikTokOpenSDKApplicationDelegate sharedInstance] application:application openURL:url sourceApplication:nil annotation:nil]) {
        return YES;
    }
    return NO;
}
@end
```
If your application does not have a `SceneDelegate`, you are good to go! If your application makes use of the `SceneDelegate`, you will need to add the following code to your `SceneDelegate.m` file.
```
#import <TikTokOpenSDK/TikTokOpenSDKApplicationDelegate.h>
@implementation SceneDelegate

- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts
{
    NSURL *url = [[URLContexts allObjects] firstObject].URL;
    [UIApplication.sharedApplication.delegate application:UIApplication.sharedApplication openURL:url options:@{}];
}

@end
```
#### API Instructions
**TikTokOpenSDKApplicationDelegate**
Log Delegate
```
@protocol TikTokOpenSDKLogDelegate <NSObject>

- (void)onLog:(NSString *)logInfo;

@end
```
TikTok internal log in level ERROR or Warning will callback in this method.You need to register log delegate in TikTokOpenSDKApplicationDelegate in didFinishLaunchingWithOptions in the App Delegate.
Usage:
```
[TikTokOpenSDKApplicationDelegate sharedInstance].logDelegate = self;
```
Check TikTok is installed :
```
- (BOOL)isAppInstalled;
```
**BDOpenPlatformObjects**
The definition of basic classes (Request or Response) to SDK.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Login Kit With Objective-C.md

Docs
# Login Kit with Objective-C
[There is a new version of this SDK: Login Kit for iOS](https://developers.tiktok.com/doc/login-kit-ios-quickstart)
### Overview
[This guide explains how to integrate with Login Kit for iOS using Objective-C. Once authenticated users authorize your app, you can access their basic TikTok profile data including their display name and avatar. Additional data access may require approval for additional Scopes. Learn more on Scopes Overview](https://developers.tiktok.com/doc/scopes-overview).
### Prerequisites
[[Obtain a client key and client secret by logging in to Developer Portal](https://developers.tiktok.com/apps/) and selecting your app. Refer to the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-ios-quickstart-objective-c) for detailed steps.
### iOS Integration
#### Authorization Request
- Create a `TikTokOpenSDKAuthRequest` and set `permissions` equal to the set of scopes you are requesting from the user. For example, `user.info``.basic,video.list`.
- Send the authorization request.
- If user authorization was successful, a `code` will be provided in the response.
- [Upload this `code` to your server-side and obtain a user access token. See Manage User Access Tokens](https://developers.tiktok.com/doc/legacy-user-access-guide) for more information.
These steps are demonstrated in the following code snippet:
```
#import <TikTokOpenSDK/TikTokOpenSDKAuth.h>

/* STEP 1: Create the request and set permissions */
NSArray *scopes = @"user.info.basic,video.list"; // list your scopes;
NSOrderedSet *scopesSet = [NSOrderedSet orderedSetWithArray:scopes];
TikTokOpenSDKAuthRequest *request = [[TikTokOpenSDKAuthRequest alloc] init];
request.permissions = scopesSet;

/* STEP 2: Send the request */
__weak typeof(self) ws = self;
[request sendAuthRequestViewController:self
                completion:^(TikTokOpenSDKAuthResponse *_Nonnull resp) {
    __strong typeof(ws) sf = ws;

    /* STEP 3: Parse and handle the response */
    if (resp.errCode == 0) {
        NSString *responseCode = resp.code;
        // Upload response code to your server and obtain user access token
        ... 
    } else {
        // User authorization failed. Handle errors
    }
}];
```
#### Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-ios-handling-errors) for error handling and debugging.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Login Kit With Swift.md

Docs
# Login Kit with Swift
[There is a new version of this SDK: Login Kit for iOS](https://developers.tiktok.com/doc/login-kit-ios-quickstart)
### Overview
[This guide explains how to integrate with Login Kit for iOS using Swift. Once authenticated users authorize your app, you can access their basic TikTok profile data including their display name and avatar. Additional data access may require approval for additional Scopes. Learn more on Scopes Overview](https://developers.tiktok.com/doc/scopes-overview).
### Prerequisites
[[Obtain a client key and client secret by logging in to Developer Portal](https://developers.tiktok.com/apps/) and selecting your app. Refer to the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-ios-quickstart-swift) for detailed steps.
### iOS Integration
#### Authorization Request
- Create a `TikTokOpenSDKAuthRequest` and set `permissions` equal to the set of scopes you are requesting from the user. For example, `user.info``.basic,video.list`.
- Send the authorization request.
- If user authorization was successful, a `code` will be provided in the response.
- [Upload this `code` to your server-side and obtain a user access token. See Manage User Access Tokens](https://developers.tiktok.com/doc/legacy-user-access-guide) for more information.
These steps are demonstrated in the following code snippet:
```
import TikTokOpenSDK

/* STEP 1: Create the request and set permissions */
let scopes = "user.info.basic,video.list" // list your scopes
let scopesSet = NSOrderedSet(array:scopes)
let request = TikTokOpenSDKAuthRequest()
request.permissions = scopesSet

/* STEP 2: Send the request */
request.send(self, completion: { resp -> Void in
    /* STEP 3: Parse and handle the response */
    if resp.errCode == 0 {
        let responseCode = resp.code
        // Upload response code to your server and obtain user access token
        ...
    } else {
        // User authorization failed. Handle errors
    }
}
```
#### Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-ios-handling-errors) for error handling and debugging.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Quickstart Swift.md

Docs
# iOS Quickstart Swift
[There is a new version of this SDK: iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart)
Integrating our open SDK can help you leverage TikTok's open platform capabilities, such as Login Kit, Sound Kit, sharing videos to TikTok, and more coming soon. We hope to help you enhance your app's discovery and engagement, as well as provide another location for your users to share their favorite content for the world to see.
## Getting Started with the TikTok SDK for iOS
### Requirements
TikTok iOS SDK requires iOS 9.3 and Xcode 4.5 or later.
### Step 1: Configure TikTok App Settings for iOS
Go to TikTok Developer App Registration Page to create your app. After approval, you will get the Client Key and Client Secret.
### Step 2: Install the SDK
#### Via Cocoapods (Recommend)
Add the pod to your Podfile:
```
pod 'TikTokOpenSDK', '~> 5.0.15'
```
And then run:
```
pod install --repo-update
```
#### Via Manual Install
[Download TikTokOpenSDK](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/TikTokOpenSDK.xcframework-5.0.15.zip), unzip the zip files, and you would find the SDKs called TikTokOpenSDK.framework.
Link Framework
- **Copy** or **Drag** the SDKs into your Xcode Project.
Select your Project in Project Navigator. Click "+" in `TARGETS -> Build Phases -> Link Binary With Libraries`, and then select `TikTokOpenSDK.``xc``framework` in your Project folder to add it.
- Add `WebKit.framework` and `Security.framework`.
- `WebKit.framework` - It is used to gain authorization through web-view when TikTok is not installed.
- `Security.framework` - Encryption and decryption library. We use this framework to ensure that communications are securely transmitted.
- Add Link Flag `-ObjC` in `TARGETS->Build Settings->Other Linker Flags`. Make sure the letter 'O' and 'C' are capitalized.
The correct configuration is shown below:
### Step 3: Configure Xcode Project
#### Configure Info.plist
- In Xcode, right-click your project's Info.plist file and select Open As -> Source Code.
- Here are 3 keys need to configuration:
- **LSApplicationQueriesSchemes: Use to Open TikTop App**
- **TikTokAppID: Use to config TikTok OpenSDK**
- **CFBundleURLTypes : Use TikTok App callback your App**
Insert the following XML snippet into the body of your file just before the final `</dict>` element.
```
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>tiktokopensdk</string>
    <string>tiktoksharesdk</string>
    <string>snssdk1180</string>
    <string>snssdk1233</string>
</array>
<key>TikTokAppID</key>
<string>$TikTokAppID</string>
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>$TikTokAppID</string>
    </array>
  </dict>
</array>
```
- Replace `$TikTokAppID` with your **App's Client Key**
Note:
- `tiktokopensdk` is used for logging in.
- `tiktoksharesdk` is used for sharing.
- `snssdk1233`, `snssdk1180` are used to check if the TikTok application is installed.
- The TikTok Open SDK auto-registers your Client Key when your App launches.
#### Make sure your app has access to Photo Library
Sharing pictures requires Photo Library access. Make sure a proper Privacy - Photo Library Usage Description is added in your Info.plist.
After the configuration, your Info.plist will look like the following.
### Step 4: Connect App delegate
You need to connect your `AppDelegate` class to the `TikTokOpenSDKApplicationDelegate.h` To do this, add the following code to your `AppDelegate.m` or `AppDelegate.swift` file.
```
import TikTokOpenSDK
@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
       TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, didFinishLaunchingWithOptions: launchOptions)
       return true
    }

    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {

        guard let sourceApplication = options[UIApplication.OpenURLOptionsKey.sourceApplication] as? String,
              let annotation = options[UIApplication.OpenURLOptionsKey.annotation] else {
            return false
        }

        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(app, open: url, sourceApplication: sourceApplication, annotation: annotation) {
            return true
        }
        return false
    }

    func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, open: url, sourceApplication: sourceApplication, annotation: annotation) {
            return true
        }
        return false
    }

    func application(_ application: UIApplication, handleOpen url: URL) -> Bool {
        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, open: url, sourceApplication: nil, annotation: "") {
            return true
        }
        return false
    }
}
```
If your application does not have a `SceneDelegate`, you are good to go! If your application makes use of the `SceneDelegate`, you will need to add the following function to your `SceneDelegate` file.
```
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

  func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
      guard let url = URLContexts.first?.url else {
          return
      }
      if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
          _ = appDelegate.application(UIApplication.shared, open: url, options: [:])
      }
  }

}
```
#### API Instructions
**TikTokOpenSDKApplicationDelegate**
Log Delegate
```
protocol TikTokOpenSDKLogDelegate {
    func onLog(_ logInfo: String) { }
}
```
TikTok internal log in level ERROR or Warning will callback in this method. You need to register log delegate in TikTokOpenSDKApplicationDelegate
Usage:
```
TikTokOpenSDKApplicationDelegate.sharedInstance().logDelegate = self
```
Check TikTok is installed:
```
func isAppInstalled() -> Bool
```
**BDOpenPlatformObjects**
The definition of basic classes (Request or Response) to SDK.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Video Kit With Objective-C.md

Docs
# Video Kit with Objective-C
[There is a new version of this SDK: Share Kit for iOS](https://developers.tiktok.com/doc/share-kit-ios-quickstart-v2)
## Introduction
Video Kit allows users to share videos and photos from your app to TikTok. Make sure your app has access to Photo Library.
Now we support long video sharing (> 1min) for up to 10 mins. Actual supported video duration may vary based on region.
## Preparation
[Before you start sharing, you need to complete all of the configurations listed in Getting Started](https://developers.tiktok.com/doc/getting-started-ios-quickstart-objective-c) with the TikTok SDK for iOS.
You can complete the sharing step by step：
### Step 1 : Import Header
Import TikTokOpenSDKShare.h
```
#import <TikTokOpenSDK/TikTokOpenSDKShare.h>
```
### Step 2 : Construct a Share Request
Construct a share request.
```
TikTokOpenPlatformShareRequest *req = [[TikTokOpenPlatformShareRequest alloc] init];
```
### Step 3 : Required Parameters
Set the shared resource type. Currently we support images and videos.
```
req.mediaType = TikTokOpenSDKShareMediaTypeImage;
//Or
req.mediaType = TikTokOpenSDKShareMediaTypeVideo;
```
---
Set share localIdentifiers as PHAsset.
e.g
```
NSMutableArray<NSString *> *mediaLocalIdentifiers = [NSMutableArray array];
for (PHAsset *asset in self.selectedAssets) {
    [mediaLocalIdentifiers addObject:asset.localIdentifier];
}
req.localIdentifiers = [mediaLocalIdentifiers copy];
```
Note:
- The aspect ratio of the images or videos should between: [1/2.2, 2.2]
- If mediaType is Image:
- The number of images should be more than one and up to 12.
- If mediaType is Video:
- Total video duration should be longer than 1 seconds.
- No more than 12 videos can be shared
- Videos with brand logo or watermark will lead to the videos being deleted or the respective accounts disabled. Make sure your application shares content without a watermark.
### Step 4 : Optional Parameters
**State**
You can customize a string to identify a share. The same state will be present in the respond.
You can bind you information with this ShareID.
```
req.state = @"a47e57c6c559acb88a9569da66ee5f65e0f779c9";
```
### Step 5 : Send Share Request
Call `-[``TikTokOpenSDKShareRequest`` sendShareRequestWithCompleteBlock:]` method to send the share request .
It will open the TikTok app and publish the content. Users can stay in TikTok or go back to your App after sharing.
If the user goes back to your app, you can receive a callback in CompleteBlock.
When any error happens, the response will have an error code with the following mapping:

| **TikTokOpenSDKErrorCode** | **errorCode** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKSuccess | 0 | Shared success. |
| TikTokOpenSDKErrorCodeCommon | -1 | Common error type e.g. network error. |
| TikTokOpenSDKErrorCodeUserCanceled | -2 | User Canceled share in TikTok. |
| TikTokOpenSDKErrorCodeSendFailed | -3 | User publish content failed. |
| TikTokOpenSDKErrorCodeAuthDenied | -4 | Auth denied. |
| TikTokOpenSDKErrorCodeUnsupported | -5 | Unsupported. |

If the error code does not make it easy for you to locate a specific error, you can use 'respond.shareState` for detail message. SDK version need 2.0.8 or higher.
The following map defines the Sharing state and specific issues.

| **TikTokOpenSDKShareRespState** | **value** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKShareRespStateSuccess | 20000 | Success. |
| TikTokOpenSDKShareRespStateUnknownError | 20001 | Unknown or current SDK version unclassified error. |
| TikTokOpenSDKShareRespStateParamValidError | 20002 | Params parsing error, media resource type difference you pass. |
| TikTokOpenSDKShareRespStateSharePermissionDenied | 20003 | Not enough permissions to operation. |
| TikTokOpenSDKShareRespStateUserNotLogin | 20004 | User not logged in. |
| TikTokOpenSDKShareRespStateNotHavePhotoLibraryPermission | 20005 | TikTok has no album permissions. |
| TikTokOpenSDKShareRespStateNetworkError | 20006 | TikTok Network error. |
| TikTokOpenSDKShareRespStateVideoTimeLimitError | 20007 | Video length doesn't meet requirements. |
| TikTokOpenSDKShareRespStatePhotoResolutionError | 20008 | Photo doesn't meet requirements. |
| TikTokOpenSDKShareRespTimeStampError | 20009 | Timestamp check failed. |
| TikTokOpenSDKShareRespStateHandleMediaError | 20010 | Processing photo resources failed. |
| TikTokOpenSDKShareRespStateVideoResolutionError | 20011 | Video resolution doesn't meet requirements. |
| TikTokOpenSDKShareRespStateVideoFormatError | 20012 | Video format is not supported. |
| TikTokOpenSDKShareRespStateCancel | 20013 | Sharing canceled. |
| TikTokOpenSDKShareRespStateHaveUploadingTask | 20014 | Another video is currently uploading. |
| TikTokOpenSDKShareRespStateSaveAsDraft | 20015 | Users store shared content for draft or user accounts are not allowed to post videos. |
| TikTokOpenSDKShareRespStatePublishFailed | 20016 | Post share content failed. |
| TikTokOpenSDKShareRespStateMediaInIcloudError | 21001 | Downloading from iCloud failed. |
| TikTokOpenSDKShareRespStateParamsParsingError | 21002 | Internal params parsing error. |
| TikTokOpenSDKShareRespStateGetMediaError | 21003 | Media resources do not exist. |

Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Video Kit With Swift.md

Docs
# Video Kit with Swift
[There is a new version of this SDK: Share Kit for iOS](https://developers.tiktok.com/doc/share-kit-ios-quickstart-v2)
This guide explains how to integrate your app with Video Kit in Swift. Long videos with a duration of up to ten minutes can be shared. The allowed duration may vary based on the region.
## Preparation
[[You are required to configure your app on TikTok for Developers website](https://developers.tiktok.com/). See Getting Started with TikTok SDK for iOS](https://developers.tiktok.com/doc/getting-started-ios-quickstart-swift) for more information.
Your app must have access to the user's photo library to successfully share videos to TikTok.
## Create a Share Request
Import the TikTokOpenShareSDK module and create a share request, as shown in the code snippet below.
Your app object is required to maintain a strong reference to the request to successfully receive the response callback. You can discard it once you have handled the response.
Set the following fields in the share request object:
- `localIdentifiers`: List of media. Media can either be all videos or all images.
- `mediaType`: The type of media you want to share.
- `shareFormat`:  Refer to the Share Formats section in this guide.
```
import TikTokOpenShareSDK

let shareRequest = TikTokShareRequest()
shareRequest.localIdentifiers = [...]
shareRequest.mediaType = .video
shareRequest.shareFormat = .normal
shareRequest.send { response in
    let shareResponse = response as? TikTokShareResponse else { return }
}
```
## Share Formats
You can use the `shareFormat` field in the share request object to share images or videos to TikTok in different formats.
- `.normal`: The default share format. This format allows your app to share image(s) or video(s), as is, to TikTok.
- `.greenScreen`: The green screen format provides a seamless experience for users to apply a video or image directly to the background of the green screen effect. Green screen videos use one video or image as the background and the creator's figure is in the front.
- The green screen feature is supported only on TikTok version 25.0.0 and later.
- The `.greenScreen` field applies only when sharing a single video or single image. If multiple videos or images are shared, then the `shareFormat` field will be ignored.
- If the application of the green screen effect fails on the TikTok app, the user is prompted to continue with regular sharing.
**Note:**
- The aspect ratio of images or videos should be between: [1/2.2, 2.2]
- A maximum of 35 images can be shared.
- A maximum of 12 videos can be shared.
- [You must be authorized to use any TikTok brand logos and watermarks. See TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal) for more details.
## Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-ios-handling-errors) for more details.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Android FileProvider.md

Docs
# Android Support for FileProvider
## Getting started
## Step 1: Integrate the fileprovider SDK
```
// Add the following to gradle：
repositories {
    maven { 
        url 'https://dl.bintray.com/aweme-open-sdk-team/public'
    }
} 
    
dependencies {
    implementation 'com.bytedance.ies.ugc.aweme:opensdk-oversea-external:0.1.4.1'
}
```
## Step 2: Integration
- In the Application onCreate，initialize TikTokOpenApiFactory
```
@Overridepublic void onCreate() {
 super.onCreate();
    String clientkey = "[Client Key]";
    TikTokOpenApiFactory.init(new TikTokOpenConfig(clientkey));
}
```
- Add permissions to your Android Manifest, and setup callback to your activity
```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /> 
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
// If you have a custom activity to receive callback, you can skip this step
<activity     android:name=".tiktokapi.TikTokEntryActivity"               
  android:launchMode="singleTask"
  android:taskAffinity="[Your package name]" 
  android:exported="true">
</activity>
```
TikTok 12.5.0 and above supports FileProvider. Below are the instructions to support FileProvider.
## FileProvider Usage
- Settings
In your app's AndroidManifest.xml, add the following settings as follows:
```
<provider  android:name="android.support.v4.content.FileProvider"
  android:authorities="${applicationPackageName}.fileprovider"
  android:exported="false"
  android:grantUriPermissions="true">
  <meta-data
    android:name="android.support.FILE_PROVIDER_PATHS"
    android:resource="@xml/file_provider_paths" />
</provider>
```
In res/xml (please create the directory if it doesn't exist), add a file file_provider_paths.xml with the content:
```
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-files-path name="sharedata" path="shareData/"/>
</paths>
```
external-files-path represents the files in the root of your app's external storage area. The root path of this subdirectory is the same as the value returned by Context.getExternalFilesDir(null)
You can also support other paths for example:
```
<files-path name="name" path="path" /> // Subdirectory returned by Context.getFilesDir()
<cache-path name="name" path="path" /> // Subdirectory returned by Contextget.CacheDir()
```
[For more information, check out this page](https://developer.android.com/reference/androidx/core/content/FileProvider).
- Using the FileProvider API
FileProvider converts a path file a content://URI format
```
public String getFileUri(Context context) {
     String filePath = context.getExternalFilesDir(null).p + "/shareData/test.png";
    // The filePath needs conforms to the path in the xml/file_provider_path file in order to be sharable
    File file = new File(filePath);
    // Use contentPath for sharing
    String contentPath = getFileUri(context, file);
 // The package name here must be consistent with what was provided in the AndroidManifest.xml's authorities.
    Uri contentUri = FileProvider.getUriForFile(context, 
        "com.example.app.fileprovider",file);
    // Authorize permission for TikTok build variants
    context.grantUriPermission("com.zhiliaoapp.musically",  
        contentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
    context.grantUriPermission("com.ss.android.ugc.trill",  
        contentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
    return contentUri.toString(); // contentUri.toString() should be prefixed with "content://"
}
```
- Sharing photos
```
TiktokOpenApi tiktokOpenApi = TikTokOpenApiFactory.create(this);
if (tiktokOpenApi.isShareSupportFileProvider() &&
        android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
    ArrayList<String> images = new ArrayList<>();
    images.add(xxx);  // Pass FileProvider formatted list here
    Share.Request request = new Share.Request();
    ImageObject imageObject = new ImageObject();
    imageObject.mImagePaths = images;
    MediaContent mediaContent = new MediaContent();
    mediaContent.mMediaObject = imageObject;
    request.mMediaContent = mediaContent;
    tiktokOpenApi.share(request);
} else {
    Toast.makeText(TestFileProviderActivity.this, "Unsupported version", Toast.LENGTH_LONG).show();
}
```
- Sharing videos
```
if (tiktokOpenApi.isShareSupportFileProvider() &&
        android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
 
    ArrayList<String> videos = new ArrayList<>();
    videos.add("video path"); // Pass FileProvider formatted list here
    Share.Request request = new Share.Request();
    VideoObject videoObject = new VideoObject();
    videoObject.mVideoPaths = videos;
    MediaContent content = new MediaContent();
    content.mMediaObject = videoObject;
    request.mMediaContent = content;
    tiktokOpenApi.share(request);
} else {
    Toast.makeText(TestFileProviderActivity.this, "Unsupported version", Toast.LENGTH_LONG).show();
}
```
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Android.md

Docs
[There is a new version of this SDK: Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart)
# Android Quickstart
Integrating our open SDK can help you leverage TikTok's open platform capabilities, such as Login Kit, Sound Kit, sharing videos to TikTok, and more coming soon. We hope to help you enhance your app's discovery and engagement, as well as provide another location for your users to share their favorite content for the world to see.
## Getting started
Below is a quick start for you to apply the TikTok SDK to your application. You should confirm that your project has a **Minimum ****API**** level of 16: Android 4.1 (Jelly Bean)** or higher.
### Step 1: Configure TikTok App Settings for Android
Use the Developer Portal to apply for Android client_key and client_secret access. Upon application approval, the Developer Portal will provide access to these keys.
### Step 2: Install the SDK and Setup Android Project
- In Project window, switch to "Android" view tab and open Gradle Scripts > build.gradle (Project). Then add the following repository in the repositories{} section. For example:
```
repositories {
    maven { url "https://artifact.bytedance.com/repository/AwemeOpenSDK" }
}
```
- Open Gradle Scripts > build.gradle (Module: app) and add the following implementation statement to the dependencies{} section:
```
dependencies {
    implementation 'com.bytedance.ies.ugc.aweme:opensdk-oversea-external:0.2.1.2'
}
```
- Edit your Application
First you need to initialize `TikTokOpenApiFactory` by using client key in your custom Application.
```
@Override
public void onCreate() {
    super.onCreate();
    String clientKey = "[CLIENT_KEY]";
    TikTokOpenConfig tiktokOpenConfig = new TikTokOpenConfig(clientKey);
    TikTokOpenApiFactory.init(new TikTokOpenConfig(tiktokOpenConfig));
}
```
- Edit Your Manifest
- Open the **/app/manifest/AndroidManifest.xml** file.
- Register `TikTokEntryActivity` for receiving callbacks in Manifest. If you have customized an activity to receive callbacks, you may skip this step.
```
// If you have customized activity to receive callbacks, you can skip the step
<activity
    android:name=".tiktokapi.TikTokEntryActivity"
    android:exported="true">
</activity>
```
Note:
- Due to changes in Android 11 regarding package visibility, when impementing Tiktok SDK for devices targeting Android 11 and higher, add the following to the Android Manifest file:
```
<queries>
    <package android:name="com.zhiliaoapp.musically" />
    <package android:name="com.ss.android.ugc.trill" />
</queries>
```
- Excellent! Now, **sync** your project and get the latest version of SDK package.
At this point, you should already set up the basic development environment. Next please refer to the feature access doc for further integrating.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Download.md

Docs
[There is a new version of this SDK: Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart)
# Download
[You can download a sample app for more details. See AndroidSDKDemo](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/app-overseaexternal-release-0.2.0.2.apk) .
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Handling Errors.md

Docs
# Handling Android Errors
In the table below, each row represents error code. For further information please see the `CommonConstants`.

| **ErrorCode** | **Description** |
| --- | --- |
| 0 | Success. |
| -1 | Unknown error. |
| -2 | User cancelled. |
| -3 | Send failed. |
| -4 | Auth denied. |
| -5 | Unsupported. |
| -12 | Network not connected. |
| -13 | Network connection timed out. |
| -14 | Network Timeout. |
| -15 | Network IO error. |
| -16 | Network unknown host error. |
| -21 | Network ssl error. |
| -30 | User cancel login or login failure. |

### For Share errors
If the error code does not make it easy for you to locate a specific error, you can use 'response.subErrorCode' for detail message. SDK version needs to be 0.0.1.5 or higher and TikTok version needs to be 14.4.0 or higher.

| **response.subErrorCode** | **Description** |
| --- | --- |
| 20002 | Params parsing error. |
| 20003 | Not enough permissions to operation. |
| 20004 | User not login. |
| 20005 | TikTok has no album permissions. |
| 20006 | TikTok Network error. |
| 20007 | Video length doesn't meet requirements. |
| 20008 | Photo doesn't meet requirements. |
| 20010 | Processing photo resources failed. |
| 20011 | Video resolution doesn't meet requirements. |
| 20012 | Video format is not supported. |
| 20013 | Sharing canceled. |
| 20015 | Users store shared content for draft or user accounts are not allowed to post videos. |
| 22001 | Unsupported resolution. |

### For Authentication errors
#### Universal

| **ErrorCode** | **Description** |
| --- | --- |
| 0 | Success. |
| 2100004 | The system is busy. Please try again later. |
| 2100005 | Invalid parameter. |
| 2100007 | No permission operation. |
| 2100009 | The user is banned from using this operation. |
| 2190001 | Quota has been used up. |
| 2190004 | The application has not obtained this ability. Please register for it on developer portal. |
| 2190015 | Request parameter access_token openid does not match. |

#### OAuth

| **ErrorCode** | **Description** |
| --- | --- |
| 10002 | Parameter error. |
| 10003 | Illegal application configuration. |
| 10004 | Illegal authorization scope. |
| 10005 | Missing parameters. |
| 10006 | Illegal redirection URI needs to be consistent with the "authorized callback domain" in the app configuration. |
| 10007 | Authorization code expired. |
| 10008 | Illegal call credentials. |
| 10009 | Illegal parameter. |
| 10010 | Refresh_token expired. |
| 10011 | The application package name is inconsistent with the configuration. |
| 10012 | App is under review and cannot be authorized. |
| 10013 | Client key or client secret error. |
| 10014 | The authorized client key is inconsistent with the access token obtained. |
| 10015 | Application type error, such as using the client_key of APP application for PC application. |
| 10017 | Authorization failed, the signature information needs to be completed. |
| 2190002 | Invalid access_token. |
| 2190003 | The user has not authorized the api. |
| 2190008 | Access_token expired, please refresh or re-authorize. |
| 6007061 | TikTok app version is too low. To continue, update to the latest version of the app. |
| 6007062 | This feature is not available for your account due to the age restriction. Try using another account. |

Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Login Kit with Android.md

Docs
[There is a new version of this SDK: Login Kit for Android](https://developers.tiktok.com/doc/login-kit-android-quickstart-v2)
# Login Kit for Android
## Overview
[This guide explains how to integrate with Login Kit for Android using Swift. Once authenticated users authorize your app, you can access their basic TikTok profile data including their display name and avatar. Additional data access may require approval for additional Scopes. Learn more on Scopes Overview](https://developers.tiktok.com/doc/scopes-overview).
## Prerequisites
[[Obtain a client key and client secret by logging in to Developer Portal](https://developers.tiktok.com/apps/) and selecting your app. Refer to the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-android-quickstart) for detailed steps. You must also provide a signing key for your Android app, as described below.
### Android App Signing Key
While registering your app for the Android platform on Developer Portal, you'll be asked to submit a signing key for your Android app. That signing key is the MD5 hex digest of your installed release app which will be used as the signature. It looks similar to something like: `114326e82c81e639a52e5c023100f12a`.
There are 2 methods for obtaining the signature of the Android installation package:
- Obtained in the code, but you must know the package name of the installation package.
```
PackageManager manager = getPackageManager();
/** Get the package information of the specified package name including the signature through the package manager **/
PackageInfo packageInfo = null;
try {
    packageInfo = manager.getPackageInfo("your package name", PackageManager.GET_SIGNATURES);
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}

/** Get the signature array through the returned package information **/
Signature[] signatures = packageInfo.signatures;
String ss = MD5.hexdigest(signatures[0].toByteArray());
if(ss != null) {
    Toast.makeText(this, "signature" + ss, Toast.LENGTH_LONG).show();
} else {
    Toast.makeText(this, "No signature", Toast.LENGTH_LONG).show();
}

/** Create an MD5 tool class **/
public class MD5 {
    private static final char[] hexDigits = { 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102 };

    public static String hexdigest(String paramString) {
        try {
            String str = hexdigest(paramString.getBytes());
            return str;
        } catch (Exception localException) {
        }
        return null;
    }

    public static String hexdigest(byte[] paramArrayOfByte) {
        try {
            MessageDigest localMessageDigest = MessageDigest.getInstance("MD5");
            localMessageDigest.update(paramArrayOfByte);
            byte[] arrayOfByte = localMessageDigest.digest();
            char[] arrayOfChar = new char[32];
            int i = 0;
            int j = 0;
            while (true) {
                if (i >= 16)
                    return new String(arrayOfChar);
                int k = arrayOfByte[i];
                int m = j + 1;
                arrayOfChar[j] = hexDigits[(0xF & k >>> 4)];
                j = m + 1;
                arrayOfChar[m] = hexDigits[(k & 0xF)];
                i++;
            }
        } catch (Exception localException) {
        }
        return null;
    }
}
```
- Inside of a terminal, enter the directory where *.jks is located, then enter into the command line:
```
keytool -list -v -keystore [xxx] -keypass [xxx]
```
Get the output MD5 value, then remove the ":" to obtain the required 32-character signature.
## Android Integration
### Request User Authorization
- Create an instance of `TiktokOpenApi`.
- Create an `Authorization.Request` instance and set the following required parameters:
- `request.scope = ``user.info``.basic`. If you are approved additional scopes , include them using comma-separated list.
- `request.state = "xxx"` . This is used to maintain the status of your request and callback. Verify that the `state` parameter returned in the callback matches what you sent earlier.
- Call the method `authorize()` on your instance of `TiktokOpenApi` .
```
// STEP 1: Create an instance of TiktokOpenApi
TiktokOpenApi tiktokOpenApi= TikTokOpenApiFactory.create(this);

// STEP 2: Create an instance of Authorization.Request and set parameters
Authorization.Request request = new Authorization.Request();
    request.scope = "user.info.basic";
    request.state = "xxx";
    return tiktokOpenApi.authorize(request);

// 3. Invoke the authorize method
tiktokOpenApi.authorize(request);
```
After successful authorization, the user will be brought back to your app via the `TikTokEntryActivity`.
### Receive Callbacks
We provide two ways for you to receive the callback data from TikTok:
- Create new activity named `TikTokEntryActivity` in your Android app and implement the `TikTokApiEventHandler` interface.
- **Note**: The path of the activity should be in the format: `{your-p``ackage``-``name``}``.tiktokapi.TikTokEntryActivity`. For example, `com.``mycoolapp``.tiktokapi.TikTokEntryActivity`.
The following example demonstrates how to use the `TikTokEntryActivity` to receive the callback data:
```
class TikTokEntryActivity extends Activity implements IApiEventHandler {

   TiktokOpenApi ttOpenApi;
   @Override
   public void onCreate(@Nullable Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       ttOpenApi= TikTokOpenApiFactory.create(this);
       ttOpenApi.handleIntent(getIntent(),this); // receive and parse callback
   }
   @Override
   public void onReq(BaseReq req) {
   }
   @Override
   public void onResp(BaseResp resp) {
       if (resp instanceof Authorization.Response)  {
          Authorization.Response response = (Authorization.Response) resp;
          Toast.makeText(this, " code：" + response.errorCode + " errorMessage：" + response.errorMsg, Toast.LENGTH_SHORT).show();
      }
   }
   @Override
   public void onErrorIntent(@Nullable Intent intent) {
       Toast.makeText(this, "Intent Error", Toast.LENGTH_LONG).show();
   }
}
```
- Alternatively, you can customize your own activity to receive the callback. To do this, implement the interface `IApiEventHandler` and set your activity path by using parameter `callerLocalEntry`.
```
// request.callerLocalEntry = "com.xxx.xxx...activity";
```
To receive callbacks when people stay in TikTok, please register to receive a broadcast:
```
public static final String ACTION_STAY_IN_TT = "com.aweme.opensdk.action.stay.in.dy";
```
### Obtain Access Token
[Upload the `code` returned in the callback to your server-side and obtain a user access token. See Manage User Access Tokens](https://developers.tiktok.com/doc/legacy-user-access-guide) for more information.
### Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-android-handling-errors) for error handling and debugging.
Was this document helpful?


---
## SOURCE: Legacy Products/Legacy Mobile SDK/Android/Video Kit With Android.md

Docs
[There is a new version of this SDK: Share Kit for Android](https://developers.tiktok.com/doc/share-kit-android-quickstart-v2)
# Video Kit with Android
### Overview
This guide details how to enable sharing from your app to TikTok. After sharing successfully to TikTok, users will see your app's name in TikTok feed.
Note: The minimum TikTok version supporting sharing is 11.3.0.
Now we support long video sharing (> 1min) for up to 10 mins. Actual supported video duration may vary based on region.
### Prerequisites
Before you can share to TikTok from your App, make sure you have obtained a Client Key from TikTok and installed the TikTok SDK to your Android project. For details on these requirements, see Getting started.
[We recommend that developers targeting Android 7.0 and above use FileProvider to share. For more details, please refer to the document](https://developers.tiktok.com/doc/video-kit-android-android-fileprovider).
### Detailed Steps
[Follow the steps mentioned in the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-android-quickstart)
#### Send Share Request
- Create a `TiktokOpenApi` to send share request.
- Build share content for images/videos into the `TikTokMediaContent` model.
- Create Share.Request instance and set required parameters: `request.mMediaContent = [TikTokMediaContent]`.
- Call method `Share()` in `TiktokOpenApi` .
```
// 1.create TiktokOpenApi
TiktokOpenApi tiktokOpenApi= TikTokOpenApiFactory.create(this);

Share.Request request = new Share.Request();
// initialize the resource path, please provide absolute path
ArrayList<String> mUri = new ArrayList<>();
mUri.add ...

// 2.build share content for photos/videos into TikTokMediaContent
VideoObject videoObject = new VideoObject();
videoObject.mVideoPaths = mUri;
MediaContent content = new MediaContent();
content.mMediaObject = videoObject;

// 3.set required parameters
request.mMediaContent = content;

// or share multi-picture，here the size of mUri must >=2
ImageObject imageObject = new ImageObject();
imageObject.mImagePaths = mUri;
MediaContent mediaContent = new MediaContent();
mediaContent.mMediaObject = imageObject;
request.mMediaContent = mediaContent;


// 4.start share
tiktokOpenApi.share(request);
```
After a successful sharing session, a Dialog will prompt for the user to choose `Back to your App` or `Stay in TikTok`.
If you want to receive callbacks when people stay in TikTok , please register to receive a broadcast :
```
public static final String ACTION_STAY_IN_TT = "com.aweme.opensdk.action.stay.in.dy";
```
**Parameters in Share.Request**

| **Parameter** | **Usage** |
| --- | --- |
| mMediaContent | You can build share content for videos or photos using following models: 1. multi-Image: see `ImageObject`model. Note: The size of Images must be > 1 and <= 12. 2. single-video\multi-video: see `VideoObject`model. Then assign required parameter as `request.mMediaContent = [MediaContent]`; |
| callerLocalEntry | Set customized callback Activity by using `request.callerLocalEntry = "com.xxx.xxx...activity";`If this parameter is not set, TikTok will callback `TikTokEntryActivity`in default. |

#### Receive Callbacks
We provides two ways for you to receive the callback data from TikTok.
- Create new activity named "TikTokEntryActivity" in your app and implement TikTokApiEventHandler interface.
**Note**: The path of the activity should be your "package name" + .tiktokapi.TikTokEntryActivity. For example, "com.tiktok.opensdk.tiktokapi.TikTokEntryActivity".
The following example shows how to use TikTokEntryActivity to receive the callback data.
```
class TikTokEntryActivity extends Activity implements IApiEventHandler {

   TiktokOpenApi ttOpenApi;
   @Override
   public void onCreate(@Nullable Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       ttOpenApi= TikTokOpenApiFactory.create(this);
       ttOpenApi.handleIntent(getIntent(),this); // receive and parse callback
   }
   @Override
   public void onReq(BaseReq req) {
   }
   @Override
   public void onResp(BaseResp resp) {
       if (resp.getType() == TikTokConstants.ModeType.SHARE_CONTENT_TO_TT_RESP)  {
           Share.Response response = (Share.Response) resp;
           Toast.makeText(this, " code：" + response.errorCode + " errorMessage：" + response.errorMsg, Toast.LENGTH_SHORT).show();
       }
   }
   @Override
   public void onErrorIntent(@Nullable Intent intent) {
       Toast.makeText(this, "Intent Error", Toast.LENGTH_LONG).show();
   }
}
```
- You can also customize your own activity to receive the callback; just implement the interface `IApiEventHandler` and set your activity path by using parameter "callerLocalEntry".
```
// request.callerLocalEntry = "com.xxx.xxx...activity";
```
### Requirements for Media
- For Video:
- Minimum video duration must be 3 seconds.
- Supported video media type: .mp4.
- The minimum of the frame size should be no more than 1100.
- For multi-Video:
- The number of Videos can be no more than 12.
- For multi-Image:
- The number of images should be more than 1 and up to 12.
- Videos cannot contain brand logos or watermarks. Violating this guideline will lead to videos being deleted or accounts being banned. Make sure your applications share content without watermarks or brand logos.
#### Handling Errors
[For error handling and debugging, check out the list of Error Codes](https://developers.tiktok.com/doc/getting-started-android-handling-errors)
Was this document helpful?
