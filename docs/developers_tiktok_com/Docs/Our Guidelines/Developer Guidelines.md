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