Docs
# Getting Started
This guide will show you how to use the Commercial Content API. Learn how to use the Commercial Content API to query ad data and fetch public advertiser data in the following use case example.
# View your client registration
[Once your application is approved, a research client will be generated for your project. You can view your approved research projects here](https://developers.tiktok.com/research/). Select a project from the list to see the research client details.
The provided **Client key** and **Client secret** are required to connect to the Commercial Content API endpoints. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).
**Note: **The client secret is a credential used to authenticate your connection to TikTok's APIs. Do not share this with anyone!
# Obtain a client access token
[Once you have obtained the client key and secret for your project, generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Commercial Content API endpoints.
# Query TikTok public content data
The cURL command below shows an example of how you can query the TikTok ads created in Italy between January 2, 2021 to January 9, 2021 with the keyword "coffee".
```
curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id' \
 -H 'authorization: bearer clt.example12345Example12345Example' \
 -d '{ 
         "filters": {
            "ad_published_date_range": {
                 "min": "20221001",
                 "max": "20230510"
             },
            "country_code": "IT"
         }, 
        "search_term": "coffee",
        "max_count": 20
    }'
```
## Pagination
If the total number of ads that match the search criteria is larger than the maximum number of ads that can be returned in a single request, the response data will be returned with different requests.

| **Field** | **Type** | **Description** | **Example** | **Required?** |
| --- | --- | --- | --- | --- |
| max_count | number | The maximum count of TikTok videos in the response. The default value is 10 and the maximum value is 50. | 12 | FALSE |
| search_id | string | The ID of a previous search to provide sequential calls for paging. | "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD" | FALSE |

### First page
When you send the first request, you do not need to set the `search_id` in the request body. In the http response, `has_more` and `search_id` are returned, which are used in the subsequent requests.
```
Try out this request:

curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id' \
  -H 'authorization: bearer clt.example12345Example12345Example' \
  -d '{ 
          "filters": {
              "ad_published_date_range": {
                 "min": "20221001",
                 "max": "20230510"
              },
              "country_code": "IT"
           }, 
          "search_term": "coffee",
          "max_count": 20
       }'
```
The following example data is returned from the response.
```
{
    "data": {
        "has_more": true,
        "search_id": "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD",
        "ads": [
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
curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id' \
  -H 'authorization: bearer clt.example12345Example12345Example' \
  -d '{ 
          "filters": {
              "ad_published_date_range": {
                 "min": "20221001",
                 "max": "20230510"
              },
              "country_code": "IT"
           }, 
          "search_term": "coffee",
          "max_count": 20,
          "search_id": "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD"
       }'
```
The following example data is returned from the response.
```
{
    "data": {
        "has_more": true,
        "search_id": "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI",
        "ads": [
            ...
        ]
    },
    "error": {
        ...
    } 
}
```
# Was this document helpful?