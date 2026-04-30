Docs
# Payment APIs
These APIs manage transactions using the platform's currency, Beans.
## Get recharge tiers
You need to first get the ID of the tiers you want to show on your recharge page.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/utility/get_tier_infos/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| tier_ids | list<string> | The list of IDs for tiers you want to get detail information of |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TierInfos | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TierInfos**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| tier_infos | map<string, TierInfoObject> | The TikTok user's unique identifier. The key in the map is `tier_id`. |

**TierInfoObject**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| tier_id | string | The ID of the tier |
| tier_name | string | The name of the tier |
| token_type | string | The type of token contained in the tier. For now, this field can only be `"BEANS"` |
| token_amount | int | The amount of token contained in the tier. For now, this filed implies the amount of Beans |
| price | string | The price of the tier |
| currency | string | The currency of the price, which follows the ISO 4217 standard. Example: `"USD"`for US Dollars |
| symbol | string | The symbol of the price. Example: `"$"`for USD. |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "tier_ids": ["1731381720000100"]
}
```
**Response**
```
{
    "data": {
        "tier_infos": {
            "1731381720000100": {
                "tier_id": "1731381720000100",
                "tier_name": "pd_beans_showcase_100",
                "token_amount": 100,
                "token_type": "BEANS",
                "price": "1.19",
                "currency": "USD",
                "symbol": "$"
            }
        }
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_od": "202411190743174589DAA30620D104990F",
    }
}
```
## Create an order
You need to pass the information of the order created in your system to TikTok to generate a trade order on TikTok's server, which is a necessary step in the pay and refund process.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/trade_order/create/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through `/oauth/access_token/`. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| token_amount | int | The amount of token contained in this order. For now, this field implies the amount of Beans. |
| order_info | OrderInfoObject | The order info from partner's side |

**OrderInfoObject**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| order_id | string | The ID of your order created in your system |
| order_url | string | The URL to the order information page in your system |
| product_name | string | The name of the product user intended to purchase |
| product_id | string | The ID of the product user intended to purchase |
| quantity | int | Number of products contained in this order |
| quantity_unit | string | Unit of the product, for example, `"episode"` |
| image_url | string | URL of the cover image of the order. We'd recommded using the poster of the drama in this field. Users can see this image on their order history page |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TradeOrderInfo | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TradeOrderInfo**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "token_amount": 100,
    "order_info": {
        "order_id": "external_order_id_003",
        "product_name": "Wake up dad! wedding time",
        "product_id": "external_product_id",
        "order_url": "/profile/order_history/external_product_id",
        "quantity": 1,
        "quantity_unit": "episode", // Pass in the unit of the item being sold based on the actual situation, such as 'episode' for a drama series unit
        "iamge_url": "https//your.domain/pics/wake_up_dad.jpg"
    }
}
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Query an order
You can track the status of the trade order by calling this API.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/trade_order/query/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The type of token you want to get tier Info for. For now, there is only one type, `"BEANS"`. Please only use `"BEANS"`in this field. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TradeOrderInfo | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TradeOrderInfo**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |
| trade_order_status | string | The status of the trade order. Available values are: `"PENDING"`and `"SUCCESS"` |

### Example
**Request**
```
{
    "trade_order_id": "TOID1732533244259"
}
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259",
        "trade_order_status": "PENDING"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202411251312430B89D17FDCB31F26244A"
    }
}
```
## Check redeem amounts
You need to make sure all the products you are trying to sell follow the correct pricing policy under TikTok's restriction. You must first check if the price you've settled on each product is legal by calling this API.
### Endpoint
_POST_ https://open.tiktokapis.com/v2/minis/utility/check_redeem_amounts/
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | TRUE |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| token_amounts | list<int> | The list of token amount you want to get detail information of. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | CheckResponse | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TierInfos**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| valid | bool | True if all amounts are valid |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "token_amounts": [11, 19, 999, 2999]
}
```
**Response**
```
{
    "data": {
        "valid": true
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_od": "202411190743174589DAA30620D104990F",
    }
}
```
Was this document helpful?