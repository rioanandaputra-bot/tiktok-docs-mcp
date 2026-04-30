Docs
# Voucher Management
The voucher redemption process leverages two APIs: Query Voucher and Redeem Voucher. Webhooks are used to trigger notifications after a redemption has been made. Note the following when redeeming vouchers:
- When the user shows the QR code to the merchant scanner, the scanner shall decode out a string. This string begins with a `TT-` prefix and corresponds to `qr_info` in the Query Vourcher API.
- One order (`shop_order_id`) can have multiple item orders (`item_order_id`).  For each item, TikTok will have a corresponding voucher code.  For example, a user buys 3 sets of products in a single order.
- If the `qr_info` has already been redeemed and the QR code gets scanned again, the `error.code` field will be "`-3000109`" and `error.message` field will be "`FulfillRedeemQRCodeExpired`".
- At the same time, the data field will just contain the voucher codes that are already redeemed under this shop-order and developers can use it to correct the voucher status in case the Redeem Voucher API times out.
- If the user wants to redeem the remaining voucher codes, developers and merchants should ask them to refresh the QR code on the TikTok app.
- When scanning a completely new QR code, developers will get all status voucher codes and must send unredeemed voucher codes to the Redeem Voucher API for redemption. Otherwise, the Redeem Voucher API may fail due to already-redeemed voucher codes.
## Query Voucher
Query coupon details based on the coupon code ID or QR code scan result.
**Note**: The maximum limit is 50 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/fulfill/get_code_item_list/`
### Request parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| third_shop_id | string | Third-party shop ID (platform will check the mapping between voucher and shop) | Yes |
| code_list | List<string> | Redeem coupon code ID list | No |
| qr_info | string | QR code encrypted information (This string starts with a "`TT-`" prefix) | No |
| locale | string | Language environment: for example, "id-ID" represents Indonesia | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | GetCodeItemListData | Actual data | No |

#### GetCodeItemListData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| code_list | List<CodeItem> | Coupon code list | Yes |
| shop_order_id | string | Shop order ID | Yes |

#### CodeItem object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| goods_image_url | string | Product image URL | Yes |
| product_name | string | Product name | Yes |
| refund_rule_desc | string | Refund rule description | Yes |
| code_can_use_time | CanUseTimeRange | Redemption code available time range | Yes |
| crossed_amount | string | Marked price (original price) | Yes |
| sale_amount | string | Selling price | Yes |
| currency | string | Currency type | Yes |
| code | string | Redemption code | Yes |
| code_cannot_use_date | CannotUseDateStruct | Redemption code unavailable date information | No |
| redemption_status | RedemptionStatus | Exchange status `INIT = 0`(Initialization) `WAIT_FULFILL = 100`(To be fulfilled) `FINISH = 400` `AFTER_SALE_PROCESSING = 500`(After-sales processing) `AFTER_SALE_SUCCESS = 501`(After-sales success) | No |
| product_id | string | Product ID | No |
| third_product_id | string | Third-party product ID | No |
| redeem_id | string | Redeem ID | No |
| redemption_source | RedemptionSource | Redemption source `MERCHANT_APP = 1` `SAAS = 2` | No |
| redeemed_shop_id | int64 | Redemption shop ID | No |
| item_order_id | string | Product order ID | No |
| redeemed_third_shop_id | string | Third-party shop ID from where the redemption occured | Yes |

#### CanUseTimeRange object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| start_time | int64 | Coupon code available start time | Yes |
| end_time | int64 | Coupon code availability deadline | Yes |

#### CannotUseDateStruct object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| enable | bool | Is the current time in the unavailable time? | Yes |
| content_list | List<ContentInfo> | Content information list | No |

#### ContentInfo object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Type `use_time`: available time `cannot_use_date`: unavailable dates | Yes |
| title | string | Title | No |
| contents | List<string> | Content list | No |

## Redeem Voucher
Verify the coupon code after checking and confirming its details.
**Note**: The maximum limit is 50 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/fulfill/redeem_code/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Third-party shop ID | Yes |
| code_list | List<string> | Coupon code list | Yes |
| shop_order_id | string | TikTok order ID (you can get this from the Query Voucher API) | Yes |
| merchant_id | string | Merchant ID | Yes |
| locale | string | Language environment: for example, "id-ID" represents Indonesia | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | RedeemCodeData | Actual data | No |

#### RedeemCodeData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| redeem_id | string | Redeem ID generated by TikTok | Yes |

## Webhook notification of after sale
[For more information on how to handle webhooks, refer to webhooks documentation](https://developers.tiktok.com/doc/webhooks-overview?enter_method=left_navigation).

| Field | Description |
| --- | --- |
| client_key | ID registered with TikTok by the third-party developer (SAAS platform) |
| event | Event name: the naming convention is generally aa.bb.cc, such as the following: Claim POI = `ttls.merchant.poi_claiming_task.result` Upload shop certification = `ttls.merchant.upload_shop_certifications_task.result` Decorate shop = `ttls.merchant.shop_decoration_task.result` Update shop's basic info = `ttls.merchant.update_shop_base_info_task.result` |
| create_time | Timestamp in seconds since the Unix epoch. For the same event, the previous `create_time`content can be discarded, and only the subsequent ones are needed. |
| user_id | TikTok user identification involved, null if no user is involved |
| content | Marshalled JSON string, serialized. TikTok only passes it through, does not parse or perceive. |
| caller | Source PSM for event generation, for troubleshooting |

#### Content

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| after_sale_event_type | string | The type of after-sale event: `RETURN_FULFILL ` `RETURN_FUNDS` `AFTER_SALE_SUCCESS` `AFTER_SALE_CLOSE` `AFTER_SALE_AUDIT_APPROVE = 5` `AFTER_SALE_AUDIT_REJECT = 6` `AFTER_SALE_NOT_NEED_AUDIT = 7 ` `AFTER_SALE_SYNC_TTS = 8 ` `AFTER_SALE_CREATE_SUCCESS = 9` `AFTER_SALE_DDL_AUTO_AUDIT = 10` | Yes |
| shop_order_id | string | The order identity at shop level | Yes |
| item_ids | list<string> | The IDs at item level that were refunded. One shop-order has multiple item IDs. | Yes |
| apply_source | int | The detailed source of after sale. `ApplySource_EXPIRE_AUTO_REFUND ApplySource = 1` `ApplySource_USER_REFUND_BEFORE_FULFILL ApplySource = 2` `ApplySource_USER_REFUND_AFTER_FULFILL ApplySource = 3` `ApplySource_PAY_SUCCESS_AFTER_ORDER_CLOSE ApplySource = 4` | Yes |
| after_sale_order_id | string | The identity of the corresponding after-sale order | Yes |
| user_id | int64 | The user ID of the corresponding shop order | Yes |

Was this document helpful?