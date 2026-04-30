Docs
# Query Reviews Info
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/review/ |
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
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Review Info Object below for a full list of values. | **Complete list**: product_name,review_text,review_like_count,create_time,review_rating | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| product_id | string | product_id as the unique identifier | "1234590980980" |
| page_start | int | The start page for the products in the shop (start with 1) | 1 |
| page_size | int | The size of data on the page (max 10) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/review/' \
--header 'Authorization: Bearer clt.2.example*0' \
--header 'Content-Type: application/json' \
--data '{
    "product_id": 12345678910,
    "fields": "product_name,review_text,display_name,review_like_count,create_time,review_rating",
    "page_start": 2,
    "page_size": 1
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Review Info Object | The returned review info data for reviews given on products available for purchase in the EU. |
| error | ErrorStructV2 | Error object |

### Product Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "review_text" | string | The text within the review |
| "review_like_count" | int64 | The number of likes a review has |
| "create_time" | int64 | The unix timestamp that the review was created on |
| "product_name" | string | The product that this review is for |
| "review_rating" | string | The rating of the product |

### Example
```
{
    "data": {
        "review_data": [
            {
                "create_time": 1722879716021,
                "product_name": "Test Product Name",
                "review_like_count": 1,
                "review_rating": "FIVE",
                "review_text": " test Text"
            }
        ]
    }
}
```
Was this document helpful?