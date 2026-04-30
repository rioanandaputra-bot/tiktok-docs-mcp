Docs
# Query TikTok Shop Reviews
## User Interaction - Reviews API endpoint
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned. As the scripting language is the same across various data categories, this value will help determine what data to fetch. | tiktok_shop_reviews | Yes |
| condition_groups | object | Specifications for what data should be used for querying. The data can be: product_name, product_id, shop_name | condition_groups = [ { "operator": "and", "conditions": [ { "field": "product_id", "operator": "eq", "field_values": ["1234567810"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | product_name,review_text,review_like_count,create_time,review_rating | No |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 10, and the maximum value is 5000 per day across end points. (The value is low here as researchers can see the data and we want to keep this data to a low sample count only) **Execution Stage** The default value is 100, and the maximum value is 1000 in one query. If there are less than 1,000 results, that number will be returned in one go. (This is where researchers get access to all data and hence the increments are maximized based on performance possible) |  | No |

### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here foe reviews given for products sold in the EU. | product_name,review_text,review_like_count,create_time,review_rating |

Was this document helpful?