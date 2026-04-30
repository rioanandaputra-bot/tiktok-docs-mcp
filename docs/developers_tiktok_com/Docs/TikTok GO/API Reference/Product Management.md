Docs
# Product Management APIs
## Category for these objects
### Pagination object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| page_size | int64 | Number of pages, starting from 1 | No |
| page_no | int64 | Number of pages, starting from 1 | Yes |

### NextPagination object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| current_page_sizegroup | int64 | Number of pages | No |
| total | int64 | Total | Yes |
| has_more | bool | Whether it contains more | Yes |

### ErrorStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| code | string | Status code, non -" 0 "means an exception has occurred | Yes |
| message | string | State description | Yes |
| logid | string | Log-id, used for troubleshooting | Yes |
| http_status_code | string | Status code Use HTTP standard status codes | Yes |

## Update/Create Product
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: Upload products after merchant onboarding and store matching are completed.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/save/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| third_product_id | string | Third-party product ID | Yes |
| category_id | string | Product category, obtained by querying the product category interface | Yes |
| product_type | ProductType | Product type Enum, only supports group buying coupons for the first phase 2 = group buying coupons | Yes |
| attr_key_value_map | map<string,string> | [Product details, the first issue only supports group buying coupon type Refer to Group-buying coupons attributes](#share-Wovcd80Dkom2PCxJpXmuTv9Ason), where Value needs to serialize the original Object to a string. | Yes |
| language | string | Language | No |

#### Group-buying coupons attributes

| **Field** | **Description** | **Type** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| rec_person_num | Recommended number of users | int | "5" | Yes |
| rec_person_num_max | Maximum number of users | int | "20" | No |
| shop_id | Stores linked to products | LIST<string> | "[\"222\"]" | Yes |
| commodity_set | The original price setting method of the product 2 = Set the original price of the product No need to set a single product price | int | "2" | Yes |
| commodity | [Item pairing (Refer to Item pairing](#share-T3EwdKXvkotclUxdzm8ukxhqsce)) | ItemGroupStruct | `"[{\"i18n_group_mame\":{\"default_text\":\"group name 1\"},\"total_count\":2,\"option_count\":\"2\",\"item_list\":[{\"i18n_name\":{\"default_text\":\"kfc\"},\"price\":\"200\",\"currency\":\"th\",\"count\":1},{\"i18n_name\":{\"default_text\":\"kfc\"},\"price\":\"300\",\"currency\":\"th\",\"count\":2}],\"allow_repeated_item\":true}]"` | Yes |
| product_name | [Product name (Refer to Product name](#share-H6YZdyhYVoVkihxy6nbuWchUsof)) | I18nText | `"{\"DefaultText\":\"product name\",\"translations\":{\"en\":\"product name-en\",\"id\":\"product name-id\"}}"` Default-text is the default language. If the query passes the ID and translations cannot be found, will default-text be used | Yes |
| image_list | [Package plan (Refer to Package plan](#share-QVpqd5VXaokV2xxVQd5ukzJOstg)) | ImageStruct | `"[{\"outer_url\":\"``http://p5.itc.cn/images03/20200519/d6c0794d068e4967a8b16a16416413f7.jpeg``\"}]"` Merchants can input the public network URL, and TT will be uploaded to the internal storage Recommended image quantity 2-10, each image does not exceed 5MB, recommended ratio is 4:3, recommended resolution is 780 x 585. Recommend the first image Upload high-resolution images to attract users | Yes |
| origin_amount | Total price | int | "3000" | Yes |
| actual_amount | Customers actually need to pay | int | "2000" | Yes |
| local_currency | Currency corresponding to the price | int | "THB" | Yes |
| stock_info | [Stock (Refer to Stock](#share-DdXIdhnMgolcYqxeT9SuXUeCsvf)) | StockInfoStruct | `"{\"stock_num\":1000,\"stock_qty_limit_type\":1}"` | Yes |
| sold_start_time | Product sales start date MilliSeconds timestamp | int | "1720666722000" | No |
| sold_end_time | This only affects product display. DO not affect product status. Product sale end date MilliSeconds timestamp | int | "1752202732000" | No |
| sold_time_type | Product Sale Date Type 1 = Limited time sale 2 = Unlimited time | int | "1" | Yes |
| use_type | Group buying method 1 = In-shop verification | int | "1" | Yes |
| limit_buy_rule | [Restricted purchasing rules (Refer to Restrict purchasing rules](#share-DLdndlMfzoJtmrxLfyuuy8L5sDh)) | LimitBuyRuleStruct | `"{\"enable_limit\":true,\"rule_list\":[{\"subject_type\":1,\"range_type\":3,\"limit_num\":10},{\"subject_type\":1,\"range_type\":2,\"limit_num\":1}]}"` product attr key[limit_buy_rule], limitNum must be between 1 and 99. | No |
| use_date | [Available date (Refer to Available date](#share-HHPHdyCyLoEByRxnbbYumSCssgc)) | UseDateStruct | `"{\"use_date_type\":2,\"day_duration\":30}"` The options of day_duration: [60,45,30] The valid period is natural days. For example, the coupon purchased at 9:00 on the 1st has a valid period of 1 day and expires at 9:01 on the 2nd. | Yes |
| cannot_use_date | [Unusable date (Refer to Unusable date](#share-OX5yd3rf7o9B2oxvVREuscB8sGe)) | CannotUseDateStruct | `"{\"enable\":true,\"days_of_week\":[1],\"date_list\":[\"2024-08-30\"]}"` The merchant's time zone corresponds to the merchant's country/region. | No |
| use_time | [Usage time (Refer to Use time](#share-LEgqdMk9Uo3KsJxDEHMu2guisuf)) | UseTimeStruct | `"{\"use_time_type\":2,\"time_period_list\":[{\"use_start_time\":\"20:00\",\"use_end_time\":\"02:00\",\"end_time_is_next_day\":true}]}"` The merchant's time zone corresponds to the merchant's country/region. | Yes |
| appointment | [Appointment information (Refer to Appointment information](#share-PBTndfFiZoR8RRxbE5AuAANIsmd)) | AppointmentStruct | `"{\"need_appointment\":true,\"ahead_time_type\":1,\"ahead_num\":20}"` | No |
| consumption_convention | [Dine-in and take-out agreement (Refer to Dine-in and take-out agreement](#share-RtipdRkR9oFwT6x3nuyutfuEsQd)) | COMSUMPTION_CONVENTION | `"{\"consumption_method\":2}"` | Yes |
| description_rich_text | [Other explanatory information (Refer to Other explanatory information](#share-AfwZd1Or9oc5O7xnJEGuII7esze)) | NoteStruct | `"{\"content\":\"{\\\"default_text\\\":\\\"Other information\\\"}\"}"` `default_text`use I18N Text | No |

#### Product name
##### I18nText object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| default_text | string | Default local language text The maximum length of this field is 1000 | Yes |
| translations | Map<string, string> | [Multilingual translation Transmit as much language as possible ID must be passed in, try EN EN first layer fallback, default second layer fallback Key: languange (refer to language code list](https://localizely.com/iso-639-1-list/)) Value: text in language The maximum length of value is 1000 | No |

### Item pairing
#### ItemGroupStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| i18n_group_name | I18nText | I18n product group name | Yes |
| group_name | string | Product group name | No |
| total_count | int32 | Total | No |
| option_count | int32 | Choose a few | Yes |
| item_list | List<ItemStruct> | List of items | Yes |
| allow_repeated_item | bool | Whether duplicate service units are allowed in the group | No |

#### ItemStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| i18n_name | I18nText | I18n item name | Yes |
| name | string | Item name (use I18nText object instead) | No |
| price | string | Price, for example: "2000" | No |
| currency | string | Currency For example: "IDR" | No |
| count | int32 | Total | Yes |
| image_list | List<ImageStruct> | Single product image list | No |

### Package plan
#### ImageStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| out_url | string | External image URL, merchants can pass this field. | Yes |

### Stock
#### StockInfoStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| stock_num | int64 | Stock quantity | Yes |
| stock_qty_limit_type | StockQtyLimitTypeEnum 1 = Limited Stock 2 = Unlimited inventory | Inventory cap type When there is no stock limit, the `stock_num`invalid | Yes |

### Available date
#### UseDateStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| use_date_type | UseDateTypeEnum | Use date type 2 = Specified number of days | Yes |
| day_duration | int32 | How many days is the purchase date? | No |

### Use time
#### UseTimeStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| use_time_type | UseTimeTypeEnum | Use time type 1 = Available all day 2 = Only available at designated times | Yes |
| time_period_list | List<TimePeriodStruct> | Time period list When UseTimeType = 2 has value | No |

#### TimePeriodStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| use_start_time | string | Start time (Format: 00:00:00) | Yes |
| use_end_time | string | End time (Format: 00:00:00) | Yes |
| end_time_is_next_day | bool | Whether it spans days | No |

### Unusable date
#### CannotUseDateStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| enable | bool | Switcher | Yes |
| days_of_week | List<DayOfWeekEnum> | Specify day of the week **not**available MONDAY = 1, TUESDAY = 2, WEDNESDAY = 3, THURSDAY = 4, FRIDAY = 5, SATURDAY = 6, SUNDAY = 7, | No |
| holidays | List<int64> | Specified holidays are not available | No |
| date_list | List<string> | Specified date is not available (Format: yyyy-MM-dd) | No |
| date_period_list | List<CanNoAppointmentDatePeriod> | Unavailable date interval, description | No |

#### CanNoAppointmentDatePeriod object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| i18n_description | I18nText | I18n description | No |
| description | string | Description | No |
| from_date | string | Start date (Format: yyyy-MM-dd) Merchant's local time zone | Yes |
| to_date | string | Deadline (Format: yyyy-MM-dd) Merchant's local time zone | Yes |

### Dine-in and take-out agreement
#### ConsumptionConventionStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| consumption_method | ConsumptionMethod | Consumption patterns DineIn = 1, (Dine-in) TakeAway = 2, (Takeout) BOTH_SUPPORTED = 3, (Both are supported) | Yes |

### Appointment information (optional)
#### AppointmentStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| need_appointment | bool | Whether to enable | No |
| ahead_time_type | AheadTimeTypeEnum | Advance appointment time type DAY = 1, HOUR = 2, MINUTE = 3, | No |
| ahead_num | int32 | Advance phone reservation is required X days/hours/minutes. | No |

### Other explanatory information (optional)
#### NoteStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| note_type | OtherNoteTypeEnum | Remark type TEXT = 1, (Text) TEXT = 1, (Text) | No |
| content | string | Content After the text is serialized with i18n | No |

### Restrict purchase rules (optional)
#### LimitBuyRuleStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| enable_limit | bool | Whether to enable restricted purchases | Yes |
| rule_list | list<LimitRuleItem> | List of purchase restriction rules | No |

#### LimitRuleItem object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| subject_type | SubjectTypeEnum | Purchase restriction subject (such as UID) UID = 1, // UID | Yes |
| range_type | RangeTypeEnum | Purchase restrictions (such as order date, lifetime, etc.) ORDER_DATE = 2, (Order date) LIFE_LONG = 3, (Lifetime) | Yes |
| limit_num | i32 | Purchase limit | Yes |
| dimension_type | DimensionTypeEnum | Effective dimensions (such as product, SKU, calendar, etc.) SKU = 2, | No |

### Response parameters
Only represents submitting Good to go, and the product review status is notified through webhook.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |

**Note**:
- Update product info won't infect the existing product's availability.  Once the update is completed,  it will take effect.
- This update/save Must provide all the key&values into the 'attr_key_value_map', in another word, not support partial update.  ( Can refer to update without review for partial update)
- Update flow won't change tt product-id. ( keep as the original save one)
- Strongly recommend merchants call "`product_opt_category/query/`" before save product.  To make sure the target shops are valid (update to date).
## Product Update (Exempt From Review)
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: After the product upload passes the review, the product inventory and price information will be updated without review and will update immediately.
#### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/update_free_audit/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| product_free_audit | ProductFreeAudit | Unapproved Update Details, Objects | Yes |
| third_product_id | string | Third-party product ID | Yes |
| language | string | Language | No |

#### ProductFreeAudit object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_product_id | string | Third-party product ID | Yes |
| local_currency | string | Commodity currency, eg: IDR | Yes |
| actual_amount | string | Product amount, eg: 12.3456 | Yes |
| stock_qty_limit_type | int | Stock type 1 = Limited inventory 2 = Unlimited inventory | Yes |
| stock_num | int | Inventory quantity, limited inventory needs to be filled in | Yes |

### Response parameters
Synchronized response, the update is successful if the request is successful.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |

## Delist the Product
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: After the product upload passes the review, the product will be removed.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/offline`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| third_product_id | string | Third-party product ID | Yes |
| language | string | Language | Yes |

### Response parameters
Synchronous response, the request is successful and the removal is successful.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |

## Product Review Revocation
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: If a product is waiting for review, you can cancel that review so the product can be resubmitted.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/withdraw_audit`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| third_product_id | string | Third-party product ID | Yes |
| language | string | Language | Yes |

### Response parameters
Synchronized response, the request is successful and the undo is successful.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |

## Product List Query
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: Check the status and details of products after they are created or updated.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/batch_query/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| product_type_list | List<ProductType> | Commodity type DISCOUNT_VOUCHER = 2 | Yes |
| list_tab | ListTabEnum | Product status information ALL = 0, (All) LISTED = 1, (Available) UNDER_REVIREW = 2,//under review REJECTED = 3,//failed REMOVED = 4,//removed SUSPENDED = 5,//banned DRAFT = 6,//draft | Yes |
| product_name | string | Product name | No |
| third_shop_ids | List<string> | List of third-party shop IDs | No |
| shop_ids | List<string> | TT Shop ID List | No |
| language | string | Language | No |
| pagination | Pagination | Pagination information | Yes |

### Response parameters
Synchronized response, the request is successful and the undo is successful.

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | MGetProductsResponseData | Actual data | No |

#### MGetProductsResponseData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| products | List<ProductListInfoStruct> | Product list information | No |
| next_pagination | NextPagination | Pagination information | No |

#### ProductListInfoStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| product_name | string | Product name | Yes |
| product_id | string | Product ID | Yes |
| third_product_id | string | Third-party product ID | Yes |
| reject_reason | string | Reason for rejection | No |
| product_type | ProductType | Product type | Yes |
| product_status | ProductStatusEnum | Product status | Yes |
| origin_amount | string | Original price | Yes |
| actual_amount | string | Actual price | Yes |
| image_url | string | Header image | Yes |
| category_id | string | POI category | Yes |
| category | CategoryStruct | Product category information | Yes |
| sold | string | Quantity sold | No |
| inventory | string | Stock | No |
| stock_qty_limit_type | StockQtyLimitTypeEnum | Inventory cap type | Yes |
| sold_start_time | int64 | Sales start time | Yes |
| sold_end_time | int64 | Sales end time | Yes |
| sold_time_type | SoldTimeTypeEnum | Sales time type | Yes |
| bond_shops | int64 | Number of bound shops | Yes |
| avaliable_shops | int64 | Number of available shops | Yes |
| create_at | int64 | Creation time | Yes |

#### CategoryStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| first_category_id | i64 | First-level category ID | Yes |
| first_description | string | First-level category description | Yes |
| second_category_id | i64 | Secondary Category ID | Yes |
| second_description | string | Secondary category description | Yes |
| third_category_id | i64 | Level 3 Category ID | Yes |
| third_description | string | Third-level category description | Yes |

#### NextPagination object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| current_page_size | int64 | Current number of pages | Yes |
| has_more | bool | Is there any more data? | No |
| total | int64 | Total | No |

## Product Details Inquiry
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: After getting the product list, view the online and audit details of a specific product.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product/query/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_product_id | string | Third-party product ID | Yes |
| merchant_id | string | Merchant ID | No |
| online | bool | Whether online True = online version False = under review version | Yes |
| language | string | Language | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | GetProductResponseData | Product data | No |

#### GetProductResponseData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| product_detail | ProductDetailStruct | Product details | No |

#### ProductDetailStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| product | ProductAndSkuStruct | Commodity basic information | Yes |
| audit_info | PlatformAuditStruct | Review information | No |
| operator | OperatorStruct | Operation Sponsor Information | No |
| product_operate_extra | ProductOperateExtra | Product operation additional information | No |

#### ProductAndSkuStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_product_id | string | Third-party product ID | No |
| product_id | string | Product ID | No |
| category_id | string | Leaf Category ID | Yes |
| product_type | common.ProductType | Commodity type DISCOUNT_VOUCHER = 2, (Group buying coupon) | Yes |
| category | CategoryStruct | Product category information | No |
| product_status | ProductStatusEnum | Product status LISTED = 1, (Available) UNDER_REVIEW = 2, (Under review) REJECTED = 3, (Failed) REMOVED = 4, (Removed) SUSPENDED = 5, (Banned) DRAFT = 6, (Draft) LISTED_UNDER_REVIREW = 11, (Released, under review) LISTED_REJECTED = 12, (Listed, review disapproved) | No |
| holiday_list | list<HolidayStruct> | Holiday list | No |
| sold | string | Quantity sold | No |
| product_full_status | ProductStatusEnum | Details page aggregation online and draft status Enumeration as above | No |
| attr_key_value_map | map<string, string> | [Additional attributes Attribute content is the same as "group buying coupon attribute". Jump to group buying coupon properties](https://bytedance.sg.larkoffice.com/docx/Opi9dojITo4zLBxbrQLlvcl4geg#UCtRdYBnmofnuJxXfmWlUNZ7gXd) | No |

#### CategoryStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| first_category_id | i64 | First-level category ID | Yes |
| first_description | string | First-level category description | Yes |
| second_category_id | i64 | Secondary Category ID | Yes |
| second_description | string | Secondary category description | Yes |
| third_category_id | i64 | Level 3 Category ID | Yes |
| third_description | string | Third-level category description | Yes |

#### HolidayStruct object

| **Field** | **Type** | **Required** | **Decription** |
| --- | --- | --- | --- |
| holiday_name | string | Yes | Holiday name |
| holiday_date | string | No | Holiday dates |
| holiday_id | i64 | Yes | Vacation Unique Device Identifier |

#### PlatformAuditStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| audit_msg | string | Review information | No |
| submit_time | i64 | Review submission time | No |
| audit_time | i64 | Approval/rejection time | No |
| audit_id | string | Review number | No |
| audit_title | string | Review Title | No |
| operator_role | OperatorRoleType | Operator role MERCHANT = 1, (Merchant) MERCHANT = 1, (Merchant) OPERATION = 2, (Operations) OPERATION = 2, (Operations) SYSTEM = 100, (System) SYSTEM = 100, (System) | No |

#### OperatorStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| operator_role | OperatorRoleType | Operator role MERCHANT = 1 , // 商家 MERCHANT = 1,//merchant OPERATION = 2 , // 运营 OPERATION = 2,//operation SYSTEM = 100, // 系统 SYSTEM = 100,//system | Yes |
| operator_id | string | Operator ID | No |
| operator_name | string | Operator name | No |
| operator_email | string | Operator mailbox | No |

#### ProductOperateExtra object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| operator | OperatorStruct | Operator information | No |
| source | Source | Operational sources | No |
| reason | string | Operational reasons | No |
| operate_time | i64 | Operating time | No |

## Product Category Inquiry
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**: View the merchant categories you can use when creating or updating products.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product_opt_category/query/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| language | string | Display language For example, en | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | GetProductOptCategoryResponseData | Data | No |

#### GetProductOptCategoryResponseData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| category_tree_list | list<CategoryTreeStruct> | Available categories | Yes |

#### CategoryTreeStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| category_id | string | Category ID | Yes |
| description | string | Category description | Yes |
| sub_category_list | list<CategoryTreeStruct> | Subcategory | Yes |
| parent_category_id | string | Parent Category ID | Yes |

## Products Can Be Queried in Shops
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note**:** **View the shops a merchant can use when creating or updating products.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/product_opt_shops/query/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| merchant_id | string | Merchant ID | Yes |
| language | string | Display language For example, en | Yes |
| pagination | Pagination | Pagination information | Yes |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error |  | Status code | Yes |
| data | GetProductOptShopsResponseData | Actual data | No |

#### GetProductOptShopsResponseData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| shops | list<ShopInfo> | Available categories | Yes |
| next_pagination | NextPagination | Pagination information | No |

#### ShopInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| shop_base_info | SearchShopInfo | shop basic information | Yes |
| available | bool | Is the shop available | Yes |
| unavailable_reason | list<int> | Reasons for shop unavailability 1 = Settlement account is not available 2 = Splitting rules do not exist 3 = The shop has not completed the claim | Yes |

#### SearchShopInfo object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| shop_id | int64 | Shop ID | Yes |
| shop_name | string | Shop name | Yes |
| third_shop_id | string | Third-party stop ID | Yes |
| location_en | string | English address | No |
| merchant_id | int64 | Merchant ID | No |

## National Holiday Inquiry
**Note**: There is a maximum queries per second (QPS) limit of 20.
**Note:** Check the merchant's national holidays to see if coupon usage should be restricted.
### Endpoint
`POST ``https://open.tiktokapis.com/v2/localservice/saas/holiday/batch_query/`
### Request parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| countries | `list<string>` | List of Requested Country Codes For example, ID | Yes |
| language | `string` | Language of returned holiday information | No |

### Response parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| error | ErrorStruct | Status code | Yes |
| data | `MGetHolidayByCountryResponseData` | Actual data | No |

#### MGetHolidayByCountryResponseData object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| holiday_map | map<string, list<HolidayStruct>> | Country and holiday information mapping table Key-country Value- Holidays | No |

#### HolidayStruct object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| holiday_id | i64 | Unique identifier for the holiday | Yes |
| holiday | string | Name of the holiday | Yes |
| starling_text | string | Starling text descriptions related to holidays | No |

## Product Status Webhook
**Note**: After the product is created and updated, the status update will be notified to the developer through the webhook.

| Field | Explanation |
| --- | --- |
| client_key | ID registered with TTOP by third-party developers (SAAS platform) |
| event product.status.doman_sync | Event name, the naming convention is generally aa.bb.cc. For example: video.upload.failed Event name: `ttls.product.status_update.result` |
| create_time | Timestamp in **seconds**since the Unix epoch |
| user_id | TikTok User Identification involved, null if no user involved |
| content | Marshalled JSON string. Serialized JSON string, TTOP only passes through, does not parse or perceive. |
| caller tiktok.local.solution_gateway | It's a tag from TT, just for debug tracking. |

#### Content

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| third_product_id | string | Third-party product ID | Yes |
| product_id | string | Product ID | Yes |
| product_type | ProductType | Product type BIZ_LINK = 1, DISCOUNT_VOUCHER = 2, (Group buying coupon) CASH_VOUCHER = 3, (Voucher) BOOKING = 4, (Order item) | Yes |
| category_id | int64 | Category ID | Yes |
| merchant_id | string | Merchant ID | Yes |
| product_status | ProductStatusEnum | Product status LISTED = 1, (Available) UNDER_REVIREW = 2, (Under review) REJECTED = 3, (failed) REMOVED = 4, (removeD) SUSPENDED = 5, (banned) DRAFT = 6, (draft) LISTED_UNDER_REVIREW = 11, (Released, under review) LISTED_REJECTED = 12, (listed, review disapproved) | Yes |
| action_type | GoodsDomainContentActionType | Operation type MERCHANT_EDITING = 0 , MERCHANT_SUBMIT = 1 , MERCHANT_WITHDRAWN = 2 , MERCHANT_DELISTED = 3 , GNE_BANNED = 4 , GNE_APPROVED = 5 , AUTO_APPROVED = 6 , GNE_REJECTED = 7 , GNE_UNBANNED = 8 , AUTO_DELISTED_ON_EXPIRATION = 9 , MERCHANT_DELETED = 10, GNE_DELISTED = 11, GNE_MODIFY = 12, | No |

Was this document helpful?