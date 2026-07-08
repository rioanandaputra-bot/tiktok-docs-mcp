# Our Guidelines

> Consolidated from 4 source files.



---
## SOURCE: Our Guidelines/Content Sharing Guidelines.md

Docs
[**New: **Content Posting API now supports posting photos](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)!
# General Guidelines
## Watermark Guidelines
We expect you to avoid adding unwanted material to content posted to TikTok. That means your apps and integrations should not superimpose or otherwise include any brand name, logo, watermark, other promotional branding, link or promotional text, on or in any content which is shared to TikTok. Doing so is a violation of these guidelines, and may also lead to deleted content or disabled accounts.
## Direct Post API - Developer Guidelines
[[Direct Post API enables developers to build "Share to TikTok" experiences in their app, which allows creators to share content directly to their TikTok profile. As a developer, you can use this API in an unverified status, but all content uploaded via this endpoint will be restricted to private viewing mode. To lift this restriction, your API client must undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
If your API client has not been audited, the following restrictions will apply:
- **User cap**: Unaudited API Clients can allow up to 5 users to post in a 24 hour window. All user accounts using the API client to post must be set to private at the time of posting.
- **Private Viewership**: Unaudited API Clients can only post contents in `SELF_ONLY` viewership. To make the contents publicly viewable later on, the account owner must first change their account visibility to public, and then change the privacy settings of each content to "Everyone."
Additionally, both audited and unaudited API clients will be subject to the following caps:
- **Creator cap**: There will be a 24-hour active creator cap for each API client based on the usage estimates provided in the audit application form.
- **Posting cap**: There is a limit on the number of posts that can be made to a creator account in a 24-hour window via Direct Post API. The upper limit may vary among creators (typically around 15 posts per day/ creator account) and is shared across all API Clients using Direct Post.
### Intended Use
1) API Clients should facilitate authentic creators to post original content to TikTok.
Not acceptable: An app that copies arbitrary contents from other platforms to TikTok. ❌
2) API Clients must not be limited to test applications and should be intended for a wide audience, not limited to internal groups/private use.
Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages. ❌
### Required UX Implementation in Your App
**1) API Clients must retrieve the latest creator info when rendering the Post to TikTok page.**
a. The upload page must display the creator's nickname, so users are aware of which TikTok account the content will be uploaded to.
b. When the _creator_info API_ returns that the creator can not make more posts at this moment, API Clients must stop the current publishing attempt and prompt users to try again later.
c. When posting a video, API clients must check if the duration of the to-be-posted video follows the `max_video_post_duration_sec` returned in the _creator_info API_.
**2) API Clients must allow users to enter or select the following metadata for a post:**
a. Title
b. Privacy Status, with the following mandatory requirements:
- The options listed in the UX must follow the `privacy_level_options` returned in the _creator_info API_.
- Users must manually select the privacy status from a dropdown and there should be no default value.
c. Interaction Ability - Allow Comment, Duet, and Stitch - with the following style requirements:
- If the creator_info API returns that one or more of these interactions have been disabled in their app settings, your UX must disable and grey out the checkbox for the interaction.
- Users must manually turn on these interaction settings and none should be checked by default.
- Duet and Stitch features are not applicable to photo posts. So, for Photo Posts, only 'Allow Comment' can be displayed in the UX.
[NOTE: Before allowing users to post through your platform, there should be a declaration asking for a user's consent before the publish button. It should clearly state: "By posting, you agree to TikTok's Music Usage Confirmation](https://www.tiktok.com/legal/page/global/music-usage-confirmation/en)"
**3) API Clients must allow users to disclose Commercial Content:**
a. **Content Disclosure Setting** - Indicate whether this content promotes yourself, a brand, product or service, with this feature `turned off` by default. Enabling this feature will display checkboxes for "Your brand" and "Branded content" below, allowing users to select their preferences.
- **Your Brand**: You are promoting yourself or your own business. This content will be classified as Brand Organic. **If this option is selected by the user, a**** prompt should state: "****Your photo/video will be labeled as 'Promotional content'****"**
- **Branded Content**: You are promoting another brand or a third party. This content will be classified as Branded Content. **If this option is selected by the user, a**** prompt should state: "****Your photo/video will be labeled as 'Paid partnership'****"**
- If both the above options are selected by the user, a prompt should state "_Your photo/video will be labeled as 'Paid partnership'_"
It is a multiple selection, and at least one of the options above must be chosen to proceed with publishing. If the commercial content disclosure toggle is `turned on` but no options are selected, the publish button should be `disabled`. To make it easier for users to follow, **hovering over will show a notification: "****You need to indicate if your content promotes yourself, a third party, or both****.****"**
b. **Privacy Management:**
- If a user wants to choose Branded Content, it is important to **note that it can only be configured with visibility as public/friends**.
- If the visibility setting is chosen as "private" (only me):
- Either the "Branded Content" option should be `disabled`, **informing the user that visibility for branded content can't be private**.
- OR, the visibility setting should be automatically switched to public if the user wants to choose Branded Content, **informing the user about the same**.
- Before selecting the privacy/visibility setting, if a user has `turned on` the commercial content disclosure toggle and checked the branded content option, then the "only me" permission should be `disabled`, and **hovering over it will display a prompt stating, "Branded content visibility cannot be set to private."**
**4) Compliance requirements:**
If the user is trying to post commercial content (i.e. commercial content toggle is `turned on`):
- [When only "Your Brand" is checked, the declaration should be the same as mentioned above: "By posting, you agree to TikTok's Music Usage Confirmation](https://www.tiktok.com/legal/page/global/music-usage-confirmation/en)."
- [[When only "Branded Content" is checked, the declaration should be changed to: "By posting, you agree to TikTok's Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en) and Music Usage Confirmation.](https://www.tiktok.com/legal/page/global/music-usage-confirmation/en)"
- [[Additionally, when both options are selected, the declaration should be: "By posting, you agree to TikTok's Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en) and Music Usage Confirmation](https://www.tiktok.com/legal/page/global/music-usage-confirmation/en)."
**5) The users of API Clients must have full awareness and control of what is being posted to their TikTok accounts.**
a. API Clients should display a preview of the to-be-posted content.
b. API Clients should not add promotional watermarks/logos to creators' content. Preset text, including any text in the title field or hashtags, should be allowed to be edited by the user before posting content.
c. API Clients must only start sending content materials to TikTok after the user has expressly consent to the upload.
d. API Clients must clearly notify users that after they finish publishing their content, it may take a few minutes for the content to process and be visible on their profile.
[e. API clients should poll the publish/status/fetch API](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status) or handle status update webhooks, so users can understand the status of their posts.
### Technical Considerations
**1) Keep client_secret confidential**
a. You must not share your API Credentials with any other third-party or embed your client_secret in open source projects.
b. Maintain appropriate technical and administrative controls to ensure the security and confidentiality of client_secret.
**2) Choose efficient means to send contents to TikTok**
a. PULL_FROM_URL should be used when API Clients already have the to-be-posted contents on server-side file storage services.
b. The supplied URL must be under the path of a domain or URL prefix API Clients have ownership on. The ownership needs to be verified through the Manage URL properties flow on the Manage Apps page in your TT4D app.
c. FILE_UPLOAD should be used when the to-be-posted video is on the users' devices (PC, Mac, Switch, etc) of API Clients.
d. If video resources are already on API Clients' servers, do not use FILE_UPLOAD; use PULL_FROM_URL instead.
Was this document helpful?


---
## SOURCE: Our Guidelines/Design Guidelines.md

Docs
# Design Guidelines
## The TikTok Brand and Use Guidelines
[Please carefully read our official TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal). You must adhere to these guidelines.
You may not use TikTok logos, icons, symbols, or designs, without our prior written permission. Additionally, you may not use names, logos, icons, symbols or designs of anyone without their permission.

|  |  |  |
| --- | --- | --- |

## Asset Packs
[To download TikTok's Logo and Button packs, click here](https://sf16-va.tiktokcdn.com/obj/eden-va2/uvzhqeh7nuhd/tt4d/logo-pack.zip).
---
### Assets for TikTok developers
Was this document helpful?


---
## SOURCE: Our Guidelines/Developer Guidelines.md

Docs
# Developer Guidelines
We are excited that you are seeking to integrate your app with TikTok. As developers, you can help us inspire creativity and bring joy by providing awesome experiences for TikTok users. This page provides guidelines for you to better understand our integration processes and requirements.
## App review process
To provide a safe and reliable experience for TikTok users, all apps seeking to integrate with our APIs and SDKs in Live are reviewed.
If an app is in Live, it means it can integrate with our APIs and SDKs for authorized access to data of TikTok end users.
After your apps are approved, requests for modification may require further reviews depending on the attributes being changed. Our review process may also provide feedback to improve your integration with TikTok.
### Submission requirements
- Make sure your app is functioning during our review process. You are required to provide demo accounts and capabilities to our approvers free of charge, if requested.
- [For incomplete apps, beta or development versions, and test versions, you are encouraged to use Sandbox mode](https://developers.tiktok.com/doc/add-a-sandbox) to test out our integrations.
- Follow our guidelines throughout the duration of your integration with TikTok. Any violations of our guidelines found through auditing, user complaints, or other means will likely lead to immediate revocation of your integration and a permanent ban on all future integrations by your account and business entity.
- [Verify ownership of all configurations with a URL, including your Privacy Policy, Terms of Service, and more. Learn more about URL verification](https://developers.tiktok.com/doc/getting-started-create-an-app#verify_url_ownership).
Note: We do not provide an official review timeline or any guarantees for approval. While we do our best to accommodate all requests and communicate promptly, this is a manual process and response times may vary. We remind you to factor the review process into your launch timelines and planning.
## Developer Principles
### Provide great experiences
By integrating with TikTok, you are helping us expand the ecosystem of experiences available to our users. Therefore, we expect your app to provide significant additional value to TikTok and its end users. Don't just build great experiences, maintain them! Even if your app is approved for integration, failure to maintain a quality experience can lead to revocation of your integration.
### Build awesome interfaces
Great experiences start with easy to understand and intuitive interfaces. Bad experiences cause user frustration so we want to avoid them. All app UI must follow industry best practices for user experience and interface design. Additionally, to maintain diversity and inclusion standards across apps, be mindful of localized expectations such as language and prioritize accessibility capabilities.
If your users are developers themselves, make sure your APIs and SDKs behave as expected based on their interface and model. Avoid overly complicated or confusing API contracts.
### Be reliable
Apps with complaints of frequent outages, timeouts, or poor performance can be rejected or have their integration revoked. To avoid this, regularly track your latency, success rates, and service availability. Manage service incidents promptly and fix any bugs in your app. Treat issues related to data security and critical functionality (for example, payments) with urgency.
### Be trustworthy
[Great experiences are transparent with users and give them control of their data and content. Be very clear with users about the purpose of your app and your integration with TikTok. Provide mechanisms for users to contact you directly, and promptly address their concerns. Don't engage in any deceptive or misleading communication. Never misguide users into thinking that you are part of the TikTok app, or, for that matter, any other app or entity that doesn't belong to you. As a reminder, make sure you have read and comply with our Branding Requirements](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal).
Understand that the user's data belongs to them. You must safeguard their data. Don't share it with anyone without their proper consent.
Here are some example behaviors to maintain trust:
- Never remove a creator's copyright mechanisms (such as watermarks) without consent.
- Protect the user's identity and anonymity.
- If you have access to a user's PII (Personally Identifiable Information), never share it with anyone without their consent.
- Follow all data sharing and privacy laws to build trust with users and governments.
- Set an accurate description, title, and icon for your app.
- Disclose your app's Terms of Service and Privacy Policy.
- Verify URL ownership.
- Provide all required data when configuring your app integration and developer profile.
**Note:** Providing fake or incomplete data may lead to the rejection of your app and delays in your integration.
## TikTok Integration Maintenance Requirements
- You must actively maintain communication with TikTok when requested. Failure to respond to correspondence in a timely manner can lead to termination of your integration.
- Check your email filters and make sure our communications are not landing in your spam or junk mail folders.
- Any sensitive communication relating to topics including but not limited to security, privacy, compliance, and user deception must be addressed immediately regarding these matters.
- TikTok reserves the right to deprecate APIs and SDKs. You must prioritize and update your integration as new features are offered by TikTok for Developers.
- You will be given notice when backward incompatible changes are made to our APIs. You must prevent any user interfaces from being broken because of deprecated integrations by promptly migrating to newer APIs.
- For any security, privacy, and compliance related concerns, you must immediately acknowledge communication from TikTok and update your integration.
- Respect our API throttling limits. It goes without saying, don't use your integration to attack us, our users, or anyone else with denial of service attempts, spam, etc. That's a surefire way to get banned forever and find yourself in more trouble than you or we need.
## Terms and Policies
Below you can find our Terms of Service and other policy documents.
- [Developer Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service )
- [Developer Data Sharing Agreement](https://www.tiktok.com/legal/tiktok-data-sharing-agreement)
- [Branding Requirements](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal)
- [Community Guidelines](https://www.tiktok.com/community-guidelines)
You are responsible for adhering to all policies and guidelines. TikTok reserves the right to reject your application for any reason, including failure to follow the guidelines mentioned in this document.
Was this document helpful?


---
## SOURCE: Our Guidelines/Our Guidelines.md

Docs
# App Review Guidelines
[Before you submit your app for review, make sure your app information is completely filled out and meets the criteria listed below. Check out our app review FAQ](https://developers.tiktok.com/doc/getting-started-faq) for answers to any additional questions you may have.
## Review criteria for app details
For your app to receive approval, your app configuration must meet the following criteria:
### App name and icon
- The app must have a custom name. The app name will be shown on the authorization page for the app.
- The name should not include a reference to social media companies (for example, "TikTok app").
- The app name should match the app or website name and not describe your app. For example, do not add "Video Content Analytics Uploader" as the name.
- [The app name must adhere to the TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal).
- The app icon must be a clear image.
- The app icon must not contain any sensitive or inappropriate content.
- The app icon must not be easily confused with another well-known brand icon.
- The app icon must be consistent with the app name or brand.
### Description
- A description of what your app or website does and how it works. This will be visible to the user. For example:
- "A website that sells pet supplies."
- "Manage all your social media content in one place."
- [The intended purpose of your app must meet our developer guidelines](https://developers.tiktok.com/doc/our-guidelines-developer-guidelines).
- Apps must not be for private or personal use.
- Apps must not contain adult content.
- Apps that are still in development or testing will not be approved.
### Website URL
- A valid official website that houses information about your web and services.
- Your website URL cannot be a landing page or login page. You must have an externally facing fully developed website.
- Your Privacy Policy and Terms of Service links must be visible on the website URL without having to open a menu to view them, and the links must be active.
### Privacy Policy and Terms of Service
- A valid Privacy Policy and Terms of Service and must be visible on your official website.
### Additional platform-specific requirements:
#### iOS
- Your app must be published in the Apple App Store.
- You must configure iOS Bundle ID under the iOS app configuration section.
#### Android
- Your app must be published in the Google Play Store.
- You must configure the Android app signature and package name under the Android app configuration section.
#### Web apps
- You must provide a valid redirect URI under the web app configuration section.
### Scopes
- To obtain access to our developer tools, be sure to add the correct scope to your app.
- Only request permissions and features that your app needs.
## App review information
In the **App review** section, you must also provide the following required information for app submission:
- A detailed explanation of how each product and scope works within your app or website.
- For first-time app review, provide a detailed explanation of how each TikTok for Developers product is utilized to enrich the user experience.
- For follow-up revisions, provide a detailed explanation of how each new and old TikTok for Developers product is utilized to enrich the user experience.
- At least one demo video that shows the complete end-to-end flow of the up-to-date integrations. You may upload a maximum of 5 videos, up to 50 MB each.
- For example, it should demonstrate how you use TikTok for Developers' capabilities, such as Login Kit, Share Kit, Display API, Content Posting API, and the relevant scopes.
- If your app has not been approved before, you are required to use a sandbox environment on the Developer Portal to demonstrate the integration.
- The demo video should showcase the website or app where the features will actually be integrated.
- All selected products and scopes must be clearly demonstrated in the video. If you don't need certain products or scopes, make sure to remove them before review. Otherwise, it will delay the review result.
- The video should clearly show the user interface and user interactions.
- If you intend to integrate with a web app, make sure the domain of the website shown in the demo video matches the website URL you provide.
- If you intend to integrate with a mobile app, the demo video should start by showing the app being opened.
TikTok for Developers will start reviewing your app once it is submitted.
Was this document helpful?
