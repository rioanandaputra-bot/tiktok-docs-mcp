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