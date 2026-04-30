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