Docs
# Query Commercial Content
Use POST /v2/research/adlib/commercial_content/query/ to query commercial content

| **HTTP URL** | https://open.tiktokapis.com/v2/research/adlib/commercial_content/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request
## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | The original media type of the resource. | application/json | true |

## Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields id create_timestamp create_date label brand_names creator videos | id,create_timestamp,brand_names,creator,videos | true |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below | true |
| max_count | i64 | The max number of results returned at once. The default value is 10, and the maximum value is 50. | 20 | false |
| search_id | string | A search_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" | false |

## Data structures
### RequestFilters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| content_published_date_range | DateRange | The time range during which the commercial contents were published. "min" needs to be after October 1st, 2022. | { "min": 20230102, "max": 20230109 } | true |
| creator_country_code | string | [The country of the commercial content's author. The default value is ALL. Supported countries: European Economic Area (EEA) countries Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) Note: United Kingdom and Switzerland are not included in this API | FR | false |
| creator_usernames | list<string> | The commercial contents' creators. | [ "joe123", "emma_lol" ] | false |

### DateRange

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| min | string | The first date of the range and this needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

## Request example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/commercial_content/report/?fields=ad_id,video_urls,business_name' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
   "filters":{
       "content_published_date_range": {
            "min": "20210102",
            "max": "20210109"
       },
       "creator_country_code": "FR"
   }
 }'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | QueryCommercialContentData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example
```
{
   "data": {
      "commercial_contents": [
         {
            "brand_names": [
               "My Awesome Co.",
               "HelloWorld Inc."
            ],
            "create_date": "20230109",
            "create_timestamp": 1696875852,
            "creator": {
               "username": "joe1234567"
            },
            "id": "v09044g40000ce6enu3c77u36l73sp20",
            "label": "Paid partnership",
            "videos": [
               {
                  "cover_image_url": "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf",
                  "url":"https://www.tiktok.com/@joe1234567/video/19384729204821234" 
               }
            ]
         }
      ],
      "has_more": "true",
      "search_id": "2837438294054038"
   },
   "error": {
      "code": "ok",
      "http_status_code": 200,
      "log_id": "202207280326050102231031430C7E754E",
      "message": ""
   }
}
```
## Data structures
### QueryCommercialContentData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| commercial_contents | list<CommercialContent> | The list of commercial contents. |  |
| has_more | bool | The flag that indicates if there are more items to be returned. | true |
| search_id | string | A search_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. If you update the`filters`in the request, please remove the `search_id`to avoid getting back unexpected results | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" |

### CommercialContent

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| id | i64 | The commercial content ID. | 38267490502373 |
| create_date | string | The create date of the commercial content in format of YYYYMMDD. | 20230109 |
| create_timestamp | i64 | The create date of the commercial content in format of Unix timestamp. | 1696875852 |
| label | string | The label of this commercial content. | Paid partnership |
| brand_names | list<string> | The brands that sponsor this commercial content. | [ "My Awesome Co.", "HelloWorld Inc." ] |
| creator | CommercialContentCreator | The commercial content creator's public information. |  |
| video | CommercialContentVideo | The commercial content video's public information. |  |

### CommercialContentCreator

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| username | string | The commercial content creator's TikTok handler. | joe123 |

### CommercialContentVideo

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| id | i64 | The commercial content video's ID. | 19384729204821234 |
| status | string | The commercial content video's status. | active |
| url | string | The commercial content video's URL. | https://www.tiktok.com/@joe1234567/video/19384729204821234 |
| cover_image_url | string | The commercial content video's cover image URL. | https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string. | ok |
| message | string | The detailed error description. |  |
| log_id | string | The unique id associated with every request for debugging purpose. | 202207280326050102231031430C7E754E |
| http_status_code | i32 | The http status code. | 200 |

Was this document helpful?