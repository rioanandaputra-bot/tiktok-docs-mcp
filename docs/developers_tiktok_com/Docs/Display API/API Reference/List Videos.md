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