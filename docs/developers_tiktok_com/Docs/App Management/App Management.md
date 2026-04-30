Docs
# Register Your App
To integrate with our products, you must connect your app to TikTok for Developers and submit your app registration for review. This guide demonstrates how to connect an app, configure app settings, and complete the submission process.
## Prerequisites
Before registering your app, do the following:
- [Create a TikTok developer account from our signup page](https://developers.tiktok.com/signup) using your email.
- [Create or join an organization](https://developers.tiktok.com/doc/working-with-organizations) representing the owning group of the app. This step is highly recommended but not required.
## Connect your app
Follow these steps to add your app to TikTok for Developers.
- [Log in](https://developers.tiktok.com/login/) using your TikTok developer account.
- [Click the profile icon in the main navigation bar, then click **Manage apps](https://developers.tiktok.com/apps)** to access a list of your apps.
Note: You won't have any apps if you just created a developer account.
- Click the **Connect an app** button to register your app.
- [When prompted to **Select the app owner**, choose one of your organizations and click **Confirm**. If you don't see any organizations](https://developers.tiktok.com/doc/working-with-organizations), consider creating one. You may also register the app directly under your individual developer account, but this is not recommended for real app integrations.
- [Fill in the information](#configure_settings_for_your_app) on the app page and add the desired products.
- [Once your app configuration is complete, submit your app for review](#submit_your_app_for_review).
[You can access this app page any time by going to the **Manage apps](https://developers.tiktok.com/apps/)** page and clicking on the app.
### App page navigation
The app page contains administrative controls and essential information about your app and product configuration.
At the top of the app page, you can perform the following operations:
- Click the info icon next to the app's name to display the **App ID** and **Ownership**.
- Toggle between **Production** mode and **Sandbox **mode:
- **Production** mode contains the version of the app that must be submitted for review to be released to the public. This guide covers the configuration and review process for **Production** mode.
- [**Sandbox** mode is a restricted environment that allows you to try out integrations without having to submit your app for review. Learn more about Sandbox mode](https://developers.tiktok.com/doc/add-a-sandbox).
- Click the **URL properties** button to verify URL properties for Content Posting API.
- Click the history icon button to access a **Changelog** and any **Review comments** if your app was not approved after submission.
- Click the **More Options** [**...**] button to transfer app ownership or delete the app.
Use the left navigation panel to view your app's review status, app details, and products.
- View your app's review status under **Production**. If you just created an app, it will be in **Draft** status.
- Click **App details**, **Products**, or **Scopes** to scroll the page to the corresponding section.
- [In the **Products** section, click the **Add products** button to choose from a list of integrations. Learn more about adding products](#products)**.**
- [In the **Scopes** section, you can add scopes to configure access to specific data or perform specific actions. Learn more about scopes](https://developers.tiktok.com/doc/).
## Configure settings for your app
Fill out the requested details and add your desired products to your app.
### App details
The **App details** section contains essential details about your app's credentials, display information, and intended platforms.
#### Credentials
The **Credentials** section contains **Client key** and **Client secret, **which are necessary for your application to invoke TikTok APIs.
#### Basic information
The** Basic information** section contains details that will be displayed to users and help us understand your app.
- **App icon **and **App name** are displayed whenever your app is present in the TikTok ecosystem. Your app icon must meet the following specifications:
- 1024 x 1024 px
- JPEG, JPG, or PNG
- Up to 5 MB
- **Category** helps us better understand your app.
- **Description** helps the user understand your app. TikTok displays the description when a user views the app authorization page.
#### Platforms
You can run your app on different platforms including Web, Android, iOS and Desktop. Select your intended platforms and then provide the requested details.
- **Web** and** Desktop** require the URL of your official website.
- **Android** requires your app's package name, Play Store URL, app signature, and signing certificate. These are used to verify your app's identity when you invoke TikTok APIs. Provide your Play Store URL to help us better understand your app.
- **iOS** requires the App Store URL and Bundle ID. These are used to verify your app's identity when you invoke TikTok APIs. Provide your App Store URL to help us better understand your app.
### Products
Click the **Add products** button in the **Products **section. Choose from a list of products to add to your app. Items appear under the **Products** section after you add them.
#### Login Kit settings example
[Each product has its own specific settings. For example, examine the product-specific settings for Login Kit](https://developers.tiktok.com/doc/login-kit-overview).
- Web, iOS, Android and Desktop require a **Redirect URI** to return an authorization code back to your app.
- [[Android's redirect URI must be an App Link](https://developer.android.com/training/app-links) or Deep Link](https://developer.android.com/training/app-links#deep-links).
- [[iOS's redirect URI must be a Universal Link](https://developer.apple.com/ios/universal-links/) and your app must have the Associated Domain](https://developer.apple.com/documentation/xcode/supporting-associated-domains?language=objc) capability.
## Verify URL ownership
Note: For Sandbox environments, URL verification is only required for Content Posting API.
Before submitting your app for review, you must verify URL properties for all URLs in your app configuration. Some features require URL verification before they can be used, like Link Sharing (beta). There are two cases for URL verification, depending on when the app was created.
- For apps created after September 9, 2024, the following URLs require verification:
- Terms of Service URL
- Privacy Policy URL
- Web or Desktop URL
- All apps that use the Content Posting API upload URL or the Link Sharing URL must verify these URLs, regardless of when the app was created.
To verify URL properties, complete the following steps:
- Click the **URL properties** button at the top of your app page.
- Ensure you are verifying properties for your app in **Production** mode, then click **Verify properties**.
- Choose whether to verify your URL by **Domain** or **URL prefix**:
- For verification by Domain, enter your domain and subdomain name, then click **Verify**.
- For verification by URL prefix, enter your complete URL, then click **Verify**. Download the provided signature file, then upload it to your URL.
## Submit your app for review
[[Before you integrate with our developer products, you must submit your app for review. Familiarize yourself with our developer guidelines](https://developers.tiktok.com/doc/our-guidelines-developer-guidelines) and app review guidelines](https://developers.tiktok.com/doc/app-review-guidelines) to understand our integration processes and requirements before submitting your changes for review.
Follow these steps to submit your app for review.
- Go to the **App review** section on your app page and complete the required information for app submission.
- In detail, explain how each product and scope works within your app or website. For revisions, you must explain changes regarding the new configuration in this section.
- Upload at least one demo video that shows the complete end-to-end flow of the integrations. You may upload a maximum of 5 videos, up to 50 MB each.
- Click the **Save **button to save your changes.
- Once you are satisfied with your app configuration, click the **Submit for review** button.
TikTok for Developers will start reviewing your app once it is submitted.
## App review status
The status of your app review is visible under **Production** in the left navigation panel.
- **Draft**: Your app has not been submitted for review yet.
- **In review:** Your app has been submitted for review and approval is pending. No further changes can be made at this stage.
- If you want to make changes, click the **Recall** button to withdraw the app from review and return it to draft status.
- **Live:** Your current revision of the app was approved and integrations are live.
- If you want to make changes, click the **Create revision** button to create a **Draft** cloned from the **Live** version. You may modify this draft version without compromising your live configuration.
- **Not approved:** After reviewing your app, we determined it did not meet our criteria. **Review comments** will be displayed on your app page and **History** with suggested actions. Complete the suggested actions and resubmit your app for review.
Once your app is approved and live, any subsequent changes must be submitted for review and approved to appear in the live release.
Was this document helpful?