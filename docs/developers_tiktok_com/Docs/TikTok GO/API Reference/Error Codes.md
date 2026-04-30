Docs
# Error Codes

| **Error classification and handling suggestions** | **Error explanation** | **Related endpoint** | **Related scene** | **HTTP Status Code** | **Error Code** |
| --- | --- | --- | --- | --- | --- |
| Parameter and permission issues, retry will not succeed. It is recommended to contact TTLS Solution with log ID. | Parameter verification failed (not triggered when the merchant initiates the expectation, triggered by the interface dimension test). | `/v2/localservice/saas/fulfill/get_code_item_list/` | Scan or enter the code | 500 | -9990001 |
| The verifier has no permission for this store. | Scan or enter the code |  | -3000000 |
| Verify the input code parameter. The input verification code must be an integer. | Input code |  | -9990001 |
| User has no permission to scan/enter code. | Scan or enter the code |  | -3000000 |
| No performance / voucher information was found (not an error). | Scan or enter the code |  | -3000111 |
| There is no coupon available for verification at this store. | Scan or enter the code |  | -3000103 |
| Retry probability is successful. It is recommended to retry in place. If it still fails, contact TTLS with log ID. | Failed to obtain the right to scan or input the code for the verifier. | `/v2/localservice/saas/fulfill/get_code_item_list/` | Scan or enter the code | 500 | -9990202 |
| Failed to obtain the store permission of the verifier. | Scan or enter the code |  | -9990202 |
| Failed to query the merchant's main account (SaaS scenario). | Scan or enter the code |  | -9990202 |
| Scan code: QR code base64 decoding failed. | Scan the QR code |  | -3000110 |
| Scan code: QR code decryption failed. | Scan the QR code |  | -3000110 |
| Scan QR code: QR code deserialization failed (unable to parse QR code information from string). | Scan the QR code |  | -9995000 |
| Failed to obtain performance/voucher information. | Scan or enter the code |  | -9990202 |
| Failed to query orders and after-sales orders. | Scan or enter the code |  | -9990202 |
| Failed to query sub-performance orders and execution orders. | Scan or enter the code |  | -9990202 |
| In the SaaS scenario, when entering the code and reading the master, the voucher list needs to be re-queried, and the query fails. | Input code |  | -9990202 |
| No voucher information was found (not an error). | Scan or enter the code |  | -3000111 |
| Failed to query the product. | Scan or enter the code |  | -9990202 |
| QR code screenshot expired. | Scan the QR code |  | -3000109 |
| Query the URL of the product image. | Scan or enter the code |  | -9990202 |
| Failed to obtain holiday information (Business scenario: The holiday is unavailable all day, just a reminder). | Scan or enter the code |  | -9990202 |
| SaaS scenario - Only pack the coupon code information of the fulfillment/refund status when the QR code expires. | Scan the QR code |  | -3000109 |
| Parameter and permission issues, retry will not succeed. Contact TTLS with log ID. | Parameter verification failed (not triggered when the merchant initiates the expectation, triggered by the interface dimension test). | `/v2/localservice/saas/fulfill/redeem_code/` | Write-off | 500 | -9990001 |
| The verifier has no permission for this store. | Write-off |  | -3000000 |
| Parameter verification failed (normal requests are not expected to trigger this). | Write-off |  | -9990001 |
| Retry probability is successful. Recommended to recheck the code verification process for `get_code_item_list`. If it still fails, contact TTLS with log ID. | Failed to obtain the name of the verifier. | `/v2/localservice/saas/fulfill/redeem_code/` | Write-off | 500 | -9990202 |
| Failed to obtain the store permission of the verifier. | Write-off |  | -9990202 |
| Failed to obtain the verification permission of the verifier. | Write-off |  | -9990202 |
| Failed to query merchant main account (SaaS scenario). | Write-off |  | -9990202 |
| Redemption interface failed (error in fulfill_core layer logic execution). | Write-off |  |  |
| Redemption interface failed (core layer redemption interface timeout or other mesh layer error). | Write-off |  | -3000105 |
| Parameter validation failed (not expected in normal requests). | Write-off |  | -9990001 |
| Redemption ID generation failed. | Write-off |  | -9990101 |
| Failed to parse redemption code. | Write-off |  | -9990001 |
| Voucher: failed to read voucher record from database. | Write-off |  | -9990400 |
| Voucher: number of voucher records read does not match number of redemption codes. | Write-off |  | -9990402 |
| Voucher: redemption code has been refunded. | Write-off |  | -3000108 |
| Voucher: redemption code not within valid usage time. | Write-off |  | -3000100 |
| Voucher: redemption code has expired. | Write-off |  | -3000101 |
| Voucher: redemption code has already been used. | Write-off |  | -3000102 |
| Voucher: redemption state machine validation failed. | Write-off |  | -3000203 |
| Execution order: failed to read execution order. | Write-off |  | -9990400 |
| Execution order: execution order has been refunded. | Write-off |  | -3000108 |
| Execution order: execution order not within valid usage time. | Write-off |  | -3000100 |
| Execution order: execution order has expired. | Write-off |  | -3000101 |
| Execution order: execution order has already been used. | Write-off |  | -3000102 |
| Execution order: redemption state machine validation failed. | Write-off |  | -3000203 |
| Sub-fulfillment order: failed to read sub-fulfillment order. | Write-off |  | -9990400 |
| Sub-fulfillment order: failed to read applicable store/snapshot. | Write-off |  | -9990202 |
| Sub-fulfillment order: no applicable stores for product. | Write-off |  | -3000200 |
| Sub-fulfillment order: sub-fulfillment order has been refunded. | Write-off |  | -3000108 |
| Sub-fulfillment order: sub-fulfillment order refund in progress. | Write-off |  | -3000104 |
| Sub-fulfillment order: applicable stores do not include the current requesting store. | Write-off |  | -3000103 |
| Sub-fulfillment order: redemption state machine validation failed. | Write-off |  | -3000203 |
| Domain event ID generation failed. | Write-off |  | -9990103 |
| Failed to update redemption data (optimistic lock or other reasons). | Write-off |  | -9990452 |

Was this document helpful?