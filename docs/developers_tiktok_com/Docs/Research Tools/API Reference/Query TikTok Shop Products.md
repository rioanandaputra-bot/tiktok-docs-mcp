Docs
# Query Product Info
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/product/ |
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
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Product Info Object below for a full list of values. | **Complete list**: product_id,product_sold_count,product_description,product_price,product_review_count,product_name,product_rating_1_count,product_rating_2_count,product_rating_3_count,product_rating_4_count,product_rating_5_count | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| shop_id | int | shop_id as the unique identifier | "127878967" |
| page_start | int | The start page for the products in the shop (start with 1) | 1 |
| page_size | int | The size of data on the page (max 10) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/product/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2.' \
--data '{
    "shop_id": 12345678910,
    "fields": "product_id,product_sold_count,product_review_count,product_rating",
    "page_start": 1,
    "page_size": 5
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Product Info Object | The returned product info data for products available for purchase in the EU. |
| error | ErrorStructV2 | Error object |

## Product Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "product_name" | string | The name of the product |
| "product_id" | int64 | The unique ID of the product |
| "product_price" | list | The price of the product |
| "product_rating" | string | The rating of the product |
| "product_review_count" | int64 | The number of reviews of the product |
| "product_rating_5_count" | int64 | The number of ratings of 5-stars the product has received |
| "product_rating_4_count" | int64 | The number of ratings of 4-stars the product has received |
| "product_rating_3_count" | int64 | The number of ratings of 3-stars the product has received |
| "product_rating_2_count" | int64 | The number of ratings of 2-stars the product has received |
| "product_rating_1_count" | int64 | The number of ratings of 1-star the product has received |
| "product_sold_count" | int64 | The number of items sold since this item was listed on TikTok shop, including items that have been returned |
| "product_description" | string | The description of the product |
| "shop_name" | string | The name of the "Shop" the product is under |

## Example
```
{
    "data": {
        "product_data": [
            {
                "product_description": "test Description",
                "product_id": 123456789,
                "product_name": "test Name",
                "product_price": [
                    "20.79GBP"
                ],
                "product_rating_1_count": 116,
                "product_rating_2_count": 47,
                "product_rating_3_count": 112,
                "product_rating_4_count": 353,
                "product_rating_5_count": 2693,
                "product_review_count": 3321,
                "product_sold_count": 37741
            }
        ]
    }
}
```
Was this document helpful?