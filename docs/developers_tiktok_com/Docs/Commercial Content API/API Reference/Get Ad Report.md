Docs
# Get Ad Report
Use POST /v2/research/adlib/ad/report/ to get a report on ad publishing.

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/adlib/ad/report/ |
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
| fields | string | The requested fields: count_time_series_by_country | count_time_series_by_country | true |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below. | true |

## Data structures
### RequestFilters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| ad_published_date_range | DateRange | The time range when the ads were published. "min" needs to be after October 1st, 2022. | { "min": "20230102", "max": "20230109" } | true |
| country_code | string | [The country where the ads/ad groups were created. The default value is ALL. Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR | false |
| advertiser_business_ids | list<i64> | The advertiser's business ID of the ads/ad groups. | [21836478203048,3484763562784] | false |

### DateRange

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| min | string | The first date of the range. "min" needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

## Request example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/report/?fields=count_time_series_by_country' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json'
--data-raw '{
   "filters":{
       "ad_published_date_range": {
            "min": "20230102",
            "max": "20230109"
       },
       "country_code":"ALL",
       "advertiser_business_ids":[21836478203048,3484763562784]
   }
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | ReportData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example
```
{
   "data": {
      "count_time_series_by_country": {
          "IT": [{"date": "20210109", "count": 45}, {"date": "20210108", "count": 24}],
          "ES": [{"date": "20210109", "count": 48}, {"date": "20210108", "count": 22}],
          ...
    }
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
### ReportData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| count_time_series_by_country | map<string,list<DateCount>> | The ad count time series of each country. |  |

### DateCount

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| date | string | The date when ads were published in the format YYYYMMDD. | 20230101 |
| count | i64 | The total number of ads published on that date. | 500032 |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string. | ok |
| message | string | The detailed error description. | "" |
| log_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http_status_code | i32 | The http status code. | 200 |

Was this document helpful?