Docs
# Getting Started
This guide will show you how to use the Research API. Learn how to use the Research API to query video data and fetch public TikTok account data in the following use case example.
# View your client registration
[Once your application is approved, a research client will be generated for your project. You can view your approved projects on your **Research projects](https://developers.tiktok.com/research/)** page. Select a project from the list to see the research client details.
The provided **Client key** and **Client secret** are required to connect to the Research API endpoints. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).
Warning: The client secret is a credential used to authenticate your connection to TikTok's APIs. Do not share this with anyone!
# Obtain a client access token
[Once you have obtained the client key and secret for your project, generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Research API endpoints.
# Query TikTok public content data
The cURL command below shows an example of how you can query the TikTok ID and like count of videos created in the US or Canada with the keyword `hello world` in the video description.
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 100,
    "cursor": 0,
    "start_date": "20181207",
    "end_date": "20181207",
    "is_random": false}
'
```
## Query condition
Similar to the WHERE clause in SQL, a condition can be used to filter data returned in a query operation. The above request is equivalent to the following SQL query:
```
 SELECT id,like_count FROM video_table WHERE region_code IN ["US", "CA"] AND create_date > 20220615
```

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| field_name | string | The field name this condition is restricting | "region_code" | Yes |
| operation | string | The comparison logic of this condition. One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" | "GT" | Yes |
| field_values | list[string] | A list of values to be compared with | ["US", "IN"] | Yes |

**Note**: Approximate string matching (or fuzzy string searching) is used to match conditions.
### field_name
The following are the `field_name` values:
- `keyword`
- `create_date`
- `username`
- `region_code`
- `video_id`
- `hashtag_name`
- `music_id`
- `effect_id`
- `video_length`
### operation
The following are the `operation` values:
- `IN`: Tests if an expression matches any value in a list of values.
- `EQ`: Tests if an expression matches the specified value.
- `GT`: Tests if an expression is strictly greater than the specified value.
- `GTE`: Tests if an expression is greater than or equal to the specified value.
- `LT`: Tests if an expression is strictly less than the specified value.
- `LTE`: Tests if an expression is less than or equal to the specified value.
### AND, OR or NOT
Conditions are grouped by the following boolean operators:
- `AND`: Displays a record if all the conditions separated by `AND` are `TRUE`.
- `OR`: Displays a record if any of the conditions separated by `OR` is `TRUE`.
- `NOT`: Displays a record if all the conditions separated by `NOT` are `FALSE`.
## Pagination
If the total number of videos that match the query criteria is larger than the max number of videos that can be returned in a single request, the response data will be returned with different requests.

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| max_count | number | The max count of TikTok videos in response. default: 10, max: 100 | 12 | No |
| cursor | number | The starting index of TikTok videos in response. default: 0 | 100 | No |
| search_id | string | The ID of a previous search to provide sequential calls for paging | "7167072234702738478" | No |

### First page
When you send the first request, you do not need to set the `search_id` or `cursor` in the request body. In the http response, `cursor` and `search_id` are returned, which are used in the subsequent requests. Try out this request:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 100,
    "cursor": 0,
    "start_date": "20181207",
    "end_date": "20181207",
    "is_random": false}
'
```
The following example data is returned from the response.
```
{
    "data": {
        "cursor": 10,
        "has_more": true,
        "search_id": "7160776277492814854",
        "videos": [
            ...
        ]
    },
    "error": {
        ...
    }
 }
```
### Next page
With the cURL command below, you can get the next page of query results.
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 10,
          "cursor": 10,
          "start_date": "20220615",
          "end_date": "20220628",
          "search_id": "7160776277492814854"
}
'
```
The following example data is returned from the response.
```
{
    "data": {
        "cursor": 20,
        "has_more": true,
        "search_id": "7160776277492814854",
        "videos": [
            ...
        ]
    },
    "error": {
        ...
    } 
}
```
# Query TikTok public account information
With the cURL command below, you can query public TikTok account information by a TikTok handle.
```
curl --location --request POST 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
--header 'Authorization: bearer {{access_token}}' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username": "example_username"
}'
```

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | TikTok user's username | "example_username" | No |

The following example data is returned from the response.
```

{
    "data": {
        "username": "example_username",
        "video_count": 64,
        "avatar_url": "https://my-awesome-avatar",
        "display_name": "joe 1234567",
        "follower_count": 111,
        "likes_count": 4146,
        "bio_description": "joe joe",
        "following_count": 103,
        "is_verified": false
    },
    "error": {
        ...
    }
}
```
### Was this document helpful?