Docs
# Overview
The Display API contains a set of HTTP-based APIs that your product can use to display a TikTok creator's videos and their profile information.
Your platform's influencers can display their TikTok profile identities and videos to enrich content, attract more audiences, and enable their followers to view their TikTok videos without leaving your platform.
## Components
Display API has three major APIs: `/v2/user/info/`, `/v2/video/list/`, and `/v2/video/query/`.
[**/v2/user/info/](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)****:** Get a TikTok user's basic profile information. This includes the user's open_id, avatar_url, display_name, profile_deep_link, and bio_description.
[**/v2/video/list/](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)****:** Get the metadata of a TikTok user's recently uploaded videos.
[**/v2/video/query/](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)****:** Get the metadata of TikTok a user's videos filtered by video Id.
## Permissions
- **video.list:** Read a user's public videos on TikTok.
- **user.info****.basic:** Read a user's profile info (open id, avatar, display name, ...).
## Example Use Cases
### Display User's TikTok Profile
Use the /v2/user/info/ API to get a TikTok user's profile data and then display their TikTok identity. In this example, when a visitor clicks the profile_deep_link, they will be redirected to the creator's profile page on the TikTok app or website.
### Display User's Self-Selected TikTok Videos
Use the /v2/video/list/ and /v2/video/query/ APIs to get the metadata of a TikTok user's videos and integrate an embedded video player into your product. In addition, you can design features to allow users to select their TikTok videos to present on their profile and enable their followers to watch the video in webview.
### Display User's Recent TikTok Videos
Use the /v2/video/list/ and /v2/video/query/ APIs to get the metadata of a TikTok user's videos and integrate an embedded video player into your product. In addition, you can design features to allow users to show their recent TikTok videos on your platform.
## Next Steps
[Get Started with Display API](https://developers.tiktok.com/doc/display-api-get-started)
Was this document helpful?