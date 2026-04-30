Docs
# Subscription APIs
## Create a subscription
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/create/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| tier_id | string | Tier ID of the subscription product | Yes |
| order_info | OrderInfoObject | The order info from partner's side | Yes |

**OrderInfoObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| order_id | string | The ID of your order created in your system | Yes |
| product_name | string | The name of the product user intended to purchase | Yes |
| order_url | string | The URL to the order information page in your system | No |
| order_detail | string | Detailed info of the order info, if any | No |

### Response data struct

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID. | Yes |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/create/' \
--header 'Authorization: Bearer {AccessToken}' 
--header 'Content-Type: application/json' \
--data '{
    "tier_id": "sandbox_499_1M",
    "order_info": {
        "order_id": "wsf_test_6",
        "product_name": "ttt1",
        "order_detail": "",
        "order_url": ""
    }
}'
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
## Reactivate subscription
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/reactivate/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| subscription_id | string | ID of user's current active subscription | Yes |
| order_info | OrderInfoObject | The order info from partner's side | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/reactivate' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "subscription_id": "784647171844-B",
    "order_info": {
        "order_id": "reactivate_test_wsf7",
        "product_name": "reactivate",
        "order_detail": "",
        "order_url": ""
    }
}'
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
## Get active subscription list
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_active_list/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscriptions | list<ThirdPartyUserSubscriptionObject> | List of active subscriptions |

**ThirdPartyUserSubscriptionObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| subscription_id | string | ID of the subscription | Yes |
| tier_id | string | ID of the subscription product | Yes |
| is_subscription_rights_valid | bool | indicate whether this right is still valid | Yes |
| is_renewal_normal | bool | indicate whether the renew is normal, false if renew is failed/onold | Yes |
| trade_order_id | string | the latest trade_order_id related to this subscription | Yes |
| begine_time | int64 | beginning time of this subscription | No |
| end_time | int64 | end time of this subscription | No |
| next_duduct_time | int64 | time of the next deduct | No |
| pay_type | string | IAP or WEB; IAP=Google/Apple Store, WEB=PayPal | No |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_active_list' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json'
```
**Response**
```
{
    "data": {
        "subscriptions": [
            {
                "subscription_id": "tb4ML0ZVim",
                "tier_id": "xohs4Jojay",
                "is_subscription_rights_valid": true,
                "is_renewal_normal": false,
                "trade_order_id": "ggG7luEdWt",
                "is_sandbox": true,
                "begin_time": 8054018414209391465,
                "end_time": 1061662930613089341,
                "next_duduct_time": 2184276991229817160,
                "pay_type": "IAP"
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Get subscription Info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_subscription_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription | ThirdPartyUserSubscriptionObject | List of active subscriptions |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_subscription_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "trade_order_id": ""
}'
```
**Response**
```
{
   "data": {
        "subscription": {
            "subscription_id": "H36qTi1gNU",
            "tier_id": "iqBaXsMxHh",
            "is_subscription_rights_valid": true,
            "is_renewal_normal": false,
            "trade_order_id": "SbUgvLyKj5",
            "is_sandbox": true,
            "begin_time": 7564558100036318910,
            "end_time": 5659157601114497266,
            "next_duduct_time": 953443659701638510,
            "pay_type": "IAP"
        }
    },
    "error": {
        "code": "gvlXZLamY7",
        "message": "2xuw0XIUIr",
        "log_id": "uPnqDeYu1S"
    }
}
```
## Get trade order Info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_trade_order_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription_tiers_info | SubscriptionTradeOrderInfoObject | List of active subscriptions |

**SubscriptionTradeOrderInfoObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | same as the requested trade_order_id | Yes |
| subscription_id | string | ID of the subscription | Yes |
| trade_order_status | string | indicate the status of the trade order: SUCCESS, PENDING,REFUNDED | Yes |
| is_sandbox | bool | Is sandbox order | No |
| begine_time | int64 | beginning time of the subscription related to this trade order | No |
| end_time | int64 | end time of the subscription related to this trade order | No |
| next_duduct_time | int64 | Happen time of the next deduction of the subscription related to this trade order | No |
| pay_type | string | IAP or WEB | No |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_trade_order_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "trade_order_id": ""
}'
```
**Response**
```
{
    "data": {
        "trade_order_id": "UIlpZZ1TIc",
        "subscription_id": "iSjgkQ9rei",
        "trade_order_status": "BRM1MQac3i",
        "is_sandbox": true,
        "begin_time": 162780036655460135,
        "end_time": 7326223299323173385,
        "actually_end_time": 7143902738493296646,
        "pay_type": "IAP"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Get subscription tier info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_subscription_tier_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| tier_ids | list<string> | The list of tier_ids of the target subscription product. For sandbox, these `tier_ids`can be used: sandbox_499_1M $4.99/Monthly sandbox_1347_3M $13.47/QUARTERLY sandbox_699_1M $6.99/Monthly sandbox_1887_3M $18.87/QUARTERLY |
| device_platform | string | Indicate user's device platform Optional value: `android`, `iphone` If this field is empty or other value, we will use `iphone`as the default value. You can determine whether a device is running IOS or Android by analyzing the User-Agent in HTTP request |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription_tiers_info | map<string, SubscriptionTradeOrderInfoObject> | List of active subscriptions |

**SubscriptionTierInfoObject**

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| tier_id | string | Same as the requested `trade_order_id` |
| deduct_cycle | string | Length of each deduction cycle. Possible values are: WEEKLY MONTHLY BIMONTHLY QUARTERLY SEMIANNYALLY ANNUALLY |
| deduct_type | string | indicate the deduction type. Possible values are: one_time auto_renew |
| price | string | Price to deduct for each cycle |
| currency | string | Currency of price to deduct for each cycle |
| symbol | string | Symbol of currency of price to deduct for each cycle |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_subscription_tier_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "tier_ids": ["awcnbwhfvvf9tmey_1347_3M"]
}'
```
**Response**
```
{
    "data": {
        "subscription_tiers_info": {
            "zqrPo2cIEE": {
                "tier_id": "IdohVeNqMX",
                "deduct_cycle": "I6Sj9ICBaW",
                "deduct_type": "CfuHfLeMoH",
                "price": "MrofV8f93l",
                "currency": "QiWeEc4YoU",
                "symbol": "uPk6QRdtsv"
            }
        }
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
Was this document helpful?