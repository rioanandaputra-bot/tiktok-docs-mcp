Docs
# Shop Management APIs
## Claim POI
**Note**: The maximum limit is 3 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/poi/batch_claim/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required ** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| data | list<PoiInfo> | Batch parameters (a limit of 5 at once) | Yes |

#### PoiInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Third-party shop ID | Yes |
| shop_name_local | string | Shop name (local language) | Yes |
| shop_name_en | string | Shop name (English) | Yes |
| shop_address_local | string | Shop address (local language) | Yes |
| shop_address_en | string | Shop address (English) | Yes |
| exterior_photo_url_list | list<string> | Outdoor pictures of the shop, accessible via a publicly available HTTP URL: Maximum 5 MB per image Up to 5 images PNG, JPG, or JPEG All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. | No |
| business_status | int | Business status: 1 = open for business | Yes |
| type_code | string | [Business category, refer to the Category Tree](https://developers.tiktok.com/doc/category-tree) | Yes |
| website | string | The URL of the business's website | No |
| latitude | string | Address location latitude, ensure that the longitude and latitude are in Indonesia | No |
| longitude | string | Address location longitude, ensure that the longitude and latitude are in Indonesia | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_list | list<PoiClaimTask> | Submitted task collection | No |

## Upload Shop Certifications
**Note**: The maximum limit is 3 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_submit/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| data | list<CertificationInfo> | Batch parameters (a limit of 5 at once) | Yes |

#### CertificationInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Third-party shop ID | Yes |
| industry_license_url | string | Industry qualification documents, such as the business identification document, accessible via a publicly available HTTP URL All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. | Yes |
| statement_letter_url | string | Statement letter, accessible via a publicly available HTTP URL All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. | Yes |

#### Certification document specifications
Each shop needs to upload at least one file that represents its Nomor Induk Berusaha (NIB). If the shop is not on the NIB list, an additional statement letter is required.
Adhere to the following file restrictions:
- File format must be PNG, JPEG, or PDF
- File size must be less than 20MB; unlimited length and width
- NIB example: Figure 3, one qualification document can cover multiple shops.
- Statement example: File 1.
##### Business identification document
You will be asked to upload a business identification/Nomor Induk Berusaha (NIB) document, as depicted:
You can submit a business identification document for one shop, or a document that covers multiple shops:
**Business identification document for a single shop: **
**Business identification document for multiple shops:**
##### Statement letter
If you have shops not listed on the NIB document, an additional statement letter indicating that your company owns those shops is required.
[The following is a template for the statement letter](https://tosv.boe.byted.org/obj/tostest/vhreh7flszld/TikTok_for_Developers/TemplateStatementLetter_OutletClaim_bilingual.docx).
### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_list | list<ShopCertificationTask> | Submitted tasks | No |

## Decorate Shop
Note: The maximum limit is 3 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_decoration/batch_submit/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| data | list<DecorationInfo> | Batch parameters (a limit of 5 at once) | Yes |

#### DecorationInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Either `third_shop_id`or `shop_id`must be filled | No |
| shop_id | i64 | Either `third_shop_id`or `shop_id`must be filled | No |
| average_price | AveragePriceInfo | Average price of the shop's products, just for display | No |
| phone | string | The store's telephone number, such as +1 123456789 | No |
| opening_time | list<OpeningTimeInfo> | The store's hours of operation | No |
| images | list<ImageInfo> | Images representing the shop, accessible via a publicly available HTTP URL Maximum 5 MB per image Up to 5 images PNG, JPG, or JPEG All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. Resubmit the image of index N. The previous image of index N will be deleted and the new image is under review. For a single call, the URLs in a batch of images are not allowed to be repeated. | No |

#### AveragePriceInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| amount | string | Amount | Yes |
| currency | string | Currency, such as Rp for Indonesia | Yes |

#### OpeningTimeInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| day | int (i32) | Day of the week: 1,2,3,4,5,6,7 Monday == 1 Sunday == 7 | Yes |
| time_periods | list<TimePeriodInfo> | Start and end times for shop hours | Yes |

Example:
```
[
{
    "day": 1,
    "time_periods": [
        {
            "start_time": "04:00",
            "end_time": "07:00"
        }
    ]
},
{
    "day": 4,
    "time_periods": [
        {
            "start_time": "04:00",
            "end_time": "07:00"
        }
    ]
}
]
```
#### TimePeriodInfo object
`https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/`

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| start_time | string | Start time, shop opening hours | No |
| end_time | string | End time, shop closing hours | No |

#### ImageInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| is_main | bool | Whether is the main image | No |
| index | int (i32) | Picture index number. 1-50, up to 50 shop pictures can be set. | No |
| origin_url | string | Image original public network HTTP URL All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_list | list<DecorationTask> | Submitted tasks | No |

## Update Shop Basic Info
Note: The maximum limit is 3 queries per second (QPS).
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_base_info/batch_update/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| data | list<CertificationInfo> | Batch parameters (a limit of 5 at once) | Yes |

#### CertificationInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Either `third_shop_id`or `shop_id`must be filled | No |
| shop_id | i64 | Either `third_shop_id`or `shop_id`must be filled | No |
| shop_name_local | string | Shop name (local language) | No |
| shop_name_en | string | Shop name (English) | No |
| shop_address_local | string | Shop address (local language) | No |
| shop_address_en | string | Shop address (English) | No |
| type_code | string | [Business category, reference: Category Tree](https://developers.tiktok.com/doc/category-tree) | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_list | list<ShopBaseInfoTask> | Submitted task collection | No |

Note:
- Updating the shop's basic info won't affect the existing shop's availability.
- The new information will take effect once the update is completed.
## Query Claim POI tasks
Note: The maximum limit is 10 queries per second (QPS).
### Endpoint
SaasBatchQueryClaimPoiTask API path:
`POST ``https://open.tiktokapis.com/v2/localservice/saas/poi_task/batch_query/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| task_id_list | list<int (i64)> | Collection of tasks to be queried, limited to 20 | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| result | map<int (i64),PoiClaimTask> | Task information | No |

## Query Upload Shop Certification tasks
Note: The maximum limit is 3 queries per second (QPS).：10
### Endpoint
SaasBatchQuerySubmitShopCertificationTask API path:
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_query/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| task_id_list | list<int (i64)> | Collection of tasks to be queried, limited to 20 | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| result | map<int (i64),ShopCertificationTask> | Task information | No |

## Query Decorate Shop tasks
Note: The maximum limit is 10 queries per second (QPS).
### Endpoint
SaasBatchQuerySubmitShopDecorationTask API path:
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_decoration_task/batch_query/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| task_id_list | list<int (i64)> | Collection of tasks to be queried, limited to 20 | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| result | map<int (i64),DecorationTask> | Task information | No |

## Query Update Shop Basic Info tasks
Note: The maximum limit is 10 queries per second (QPS).
### Endpoint
SaasBatchQueryUpdateShopBaseInfoTask API path:
`POST`` ``https://open.tiktokapis.com/v2/localservice/saas/update_shop_base_info_task/batch_query/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| task_id_list | list<int (i64)> | Collection of tasks to be queried, limited to 20 要查询的任务集合,限制20条 | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| result | map<int (i64),ShopBaseInfoTask> | Task information | No |

## Batch Query Shop Information
Note: The maximum limit is 10 queries per second (QPS).
### Endpoint
SaasMGetShop API path:
`POST ``https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/`
### Authorization header

| **Field** | **Type** | **Description** | Example | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token obtained through `/oauth/access_token/`bearing user authorization | `Bearer act.example12345Example12345Example` | Yes |

### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | TT merchant ID | Yes |
| shop_ids | list<i64> | Either `third_shop_ids`or `shop_ids`must be filled, at most 20 | No |
| third_shop_ids | list<string> | Either `third_shop_ids`or `shop_ids`must be filled, at most 20 | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_infos | map<string,ShopInfo> | If you provided `third_shop_ids`, this value will be returned. | No |
| shop_infos | map<i64,ShopInfo> | If you provided `shop_ids`, this value will be returned. | No |

#### ShopInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_shop_id | string | Either `third_shop_id`or `shop_id`must be filled | No |
| shop_id | i64 | Either `third_shop_id`or `shop_id`must be filled | No |
| merchant_id | string | TT merchant ID | No |
| shop_name | string | Shop name (local language) | No |
| poi_id | int (i64) | TikTok's point of interest identifier for the shop’s location entity | No |
| poi_name | string | POI name | No |
| longitude | double | Longitude | No |
| latitude | double | Latitude | No |
| address | string | Address | No |
| average_price | AveragePriceInfo | Average price of the shop's products, just for display | No |
| phone | string | The store's telephone number | No |
| opening_time | list<OpeningTimeInfo> | The store's hours of operation | No |
| images | list<ImageInfo> | Images representing the shop All file interaction fields must use a public network URL, and the file access period must not be shorter than 10 minutes. | No |
| business_status | int | Business status: 1 = open for business | No |

Example of OpeningTimeInfo object:
```
{
    "day": 1,
    "time_periods": [
        {
            "start_time": "04:00",
            "end_time": "07:00"
        }
    ]
}
```
## Webhook notifications for shop management APIs
[For more information on how to handle webhooks, refer to webhooks documentation](https://developers.tiktok.com/doc/webhooks-overview?enter_method=left_navigation).
Info: For the following shop management APIs, you will be notified of status updates through the webhook.
- Claim POI
- Upload shop certification
- Decorate shop
- Update shop's basic info

| Field | Description |
| --- | --- |
| client_key | ID registered with TikTok by the third-party developer (SAAS platform) |
| event | Event name: the naming convention is generally aa.bb.cc, such as the following: Claim POI = `ttls.merchant.poi_claiming_task.result` Upload shop certification = `ttls.merchant.upload_shop_certifications_task.result` Decorate shop = `ttls.merchant.shop_decoration_task.result` Update shop's basic info = `ttls.merchant.update_shop_base_info_task.result` |
| create_time | Timestamp in seconds since the Unix epoch. For the same event, the previous `create_time`content can be discarded, and only the subsequent ones are needed. |
| user_id | TikTok user identification involved, null if no user is involved |
| content | Marshalled JSON string, serialized. TikTok only passes it through, does not parse or perceive. |
| caller | Source PSM for event generation, for troubleshooting |

#### Content
- Claim POI = **PoiClaimTask**
- Upload shop certification = **ShopCertificationTask**
- Shop decoration task = **DecorationTask**
- Shop basic information update = **ShopBaseInfoTask**
## Public structs for shop management APIs
Publicly exposed data models that the API will return or accept as JSON.
#### PoiClaimTask object
Tracks the process of claiming a POI for a shop, including task status, POI ID, and third-party shop ID. Rejection reasons are provided as a map of field → message.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_id | int (i64) | Unique identifier for this certification task | No |
| task_status | int | Current status code of the task: 1 = Under review: certification is in progress; no TT `shop_id`is returned yet 2 = Successful: certification completed; TT `shop_id`is returned for the first time 3 = Failed: certification rejected; see `reject_reason`for why | No |
| poi_id | int (i64) | TikTok's point of interest identifier for the shop’s location entity | No |
| third_shop_id | string | Third-party shop ID | No |
| reject_reason | map<string,string> | Audit rejection reason, the field name is the reason | No |

Example of failed task:
```
{
    "task_id": 1000,
    "task_status": 3,
    "third_shop_id": "third id",
    "poi_id": 2000,
    "reject_reason":
    {
        "address": "The address provided is not within the service area."
    }
}
```
#### ShopBaseInfoTask object
Manages the review/update of a shop’s basic profile with status, TT shop ID, and third-party shop ID. Failures include a field-to-reason map explaining which base info was rejected.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_id | int (i64) | Unique identifier for this certification task | No |
| task_status | int | Current status code of the task: 1 = Under review: certification is in progress; no TT `shop_id`is returned yet 2 = Successful: certification completed; TT `shop_id`is returned for the first time 3 = Failed: certification rejected; see `reject_reason`for why | No |
| shop_id | int (i64) | Shop ID assigned by TikTok | No |
| third_shop_id | string | Third-party shop ID | No |
| reject_reason | map<string,string> | Audit rejection reason, field name- > reason | No |

Example of failed task:
```
{
    "task_id": 1000,
    "task_status": 3,
    "third_shop_id": "third id",
    "shop_id": 10010101,
    "reject_reason":
    {
        "name": "The name has no letters or numbers and is made up of only space, punctuations, or emojis."
    }
}
```
#### ShopCertificationTask object
Represents the review process for certifying a merchant’s shop on TikTok. It tracks the task’s unique ID, current status, identifiers for the shop (both third-party and TikTok), and an optional rejection reason.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_id | int (i64) | Unique identifier for this certification task | No |
| task_status | int | Current status code of the task: 1 = Under review: certification is in progress; no TT `shop_id`is returned yet 2 = Successful: certification completed; TT `shop_id`is returned for the first time 3 = Failed: certification rejected; see `reject_reason`for why | No |
| poi_id | int (i64) | TikTok's point of interest identifier for the shop’s location entity | No |
| third_shop_id | string | The shop identifier in your third-party system | No |
| shop_id | i64 | Shop ID assigned by TikTok. This is only provided when certification succeeds (`task_status`= 2) and is the first moment the merchant can receive the TT `shop_id`. | No |
| reject_reason | string | Reason provided when `task_status`= 3 (Failed). | No |

Note: Upon success (`task_status` = 2), store the returned `shop_id` immediately. This is the first moment the platform returns it, and you should persist it for future operations and linking.
Example of failed task:
```
{
    "task_id": 1000,
    "task_status": 3,
    "poi_id": 2000,
    "shop_id": 10010101,
    "third_shop_id": "third id",
    "reject_reason": "license invalid"
}
```
#### DecorationTask object
Handles batch review/update of a shop’s decoration/layout content. Supports partial success (status = 4) and returns separate maps explaining information vs. image rejections. Either TT `shop_id` or `third_shop_id` must be provided.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| task_id | int (i64) | Unique identifier for this certification task | No |
| task_status | int | Current status code of the task: 1 = Under review: certification is in progress; no TT `shop_id`is returned yet 2 = Successful: certification completed; TT `shop_id`is returned for the first time 3 = Failed: certification rejected; see `reject_reason`for why 4 = Partial success | No |
| third_shop_id | string | Either `third_shop_id`or `shop_id`must be filled | No |
| shop_id | i64 | Either `third_shop_id`or `shop_id`must be filled | No |
| info_reject_reason | map<string,string> | Reason for information rejection, the field key is the reason | No |
| image_reject_reason | map<string,string> | Reason for image rejection, the field key is the reason | No |

Example of failed task:
```
{
    "task_id": 1000,
    "task_status": 2,
    "shop_id": 123,
    "third_shop_id": "third id",
    "info_reject_reason":
    {
        "address": "The address provided is not within the service area."
    },
    "image_reject_reason":
    {
        "2": "picture illegal"
    }
}
```
Was this document helpful?