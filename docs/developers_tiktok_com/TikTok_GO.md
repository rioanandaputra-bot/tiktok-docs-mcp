# TikTok GO

> Consolidated from 14 source files.



---
## SOURCE: TikTok GO/Integrate With Dining SaaS.md

Docs
# Integrate With Dining SaaS
This guide lists the key API connections for you to integrate TikTok GO Dining services with your system.
Alternatively, you can use the Merchant Portal to manage your business activities such as shops, products and sales. However, certain features are only available through API integration, such as voucher redemption management.
## Shop Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| POI Claiming | Allows you to create a new POI for a shop or outlet and query existing POIs | [[[Shop Management APIs](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Claim POI tasks](https://developers.tiktok.com/doc/shop-management#) Description | Create a new outlet → Fill in the outlet's Basic information |
| Shop Certifications Upload and Check | Allows you to upload shop certifications and check for existing certifications | [[[[Upload Shop Certifications API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Upload Shop Certification tasks](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Upload and submit certifications for your outlet |
| Shop Decoration | Allows you to upload and view detailed information and images for your shop | [[[Batch Submit Shop Decoration API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Decorate Shop API](https://developers.tiktok.com/doc/shop-management#) Description | Edit outlet information → add business information |
| Shop Basic Info | Allows you to update the basic information for your shops | [[[[Update Shop Basic Info API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Update Shop Basic Info tasks API](https://developers.tiktok.com/doc/shop-management#)Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Create a new outlet → Fill in the outlet's Basic information |
| Batch Query Shop Information | Allows you to query information for multiple shops in a single request | [[Batch Query Shop Information API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A |

## Product Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| Product Creation and Update | Allows you to create and update the product information | [[Update/Create Product](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Create new product → fill in product information |
| National Holiday Inquiry | Allows you to query the national holiday by countries | [[National Holiday Inquiry](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A |
| Product Query | Allows you to query various product information after creation | [[[[[[Get Delist the Product API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Product Category Inquiry](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Products Can Be Queried in Shops API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Filter listed products |
| Product Update (Exempt from Review) | Allows you to update certain product information that is exempt from review after the initial review is approved | [[Product Update (Exempt From Review) API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Edit audit-free information |
| Product Review Revocation | Allows you to withdraw a product from review | [[Product Review Revocation API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Filter products under review |
| Voucher Query | Allows you to query voucher information | [Query Voucher API](https://developers.tiktok.com/doc/product-management#) Description | N/A |
| Redeem Management (Recommended) | Allows you to redeem vouchers using a QR code scanner or voucher codes | [[Redeem Voucher](https://developers.tiktok.com/doc/voucher-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A (Merchant Portal doesn't support this feature) |

## Voucher Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| Voucher Query | Allows you to query voucher information | [Voucher Query API](https://developers.tiktok.com/doc/voucher-management#) Description | N/A |
| Redemption management (Recommended) | Allows you to redeem vouchers using QR code scanner or vouchers' code | [[Redeem Code API](https://developers.tiktok.com/doc/voucher-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A (Merchant Portal doesn't support this feature) |

Was this document helpful?


---
## SOURCE: TikTok GO/Launch Your Solution.md

Docs
# Launch Your Solution
After you've successfully completed acceptance testing, you are ready to launch your solution.
### Prerequisites for launch
Before launch, go through the following checklist to ensure you've completed all of the necessary items.

| **Item** | **Task ** | **Details** |
| --- | --- | --- |
| 1 | Complete acceptance testing | Make sure you have passed all test cases on the **Acceptance testing**page of your developer app |
| 2 | Ensure all outlets are claimed | Either use APIs or the Merchant Portal to claim outlets. Make sure that you have the relevant documents and basic information about outlets prepared. You can check the status of your outlets on the Merchant Portal. This step may have been completed during the integration process. |
| 3 | Finish creating products | Prepare product photos, title, and descriptions and create all the products and make sure they are associated with relevant outlets. You can use APIs or the Merchant Portal to do so. This step may have been completed during the integration process. |
| 4 | Make sure that products and outlets are mapped with merchant's own system | [TikTok needs to understand the relationship between the merchant's outlet ID and TikTok's outlet ID and vice versa with the product ID. This is so TikTok knows which outlet or product is being redeemed when the merchant sends the request to TikTok. There are two ways to build the mapping relationship: you can upload a spreadsheet into the Merchant Portal or use the Update Product API](https://developers.tiktok.com/doc/product-management#). This step may have been completed during the integration process. |
| 5 | All relevant employees at the outlets should be trained to handle QR codes | Store employees at outlets must be trained on the following: How to open QR codes in TikTok and direct customers how to do so How to redeem multiple QR codes or multiple orders How to handle errors TikTok suggests employees should retry the redemption if an error occurs |
| 6 | Connect the approved app with your merchant | [Refer to the steps to connect your app to your merchant](https://developers.tiktok.com/doc/set-up-developer-portal-account#) |

### Launch procedure
To launch your solution, log into your developer account and go to your app:
- Under **Solutions**, click the **Access** tab.
- On the **Dining purchasing solutions** page, click the **Publish** button.
- If you don't see the **Publish** button, click the** Next** button until you see it.
- If there are no issues, you will see the success page. Click the **Done** button to return.
**Note**: The **Sandbox **icon next to the solutions title will disappear after launch.
Was this document helpful?


---
## SOURCE: TikTok GO/Obtain Access Token for APIs.md

Docs
# Obtain Access Token for APIs
To use TikTok's APIs, you will need to use an access token. Use the following reference tables to retrieve and refresh an access token.
## Get Access Token
For the first time, when developers receive notification that merchants have approved their request for certain scopes, they can send an HTTP request to get their access token bundle.
### Endpoint
`POST ``https://open.tiktokapis.com/merchant/oauth/token/`
### Authorization headers

| **Field** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |
| x-tt-target-idc | alisg |

### Request

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Unique identification key provisioned to the partner |
| client_secret | string | Unique identification secret provisioned to the partner |
| merchant_id | string | Unique identification of merchant that partner applied for |
| grant_type | string | Action type such as `access_token`to retrieve access token |

Example:
```
curl --location 'https://open.tiktokapis.com/merchant/oauth/token/' \
--header 'x-tt-target-idc: alisg' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=xxxxxxx' \
--data-urlencode 'client_secret=xxxxxxxx' \
--data-urlencode 'grant_type=access_token' \
--data-urlencode 'merchant_id=xxxxxx'
```
### Response

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| access_token | string | Access token used for API call self identification |
| expires_in | int64 | Unix timestamp indicating when the access token expires |
| refresh_token | string | Refresh token used to request a new access token when the current one expires |
| refresh_expires_in | int64 | Unix timestamp indicating when the refresh token expires |

Example:
```
{
    "access_token": "xxx",
    "expires_in": 1749368707,
    "refresh_expires_in": 1906616707,
    "refresh_token": "xxx"
}
```
## Refresh Access Token
Each access aoken usually has an expiration time of 120 hours (5 days). After they expire, developers should use refresh the access token.
Note that if there is a scope range change (for example, if merchants revoke or approve new scopes), the access token value will change.
### Endpoint
`POST ``https://open.tiktokapis.com/merchant/oauth/token/`
### Authorization headers

| **Field** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |
| x-tt-target-idc | alisg |

### Request Body

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Unique identification key provisioned to the partner |
| client_secret | string | Unique identification secret provisioned to the partner |
| merchant_id | string | Unique identification of the merchant that the partner applied for |
| grant_type | string | Action type such as `refresh_token`for refreshing the access token |
| refresh_token | string | Token previously issued to the client used to request a new access token without re authentication |

Example:
```
curl --location 'https://open.tiktokapis.com/merchant/oauth/token/' \
--header 'x-tt-target-idc: alisg' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_key=xxxxx' \
--data-urlencode 'client_secret=xxxxxx' \
--data-urlencode 'grant_type=access_token' \
--data-urlencode 'merchant_id=xxxxxxx' \
--data-urlencode 'refresh_token=mrt.xxxxxx.s1'
```
### Response

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| access_token | string | Access token used for API call self identification |
| expires_in | int64 | Access token expiration time Unix timestamp |
| refresh_token | string | Refresh token used to refresh an access token when it expires |
| refresh_expires_in | int64 | Refresh token expiration time Unix timestamp |

Example:
```
{
    "access_token": "xxx",
    "expires_in": 1749368707,
    "refresh_expires_in": 1906616707,
    "refresh_token": "xxx"
}
```
Was this document helpful?


---
## SOURCE: TikTok GO/Prepare Product Content.md

Docs
# Prepare Product Content
This guide demonstrates how to configure your products. There are two methods to create and manage product content: via the Merchant Portal, or SaaS APIs.
## Create a product via Merchant Portal
- Log into the Merchant Portal.
- Click on the **Products** tab.
- Click the **Create Product** button.
- When prompted to create a new product, select the relevant category and type. **Discount voucher** will be selected by default. Click the **Next** button.
- Upload an image of the product and input the product's name. Click the **Confirm **button.
- The newly created product will be listed with the status **Under review**.
You can view, edit, withdraw, or offline each product using the icons next to the listed product.
## Create a product via SaaS APIs
[You can also use SaaS APIs to create products. Refer to the parameter details and implementation in the Create Product API reference](https://developers.tiktok.com/doc/product-management#).
### Product creation example
**API Request**
_Please refer to the detailed API page for compulsory fields as well as format_
```
curl --location 'https://open.tiktokapis.com/v2/localservice/saas/product/save/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer mat.sjhBhSeKr6rC3lYgEJ4a0I9IazsQh0vVlGiwAuxTljjE61DCOOHVJQayqKpH.s1' \
--header 'x-tt-env: ppe_ttls_se_portal' \
--header 'x-use-ppe: 1' \
--data '{
    "merchant_id": "100983406680068",
    "third_product_id": "test_portal_1736",
    "category_id": "24020301",
    "product_type": 2,
    "
```
**API Response**
```

{
    "data": {
        "product_id": "19271577661700"
    },
    "error": {
        "code": "0",
        "message": "success",
        "log_id": "202512201737102D104F5A72E94ABB401A"
    }
}
```
Was this document helpful?


---
## SOURCE: TikTok GO/Run Acceptance Tests.md

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


---
## SOURCE: TikTok GO/Set Up Developer Portal Account.md

Docs
# Set Up Developer Portal Account
To connect to the TikTok Go Dining SaaS API gateway, you must create an app on the TikTok for Developers website. This developer app will allow you to access TikTok's APIs.
## Register for a TikTok developer account
[Sign up for an account](https://developers.tiktok.com/signup) on the TikTok for Developers website using an official merchant email such as an admin-level company email, or a company email like "merchant-tiktok@merchant.com".
## Create an organization
Create an organization on the Developer Portal that represents your business:
- Click **Developer Portal** in the navigation bar of the TikTok for Developers website.
- Click **My organizations**.
- Click **Create organization**.
- Name your organization using the full name of your business entity. This information will be displayed to TikTok users.
**Note**: You cannot change the organization name after you create it.
**Important**: Once you've created your organization, please inform your business development (BD) partner at TikTok that you intend to also create an app on the Developer Portal.
## Create an app
Create an app in the Developer Portal that represents your service. You will use this app to register information and activate business solutions.
- Click **Developer Portal** in the navigation bar of the TikTok for Developers website.
- Click **Manage apps**.
- Click the **Connect an app** button.
- Select the organization you created as the app's owner.
- Enter your brand name as the **App name**.
- Select **TikTok Go** as the app type.
**Note**: If you do not see "TikTok GO" as an app type, reach out to your BD partner at TikTok.
After you've created an app, click the **Basic information** tab to view and manage your app's main information.
- **App ID**: Your app's unique identifier.
- **Client key and Client secret**: Unique identification credentials that are unique to your app; these are required when using TikTok's APIs.
## Request solution activation
Go to the **Activation** page, located under **Solutions** on the sidebar of your app page. Each solution listed has multiple capabilities that you can select.
You must apply for solutions to activate them:
- Click on the name of the desired solution. If your platform offers dining services, select **Dining purchasing solutions**.
- Select which permissions you want to apply for.
- For **Dining purchasing solutions**, the **Vouchers Verification** scope is required. **Outlets management** and **Products management** are optional.
- Click the **Apply for activation** button.
- Fill in the reason for your application. You must include the name of your merchant and the full name of your business development colleague at TikTok.
- Click the **Submit** button. Our team will review your application.
## Connect your app to webhooks
After your solution activation application has been approved, you must connect to TikTok's relevant webhooks. First set a launch time for when you want to start using the requested capabilities.
- Go to the **Access** tab on your app page and find your desired solution. Click the **Connect** button.
- Select the capabilities you want to integrate, then click the **Apply for access** button.
- Select a date for your launch time, which is when you would like to start using this capability. Click the **Confirm** button.
Next, you must configure webhooks. TikTok currently offers six webhooks to merchants. Connect to all of the necessary webhooks by providing a callback URL.
- Click the **Add URL** button.
- Enter a valid callback URL then click the **Confirm** button.
- Verify the webhook on your end to make sure the provided URL is correct.
**Note**: If you need to change or reconfigure any of your capabilities up to this point, you must discard your solution and start over.
## Prepare accounts and merchants for testing
To prepare for acceptance testing, you'll need to register two types of accounts to test your solutions. These accounts should only be used for testing purposes.
- A TikTok account
- A test merchant
### Prepare TikTok test accounts
Test TikTok accounts should belong to your staff, and will be used to test redemption capabilities. To register test TikTok accounts, first go to the **Access** tab on your app page.
- On the **Acceptance preparation** page, make sure the toggle is switched to **TikTok accounts**.
- Click **Add TikTok account**.
- Enter TikTok account's UID, then click the **Confirm** button.
- You can add up to five TikTok test accounts.
### Prepare test merchants
Test merchants will be used to test API development. To register test merchants, do the following:
- Switch the toggle on the Acceptance preparation page to **Shared test merchant**.
- Click **Apply for a shared test merchant**.
- Select an automatically generated test merchant and input a phone number or email address, then click the **Apply** button.
- When you apply for a test merchant, outlets are automatically generated. You will need to claim these outlets in the Merchant Portal.
- You can subsequently create other outlets and create products associated with those outlets.
- Each test merchant is only valid for 30 days.
- You will receive an SMS message or email with a link to activate the test merchant.
- If you haven't received the activation link, you can also log into the Merchant Portal to manually activate it.
After you've added your test merchant, you can perform the following actions:
- **Log in**: Log into your merchant account
- **Extend time**: Add 15 days to your shared test outlet access period. You have a maximum of 5 extensions.
- **View**: Scan the QR code using your registered TikTok test account to view your outlet's detail page on TikTok.
Note: Creating products requires moderation from TikTok.
## Connect the approved app with your merchant
After adding test merchants, you'll need to authorize them in the Merchant Portal.
- Log into the Developer Portal.
- Click **Dining merchant authorization **under the **Collaborative** tab.
- Click **Request permission **and enter the **Merchant ID.**
- Click **Request**.
- Log into the Merchant Portal.
- Go to the **Application authorization** tab.
- Click the **Authorize** button next to the application from your test merchant. Click the **Accept** button to approve this test merchant.
**Note**: You must complete this process once with your test merchant and once with your actual live merchant.
## Bind outlet to third shop ID
The "third shop ID" refers to the outlet's ID in your own system. In this step, you need to bind your outlet ID with the outlet ID created by TikTok GO.
- Log into your Merchant Portal account.
- Under the **Manage Outlets** tab, click the **Outlet data** dropdown, then click **Upload application ID**.
- Click on the **Download** button to download the spreadsheet file.
- Add the following information to the file:
- Client Access Key of this merchant, you may copy it from the main page
- TikTok Outlet ID which you can copy from the **Manage outlets** page
- Third_shop_ID which should be your outlet ID in your own system
- Save the file then upload it.
- Click **Confirm** button to submit the file.
Was this document helpful?


---
## SOURCE: TikTok GO/Set Up Merchant Portal Account.md

Docs
# Set Up Merchant Portal Account
As a new merchant, you must register on the TikTok Go Merchant Portal to manage your accounts and business seamlessly. This guide demonstrates how to create a new Merchant Portal account and onboard your business in five steps:
- Register a primary account
- Submit onboarding qualifications
- Claim outlets
- Create and activate a cashier account
- Set up a collection account
## Register and log in with the primary account
Note: The current Merchant Portal only available to merchants in Indonesia by invitation.
To create an account as a new merchant, do the following:
- [Visit the Tokopedia Go for Dining website](https://merchant-id.tokopedia.com/account/login?redirect_url=%2F&mode=1&phoneLoginMode=1) to create a Merchant Portal account. Enter the invitation code when prompted, then click the **Submit** button.
- Choose to register a primary account using either a phone number or an email address.
- Log in using your registered account information.
## Submit onboarding qualifications
After you've registered and logged in, submit your onboarding qualifications to get your business listed.
- Click the **Get started** button.
- Fill in the requested information and upload qualification images (up to 10 MB).
- Click the **Submit** button to enter the review process. This process is expected to take 1-3 working days.
## Claim outlets
To claim an outlet, you must first select the outlets you want to claim, and then submit certification for each outlet. There are three methods to claim outlets:
- Search for outlets to claim
- Add new outlets to claim
- Batch upload outlet information to claim
To access outlets on the Merchant Portal, click the **Claim** button on the homepage, or go to the** Outlets** tab, then **Manage outlets**.
### Select outlets to claim
#### Method 1: Search for outlets to claim
If your outlet exists within Tokopedia's system, you can search for it. On the **Manage outlets** page:
- Click the **Claim** button.
- Search for your outlets using keywords.
- Select the outlets you want to claim from the list. You can select one or more outlets (up to 50 outlets per batch).
- Click the **Submit **button.
- Preview the selected items. You can delete any unwanted outlets.
- Click the **Confirm **button, and then the **Submit** button to proceed to the qualification upload page.
#### Method 2: Add new outlets to claim
If a desired outlet is not found in the search results, do the following:
- Click** Create a new outlet** to add the outlet.
- Fill in the required basic outlet information.
**Important**: Ensure the accuracy of the information you provide.
- You can reference map software for details such as latitude and longitude.
- Fill in business information such as the phone number, opening hours, and average spending based on the actual situation.
- Click the **Create **button** **to proceed to the certification upload page.
#### Method 3: Batch upload outlet information to claim
If you want to upload multiple outlets at once:
- On the **Manage outlets** page, click the dropdown next to the **Claim** button. Click **Upload to claim**.
- Click **Download** to download the outlet information spreadsheet template.
- After filling in the outlet information required for the template, upload the completed form on this page.
- Click **Next **to proceed to the qualification upload page.
The outlet information template is as shown:
- Do not modify the header or any other template information. Ensure that all data is entered in **Sheet1.**
- Start entering data from **Row 4**, as the system parses data from there.
- It is recommended to upload no more than 20 rows at a time.
### Submit certifications for outlets
After completing selecting your desired outlets, you must submit certification for each outlet.
- Proceed to the outlet qualification upload page and upload the required files as instructed.
- If you want to upload qualifications later, you can close the window. You can find outlets awaiting qualifications on the **Manage outlets** page, and click **Batch submit** to submit qualifications in batches.
## Create and activate cashier accounts
Before you begin merchant operations, you must create and activate cashier accounts for each outlet under your primary Merchant Portal account. These cashier accounts correspond to staff members who can redeem vouchers at each outlet location.
**Note**: Alternatively, you can use SaaS API to complete this account creation step.
### Create a cashier account
Log into the Merchant Portal with the primary account. Then go to the **Manage staff** page and click the **Add member** dropdown. You can create accounts individually or in batches.
#### Method 1: Single account creation
- Select **Add new member**.
- Fill in the staff member's information and invite them via phone number or email address.
- Set** Scope** to "**Selected outlets**” and select the desired outlet.
- Assign the role of **Cashier**.
#### Method 2: Batch account creation
- Select **Batch import members**.
- Download the template and fill in the required information in the spreadsheet.
- Upload the completed template then click the **Import** button.
### Activate the cashier account
After you create accounts for your cashiers, they will receive an SMS message or email with an activation link.
Once they receive the activation link, staff members must open the link, complete identity verification, and set a login password.** **This activates the cashier account.
After activation, the cashier needs to download the Tokopedia app and log into their cashier account.
## Set up a collection account
Merchants do not need to provide additional information for setting up a collection account. Click the **Set up** button to initiate the account opening review process. Once the process is completed, the collection account will be ready for use.
Was this document helpful?


---
## SOURCE: TikTok GO/TikTok GO.md

Docs
# Dining Overview
TikTok GO Dining is a service that helps local dining establishments to list outlets online and provide a dynamic channel to sell and manage merchants' product vouchers, manage user relationships, and more. TikTok GO Dining has two components:
- [**TikTok GO Dining SaaS**: APIs that connect the merchant's system to TikTok, enabling seamless integration in creation of outlets and vouchers as well as voucher redemption. These are accessed through the Developer Portal on the TikTok for Developers website](https://developers.tiktok.com/).
- **Merchant Portal**: A separate online portal where merchants can manage sales accounts, products, reply to user comments, and more.
## Key modules of Dining SaaS
Dining SaaS offers three suites of APIs that let you manage your shops (outlets), products, and voucher redemption.

| **Shop (outlet) management** | **Product management** | **Redemption functionalities** |
| --- | --- | --- |
| A set of APIs that allow merchants to manage its shops (also called outlets): Claim outlets Upload certifications Decorate outlets Query and check outlet information | A set of APIs that allow merchants to manage its products/vouchers: Create and update product information Remove products or change to offline Query and check product information | A set of APIs that allow merchants to redeem or change the status of vouchers: Redeem vouchers Refund vouchers Query vouchers |

## Steps to integrate with TikTok Go Dining SaaS
You will need to follow the steps below to integrate your business with TikTok Go Dining System:
Refer to our documentation for step-by-step instructions:
### Administration

| **Action** | **Guide** |
| --- | --- |
| Create an account on the Merchant Portal to manage your business | [Set Up Merchant Portal Account](https://developers.tiktok.com/doc/set-up-merchant-portal-account) |
| Create an account on the Developer Portal to obtain access to technical integrations | [Set Up Developer Portal Account](https://developers.tiktok.com/doc/set-up-developer-portal-account) |
| Obtain an access token to use TikTok's APIs | [Obtain Access Token for APIs](https://developers.tiktok.com/doc/obtain-access-token-for-apis) |

### Development

| **Action** | **Guide** |
| --- | --- |
| Use TikTok's SaaS APIs to manage shops, products, vouchers, and more | [[Integrate With Dining SaaS](https://developers.tiktok.com/doc/integrate-with-dining-saas) Dining SaaS Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code) |

### Content Prep

| **Action** | **Guide** |
| --- | --- |
| Configure your products on the Merchant Portal or using SaaS APIs | [Prepare Product Content](https://developers.tiktok.com/doc/prepare-product-content) |

### Testing

| **Action** | **Guide** |
| --- | --- |
| Complete test cases after development to ensure API functionality | [Run Acceptance Tests](https://developers.tiktok.com/doc/run-acceptance-tests) |

### Launch

| **Action** | **Guide** |
| --- | --- |
| Launch your solution on TikTok | [Launch Your Solution](https://developers.tiktok.com/doc/launch-your-solution) |

Was this document helpful?


---
## SOURCE: TikTok GO/API Reference/API Reference.md

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


---
## SOURCE: TikTok GO/API Reference/Category Tree.md

Docs
# Category Tree
## Food and Drink

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 50000 | Food and Drink | 50100 | Bakery Shop | 05a1a0 | Bakery Shop |
| 50000 | Food and Drink | 50200 | Confectionery | 05a1a4 | Confectionery Shop |
| 50000 | Food and Drink | 50300 | Dessert Shop | 05a1a1 | Dessert Shop |
| 50000 | Food and Drink | 50300 | Dessert Shop | 05a1a2 | Ice Cream Shop |
| 50000 | Food and Drink | 50300 | Dessert Shop | 05a4a1 | Yogurt Shop |
| 50000 | Food and Drink | 50400 | Drinks | 05a0a4 | Drinks |
| 50000 | Food and Drink | 50400 | Drinks | 05a0a1 | Bubble Tea Shop |
| 50000 | Food and Drink | 50400 | Drinks | 05a0a2 | Juice Shop |
| 50000 | Food and Drink | 50400 | Drinks | 05a0a3 | Coffee Shop |
| 50000 | Food and Drink | 50400 | Drinks | 05a0a5 | Tea Shop |
| 50000 | Food and Drink | 50500 | Restaurant | 05a2b6 | Restaurants |
| 50000 | Food and Drink | 50600 | Cafeteria | 05a2a5 | Cafe |
| 50000 | Food and Drink | 50700 | Deli Restaurant | 05a2a6 | Deli Restaurant |
| 50000 | Food and Drink | 50800 | Food Court | 05a2a9 | Food Court |
| 50000 | Food and Drink | 50900 | Snacks | 05a4a0 | Snacks |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a3b7 | Specialty Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05b0b0 | Soup Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05b0b1 | Porridge Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05b0b2 | Fine Dining Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2b5 | Vegetarian And Vegan Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2b2 | Salad Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2a2 | Breakfast Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2a3 | Brunch Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2a4 | Buffet Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2a7 | Family Restaurant |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2b1 | Gastropub |
| 50000 | Food and Drink | 51000 | Speciality Dining | 05a2b0 | Fusion Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05a3a1 | Chinese Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b3 | Hong Kong Style Cafe / Cha Chaan Teng |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b4 | Dim Sum Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b5 | Hot Pot Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b6 | Chinese Dumpling Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b7 | Chinese Noodle Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b8 | Cantonese Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b0b9 | Sichuan Restaurant |
| 50000 | Food and Drink | 51100 | Chinese Cuisine | 05b1b0 | Beijing Restaurant |
| 50000 | Food and Drink | 51200 | European Cuisine | 05b1b1 | European Cuisine |
| 50000 | Food and Drink | 51200 | European Cuisine | 05b1b2 | Spanish Restaurant |
| 50000 | Food and Drink | 51200 | European Cuisine | 05b1b3 | Tapas Restaurant |
| 50000 | Food and Drink | 51200 | European Cuisine | 05b1b4 | Creperie |
| 50000 | Food and Drink | 51200 | European Cuisine | 05b1b5 | Greek Restaurant |
| 50000 | Food and Drink | 51200 | European Cuisine | 05a3a3 | French Restaurant |
| 50000 | Food and Drink | 51200 | European Cuisine | 05a3a4 | German Restaurant |
| 50000 | Food and Drink | 51300 | Italian Cuisine | 05a3a7 | Italian Restaurant |
| 50000 | Food and Drink | 51300 | Italian Cuisine | 05b1b6 | Italian Pasta Restaurant |
| 50000 | Food and Drink | 51300 | Italian Cuisine | 05b1b7 | Italian Pizza Restaurant |
| 50000 | Food and Drink | 51300 | Italian Cuisine | 05b1b8 | Tuscan Restaurant |
| 50000 | Food and Drink | 51300 | Italian Cuisine | 05b1b9 | Sicilian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a5a0 | Other Food and Drinks |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05a3b4 | Thai Restaurant |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05b2b0 | Thai Street Food Stall |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05b2b1 | Thai Noodle Restaurant |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05b2b2 | Thai Seafood Restaurant |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05b2b3 | Tom Yum Goong Restaurant |
| 50000 | Food and Drink | 51400 | Thai Cuisine | 05b2b4 | Som Tum Restaurant |
| 50000 | Food and Drink | 51500 | Western Cuisine | 05b2b5 | Western Restaurant |
| 50000 | Food and Drink | 51500 | Western Cuisine | 05a2b4 | Steak House |
| 50000 | Food and Drink | 51500 | Western Cuisine | 05a2a0 | Barbecue And Grill Restaurant |
| 50000 | Food and Drink | 51500 | Western Cuisine | 05b2b6 | Diner |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05a3b6 | Vietnamese Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b2b7 | Pho Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b2b8 | Hue Food Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b2b9 | Banh Xeo Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b3b0 | Steamed Rice Roll Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b3b1 | Broken Rice Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b3b2 | Banh Mi Restaurant |
| 50000 | Food and Drink | 51600 | Vietnamese Cuisine | 05b3b3 | Vietnamese Street Food Stall |
| 50000 | Food and Drink | 51700 | Indian Cuisine | 05a3a5 | Indian Restaurant |
| 50000 | Food and Drink | 51700 | Indian Cuisine | 05b3b4 | Biryani Restaurant |
| 50000 | Food and Drink | 51700 | Indian Cuisine | 05b3b5 | Bangladeshi Restaurant |
| 50000 | Food and Drink | 51700 | Indian Cuisine | 05b3b6 | Tiffin Center |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a3a6 | Indonesian Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a1 | Martabak |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a2 | Bakso Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a3 | Nasi Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a4 | Padang Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a5 | Nasi Goreng Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a6 | Soto Ayam Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a7 | Tegal Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a8 | Seblak Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05a8a9 | Soto Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b3b7 | Pecel Lele Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b3b8 | Pempek Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b3b9 | Betawi Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b0 | Nasi Uduk Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b1 | Ayam Penyet Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b2 | Sundanese Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b3 | South Sulawesi Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b4 | Balinese Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b5 | Javanese Restaurant |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b6 | Satay |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b7 | Indonesian Noodles |
| 50000 | Food and Drink | 51800 | Indonesian Cuisine | 05b4b8 | Indonesian Chicken & Duck |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05a3a8 | Japanese Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b4b9 | Ramen Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b0 | Udon Noodle Shop |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b1 | Shabu Shabu And Sukiyaki Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b2 | Soba Noodle Shop |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b3 | Unagi Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b4 | Oden Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b5 | Yakisoba Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b6 | Donburi Dishes |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b7 | Japanese Curry Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b8 | Okonomiyaki Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b5b9 | Sushi Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b0 | Yakitori Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b1 | Tempura Dish Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b2 | Washoku Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b3 | Yakiniku Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b4 | Gyoza Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b5 | Kusiage Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b6 | Sashimi Restaurant |
| 50000 | Food and Drink | 51900 | Japanese Cuisine | 05b6b7 | Japanese Izakaya Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05a3a9 | Korean Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b6b8 | Gimbap Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b6b9 | Kalguksu Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b0 | Tteokbokki Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b1 | Gamjatang Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b2 | Chueotang Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b3 | Korean Street Food |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b4 | Gukbap Restaurant |
| 50000 | Food and Drink | 52000 | Korean Cuisine | 05b7b5 | Korean Barbecue Restaurant |
| 50000 | Food and Drink | 52100 | Mexican Cuisine | 05a3b1 | Mexican Restaurant |
| 50000 | Food and Drink | 52100 | Mexican Cuisine | 05b7b6 | Taco Restaurant |
| 50000 | Food and Drink | 52100 | Mexican Cuisine | 05b7b7 | Tamale Shop |
| 50000 | Food and Drink | 52100 | Mexican Cuisine | 05b7b8 | Pozole Restaurant |
| 50000 | Food and Drink | 52100 | Mexican Cuisine | 05b7b9 | Barbacoa Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a3a0 | Brazilian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a0 | Taiwanese Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a3b0 | Malaysian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a3b2 | Russian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a3a2 | Cuban Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a1 | African Cuisine |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a2 | Puerto Rican Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a3 | Sri Lankan Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a4 | Mediterranean Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a5 | Lebanese Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a6 | Colombian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a7 | Filipino Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a8 | Middle Eastern Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b8a9 | Pakistani Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05b9a0 | Hawaiian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a0 | Peruvian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a1 | Caribbean Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a2 | Jamaican Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a3 | Portuguese Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a4 | Arabic Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a5 | Nepalese Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a6 | Egyptian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a7 | Moroccan Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a8 | Cajun Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c0a9 | Persian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c1a0 | Venezuelan Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c1a1 | Singaporean Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05c1a2 | Asian Restaurant |
| 50000 | Food and Drink | 52200 | Other Cuisine | 05a3b5 | Turkish Restaurant |
| 50000 | Food and Drink | 52300 | Seafood Restaurant | 05a2b3 | Seafood Restaurant |
| 50000 | Food and Drink | 52300 | Seafood Restaurant | 05c2a0 | Oyster Bar |
| 50000 | Food and Drink | 52300 | Seafood Restaurant | 05c2a1 | Crab Restaurant |
| 50000 | Food and Drink | 52300 | Seafood Restaurant | 05c2a2 | Eel Restaurant |
| 50000 | Food and Drink | 52400 | Fast Food | 05a2a8 | Fast Food Store |
| 50000 | Food and Drink | 52400 | Fast Food | 05c2a3 | Hamburger Fast Food |
| 50000 | Food and Drink | 52400 | Fast Food | 05c2a4 | Kebab Store |
| 50000 | Food and Drink | 52400 | Fast Food | 05c2a5 | Pizza Fast Food |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d0 | Food And Beverage Retail |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d1 | Beer/Wine Sale Store |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d2 | Beverage Sale Store |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d3 | Dairy Sale Store |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d4 | Fresh Sale Store |
| 50000 | Food and Drink | 52500 | Food and Beverage Retail | 05d0d5 | Snack Sale Store |

## Accommodation

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a0 | Experiential Stay |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a1 | Houseboat |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a2 | Farm Stay |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a3 | Camping |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a4 | Holiday Park |
| 100000 | Accommodation | 100100 | Experiential stay | 10a0a5 | Ski Resort Accommodation |
| 100000 | Accommodation | 100200 | Entire House | 10a1a0 | Homestay |
| 100000 | Accommodation | 100200 | Entire House | 10a1a1 | Entire House |
| 100000 | Accommodation | 100200 | Entire House | 10a1a2 | Villa |
| 100000 | Accommodation | 100300 | Country house | 10a6a0 | Country House |
| 100000 | Accommodation | 100300 | Country house | 10a6a1 | Lodging |
| 100000 | Accommodation | 100400 | Service Apartment | 10a7a0 | Service Apartment |
| 100000 | Accommodation | 100500 | Apartment | 10a8a0 | Apartment |
| 100000 | Accommodation | 100600 | Hostel | 10a2a0 | Hostel |
| 100000 | Accommodation | 100600 | Hostel | 10a2a1 | Capsule Hotel |
| 100000 | Accommodation | 100700 | Hotel | 10a3a0 | Hotel |
| 100000 | Accommodation | 100700 | Hotel | 10a3a1 | Ryokan |
| 100000 | Accommodation | 100700 | Hotel | 10a3a2 | Resort |
| 100000 | Accommodation | 100700 | Hotel | 10a3a3 | Inn |
| 100000 | Accommodation | 100700 | Hotel | 10a3a4 | Motel |
| 100000 | Accommodation | 100700 | Hotel | 10a3a5 | Love Hotel |

## Outdoors and attractions

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b6 | Landmarks |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a0 | Bridge |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a1 | Castle |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a2 | Dam |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a3 | Fountain |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a5 | Lighthouse |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a9 | Palace |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b0 | Plaza |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b1 | Statue |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b2 | Tower |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b4 | Tunnel |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b5 | Windmill |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a6 | Memorial Site |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0a7 | Notable Street |
| 80000 | Outdoors and attractions | 80100 | Landmarks | 08a0b3 | Town Square |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c8 | Natural Landmarks |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a0 | Beach |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a1 | Cave |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a2 | Cliff |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a3 | Desert |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b4 | Mountain |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a4 | Forest |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c6 | Volcano |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c7 | Waterfall |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c1 | Protected Area |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a5 | Geyser |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a6 | Glacier |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a7 | Gorge |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a8 | Grassland |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1a9 | Gully |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b0 | Island |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b1 | Lagoon |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b2 | Lake |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b3 | Marsh |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b5 | Oasis |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b6 | Panhandle |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b7 | Peninsula |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b8 | Pond |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1b9 | Promontory |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c0 | Reef |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c2 | River |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c3 | Spring |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c4 | Strait |
| 80000 | Outdoors and attractions | 80200 | Natural landmarks | 08a1c5 | Valley |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a5a4 | Nature-based attraction |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a5a0 | Aquarium |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a5a1 | Botanical Garden |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a0a4 | Garden |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a5a2 | Zoo |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a0 | Memorial Park |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a1 | Nature Park |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a2 | Rv Park |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a3 | National Park |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a5 | Parks |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a2a6 | Bike Park |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a4a2 | Hot Spring |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a4a3 | Scenic Lookout |
| 80000 | Outdoors and attractions | 80300 | Nature-based attraction | 08a4a5 | Farms |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a6 | Religious Destinations |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a0 | Church |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a1 | Monastery |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a2 | Mosque |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a3 | Religious Institution |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a4 | Synagogue |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a5 | Temple |
| 80000 | Outdoors and attractions | 80400 | Religious destinations | 08a3a7 | Shinto Shrine |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a4a4 | Attractions |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a0a8 | City Sightseeing |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a0 | Winery |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a1 | Distillery |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a2 | Brewery |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a3 | Observation Deck |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a4 | Yakatabune |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a5 | Historical Sites |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a6 | Ticketing Booth |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a7 | Theme Parks |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a8 | Amusement Parks |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a7a9 | Planetarium |
| 80000 | Outdoors and attractions | 80500 | Attractions | 08a8a0 | Ferris Wheel |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a1 | Water Adventure Destinations |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a2a4 | Water Park |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a2 | Scuba Diving Spot |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a3 | Surfing Spot |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a4 | Snorkeling Spots |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a5 | Rafting Spots |
| 80000 | Outdoors and attractions | 80600 | Water Adventure Destinations | 08a8a6 | Kayaking Spots |
| 80000 | Outdoors and attractions | 80700 | Extreme sports attractions | 08a8a7 | Atv Facility |
| 80000 | Outdoors and attractions | 80700 | Extreme sports attractions | 08a8a8 | Skydiving Center |
| 80000 | Outdoors and attractions | 80700 | Extreme sports attractions | 08a8a9 | Bungee Jump Center |
| 80000 | Outdoors and attractions | 80700 | Extreme sports attractions | 08a9a0 | Ski Slope |
| 80000 | Outdoors and attractions | 80700 | Extreme sports attractions | 08a9a1 | Extreme Sports Facility |
| 80000 | Outdoors and attractions | 80800 | Arts and Cultural attractions | 08a9a2 | Arts And Cultural Attractions |
| 80000 | Outdoors and attractions | 80800 | Arts and Cultural attractions | 08a9a3 | Art Gallery |
| 80000 | Outdoors and attractions | 80800 | Arts and Cultural attractions | 08a9a4 | Museum |
| 80000 | Outdoors and attractions | 80800 | Arts and Cultural attractions | 08a9a5 | Gallery And Exhibitions |
| 80000 | Outdoors and attractions | 80900 | Tourist Information and Service | 08a9a6 | Tourist Information And Service |
| 80000 | Outdoors and attractions | 81000 | Outdoor and attractions destination | 08a9a7 | Outdoor And Attractions Destination |

## Leisure

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 210000 | Leisure | 210100 | Entertainment | 21a0a4 | Children's Amusement Center |
| 210000 | Leisure | 210100 | Entertainment | 21a0a3 | Casino |
| 210000 | Leisure | 210100 | Entertainment | 21a0a5 | Cinema |
| 210000 | Leisure | 210100 | Entertainment | 21b0b5 | Bars And Clubs |
| 210000 | Leisure | 210100 | Entertainment | 21a0a7 | Do It Yourself |
| 210000 | Leisure | 210100 | Entertainment | 21a0a8 | Escape Room |
| 210000 | Leisure | 210100 | Entertainment | 21a0b0 | Gaming Cafe |
| 210000 | Leisure | 210100 | Entertainment | 21a0b1 | Haunted House |
| 210000 | Leisure | 210100 | Entertainment | 21a0b2 | Internet Cafe |
| 210000 | Leisure | 210100 | Entertainment | 21a0b3 | Karaoke Bar |
| 210000 | Leisure | 210100 | Entertainment | 21a0b4 | Laser Tag Center |
| 210000 | Leisure | 210100 | Entertainment | 21b0b0 | Board Games Cafe |
| 210000 | Leisure | 210100 | Entertainment | 21b0b1 | Photo Booth |
| 210000 | Leisure | 210100 | Entertainment | 21b0b2 | Arcade |
| 210000 | Leisure | 210100 | Entertainment | 21b0b3 | Pool And Beach Clubs |
| 210000 | Leisure | 210100 | Entertainment | 21b0b4 | Entertainment venues |
| 210000 | Leisure | 210100 | Entertainment | 21a3b6 | Pool Hall |
| 210000 | Leisure | 210100 | Entertainment | 21a3a6 | Bowling Alley |
| 210000 | Leisure | 210200 | Leisure facilities | 21a4a0 | Leisure Facilities |
| 210000 | Leisure | 210200 | Leisure facilities | 14a1a2 | Library |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a7 | Performing Arts Centre |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a0 | Concert Hall |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a1 | Circus |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a2 | Magic Show |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a3 | Theater |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a4 | Comedy Club |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a5 | Dance Club |
| 210000 | Leisure | 210300 | Performing Arts | 21a2a6 | Musical Club |
| 210000 | Leisure | 210300 | Performing Arts | 21a3a2 | Ballroom |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c7 | Sports Facilities |
| 210000 | Leisure | 210400 | Sports Facilities | 21a4a2 | Sports And Entertainment Venues |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b9 | Skating Rink |
| 210000 | Leisure | 210400 | Sport facilities | 21a4a1 | Rock Climbing And Bouldering Facilities |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a8 | Disc Golf Course |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a9 | Equestrian |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b3 | Gun Range |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a7 | Cricket Field |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b1 | Football Field |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b5 | Hockey Field |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b7 | Rugby Field |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c4 | Table Tennis Court |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c6 | Volleyball Court |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a1 | Badminton Court |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a3 | Baseball Field |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3a4 | Basketball Court |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c5 | Tennis Court |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c1 | Sport Studio |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b2 | Golf Course |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3b4 | Gym |
| 210000 | Leisure | 210400 | Sports Facilities | 21a3c3 | Swimming Complex |
| 210000 | Leisure | 210400 | Sports Facilities | 21a0a1 | Aquatic Center |
| 210000 | Leisure | 210500 | Health and Beauty Facilities | 21a5a0 | Spa |
| 210000 | Leisure | 210500 | Health and Beauty Facilities | 21a5a1 | Bath House |
| 210000 | Leisure | 210500 | Health and Beauty Facilities | 21a5a2 | Massage |
| 210000 | Leisure | 210500 | Health and Beauty Facilities | 21a5a3 | Sauna |
| 210000 | Leisure | 210600 | Recreational clubs | 21a0a6 | Recreational Clubs |

## Transport Hub

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a0 | Transport Hub |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a1 | Airport |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a2 | Harbor |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a3 | Railway Station |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a4 | Cable Car Station |
| 220000 | Transport Hub | 220100 | Transport Hub | 22a0a5 | Rest Area |
| 220000 | Transport Hub | 220200 | Public Transit Stops | 22a0a6 | Bus Stop |
| 220000 | Transport Hub | 220200 | Public Transit Stops | 22a0a7 | Subway Station |
| 220000 | Transport Hub | 220200 | Public Transit Stops | 22a0a8 | Taxi Stand |

## Beauty

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a1 | Barbershop |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a2 | Beauty Salon |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a3 | Body Piercing Shop |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a4 | Hair Removal Service |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a5 | Hair Salon |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a6 | Makeup |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a7 | Nail Salon |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a8 | Tanning Salon |
| 250000 | Beauty | 250100 | Health and Beauty Service | 25a0a0 | Beauty Services Store |

## Public Facilities

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 230000 | Public facilities | 230100 | Shared facilities | 23a0a3 | Gas Station |
| 230000 | Public facilities | 230100 | Shared facilities | 23a0a0 | Ev Charging Station |
| 230000 | Public facilities | 230100 | Shared facilities | 23a0a1 | Atm |
| 230000 | Public facilities | 230100 | Shared facilities | 23a0a2 | Playground |

## Lifestyle services

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 70000 | Lifestyle services | 70100 | Services | 07c1a0 | Services |
| 70000 | Lifestyle services | 70200 | Automotive Service | 07a1a0 | Automotive Rental |
| 70000 | Lifestyle services | 70200 | Automotive Service | 07a1a1 | Automotive Repair |
| 70000 | Lifestyle services | 70200 | Automotive Service | 07a1a2 | Car Wash And Detail |
| 70000 | Lifestyle services | 70200 | Automotive Service | 07a1a4 | Other Automotive Service |
| 70000 | Lifestyle services | 70300 | Funeral | 07a3a0 | Funeral |
| 70000 | Lifestyle services | 70400 | Home Improvement Service | 07a5a0 | Home Improvement Service |
| 70000 | Lifestyle services | 70500 | Laundry Service | 07a7a0 | Laundry Service |
| 70000 | Lifestyle services | 70600 | Logistic Service | 07a9a1 | Post Office |
| 70000 | Lifestyle services | 70600 | Logistic Service | 07a9a2 | Other Logistic Service |
| 70000 | Lifestyle services | 70600 | Logistic Service | 07a9a0 | Courier Service |
| 70000 | Lifestyle services | 70700 | Business POI | 07b0a0 | Business Poi |
| 70000 | Lifestyle services | 70800 | Pet Service | 07b1a0 | Pet Grooming Service |
| 70000 | Lifestyle services | 70800 | Pet Service | 07b1a1 | Pet Sitting And Boarding Service |
| 70000 | Lifestyle services | 70800 | Pet Service | 07b1a2 | Pet Service |
| 70000 | Lifestyle services | 70800 | Pet Service | 09a4a0 | Veterinary Services |
| 70000 | Lifestyle services | 70900 | Photography Service | 07b2a0 | Photography Service |
| 70000 | Lifestyle services | 71000 | Wedding Service | 07c0a0 | Wedding Service |
| 70000 | Lifestyle services | 71100 | Repair Service | 07b6a0 | Repair Service |
| 70000 | Lifestyle services | 71200 | Print/copy Store | 07b3a0 | Print/Copy Store |

## Professional services

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 240000 | Professional services | 240100 | Financial Service | 24a0a0 | Bank |
| 240000 | Professional services | 240100 | Financial Service | 24a0a1 | Money Exchange |
| 240000 | Professional services | 240100 | Financial Service | 24a0a2 | Loans Agency |
| 240000 | Professional services | 240100 | Financial Service | 24a0a3 | Stock Broker |
| 240000 | Professional services | 240100 | Financial Service | 24a0a4 | Financial Services |
| 240000 | Professional services | 240200 | Insurance Service | 24a0a5 | Insurance Service |
| 240000 | Professional services | 240300 | Legal Service | 24a0a6 | Legal Service |
| 240000 | Professional services | 240400 | Publisher | 24a0a7 | Publisher |
| 240000 | Professional services | 240500 | Real Estate Service | 24a0a8 | Real Estate Service |
| 240000 | Professional services | 240600 | Security Service | 24a0a9 | Security Service |

## Shopping

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 60000 | Shopping | 60100 | Food and Beverage Retail | 06c9a1 | Supermarket |
| 60000 | Shopping | 60100 | Food and Beverage Retail | 06a7a0 | Baking Supply Store |
| 60000 | Shopping | 60100 | Food and Beverage Retail | 06c0a0 | Market |
| 60000 | Shopping | 60100 | Food and Beverage Retail | 06b4a0 | Convenience Store |
| 60000 | Shopping | 60200 | Automotive Retail | 06a5a0 | Car Dealership |
| 60000 | Shopping | 60200 | Automotive Retail | 06a5a1 | Car Parts And Accessories |
| 60000 | Shopping | 60200 | Automotive Retail | 06a5a2 | Motorcycle Dealership |
| 60000 | Shopping | 60200 | Automotive Retail | 06a5a3 | Automotive Retail |
| 60000 | Shopping | 60300 | Baby and Children’s Supplies | 06a6a0 | Baby Supplies Store |
| 60000 | Shopping | 60300 | Baby and Children’s Supplies | 06b0a0 | Childrens Supplies Store |
| 60000 | Shopping | 60300 | Baby and Children’s Supplies | 06d3a0 | Toy Store |
| 60000 | Shopping | 60400 | Bridal Store | 06a9a0 | Bridal Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06b1a0 | Children'S Clothing Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06b1a1 | Men'S Clothing Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06b1a2 | Women'S Clothing Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06b1a3 | Clothing Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06b9a0 | Jewelry Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06c8a0 | Shoe Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06d0a0 | Sporting Goods Store |
| 60000 | Shopping | 60500 | Apparel and Accessories | 06d4a0 | Watch Store |
| 60000 | Shopping | 60600 | Home and Living | 06b2a0 | Computers And Electronics Retail |
| 60000 | Shopping | 60600 | Home and Living | 06b7a0 | Furniture And Home Store |
| 60000 | Shopping | 60600 | Home and Living | 06d2a0 | Tool Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06a3a0 | Arts And Crafts Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06a1a0 | Antique Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06a2a0 | Aquarium Shop |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06a4a0 | Audio And Video Shop |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06a8a0 | Bookstore |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06b8a0 | Gift Shop |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06b5a0 | Flower Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c1a0 | Musical Instrument Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c2a0 | Newsagent |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c3a0 | Office Supply Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c4a0 | Optician |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c5a0 | Perfume Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06c7a0 | Record Store |
| 60000 | Shopping | 60700 | Retail and Lifestyle Stores | 06d1a0 | Tobacco Store |
| 60000 | Shopping | 60800 | Pet Store | 06c6a0 | Pet Store |
| 60000 | Shopping | 60800 | Pet Store | 06c6a1 | Pet Supplies Store |
| 60000 | Shopping | 60800 | Pet Store | 06c6a2 | Other Pet Store |
| 60000 | Shopping | 60900 | Shopping Area | 06d6a0 | Shopping Stores |
| 60000 | Shopping | 60900 | Shopping Area | 06c9a0 | Outlet |
| 60000 | Shopping | 60900 | Shopping Area | 06c9a2 | Shopping Mall |
| 60000 | Shopping | 60900 | Shopping Area | 06c9a3 | Shopping District |
| 60000 | Shopping | 61000 | Business-related Retail | 06b3a0 | Construction Supplies Store |
| 60000 | Shopping | 61000 | Business-related Retail | 06a0a0 | Agricultural Supplies Store |
| 60000 | Shopping | 61000 | Business-related Retail | 06d5a0 | Wholesale |

## Office and Industrial

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 130000 | Office and Industrial | 130100 | Business Facility | 13a0a2 | Company |
| 130000 | Office and Industrial | 130100 | Business Facility | 13a0a3 | Conference Center |
| 130000 | Office and Industrial | 130100 | Business Facility | 13a0a4 | Business Facilities |
| 130000 | Office and Industrial | 130100 | Business Facility | 13a0a0 | Business Exhibition |
| 130000 | Office and Industrial | 130200 | Government | 13a1a0 | City Hall |
| 130000 | Office and Industrial | 130200 | Government | 13a1a1 | Courthouse |
| 130000 | Office and Industrial | 130200 | Government | 13a1a3 | Drivers License Office |
| 130000 | Office and Industrial | 130200 | Government | 13a1a4 | Embassy |
| 130000 | Office and Industrial | 130200 | Government | 13a1a5 | Fire Station |
| 130000 | Office and Industrial | 130200 | Government | 13a1a6 | Police Station |
| 130000 | Office and Industrial | 130200 | Government | 13a1a7 | Social Security Office |
| 130000 | Office and Industrial | 130200 | Government | 13a1a8 | Tax Department |
| 130000 | Office and Industrial | 130200 | Government | 13a1a9 | Visa And Passport Office |
| 130000 | Office and Industrial | 130200 | Government | 13a1b0 | Government Offices |
| 130000 | Office and Industrial | 130200 | Government | 13a1a2 | Department Of Motor Vehicles |
| 130000 | Office and Industrial | 130300 | Industrial Facilities | 13a2a0 | Factory |
| 130000 | Office and Industrial | 130300 | Industrial Facilities | 13a2a1 | Industrial Estate |
| 130000 | Office and Industrial | 130300 | Industrial Facilities | 13a2a2 | Manufacturer |
| 130000 | Office and Industrial | 130300 | Industrial Facilities | 13a2a3 | Warehouse |
| 130000 | Office and Industrial | 130300 | Industrial Facilities | 13a2a4 | Industrial Facilities |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a0 | Community Office |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a3 | Radio Broadcaster |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a4 | Shelter |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a5 | Tv Station |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a6 | Other Organization |
| 130000 | Office and Industrial | 130400 | Organization | 13a3a2 | Orphanage |
| 130000 | Office and Industrial | 130500 | Other Office and Industrial | 13a4a0 | Office And Industrial |

## Education

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 140000 | Education | 140100 | College and University | 14a0a0 | Business School |
| 140000 | Education | 140100 | College and University | 14a0a1 | Engineering School |
| 140000 | Education | 140100 | College and University | 14a0a2 | School Of Humanities |
| 140000 | Education | 140100 | College and University | 14a0a3 | Law School |
| 140000 | Education | 140100 | College and University | 14a0a4 | Medical School |
| 140000 | Education | 140100 | College and University | 14a0a5 | Science School |
| 140000 | Education | 140100 | College and University | 14a0a6 | College And University |
| 140000 | Education | 140200 | Education Facility | 14a1a5 | Education Facility |
| 140000 | Education | 140200 | Education Facility | 14a1a0 | Dormitory |
| 140000 | Education | 140200 | Education Facility | 14a1a1 | Lab |
| 140000 | Education | 140200 | Education Facility | 14a1a4 | Research Institute |
| 140000 | Education | 140200 | Education Facility | 14a1a3 | Observatory |
| 140000 | Education | 140300 | Educational insitutions | 14a5a0 | Educational Insitutions |
| 140000 | Education | 140300 | Educational insitutions | 14a2a0 | Kindergarten |
| 140000 | Education | 140300 | Educational insitutions | 14a2a1 | Other Preschool |
| 140000 | Education | 140300 | Educational insitutions | 14a3a0 | Elementary School |
| 140000 | Education | 140300 | Educational insitutions | 14a3a1 | High School |
| 140000 | Education | 140300 | Educational insitutions | 14a3a2 | Middle School |
| 140000 | Education | 140300 | Educational insitutions | 14a3a3 | Other Primary And Secondary School |
| 140000 | Education | 140400 | Training School | 14a4a0 | Art School |
| 140000 | Education | 140400 | Training School | 14a4a1 | Driving School |
| 140000 | Education | 140400 | Training School | 14a4a2 | Language School |
| 140000 | Education | 140400 | Training School | 14a4a3 | Music School |
| 140000 | Education | 140400 | Training School | 14a4a4 | Nursing School |
| 140000 | Education | 140400 | Training School | 14a4a6 | Sport School |
| 140000 | Education | 140400 | Training School | 14a4a7 | Trade School |
| 140000 | Education | 140400 | Training School | 14a4a8 | Other Training School |
| 140000 | Education | 140400 | Training School | 14a4a5 | Special Needs School |
| 140000 | Education | 140400 | Training School | 07b9a0 | Other Tutoring Service |

## Healthcare

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 90000 | Healthcare | 90100 | Clinic | 09a0a4 | Clinic |
| 90000 | Healthcare | 90100 | Clinic | 09a0a0 | Dentist Clinic |
| 90000 | Healthcare | 90100 | Clinic | 09a0a1 | Family Doctor Clinic |
| 90000 | Healthcare | 90100 | Clinic | 09a0a2 | Nutritionist Clinic |
| 90000 | Healthcare | 90100 | Clinic | 09a0a3 | Ophthalmologist Clinic |
| 90000 | Healthcare | 90200 | Health supplments and Medicine Store | 09a1a3 | Health And Medicine Store |
| 90000 | Healthcare | 90200 | Health supplments and Medicine Store | 09a1a0 | Medical Supply Store |
| 90000 | Healthcare | 90200 | Health supplments and Medicine Store | 09a1a1 | Pharmacy |
| 90000 | Healthcare | 90200 | Health supplments and Medicine Store | 09a1a2 | Vitamin And Supplements Store |
| 90000 | Healthcare | 90300 | Healthcare services | 09a5a0 | Healthcare Services |
| 90000 | Healthcare | 90300 | Healthcare services | 09a2a0 | Differently Abled Persons Service |
| 90000 | Healthcare | 90300 | Healthcare services | 09a2a3 | Nursing Home |
| 90000 | Healthcare | 90300 | Healthcare services | 09a2a4 | Rehabilitation Center |
| 90000 | Healthcare | 90300 | Healthcare services | 09a2a1 | Emergency Service |
| 90000 | Healthcare | 90300 | Healthcare services | 09a2a2 | Mental Health Service |
| 90000 | Healthcare | 90300 | Healthcare services | 09a3a0 | Hospital |

## Place and Address

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 190000 | Place and Address | 190100 | Places | 19a3a6 | Other Places |
| 190000 | Place and Address | 190100 | Places | 19a3a0 | City |
| 190000 | Place and Address | 190100 | Places | 19a3a1 | Country |
| 190000 | Place and Address | 190100 | Places | 19a3a2 | District |
| 190000 | Place and Address | 190100 | Places | 19a3a3 | Province |
| 190000 | Place and Address | 190100 | Places | 19a3a4 | Town |
| 190000 | Place and Address | 190100 | Places | 19a3a5 | Village |
| 190000 | Place and Address | 190100 | Places | 19a3b0 | Prefecture |
| 190000 | Place and Address | 190100 | Places | 19a3b1 | State |
| 190000 | Place and Address | 190100 | Places | 19a3b2 | Federal District |
| 190000 | Place and Address | 190100 | Places | 19a3b3 | County |
| 190000 | Place and Address | 190100 | Places | 19a3b4 | Department |
| 190000 | Place and Address | 190100 | Places | 19a3b5 | Region |
| 190000 | Place and Address | 190100 | Places | 19a3b6 | Tambon |
| 190000 | Place and Address | 190100 | Places | 19a3b7 | Municipality |
| 190000 | Place and Address | 190200 | Roads | 19a4a0 | Road Intersection |
| 190000 | Place and Address | 190200 | Roads | 19a5a0 | Road Name |
| 190000 | Place and Address | 190300 | Other Place and Address | 19a8a0 | Places And Address |
| 190000 | Place and Address | 190300 | Other Place and Address | 19a0a0 | Other Places |
| 190000 | Place and Address | 190300 | Other Place and Address | 19a1a0 | Other Construction |
| 190000 | Place and Address | 190400 | Parking | 19a2a0 | Other Parking |
| 190000 | Place and Address | 190500 | Non-administrative area | 19a3b8 | Non-administrative area |

## Residential

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 120000 | Residential | 120100 | Residential | 12a0a0 | Residential |

## Other

| **TT Code L1** | **Level 1 Category** | **TT Code L2** | **Level 2 Category** | **TT Code L3** | **Level 3 Category** |
| --- | --- | --- | --- | --- | --- |
| 990000 | Other | 990100 | Other | 99a0a0 | Other |

Was this document helpful?


---
## SOURCE: TikTok GO/API Reference/Dining SaaS Sample Code.md

Docs
# Dining SaaS Sample Code
This document provides a comprehensive sample code demo of each API module for external developers onboarding with TikTok Go Dining SaaS. You can refer to these examples when developing and testing your API integrations.
The sample code is demonstrated in **Java** and **GoLang **respectively.
## Authentication
Authentication is the first step to interacting with TikTok Local Services (TTLS) APIs. It involves obtaining an access token that must be included in the header of subsequent API calls.
### Get New Token
**Purpose:** To obtain a new access token for the first time.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.stream.Collectors;

public class GetAccessToken {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        Map<Object, Object> data = Map.of(
                "client_key", "{CLIENT_KEY}",
                "client_secret", "{CLIENT_SECRET}",
                "merchant_id", "{MERCHANT_ID}",
                "grant_type", "access_token"
        );

        String form = data.entrySet()
                .stream()
                .map(e -> e.getKey() + "=" + URLEncoder.encode(e.getValue().toString(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/merchant/oauth/token/"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .header("x-tt-target-idc", "alisg")
                .POST(HttpRequest.BodyPublishers.ofString(form))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
    "strings"
)

func main() {
    apiURL := "https://open.tiktokapis.com/merchant/oauth/token/"

    data := url.Values{}
    data.Set("client_key", "{CLIENT_KEY}")
    data.Set("client_secret", "{CLIENT_SECRET}")
    data.Set("merchant_id", "{MERCHANT_ID}")
    data.Set("grant_type", "access_token")

    req, err := http.NewRequest("POST", apiURL, strings.NewReader(data.Encode()))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
    req.Header.Set("x-tt-target-idc", "alisg")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Refresh Access Token
**Purpose:** To obtain a new access token using a refresh token when the current access token expires.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.stream.Collectors;

public class RefreshAccessToken {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        Map<Object, Object> data = Map.of(
                "client_key", "{CLIENT_KEY}",
                "client_secret", "{CLIENT_SECRET}",
                "merchant_id", "{MERCHANT_ID}",
                "grant_type", "refresh_token",
                "refresh_token", "{REFRESH_TOKEN}"
        );

        String form = data.entrySet()
                .stream()
                .map(e -> e.getKey() + "=" + URLEncoder.encode(e.getValue().toString(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/merchant/oauth/token/"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .header("x-tt-target-idc", "alisg")
                .POST(HttpRequest.BodyPublishers.ofString(form))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.outprintln("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
    "strings"
)

func main() {
    apiURL := "https://open.tiktokapis.com/merchant/oauth/token/"

    data := url.Values{}
    data.Set("client_key", "{CLIENT_KEY}")
    data.Set("client_secret", "{CLIENT_SECRET}")
    data.Set("merchant_id", "{MERCHANT_ID}")
    data.Set("grant_type", "refresh_token")
    data.Set("refresh_token", "{REFRESH_TOKEN}")

    req, err := http.NewRequest("POST", apiURL, strings.NewReader(data.Encode()))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
    req.Header.Set("x-tt-target-idc", "alisg")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
## Shop Management
This section covers APIs for managing shops, including claiming, certification, decoration, and querying shop information.
### POI Claiming
**Purpose:** To claim a Point of Interest (POI) on TikTok and link it to a merchant's shop.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PoiClaiming {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "shop_name_local": "Toko Kue Enak",
                    "shop_name_en": "Delicious Cake Shop",
                    "shop_address_local": "Jl. Merdeka No. 1, Jakarta",
                    "shop_address_en": "1 Merdeka Street, Jakarta",
                    "business_status": 1,
                    "type_code": "722511",
                    "latitude": "-6.2088",
                    "longitude": "106.8456"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/poi/batch_claim/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/poi/batch_claim/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "shop_name_local": "Toko Kue Enak",
                "shop_name_en": "Delicious Cake Shop",
                "shop_address_local": "Jl. Merdeka No. 1, Jakarta",
                "shop_address_en": "1 Merdeka Street, Jakarta",
                "business_status": 1,
                "type_code": "722511",
                "latitude": "-6.2088",
                "longitude": "106.8456"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Upload Shop Certifications
**Purpose:** To submit certification documents for a shop, such as business licenses or other required legal documents.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UploadShopCertifications {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "industry_license_url": "https://example.com/license.pdf"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_submit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_submit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "industry_license_url": "https://example.com/license.pdf"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Shop Decoration
**Purpose:** To update a shop's decorative information, such as photos, opening hours, and average price.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ShopDecoration {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "phone": "+621234567890",
                    "average_price": {
                        "amount": "100000",
                        "currency": "Rp"
                    },
                    "opening_time": [
                        {
                            "day": 1,
                            "time_periods": [
                                {
                                    "start_time": "09:00",
                                    "end_time": "22:00"
                                }
                            ]
                        }
                    ],
                    "images": [
                        {
                           "is_main": true,
                           "index": 1,
                           "origin_url": "https://example.com/shop_image.jpg"
                        }
                    ]
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_decoration/batch_submit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_decoration/batch_submit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "phone": "+621234567890",
                "average_price": {
                    "amount": "100000",
                    "currency": "Rp"
                },
                "opening_time": [
                    {
                        "day": 1,
                        "time_periods": [
                            {
                                "start_time": "09:00",
                                "end_time": "22:00"
                            }
                        ]
                    }
                ],
                "images": [
                    {
                       "is_main": true,
                       "index": 1,
                       "origin_url": "https://example.com/shop_image.jpg"
                    }
                ]
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Update Shop's Basic Info
**Purpose:** To update a shop's basic information, such as name, address, and business category.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UpdateShopBaseInfo {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "shop_name_local": "Toko Roti Baru",
                    "shop_name_en": "New Bakery Shop"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_base_info/batch_update/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_base_info/batch_update/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "shop_name_local": "Toko Roti Baru",
                "shop_name_en": "New Bakery Shop"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Task Query for Shop Operations
**Purpose:** To query the status of asynchronous tasks submitted for POI claiming, shop certification, shop decoration, and shop basic info updates.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class QueryShopTasks {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "task_id_list": [12345, 67890]
        }
        ''';

        // Example for POI task query
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/poi_task/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    // Example for POI task query
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/poi_task/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "task_id_list": [12345, 67890]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Batch Query Shop Information
**Purpose:** To retrieve detailed information for multiple shops in a single request.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class BatchQueryShopInfo {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_shop_ids": ["{THIRD_SHOP_ID_1}", "{THIRD_SHOP_ID_2}"]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_shop_ids": ["{THIRD_SHOP_ID_1}", "{THIRD_SHOP_ID_2}"]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Webhook Overview for Shop-Related Events
**Purpose:** To receive real-time notifications about the status of shop-related operations.
**Implementation Notes:**
- **Retry Logic:** Your webhook endpoint should be prepared to handle retries from TikTok's servers in case of network issues or non-2xx responses.
- **Idempotency:** Implement idempotency checks on your end to prevent duplicate processing of the same event. The `create_time` field can be used for this purpose.
**Event Names:**
- `ttls.merchant.poi_claiming_task.result`: For POI claiming tasks.
- `ttls.merchant.upload_shop_certifications_task.result`: For shop certification tasks.
- `ttls.merchant.shop_decoration_task.result`: For shop decoration tasks.
- `ttls.merchant.update_shop_base_info_task.result`: For shop basic info update tasks.
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the details of the task. The structure of this JSON will correspond to the task type (e.g., `PoiClaimTask`, `ShopCertificationTask`). Key fields to inspect are:
- `task_id`: The ID of the task.
- `task_status`: The status of the task (e.g., `2` for Success, `3` for Failed).
- `reject_reason`: If the task failed, this field will contain the reason for rejection.
## Product Management
This section details the APIs for managing products, including creating, updating, and querying product information.
### Save Product
**Purpose:** To create a new product or update an existing one. This is a comprehensive endpoint that requires all product attributes to be provided.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class SaveProduct {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "category_id": "722511",
            "product_type": 2,
            "attr_key_value_map": {
                "rec_person_num": "\"1\"",
                "shop_id": "[\"{SHOP_ID}\"]",
                "commodity_set": "2",
                "commodity": "[{\"i18n_group_mame\":{\"default_text\":\"Pizza Group\"},\"total_count\":1,\"option_count\":1,\"item_list\":[{\"i18n_name\":{\"default_text\":\"Large Pizza\"},\"price\":\"100000\",\"currency\":\"Rp\",\"count\":1}]}]",
                "product_name": "{\"default_text\":\"Pizza Voucher\"}",
                "image_list": "[{\"outer_url\":\"https://example.com/pizza.jpg\"}]",
                "origin_amount": "150000",
                "actual_amount": "100000",
                "local_currency": "Rp",
                "stock_info": "{\"stock_num\":100,\"stock_qty_limit_type\":1}",
                "sold_time_type": 2,
                "use_type": 1,
                "use_date": "{\"use_date_type\":2,\"day_duration\":30}",
                "use_time": "{\"use_time_type\":1}",
                "consumption_convention": "{\"consumption_method\":3}"
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/save/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/save/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "category_id": "722511",
        "product_type": 2,
        "attr_key_value_map": {
            "rec_person_num": "\"1\"",
            "shop_id": "[\"{SHOP_ID}\"]",
            "commodity_set": "2",
            "commodity": "[{\"i18n_group_mame\":{\"default_text\":\"Pizza Group\"},\"total_count\":1,\"option_count\":1,\"item_list\":[{\"i18n_name\":{\"default_text\":\"Large Pizza\"},\"price\":\"100000\",\"currency\":\"Rp\",\"count\":1}]}]",
            "product_name": "{\"default_text\":\"Pizza Voucher\"}",
            "image_list": "[{\"outer_url\":\"https://example.com/pizza.jpg\"}]",
            "origin_amount": "150000",
            "actual_amount": "100000",
            "local_currency": "Rp",
            "stock_info": "{\"stock_num\":100,\"stock_qty_limit_type\":1}",
            "sold_time_type": 2,
            "use_type": 1,
            "use_date": "{\"use_date_type\":2,\"day_duration\":30}",
            "use_time": "{\"use_time_type\":1}",
            "consumption_convention": "{\"consumption_method\":3}"
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Update (Free Audit)
**Purpose:** To update a product's stock and price information without requiring a review. This allows for real-time changes to inventory and pricing.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UpdateFreeAudit {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "product_free_audit": {
                "local_currency": "Rp",
                "actual_amount": "95000",
                "stock_qty_limit_type": 1,
                "stock_num": 50
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/update_free_audit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/update_free_audit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "product_free_audit": {
            "local_currency": "Rp",
            "actual_amount": "95000",
            "stock_qty_limit_type": 1,
            "stock_num": 50
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Delist Product
**Purpose:** To take a product offline, making it unavailable for purchase.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class DelistProduct {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/offline"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/offline"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Withdraw Product Audit
**Purpose:** To withdraw a product from the audit process before it is completed.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class WithdrawProductAudit {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/withdraw_audit"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/withdraw_audit"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Batch Query Products
**Purpose:** To retrieve a list of products based on various filter criteria.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class BatchQueryProducts {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "product_type_list": [2],
            "list_tab": 1,
            "pagination": {
                "page_size": 10,
                "page_no": 1
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "product_type_list": [2],
        "list_tab": 1,
        "pagination": {
            "page_size": 10,
            "page_no": 1
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Query Product Details
**Purpose:** To retrieve detailed information about a single product, including its online and under-review versions.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class QueryProductDetails {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "merchant_id": "{MERCHANT_ID}",
            "online": true
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/query/"

    jsonBody := []byte(`{
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "merchant_id": "{MERCHANT_ID}",
        "online": true
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product Category Query
**Purpose:** To retrieve the available product categories for a merchant.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ProductCategoryQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "language": "en"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product_opt_category/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product_opt_category/query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "language": "en"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product-Available Shops Query
**Purpose:** To retrieve a list of shops where a product can be made available.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ProductAvailableShopsQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "language": "en",
            "pagination": {
                "page_size": 10,
                "page_no": 1
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product_opt_shops/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product_opt_shops/query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "language": "en",
        "pagination": {
            "page_size": 10,
            "page_no": 1
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### National Holiday Query
**Purpose:** To retrieve a list of national holidays for specified countries.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class NationalHolidayQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "countries": ["ID"],
            "language": "en"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/holiday/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/holiday/batch_query/"

    jsonBody := []byte(`{
        "countries": ["ID"],
        "language": "en"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product Status Webhook Overview
**Purpose:** To receive real-time notifications about changes in product status.
**Event Name:**
- `ttls.product.status_update.result`
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the following key fields:
- `third_product_id`: The unique ID of the product in the third-party system.
- `product_id`: The TikTok product ID.
- `product_status`: The new status of the product (e.g., `1` for Listed, `3` for Rejected).
- `action_type`: The type of action that triggered the status change.
## Redeem Management
This section covers APIs for managing voucher redemption.
### Voucher Query
**Purpose:** To query the details of a voucher using its code or a QR code.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class VoucherQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_shop_id": "{THIRD_SHOP_ID}",
            "code_list": ["123456789012"]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/fulfill/get_code_item_list/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/fulfill/get_code_item_list/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_shop_id": "{THIRD_SHOP_ID}",
        "code_list": ["123456789012"]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Voucher Redeem
**Purpose:** To redeem a voucher, marking it as used.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class VoucherRedeem {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "third_shop_id": "{THIRD_SHOP_ID}",
            "code_list": ["123456789012"],
            "shop_order_id": "{SHOP_ORDER_ID}",
            "merchant_id": "{MERCHANT_ID}",
            "locale": "id-ID"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/fulfill/redeem_code/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/fulfill/redeem_code/"

    jsonBody := []byte(`{
        "third_shop_id": "{THIRD_SHOP_ID}",
        "code_list": ["123456789012"],
        "shop_order_id": "{SHOP_ORDER_ID}",
        "merchant_id": "{MERCHANT_ID}",
        "locale": "id-ID"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### After-sale Webhook Overview
**Purpose:** To receive real-time notifications about after-sale events, such as refunds.
**Event Name:**
- `ttls.fulfill.after_sale.result`
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the following key fields:
- `after_sale_event_type`: The type of after-sale event (e.g., `AFTER_SALE_SUCCESS`).
- `shop_order_id`: The ID of the order.
- `item_ids`: A list of item IDs that were refunded.
- `after_sale_order_id`: The ID of the after-sale order.
Was this document helpful?


---
## SOURCE: TikTok GO/API Reference/Error Codes.md

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


---
## SOURCE: TikTok GO/API Reference/Product Management.md

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


---
## SOURCE: TikTok GO/API Reference/Voucher Management.md

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
