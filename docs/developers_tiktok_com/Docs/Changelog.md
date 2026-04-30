Docs
# Changelog
This document describes major and critical changes made to TikTok for Developer products and documentation. Please note that this document is not an exhaustive list of all changes.
## February 26, 2026
**Product**
- `Research Tools`: Updated data pipeline logic to ensure comprehensive coverage of all public video content, including videos not eligible for recommendation to the For You feed.
## January 20, 2026
**Product**
- `TikTok GO`: Launched TikTok GO for Dining and associated SaaS APIs.
## December 23, 2025
**Product**
- [`Research Tools`: Added a data access application](https://developers.tiktok.com/application/vetted-researcher) for vetted researchers.
- `Mini Games`: Released integration workflow and APIs for TikTok Mini Games.
Website enhancement
- `Organizations`: Updated the user interface for organization management on the Developer Portal.
## October 18, 2025
**Product**
- [`Research Tools`: Published a webpage for vetted researchers](https://developers.tiktok.com/products/research-api/vetted-researcher-data-access), explaining the types of data vetted researchers can access.
## May 16, 2025
**Product**
- [`Research Tools`: Launched Batch Compliance APIs](https://developers.tiktok.com/doc/batch-compliance-apis) that allow you to retrieve the compliance status of user IDs in batches.
## April 26, 2025
**Product**
- `Research Tools`: Introduced data filtering to the Test Stage of the Virtual Compute Environment, limiting data access to users that have at least 25,000 followers.
## April 17, 2025
**Product**
- `Research Tools`: Updated existing APIs to enrich and return additional parameters:
- Query Videos, Query User Liked Videos, Query User Pinned Videos, and Query User Reposted Videos now include the following: `video_mention_list, hashtag_info_list, sticker_info_list, video_label, video_tag`
- Query User Info now includes `author_profile_URL`
- Query Video Comments now includes `display_name`
## February 28, 2025
**Product**
- Launched Hotel Integration solution to allow travel partners to create listings within TikTok.
## December 9, 2024
**Product**
- `Research API`: Launched TikTok Shop related APIs for EU based shops.
## November 4, 2024
**Product**
- `Research API`: Added `hashtag_info`, user `bio_url`, `video_mention_list` and `video_label`.
## October 22, 2024
**App Requirements**
- `App Review`: Added an app review section to the app page that requires additional information for app submission, and introduced technical specifications for app icons.
## October 8, 2024
**Product**
- [`Login Kit`: Login Kit for Android](https://developers.tiktok.com/doc/login-kit-android-quickstart-v2) now requires the authorization request's redirect URI to follow an HTTPS scheme.
## September 9, 2024
**App Requirements**
- [`URL Properties`: Implemented verification of URL ownership](https://developers.tiktok.com/doc/getting-started-create-an-app#) as a mandatory component for app configuration. Only apps created after effective date require URL ownership verification.
## July 23, 2024
**Product**
- `Embed Player`: Added a code example for the Embed Player doc.
## July 09, 2024
**Product**
- [`Research API`: Launched Playlist Info endpoint for Research API and added additional fields to existing APIs. Learn more about the Playlist Info endpoint](https://developers.tiktok.com/doc/research-api-specs-query-playlist-info).
## June 24, 2024
**Documentation**
- [[[`Developer Website`: Updated Register Your App](https://developers.tiktok.com/doc/getting-started-create-an-app) and App Review FAQ](https://developers.tiktok.com/doc/getting-started-faq) to accommodate the new app page interface. Published App Review Guidelines](https://developers.tiktok.com/doc/app-review-guidelines) to facilitate understanding of our app review criteria.
**Website Enhancement**
- [`Developer Website`: Launched Sandbox mode and updated the app page interface. Learn more about Sandbox mode](https://developers.tiktok.com/doc/add-a-sandbox).
## February 07, 2024
**Product**
- `Research API`: Launched five additional APIs that allows querying liked videos, reposted videos, pinned videos and the followers and following lists of a user.
## January 17, 2024
**Website Enhancement**
- [`Developer Website`: Introduced search function for technical documentation on developers.tiktok.com/doc](http://developers.tiktok.com/doc).
## November 28, 2023
**Website Enhancement**
- [`Developer Website`: Added a new space for blogs](https://developers.tiktok.com/blogs). You can now learn about our developer products and interesting stories from the tech teams that build TikTok.
## November 3, 2023
**Product**
- [[`Content Posting API`: TikTok's Content Posting API now supports Photos! Developers can now integrate with the new API endpoints](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post) to allow creators post photos to their TikTok account directly from your app. Learn more here](https://developers.tiktok.com/doc/content-posting-api-get-started).
## October 16, 2023
**Product**
- [`Login Kit`: Released v2 of our QR code authorization API. Learn more about QR code authorization](https://developers.tiktok.com/doc/login-kit-qr-code-authorization).
## October 5, 2023
**Product**
- [`Login Kit`: TikTok's Login Kit is now available for use on Desktop. Learn more about Login Kit for Desktop](https://developers.tiktok.com/doc/login-kit-desktop/).
## September 21, 2023
**Product**
- [`Login Kit`: The deadline for web apps using v1 OAuth to migrate to v2 OAuth has been extended to February 29, 2024. Learn more about OAuth migration](https://developers.tiktok.com/bulletin/migration-guidance-oauth-v1).
- [[`Login Kit`: The deadline for apps using user.info](http://user.info).basic to request continued access to data protected by new scopes has been extended to February 29, 2024. Learn more about User Info API scope migration](https://developers.tiktok.com/bulletin/user-info-scope-migration).
## August 10, 2023
**Product**
- [`Research API`: Expanded Research API to Europe-based non-profit academic institutions. Learn more here](https://developers.tiktok.com/products/research-api).
## August 8, 2023
**Website Enhancement**
- [`Developer Website`: Developers may apply for assessment to integrate their app with TikTok before their app is launched to the public. Learn more in the submission requirements](https://developers.tiktok.com/doc/our-guidelines-developer-guidelines#submission_requirements) section of our developer guidelines.
- [`Developer Website`: Added support for group collaboration using organizations. Developers working together can now register apps under organizations for shared access. Learn more here](https://developers.tiktok.com/doc/working-with-organizations).
## July 20, 2023
**Product**
- [`Commercial Content API`: Launched Commercial Content API (only including data from EU countries) to global researcher/professional. Learn more here](https://developers.tiktok.com/products/commercial-content-api).
## June 20, 2023
**Product**
- `Share Kit`: Released urgent hotfix in TikTok OpenSDK 0.2.1.2 to patch app redirect issues with Share Kit on Android 13+.
## June 8, 2023
**Product**
- [[[`TikTok OpenSDK`: Our revamped Android](https://github.com/tiktok/tiktok-opensdk-android) and iOS](https://github.com/tiktok/tiktok-opensdk-ios) SDKs, Login Kit and Share Kit, are available to checkout on GitHub. Get Started here](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart).
## June 7, 2023
**Product**
- [`Content Posting API`: TikTok's Direct Post API is live! Creators can now post content to their TikTok account directly from your app. Learn more here](https://developers.tiktok.com/doc/content-posting-api-get-started/).
## June 5, 2023
**Website Enhancement**
- [`Developer Website`: You can now also initiate deletion of your developer account from your account settings](https://developers.tiktok.com/settings/#account-setting) page.
## May 23, 2023
**Product**
- `Content Posting API`: TikTok's Content Posting API now supports video uploads by pulling content from a URL. Learn more here.
## May 22, 2023
**Product**
- [`Login Kit + Display API`: `user.info``.basic` returns fewer fields than before through Display APIs(include `Post:/user/info/` and `Get:/v2/user/info/`). Learn more here](https://developers.tiktok.com/bulletin/user-info-scope-migration).
## May 11, 2023
**Product**
- [`Login Kit`: Released our improved OAuth v2 API for web apps to provide a secure authorization and token management flow. Learn more here](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens).
**Documentation**
- [[[`Developer Website`: Consolidated Server API](https://developers.tiktok.com/doc/tiktok-api-v2-rate-limit), Mobile SDK](https://developers.tiktok.com/doc/getting-started-ios-quickstart-objective-c), and webhook](https://developers.tiktok.com/doc/webhooks-overview) documentation under Integration Essentials.
## May 10, 2023
**Documentation**
- [[[`Display API`: Reorganized Display API user and video endpoint documentation:Consolidated v2 user](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info) and video](https://developers.tiktok.com/doc/tiktok-api-v2-video-query) endpoint references under Display API.Archived v1 user and video endpoint documentation under Legacy API section](https://developers.tiktok.com/doc/tiktok-api-v2-introduction).
## April 27, 2023
**Product**
- [`Video Kit`: Announced deprecation and migration](https://developers.tiktok.com/bulletin/migration-notice-share-video-api/) for Video Kit for Web (Share Video API).
- [`Content Posting API`: Launched Content Posting API. Get started](https://developers.tiktok.com/doc/content-posting-api-get-started) by uploading a video to TikTok!
## March 22, 2023
**Documentation**
- [`Developer Website`: Published Developer Guidelines](https://developers.tiktok.com/doc/our-guidelines-developer-guidelines) to provide a better understanding of our integration processes and requirements.
## March 16, 2023
**Website Enhancement**
- [`Developer Website`: Added account settings](https://developers.tiktok.com/settings/notification/) page. You can now manage your email notification preferences to stay up-to-date on our latest news and products.
## March 2, 2023
**Documentation**
- `Changelog`: Introduced this changelog in our documentation section.
## February 21, 2023
**Product**
- [`Research API`: Launched Research API to US non-profit academic institutions. Learn more here](https://developers.tiktok.com/products/research-api).
Was this document helpful?