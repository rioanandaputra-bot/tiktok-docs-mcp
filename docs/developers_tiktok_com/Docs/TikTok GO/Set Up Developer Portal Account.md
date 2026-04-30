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