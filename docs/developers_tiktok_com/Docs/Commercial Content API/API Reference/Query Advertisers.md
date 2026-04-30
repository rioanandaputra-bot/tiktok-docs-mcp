Docs
# Query Advertisers
Use POST /v2/research/adlib/advertiser/query to query advertisers.

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/adlib/advertiser/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request
## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

## Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: business_name business_id country_code | business_name,business_id,country_code | true |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| search_term | string | The terms to search for in the query. The limit of the string is 50 characters or less. | awesome | true |
| max_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20 | false |

## Request example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/advertiser/query/?fields=business_id,business_name' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json'
--data-raw '{
   "search_term": "awesome",
   "max_count": 25
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | QueryAdvertiserData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example
```
{
   "data": {
      "advertisers": [
         {
            "business_id": 1755645247067185,
            "business_name": "Awesome Food Co.",
            "country_code": "US",        
         },
         {
            "business_id": 183746395837294,
            "business_name": "Awesome Drink Co.",
            "country_code": "CA",        
         }
      ]
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
### QueryAdvertiserData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| advertisers | list<Advertiser> | The list of advertisers that match all the criteria. |  |

### Advertiser

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| business_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business_name | string | The advertiser's business name. | Awesome Food Co. |
| country_code | string | The advertiser's country in the format of a two-letter code defined in ISO 3166-1. | US |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string. | ok |
| message | string | The detailed error description. |  |
| log_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http_status_code | i32 | The http status code. | 200 |

Was this document helpful?