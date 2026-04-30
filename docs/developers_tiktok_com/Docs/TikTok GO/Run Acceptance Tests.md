Docs
# Run Acceptance Tests
Before you launch your solution, you must run acceptance tests. This is to ensure API integrations for each module are properly setup and simulate the end-to-end flow of POI claiming, product creation, and voucher redemption.
**Note**: For acceptance testing, the coding work should be finalized and be ready for testing. For detailed coding work, see the API reference documentation.
This guide demonstrates how to run and complete a mandatory acceptance test before launch.
## Test case availability
Please note that some business activities such as shop management and product management can be achieved via the Merchant Portal or API integration. You have the flexibility of selecting either one of these methods or both to manage your business activities.
For simplicity, this section will walk through all the test cases for supported modules. However, you will see only test cases with which you have established an API integration. For example, if you only integrate your redemption management model using APIs while managing shops and products through the Merchant Portal, you will only see a test case for voucher verification. All other test cases will not be visible to you.
Acceptance tests are conducted through your registered app on the Developer Portal.
## Testing preparation checklist
Before you begin testing, ensure you have the following items ready:

| **Item** | **Sandbox testing** |
| --- | --- |
| Developer Portal app | Your app has been set up and approved on the TikTok for Developers website. |
| Test merchant account | [You have a test merchant account](https://developers.tiktok.com/doc/set-up-developer-portal-account#) set up on your developer app |
| Merchant Platform account | You have a merchant platform account that has been bound to your Developer Portal app. |
| API credentials | Use client key of your Developer Portal app and the outet ID of the test mer |
| Shops | Create shops by API or under a test merchant on the Merchant Portal |
| Shops that link to a TikTok POI | TikTok can provide a test POI so you can link your test shops to that POI. You can use your test TikTok account to visit this testing POI. |
| Products | Create products by API or under a test merchant on the Merchant Portal |
| Payment & refund | The payment flow for testing is real, so we recommend setting a low product price for testing, such as $0.01 |
| Redemption | The redemption function should be ready either by QR code scanner or voucher code redemption |

## Acceptance testing procedure
You will need to complete multiple test cases, depending on what API integrations you used. The objective of each test case is to make sure the API setup is correct and there is no connection issue.
- Log into your TikTok for Developers account to access your developer app
- On your app page, click the **Access** tab. You should have already added test TikTok accounts and test merchants.
- Click the **Next** button until you reach the **Acceptance testing** page.
- Click the **Start testing** button to access each of the listed test cases.
- Use the provided example code for each test case and enter a **task_id** to verify whether the task was completed successfully.
## Test case descriptions
Note: The number of test cases that appear on your app page depends on which APIs you have integrated with.

| **Test case** | **Workflow** | **Steps** | **Associated scope** | **Verification steps** |
| --- | --- | --- | --- | --- |
| Claim outlets | Claim outlet (obtain task) → Claim task through query | 2 Steps | Shop Management | [[Create a POI claim](https://developers.tiktok.com/doc/shop-management#) via API, and copy the `task_id`from the API response Validate the `task_id`in the UI Perform a query to check the POI](https://developers.tiktok.com/doc/shop-management#) created, then copy the log ID from the response Validate the log ID from the UI |
| Upload qualifications | Outlet qualification upload (obtain task) → Qualification task through query | 2 Steps | Shop Management | [[Upload the shop qualifications](https://developers.tiktok.com/doc/shop-management#) via API, and copy the `task_id`from the API response Validate the `task_id`from the UI Perform a query of the qualification information](https://developers.tiktok.com/doc/shop-management#), then copy the log ID from the response Validate the log ID from the UI (only validate once per log ID) |
| Edit outlet information | Outlet basic information update (obtain task) → Update task query | 2 Steps | Shop Management | [[Update the shop's basic information](https://developers.tiktok.com/doc/shop-management#) via API, then copy the `task_id`from the API response Validate the `task_id`from the UI Perform a query to check the update status](https://developers.tiktok.com/doc/shop-management#), copy the log ID from the response Validate the log ID from the UI (only validate once per log ID) |
| Edit outlet details | Update outlet decoration - business hours, modify header image (obtain task) → Decoration task through query | 2 Steps | Shop Management | [[Modify any of the below fields](https://developers.tiktok.com/doc/shop-management#) such as image, business hours, phone number, or average per-person price via API, then copy the `task_id`from the API response Validate the `task_id`from the UI Perform a query to check the status](https://developers.tiktok.com/doc/shop-management#) of the task, then copy the log ID from the response Validate the log ID from the UI (only validate once per log ID) |
| Transaction refunds | Query product outlets that can be mounted → Create/update merchandise (obtain task) → Review task query → Remove merchandise from shelves | 4 Steps | Product Management | [[[[Query if the product outlet can be mounted](https://developers.tiktok.com/doc/product-management#) list, then copy the log ID from the response Validate the log ID from the UI Create the product](https://developers.tiktok.com/doc/product-management#) via API Validate the product ID from the UI Query the product details](https://developers.tiktok.com/doc/product-management#)via API, then copy the log ID from the response Validate the log ID from the UI Remove the product](https://developers.tiktok.com/doc/product-management#) via API Validate the product ID from the UI |
| Product changes | Third-party order placement → Order query → Order verification | 1 Step | Voucher Management | [Query the voucher code information](https://developers.tiktok.com/doc/voucher-management#), then copy the log ID from the response Enter the log ID to verify the query result |

## Testing results
Make sure each test case is successfully completed before moving forward with the launch process. If you face persistent errors in any of the test cases, please contact your point of contact at TikTok for assistance.
Was this document helpful?