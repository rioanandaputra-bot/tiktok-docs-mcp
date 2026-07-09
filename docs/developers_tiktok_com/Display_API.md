# Display API

> Consolidated from 6 source files.

---
## SOURCE: Display API/Display API.md

Docs
# Overview
The Display API contains a set of HTTP-based APIs that your product can use to display a TikTok creator's videos and their profile information.
Your platform's influencers can display their TikTok profile identities and videos to enrich content, attract more audiences, and enable their followers to view their TikTok videos without leaving your platform.
## Components
Display API has three major APIs: `/v2/user/info/`, `/v2/video/list/`, and `/v2/video/query/`.
[**/v2/user/info/](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)****:** Get a TikTok user's basic profile information. This includes the user's open_id, avatar_url, display_name, profile_deep_link, and bio_description.
[**/v2/video/list/](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)****:** Get the metadata of a TikTok user's recently uploaded videos.
[**/v2/video/query/](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)****:** Get the metadata of TikTok a user's videos filtered by video Id.
## Permissions
- **video.list:** Read a user's public videos on TikTok.
- **user.info****.basic:** Read a user's profile info (open id, avatar, display name, ...).
## Example Use Cases
### Display User's TikTok Profile
Use the /v2/user/info/ API to get a TikTok user's profile data and then display their TikTok identity. In this example, when a visitor clicks the profile_deep_link, they will be redirected to the creator's profile page on the TikTok app or website.
### Display User's Self-Selected TikTok Videos
Use the /v2/video/list/ and /v2/video/query/ APIs to get the metadata of a TikTok user's videos and integrate an embedded video player into your product. In addition, you can design features to allow users to select their TikTok videos to present on their profile and enable their followers to watch the video in webview.
### Display User's Recent TikTok Videos
Use the /v2/video/list/ and /v2/video/query/ APIs to get the metadata of a TikTok user's videos and integrate an embedded video player into your product. In addition, you can design features to allow users to show their recent TikTok videos on your platform.
## Next Steps
[Get Started with Display API](https://developers.tiktok.com/doc/display-api-get-started)
Was this document helpful?

---
## SOURCE: Display API/Get Started.md

Docs
# Get Started
This guide will show you how to get an authorization code and an access token in order to utilize the Display APIs. We will use the Display APIs to display a TikTok user's profile and videos on your platform.
## Before You Start
You will need access to:
- A TikTok developer account on TikTok Developer Portal
- Approval for both a Login Kit and TikTok API products
- Granted `user.info``.basic` and `video.list` scopes for your app
- A TikTok account with a few posted videos
## Authorization
### Get an Authorization Code
Follow these documents to integrate with our login kit, and use your TikTok account to authorize and get an access token. You will need to set scope=user.info.basic,video.list.
- [iOS](https://developers.tiktok.com/doc/login-kit-ios-quickstart)
- [Android](https://developers.tiktok.com/doc/login-kit-android-quickstart-v2)
- [Web](https://developers.tiktok.com/doc/login-kit-web/)
After following one of the tutorials to get user authorization, you will be able to get an authorization code that looks like the following:
`wFPH5DePZMb07BPJvpWi-WotFlq1ISzFYQBDb9S9CBUQkGZRGW3zOAbYzhGXkoYkFx-aDeph0hTFk3l6ngGYuoixRvvZBWV1e3Q_BFoBELY*0!6410`
### Get an Access Token
[Follow this tutorial](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens/) to use the authorization code to retrieve the user's access token and open id.
```
{
    "data": {
        "access_token": "act.example12345Example12345Example",
        "captcha": "",
        "desc_url": "",
        "description": "",
        "error_code": 0,
        "expires_in": 86400,
        "log_id": "20220714041044010002007735002037040BAF34",
        "open_id": "abcdefgh-1a2b-123c4-ab12-abc123abc1234",
        "refresh_expires_in": 31536000,
        "refresh_token": "rft.example12345Example12345Example",
        "scope": "user.info.basic"
    },
    "message": "success"
}
```
## Display User's TikTok Profile
- Design and build a UI to host the TikTok account profile.
- [Call **GET /v2/user/info/](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)** API using access_token to get user profile information.
Example request:
```
curl -L -X GET 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url,display_name' \
-H 'Authorization: Bearer act.example12345Example12345Example'
```
Example response:
```
{
   "data":{
      "user":{
         "avatar_url":"https://p19-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/b17f0e4b3a4f4a50993cf72cda8b88b8~c5_168x168.jpeg",
         "open_id":"723f24d7-e717-40f8-a2b6-cb8464cd23b4",
         "union_id":"c9c60f44-a68e-4f5d-84dd-ce22faeb0ba1",
         "display_name": "Tik Toker"
      }
   },
   "error":{
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
- Parse the returned profile information and display it in your UI.
## Display User's Recent TikTok Videos
- Design and build your interface to encourage users to authorize displaying their most recent TikTok videos on your platform.
- [Call **POST /v2/video/list/](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)** using the access token to get a list of a specified user's most recent videos. The returned videos are sorted by their creation time in descending order.
Example request:
```
curl -L -X POST 'https://open.tiktokapis.com/v2/video/list/?fields=id,title,video_description,duration,cover_image_url,embed_link' \
-H 'Authorization: Bearer act.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "max_count": 20
}'
```
Example response:
```
{
    "data": {
        "videos": [
            {
                "id": "7080213458555737986",
                "title": "video 1",
                "video_description": "Test video 1",
                "duration": 2,
                "cover_image_url": "https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/49b5eb2713004dfa429eab84566e~tplv-noop.image?x-expires=1657851434&x-signature=FjrSxXTCWpQUM57Ao2SNsoLtf%2B0%3D",
                "share_url": "https://www.tiktok.com/@user_id/video/7080213458555737986?utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
                "embed_link": "https://www.tiktok.com/static/profile-video?id=7080213458555737986&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
            },
            {
                "id": "7080217258545735586",
                "title": "video 2",
                "video_description": "Test video 2",
                "duration": 3,
                "cover_image_url": "https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/49b5eb2713004dfa422dab84566e~tplv-noop.image?x-expires=1657851434&x-signature=FjrSxXTCWpQUM57Ao2SNsoLtf%2B0%3D",
                "share_url": "https://www.tiktok.com/@user_id/video/7080217258545735586?utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
                "embed_link": "https://www.tiktok.com/static/profile-video?id=7080217258545735586&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
            },
            ...
        ],
        "cursor": 1646883959000,
        "has_more": true
    },
    "error": {
        "code":"ok",
        "message":"",
        "log_id":"20220829194722CBE87ED59D524E727021"
    }
}
```
- Use the URLs in `embed_link` to open webviews and display videos as needed.
- Schedule background jobs to keep the access token up-to-date using Refresh Token. This will fetch and update the user's recent TikTok videos every 12 hours.
## Display User's Self-Selected TikTok Videos
Design and build a UI to encourage users to bring their TikTok videos to your platform.
- [Call **POST /v2/video/list/](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)** using an access token to get a list of user's videos. This part is the same as displaying a user's recent TikTok videos.
- Design the UI to display the videos with `cover_image_url` and `duration`.
- Allow the user to select videos to add to your app. After they complete their selection, save the metadata of the user's selected videos. Design the UI to present user's TikTok videos.
- [The `cover_image_url` will expire after some time, so we need to call **POST /v2/video/query/](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)**** **to query the video metadata filtered by video_id.
Example request:
```
curl -L -X POST 'https://open.tiktokapis.com/v2/video/query/?fields=id,cover_image_url,embed_link' \
-H 'Authorization: Bearer act.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "filters": {
        "video_ids": [
            "7077642457847994444",
            "7080217258529732386"
        ]
    }
}'
```
Example response:
```
{
    "data": {
        "videos": [
            {
                "cover_image_url": "https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/c5e4394893164bbf90605100e8bdd45c~tplv-noop.image?x-expires=1657852284&x-signature=e%2FMfIsqpUUUoXBe0mXuz5wVdfhc%3D",
                "id": "7077642457847994444",
                "embed_link": "https://www.tiktok.com/static/profile-video?id=7077642457847994444&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
            },
            {
                "cover_image_url": "https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0037/49b5eb2713004cc2be8a429eab84566e~tplv-noop.image?x-expires=1657852284&x-signature=kNFfMCgOsal78%2BpX8alQooUpNbo%3D",
                "id": "7080217258529732386",
                "embed_link": "https://www.tiktok.com/static/profile-video?id=7080217258529732386&hide_author=1&utm_campaign=tt4d_open_api&utm_source=awbx37vxswqcvsf6",
            }
        ],
        "cursor": 0,
        "has_more": false
    },
    "error": {
        "code":"ok",
        "message":"",
        "log_id":"20220829194722CBE87ED59D524E727021"
    }
}
```
- Open a web view with the url `embed_link` to consume the video on user clicks. Users can now view TikTok videos on your platform to know more about the author.
Was this document helpful?

---
## SOURCE: Display API/API Reference/API Reference.md

Docs
# Get User Info
[There is a migration plan related to this API. Learn more here](https://developers.tiktok.com/bulletin/user-info-scope-migration).
## Overview
The `/v2/user/info/` endpoint returns some basic information for a given TikTok user.

| **HTTP ****URL** | https://open.tiktokapis.com/v2/user/info/ |
| --- | --- |
| **HTTP Method** | GET |
| **Scope** | [Needs relevant scopes](#user_object) to be authorized by the TikTok user through the authorization flow. |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | true |

### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The set of user fields to request for | open_id,union_id,avatar_url | true |

### Example
```
curl -L -X GET 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url' \
-H 'Authorization: Bearer act.example12345Example12345Example'
```
## Response

| **Key** | **Type** |
| --- | --- |
| data | map<string, User Object> |
| error | [Error Object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

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
         "open_id":"723f24d7-e717-40f8-a2b6-cb8464cd23b4",
         "union_id":"c9c60f44-a68e-4f5d-84dd-ce22faeb0ba1"
      }
   },
   "error":{
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
Was this document helpful?

---
## SOURCE: Display API/API Reference/List Videos.md

Docs
# List Videos
## Overview
The `/v2/video/list/` endpoint can return a paginated list for the given user's **public** TikTok video posts, sorted by `create_time` in descending order.

| **HTTP URL** | https://open.tiktokapis.com/v2/video/list/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | video.list |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | true |
| Content-Type | string | indicate the original media type of the resource | application/json | true |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| cursor | int64 | Cursor for pagination. If `response.has_more`is true, pass in the `response.cursor`to the next request will yield the results for the next page. _Note: the cursor value is a __UTC__Unix timestamp in milli-seconds. You can pass in a customized timestamp to fetch the user's videos posted before the provided timestamp._ | 1643332803000 | false |
| max_count | int32 | The maximum number of videos that will be returned from each page. Default is 10. Maximum is 20. | 20 | false |

### Example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/video/list/?fields=cover_image_url,id,title' \
-H 'Authorization: Bearer act.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "max_count": 20
}'
```
## Response

| **Key** | **Type** |
| --- | --- |
| data | map<string, UserVideoListPostResponseData> |
| error | [Error Object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

### UserVideoListPostResponseData

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| videos | [list<Video Object](https://developers.tiktok.com/doc/tiktok-api-v2-video-object)> | A list of video objects |
| cursor | i64 | Cursor for pagination. If `response.has_more`is true, pass in the `response.cursor`to the next request will yield the results for the next page. _Note: the cursor value is a __UTC__Unix timestamp in milli-seconds. You can pass in a customized timestamp to fetch the user's videos posted before the provided timestamp._ |
| has_more | bool | Whether there is more videos |

### Example
```
{
   "data":{
      "videos":[
         {
            "cover_image_url":"https://p16-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/979e93dbc5df40198f7ac935fb3e3342~tplv-noop.image?x-expires=1659000367&x-signature=EZIo1pVYVGYh%2FaNNaHHlbWEvw%2BM%3D",
            "id":"12345123451234512345",
            "title": "Video Title",
         }
      ],
      "cursor":1643332803000,
      "has_more":false
   },
   "error": {
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
Was this document helpful?

---
## SOURCE: Display API/API Reference/Query Videos.md

Docs
# Query Videos
## Overview
Given an authorized user and a list of video IDs, the `/v2/video/query/` endpoint verifies that the videos belong to the user and returns video details. It can be used to refresh the given videos' cover image URL TTL. Up to 20 video IDs can be included per request.

| **HTTP URL** | https://open.tiktokapis.com/v2/video/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scope** | video.list |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | true |
| Content-Type | string | indicate the original media type of the resource | application/json | true |

### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | [The requested fields, choose from Video Object](https://developers.tiktok.com/doc/tiktok-api-v2-video-object)'s fields: [id, create_time, cover_image_url, share_url, video_description, duration, height, width, title, embed_html, embed_link, like_count, comment_count, share_count, view_count] | id,title,fps | true |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| filters | VideoFilters | Filter videos by video_ids | { "video_ids":[ "7077642457847991554", "7080217258529737986" ] } | true |

### Request Example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/video/query/?fields=id,title' \
-H 'Authorization: Bearer act.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "filters": {
        "video_ids": [
            "1234123412345678567",
            "1010102020203030303"
        ]
    }
}'
```
## Response

| **Key** | **Type** |
| --- | --- |
| data | map<string, QueryUserVideoResponseData> |
| error | [Error object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

### QueryUserVideoResponseData

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| videos | [list<video object](https://developers.tiktok.com/doc/tiktok-api-v2-video-object)> | A list of video objects |

### Example
```
{
   "data":{
      "videos":[
         {
            "title":"Video 1",
            "id":"1234123412345678567"
         },
         {
            "title":"Video 2",
            "id":"1010102020203030303"
         }
      ]
   },
   "error": {
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
Was this document helpful?

---
## SOURCE: Display API/API Reference/Video Object.md

Docs
# Video Object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Unique identifier for the TikTok video. Also called "item_id" |
| create_time | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. |
| cover_image_url | string | A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a **TTL****of 6 hours.** |
| share_url | string | A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices. |
| video_description | string | The description that the creator has set for the TikTok video. Max length: 150 |
| duration | int32 | The duration of the TikTok video in seconds. |
| height | int32 | The height of the TikTok video. |
| width | int32 | The width of the TikTok video. |
| title | string | The video title. Max length: 150 |
| embed_html | string | HTML code for embedded video |
| embed_link | string | Video embed link of tiktok.com |
| like_count | int32 | Number of likes for the video |
| comment_count | int32 | Number of comments on the video |
| share_count | int32 | Number of shares of the video |
| view_count | int64 | Number of views of the video |

Was this document helpful?
