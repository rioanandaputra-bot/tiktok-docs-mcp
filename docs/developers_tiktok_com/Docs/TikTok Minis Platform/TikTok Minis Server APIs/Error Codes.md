Docs
# Error Codes
TikTok Minis APIs return errors in three categories: System Errors (server-side issues), Invalid Parameter Errors (request validation failures), and Business Errors (payment/subscription domain constraints). Use the error code and `log_id` to trace issues.
## System Error

| Code | Description | Action |
| --- | --- | --- |
| 50001000 | TikTok Internal Error | Retry or do nothing |

## Invalid Param Error

| Code | Description | Action |
| --- | --- | --- |
| 40001000 | Invalid Parameters | Check your request parameters |

## Business Errors

| Code | Description | Action |
| --- | --- | --- |
| 20011002 | Order not existed | Verify client key, trade order ID, and user ID |
| 20021001 | Submerchant ID invalid | Contact TikTok to enable payment capabilities |
| 20021002 | Outer order ID existed | Your external order ID is a duplicate |
| 20001003 | Tier ID invalid | Check the tier ID |
| 20021101 | Subscription is active | Cannot create a new one |
| 20021102 | Subscription is canceled | Can only reactivate, not create a new one |
| 20021103 | Subscription is on hold | Guide user to handle their current subscription |
| 20021108 | Change subscription unfinished | Wait 1 hour between change requests |
| 20021111 | Subscription too close to renewal | Cannot be changed within 24 hours of renewal |

Was this document helpful?