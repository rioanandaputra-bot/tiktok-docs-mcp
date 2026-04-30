Docs
# App Review FAQ
The first step to obtain access to our developer tools is to submit an app for review with your TikTok for Developers account. Our team reviews all applications and will either approve them or provide feedback with suggested updates. Please note that you will not have access to the APIs until your application has been approved. This page covers some frequently asked questions about the app review process.
## Frequently asked questions about app review
### How long does the app review process take?
[App review may take several days to two weeks after submission. If your app is not approved, contact us through our Support page](https://developers.tiktok.com/support/) for further guidance.
### What are the minimum requirements for submitting my app for approval?
[All app review criteria are stated in the app review guidelines](https://developers.tiktok.com/doc/app-review-guidelines).
### Does my mobile app need to be live on an app store?
- If you have a mobile app, it must be available in the Apple and/or Google Play App Stores.
- If you have a web application and are applying for Login Kit access, you must provide a valid redirect URI.
### What are the scopes that I can apply for?
[Visit our scopes documentation](https://developers.tiktok.com/doc/scopes-overview) to learn more about available permissions.
### What should I put in the "Submit for review" text box?
Explain how your app utilizes the TikTok for Developers APIs, for example:
- "We would like to enable users to quickly and securely sign into our app with their TikTok account"
- "We would like to add a "Share to TikTok" button to our app so our users can share their videos to TikTok"
### How can I track the status of my application?
On the app page, you can view the status of your application under **Production** in the left navigation panel.
- **Draft**: Your app has not been submitted for review yet.
- **In review:** Your app has been submitted for review and approval is pending. No further changes can be made at this stage.
- **Live:** Your current revision of the app was approved and integrations are live.
- **Not approved:** After reviewing your app, we determined it did not meet our criteria. Click the history icon button at the top of the app page to access **Review comments**. Complete the suggested actions and resubmit your app for review.
Once your app is approved and live, any subsequent changes must be submitted for review and approved to appear in the live release.
### Why was my app not approved?
Apps are not approved for various reasons. Please review the application feedback in the **Review comments** available under your app's **History**. Once you have made edits to your application, be sure to resubmit your application.
[Contact us](https://developers.tiktok.com/support/) if you have questions relating to the feedback.
### Is TikTok for Developers compatible with apps built in React Native?
Yes. Login Kit will work with web and React Native builds for Android and iOS apps. The same applies to all of our developer tools.
### How can I get access to the APIs?
[For each app, a TikTok for Developer application must be submitted to request API access. Please review our application criteria](https://developers.tiktok.com/doc/app-review-guidelines) before applying. Once your application has been reviewed by our team and approved, your app status will show as Live and your app will have access to the products and scopes requested in the application.
### How can I test the APIs for my app that is still in development?
Beta or development versions, incomplete apps, and test versions are not encouraged and will not be approved for integration with TikTok in most cases to safeguard the user experience.
If you are launching a new app and would like to integrate with TikTok from the beginning, you are expected to undergo an audit and provide additional supporting information such as reasoning and your UX mockups. We reserve the right to reject or approve such unpublished apps in our sole discretion based on the app's credibility, benefits to TikTok users, and other factors. To start this process, apply for integration assessment for unreleased apps.
### What APIs offer Marketing and Ad Campaigns?
[TikTok for Developers products do not offer these functionalities. TikTok for Business offers Marketing and Ad Campaign APIs. Visit the TikTok for Business website](https://getstarted.tiktok.com/ttvalue?attr_source=google&attr_medium=search-br-ad&attr_adgroup_id=131664210937&attr_term=tiktok%20for%20business&gad_source=1&gclid=Cj0KCQiA4Y-sBhC6ARIsAGXF1g7-Vas1empg2j8UFkDX0Xv_LLhKuodyZc85w2zqsKywdEekKCjEws0aAvtVEALw_wcB&lang=en-US) for a list of their products.
### Can I increase my active user cap?
[Please contact us via our Support form](https://developers.tiktok.com/support/) to request an increase in your active user cap. Please note that your app must be in production to request and increase, and not all requests will be approved.
### Can I request an infinite user access token?
[User Access Tokens can be extended to a maximum of one year. For more information on how to change user access token lengths, please refer to the documentation on managing user access tokens](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens).
### Where can I get support for bugs and error messages for my app that's in production?
[You may contact us via our Support form](https://developers.tiktok.com/support/) for further help on technical issues.
### Why are my posts private using the Content Posting API?
All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must undergo an audit to verify compliance with our Terms of Service.
Was this document helpful?