Docs
# Query Ads
Use POST /v2/research/adlib/ad/query to query ads.

| **HTTP URL** | https://open.tiktokapis.com/v2/research/adlib/ad/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request
## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | The original media type of the resource. | application/json | true |

## Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: ad.id ad.first_shown_date ad.last_shown_date ad.status ad.status_statement ad.videos ad.image_urls ad.reach advertiser.business_id advertiser.business_name advertiser.paid_for_by | ad.id, ad.first_shown_date, ad.last_shown_date | true |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| filters | RequestFilters | The filters that will be applied to the query. | See the "Request example" section below | true |
| search_term | string | The terms to search for in the query. The limit of the string is 50 characters or less. If you provide "search_term", the "advertiser_business_ids" filter will be ignored | mobile games | false |
| search_type | string | The search type (which is case insensitive): "exact_phrase": Returns results that contain an exact match for the search term. The default search type. "fuzzy_phrase": Returns results that contain any or all of the words in the search term in any order. | fuzzy_phrase | false |
| max_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20 | false |
| search_id | string | A search_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. If you want to start a new search with an updated`search_term`or `filters`value in the request, remove the `search_id`to avoid getting unexpected results. | 20230501124205358FF99E4D6D1294A2A7 | false |

## Data structures
### RequestFilters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| ad_published_date_range | DateRange | The date range during which the ads were published. The "min" value should represent a date after October 1, 2022. | { "min": 20230102, "max": 20230109 } | true |
| country_code | string | [The country where the ads were targeted. The default value is ALL. Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR | false |
| advertiser_business_ids | list<i64> | The advertiser's business ID of the ads. If you provide "search_term", this filter will be ignored. | [294854736284058, 495736284058473] | false |
| unique_users_seen_size_range | SizeRange | The range of the number of users who've seen the content of this ad. | { "min": "10K", "max": "20K" } | false |

### DateRange

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| min | string | The first date of the range and this needs to be after October 1, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

### SizeRange

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| min | string | The minimum size in thousands (K), millions (M), or billions (B). The number before "K", "M", and "B" must be an integer less than 1000. | Valid: 0K, 120K, 2M, 1B Invalid: 2000K, 1.1M, 1B2M | false |
| max | string | The maximum size in thousands (K), millions (M), or billions (B) The number before "K", "M", and "B" must be an integer less than 1000. The value must be greater than 0. | Valid: 120K, 2M, 1B Invalid: 0K, 2000K, 1.1M, 1B2M | false |

## Request example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
   "filters":{
       "advertiser_business_ids": [3847236290405, 319282903829],
       "ad_published_date_range": {
            "min": "20210102",
            "max": "20210109"
       },
       "country_code": "FR",
       "unique_users_seen_size_range": {
           "min": "10K",
           "max": "1M"
       },
   },
   "search_term": "mobile games"
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | QueryAdData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example
```
{
   "data": {
      "ads": [
         {
            "ad": {
               "first_shown_date": 20210101,
               "id": 1923845247192304,
               "image_urls": [
                  "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf"
               ],
               "last_shown_date": 20210101,
               "status": "active",
               "videos": [
                  {"url": "https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4"},
                  {"url": "https://asdfcdn.com/..../1kmeidhfb38u21nd82hsk389fd/?mime_type=video_mp4"}
               ],
               "reach": {
                  "unique_user_seen": "11K"
                }
            },
            "advertiser": {
                "buisness_id": 3847236290405,
                "business_name": "Awe Food Co.",
                "paid_by": "Awe Co."
            }
         }
      ],
      "has_more": "true",
      "search_id": "2837438294054038"
   },
   "error": {
      "code": "ok",
      "http_status_code": 200,
      "log_id": "202304280326050102231031430C7E754E",
      "message": ""
   }
}
```
## Data structures
### QueryAdData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| ads | list<AdDto> | The list of ads that match all the criteria. |  |
| has_more | bool | The flag that indicates if there are more items to be returned. | true |
| search_id | string | A unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | 2837438294054038 |

### AdDto

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| ad | Ad | The metadata of this ad. |  |
| advertiser | Advertiser | The metadata of the advertiser. |  |

### Ad

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| id | i64 | The ad ID. | 1923845247192304 |
| first_shown_date | string | The first day when this ad was shown. | 20210101 |
| last_shown_date | string | The last day when this ad was shown. | 20210101 |
| status | string | The audit status of this ad: active or inactive. | active |
| videos | list<AdVideo> | The list of videos. |  |
| image_urls | list<string> | The image URL list of this ad. | [ "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf" ] |
| reach | Reach | The number of users who have seen this ad. | { "unique_users_seen": "11K" } |

### AdVideo

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| url | string | The video url of this ad | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4 |

### Reach

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| unique_users_seen | string | The number of users who have seen this ad. | "11K" |

### Advertiser

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| business_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business_name | string | The advertiser's business name. | Awe Food Co. |
| paid_by | string | The advertiser's funding source. | Awe Co. |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string. | ok |
| message | string | The detailed error description. |  |
| log_id | string | The unique ID associated with every request for debugging purporse. | 202207280326050102231031430C7E754E |
| http_status_code | i32 | The http status code. | 200 |

Was this document helpful?