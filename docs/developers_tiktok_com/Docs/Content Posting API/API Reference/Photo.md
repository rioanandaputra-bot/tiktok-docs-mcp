Docs
# Photo
## Overview
The `/v2/post/publish/content/init/` endpoint allows you to post directly or upload photos to TikTok.

| HTTP URL | /v2/post/publish/content/init/ |
| --- | --- |
| HTTP Method | POST |
| Scope | video.publish or video.upload |

To directly post photos to users' TikTok accounts, you must query creator information to render the UI elements to be displayed on the export page of your app before you call this Content Posting API.
- [Learn more about the UX guidelines.](https://developers.tiktok.com/doc/content-sharing-guidelines#)
- [Learn more about the creator_info/query API](https://developers.tiktok.com/doc/content-posting-api-reference-query-creator-info).
## Request
**Note**: Each user access_token is limited to six requests per minute.
### Header

| **Field Name** | **Description** | **Value** | **Required** |
| --- | --- | --- | --- |
| Authorization | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/ | Bearer {$UserAccessToken} | true |
| Content-Type | The content format of the body of this HTTP request | application/json; charset=UTF-8 | true |

### Body

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| media_type | string | Currently only `PHOTO`is allowed | true |
| post_mode | string | Enum of: `DIRECT POST`: Directly post the content to TikTok user's account. `MEDIA_UPLOAD`: Upload content to TikTok for users to complete the post using TikTok's editing flow. Users will receive an inbox notification. | true |
| post_info | [Post Info Object](#eK35Sd) | The post information | true |
| source_info | [Source Info Object](#D9SdTz) | The media source information | true |

#### Post Info Object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| title | string | The post title. The maximum length for photo posts is 90 in UTF-16 runes. | false |
| description | string | The post description. The maximum length for photo posts is 4000 in UTF-16 runes. | false |
| privacy_level | string | Enum of: `PUBLIC_TO_EVERYONE` `MUTUAL_FOLLOW_FRIENDS` `FOLLOWER_OF_CREATOR` `SELF_ONLY` The provided value must match one of the `privacy_level_options`returned in the `/creator_info/query/`API. | Required for `DIRECT POST` |
| disable_comment | bool | Only works for post_mode = `DIRECT POST`. If set to `true`, other TikTok users will not be allowed to make comments on this post. | false |
| auto_add_music | bool | Only works for post_mode = `DIRECT POST`. If set to `true`, recommended music will be automatically added to photos, and users can later choose to change the post's music in TikTok if they prefer other music. | false |
| brand_content_toggle | bool | Only works for post_mode = `DIRECT POST`. Set to `true`if the content is a paid partnership to promote a third-party business. | true |
| brand_organic_toggle | bool | Only works for post_mode = `DIRECT POST`. Set to `true`if this content is promoting the creator's own business. | true |

#### Source Info Object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| source | string | Only `PULL_FROM_URL`is allowed | true |
| photo_images | list<string> | [An array containing up to 35 photo content URLs. The URLs must be publicly accessible and verified by your app. Learn more about pulling from URLs](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#pull_from_url). | true |
| photo_cover_index | int | Indicates the index (starting from 0) of the photo to be used as the cover | true |

### Example
#### Direct Post
**Note**: To use Direct Post, the target TikTok user must have authorized your app for the `video.publish` scope.
[[All content posted by unaudited clients will be restricted to private viewing mode. Once you have successfully tested your integration, to lift the restrictions on content visibility, your API client must undergo an audit](https://developers.tiktok.com/application/content-posting-api) to verify compliance with our Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service?lang=en).
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photomode on your @tiktok #fyp",
        "disable_comment": true,
        "privacy_level": "PUBLIC_TO_EVERYONE",
        "auto_add_music": true
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "DIRECT_POST",
    "media_type": "PHOTO"
}'
```
#### Upload
After uploading from your app, you should inform users that they must click on inbox notifications to continue the editing flow in TikTok and complete the post. Title and description parameters are now supported with sending photos.
**Note**: To use upload method, the target TikTok user must have authorized your app for the `video.upload` scope.
We now support sending title and description in this method and it will be reflected in the editing flow once user clicks on the inbox notification.
```
curl --location 'https://open.tiktokapis.com/v2/post/publish/content/init/' \
--header 'Authorization: Bearer act.example12345Example12345Example' \
--header 'Content-Type: application/json' \
--data-raw '{
    "post_info": {
        "title": "funny cat",
        "description": "this will be a #funny photomode on your @tiktok #fyp"
    },
    "source_info": {
        "source": "PULL_FROM_URL",
        "photo_cover_index": 1,
        "photo_images": [
            "https://tiktokcdn.com/obj/example-image-01.webp",
            "https://tiktokcdn.com/obj/example-image-02.webp"
        ]
    },
    "post_mode": "MEDIA_UPLOAD",
    "media_type": "PHOTO"
}'
```
## Response

| **Field Name** | **Nested Field** | **Type** | **Description** |
| --- | --- | --- | --- |
| data | publish_id | string | An identifier to track the posting action, which you can use to check status. The maximum length of this field is 64. |
| error | code | string | [You can decide whether the request is successful based on the error code. Any code other than `ok`indicates the request did not succeed. Learn more about error codes](#DU14lm). |
| message | string | A human-readable description of the error |
| logid | string | A unique identifier for the execution of this request |

### Example
```
200 OK
{
    "data": {
        "publish_id": "p_pub_url~v2.123456789"
    },
    "error": {
         "code": "ok",
         "message": "",
         "log_id": "202210112248442CB9319E1FB30C1073F3"
     }
}
```
### Error codes

| **HTTP Status** | **error.code** | **Description** |
| --- | --- | --- |
| 400 | invalid_param | Check error message for details |
| app_version_check_failed | To use `MEDIA_UPLOAD`post_mode, users' TikTok APP version must not be less than 31.8 |
| 403 | spam_risk_too_many_posts | The daily post cap from API is reached for the current user |
| spam_risk_user_banned_from_posting | The user is banned from making new posts |
| spam_risk_too_many_pending_share | The daily upload cap from the API is reached for the current user. To reduce spamming, TikTok limits the number of videos that can be uploaded via API that are not pending approval and posting by the creator. There may be at most 5 pending shares within any 24-hour period. |
| reached_active_user_cap | The daily quota for active publishing users from your client is reached |
| unaudited_client_can_only_post_to_private_accounts | Unaudited clients can only post to private account. The publish attempt will be blocked when calling `/publish/content/init/`. |
| url_ownership_unverified | [To use `PULL_FROM_URL`as the content transfer method, developer must verify the ownership of the URL prefix or domain. Learn more about content transfer](https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide#). |
| privacy_level_option_mismatch | `privacy_level`is either unspecified or not among the options from the `privacy_level_options`returned in /publish/creator_info/query/ API. All clients are required to correctly display the creator account's privacy level options and honor the users' choice. Occurances of this error for product-use applications suggest violations to TikTok's product-use guidance. |
| 401 | access_token_invalid | The access_token is invalid or has expired |
| scope_not_authorized | The access_token does not bear user's grant on `video.publish`or `video.upload`scope |
| 429 | rate_limit_exceeded | Your request is blocked due to exceeding the API rate limit |
| 5xx | internal_error | TikTok server or network error. Try again later. |

Was this document helpful?