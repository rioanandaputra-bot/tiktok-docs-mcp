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