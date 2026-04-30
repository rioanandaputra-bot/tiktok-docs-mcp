Docs
# Scopes Reference

| **Topic** | **Scope** | **Definition** | **User Display** | **Target APIs** |
| --- | --- | --- | --- | --- |
| Local Service | local.product.manage | Create and manage the product listing. | Create and manage the product listing. |  |
| local.shop.manage | Create and manage the local shops. | Create and manage the local shops. |  |
| local.voucher.manage | Validate and redeem the voucher. | Validate and redeem the voucher. |  |
| Portability | portability.activity.ongoing | Make ongoing requests for activity data on the user's behalf | Export copies of your activity data |  |
| portability.activity.single | Make a single request for activity data on the user's behalf | Export a copy of your activity data |  |
| portability.all.ongoing | Make ongoing requests for all available data on the user's behalf | Export copies of your full user data archive |  |
| portability.all.single | Make a single request for all available data on the user's behalf | Export a copy of your full user data archive |  |
| portability.directmessages.ongoing | Make ongoing requests for direct message data on the user's behalf | Export copies of your direct message data |  |
| portability.directmessages.single | Make a single request for direct message data on the user's behalf | Export a copy of your direct message data |  |
| portability.postsandprofile.ongoing | Make ongoing requests for posts and profile data on the user's behalf | Export copies of your posts and profile data |  |
| portability.postsandprofile.single | Make a single request for posts and profile data on the user's behalf | Export a copy of your posts and profile data |  |
| research_adlib | research.adlib.basic | Access to public commercial data for research purposes | Access to public commercial data for research purposes |  |
| research | research.data.basic | Access to TikTok public data for research purposes | Access to TikTok public data for research purposes |  |
| Research API | research.data.u18eu | Allow access to data from European users under 18, and all other public data, for research purposes | Allow access to data from European users under 18, and all other public data, for research purposes |  |
| Research VRA | research.data.vra | Access to provisioned data for vetted researchers. | Access to provisioned data for vetted researchers. |  |
| user | user.info.basic | Read a user's profile info (open id, avatar, display name ...) | Read your profile info (avatar, display name) | [User Info](https://developers.tiktok.com/doc/tiktok-api-v1-user-info) |
| user.info.profile | Read access to profile_web_link, profile_deep_link, bio_description, is_verified. | Read your additional profile information, such as bio description, profile link, and account verification status | [User Info](https://developers.tiktok.com/doc/tiktok-api-v1-user-info) |
| user.info.stats | Read access to a user's statistical data, such as likes count, follower count, following count, and video count | Read your profile engagement statistics, such as like count, follower count, following count, and video count | [User Info](https://developers.tiktok.com/doc/tiktok-api-v1-user-info) |
| video | video.list | Read a user's public videos on TikTok | Read your public videos on TikTok | [[Query Videos](https://developers.tiktok.com/doc/tiktok-api-v1-video-query) List Videos](https://developers.tiktok.com/doc/tiktok-api-v1-video-list) |
| video.publish | Directly post content to a user's TikTok profile. | Post content to TikTok. | [[Direct Post](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post) Get Post Status](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status) |
| video.upload | Share content to creator's account as a draft to further edit and post in TikTok. | Share content as a draft to your TikTok account. | [[[Upload](https://developers.tiktok.com/doc/content-posting-api-reference-upload-video) Get Post Status](https://developers.tiktok.com/doc/content-posting-api-reference-get-video-status) Share Video API](https://developers.tiktok.com/doc/web-video-kit-with-web) |