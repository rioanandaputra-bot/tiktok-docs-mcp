Docs
# Query Shop Details
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/shop/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Shop Info Object below for a full list of values. | **Complete list**: shop_name,shop_rating,shop_review_count,item_sold_count,shop_id | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| shop_name | string | shop_name as the unique identifier | "Test Shop" |
| limit | int | Max data can be returned at one time (max 10 for TTS related data) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/shop/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2.example' \
--data '{
    "shop_name": "TEST SHOP",
    "fields":"shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value",
    "limit": 10
}'

curl --location 'https://open.tiktokapis.com/v2/research/tts/shop/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2' \
--data '{
    "shop_name": "test shop",
    "fields":"shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value",
    "limit": 1
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Shop Info Object | The returned shop info for shops operating in the EU. |
| error | ErrorStructV2 | Error object |

## Shop Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "shop_name" | string | The name of the shop |
| "shop_rating" | String | The rating of the shop |
| "shop_review_count" | int64 | The number of reviews the shop has received |
| "item_sold_count" | int64 | The number of items the shop has sold |
| "shop_performance_value" | int64 | The value of shop performance (Ex: 90) |

## Example
```
{
    "data": {
        "shop_data": [
            {
                "item_sold_count": 1216959,
                "shop_id": 123456789,
                "shop_name": "Test Name",
                "shop_rating": "4.5",
                "shop_review_count": 12345
            }
        ]
    }
}
```
Was this document helpful?