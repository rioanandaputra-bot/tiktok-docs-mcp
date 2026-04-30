Docs
# Query TikTok Shop Info
## User Interaction - Shop API endpoint
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned. As the scripting language is the same across various data categories, this value will help determine what data to fetch. | tiktok_shop_info | Yes |
| condition_groups | object | Specifications for what data should be used for querying. | condition_groups = [``{``"operator": "and",``"conditions": [``{``"field": "shop_name",``"operator": "eq",``"field_values": ["tiktok_shop"]``}``]``}``] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | shop_name,shop_rating,shop_review_count,item_sold_count,shop_id | No |
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
| result | string | Data fields returned from the query. Interface will only return the fields listed here for shops actively listed in the EU. | shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value |

Was this document helpful?