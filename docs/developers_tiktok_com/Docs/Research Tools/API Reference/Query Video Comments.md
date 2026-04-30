Docs
# Query Video Comments
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/video/comment/list/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |
| Content-Type | string | Content type for the return data | application/json |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields. Choose from the Comment Object fields. | **Complete list**: id, video_id, text, like_count, reply_count, parent_comment_id, create_time | Yes |

### Body Parameters
**Note**: In your query, you must request either `video_id` or `comment_id` depending on what data you want to retrieve. You may only request one or the other; both cannot be requested at the same time.
- Requesting `video_id` will return data for the specified video's comments.
- Requesting `comment_id` will return data for the specified comment's replies.

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| video_id | int64 | The ID of the video that the comments are made to | Yes |
| comment_id | int64 | The ID of the comment that the replies are made to | Yes |
| max_count | int64 | The number of comments in response. Default is 10, max is 100. It is possible that the API returns less comments than the max count due to reasons such as comments deleted by users etc. | No |
| cursor | int64 | The starting index of the comments in the response. | No |

### Example
`video_id`:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/comment/list/?fields=id%2Ctext' \
--header 'Authorization: Bearer clt.abcdefg' \
--header 'Content-Type: application/json' \
--data '{
   "video_id": 12345678901,
   "max_count": 100,
   "cursor":0
}'
```
`comment_id`:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/comment/list/?fields=id%2Ctext' \
--header 'Authorization: Bearer clt.abcdefg' \
--header 'Content-Type: application/json' \
--data '{
   "comment_id": 1234,
   "max_count": "100",
   "cursor":0
}'
```
# Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | ResearchVideoCommentsData | A list of comment objects for a given video |
| error | ErrorStructV2 | Error object |

##### ResearchVideoCommentsData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| comments | CommentObject | The metadata of a comment. | See example below |
| cursor | int64 | The cursor of the next page. | 1050 |
| has_more | bool | Whether there are more videos or not. | true |

##### Comment Object

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| id | int | The unique ID for the comment |
| text | string | The text within the comment |
| video_id | int | The ID of the video or item that the comment is under |
| parent_comment_id | int | The ID of the comment's parent comment, if any |
| like_count | int | The number of likes a comment has |
| reply_count | int | The number of replies a comment has |
| create_time | int | The unix timestamp that the comment was created on |

### Example
`video_id`:
```
{
    "data": {
        "comments": [
            {
                "text": "AWEEEEEE 🥰🥰🥰",
                "video_id": 1234563451201523412,
                "create_time": 1671491598,
                "id": 12345616934634134,
                "like_count": 50,
                "parent_comment_id": 1234561201524010,
                "reply_count": 10
            },
            ...
        ],
        "has_more": true,
        "cursor": 300
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202207280326050102231031430C7E754E"
    }
}
```
`comment_id`:
```
{
    "data": {
        "has_more": false,
        "comments": [
            {
                "parent_comment_id": 1234567876543,
                "reply_count": 0,
                "text": "Lalalaa",
                "create_time": 1740510402,
                "display_name": "test",
                "id": 12345678909876
            }
        ],
        "cursor": 1
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "20123456789876543"
    }
}
```
**Personal information (phone number, email and credit card account, etc) in the comments will be redacted. See the example below.**
Comment (original): "Could you please contact me? 4059233930 is my number. Hi Edmond, email Mwen numerow at acharles@emortgagecapital.com, epi map relew. Download “Temu” make an account then search up 23216471 then click accept."
Comment (returned by the API): "Could you please contact me? 40******30 is my number.
Hi Edmond, email Mwen numerow at a*******@********************, epi map relew.
Download “Temu” make an account then search up ****6471 then click accept."
Was this document helpful?