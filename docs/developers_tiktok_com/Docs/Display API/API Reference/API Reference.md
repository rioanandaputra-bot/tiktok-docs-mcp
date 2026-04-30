Docs
# Get User Info
[There is a migration plan related to this API. Learn more here](https://developers.tiktok.com/bulletin/user-info-scope-migration).
## Overview
The `/v2/user/info/` endpoint returns some basic information for a given TikTok user.

| **HTTP ****URL** | https://open.tiktokapis.com/v2/user/info/ |
| --- | --- |
| **HTTP Method** | GET |
| **Scope** | [Needs relevant scopes](#user_object) to be authorized by the TikTok user through the authorization flow. |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | true |

### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The set of user fields to request for | open_id,union_id,avatar_url | true |

### Example
```
curl -L -X GET 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url' \
-H 'Authorization: Bearer act.example12345Example12345Example'
```
## Response

| **Key** | **Type** |
| --- | --- |
| data | map<string, User Object> |
| error | [Error Object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

### User Object

| **Field** | **Type** | **Description** | **Authorized ****Scope** |
| --- | --- | --- | --- |
| open_id | string | The unique identification of the user in the current application.Open id for the client | user.info.basic |
| union_id | string | The unique identification of the user across different apps for the same developer. For example, if a partner has X number of clients, it will get X number of open_id for the same TikTok user, but one persistent union_id for the particular user | user.info.basic |
| avatar_url | string | User's profile image | user.info.basic |
| avatar_url_100 | string | User`s profile image in 100x100 size | user.info.basic |
| avatar_large_url | string | User's profile image with higher resolution | user.info.basic |
| display_name | string | User's profile name | user.info.basic |
| bio_description | string | User's bio description if there is a valid one | user.info.profile |
| profile_deep_link | string | The link to user's TikTok profile page | user.info.profile |
| is_verified | boolean | Whether TikTok has provided a verified badge to the account after confirming that it belongs to the user it represents | user.info.profile |
| username | string | User's username. | user.info.profile |
| follower_count | int64 | User's followers count | user.info.stats |
| following_count | int64 | The number of accounts that the user is following | user.info.stats |
| likes_count | int64 | The total number of likes received by the user across all of their videos | user.info.stats |
| video_count | int64 | The total number of publicly posted videos by the user | user.info.stats |

### Example
```
{
   "data":{
      "user":{
         "avatar_url":"https://p19-sign.tiktokcdn-us.com/tos-avt-0068-tx/b17f0e4b3a4f4a50993cf72cda8b88b8~c5_168x168.jpeg",
         "open_id":"723f24d7-e717-40f8-a2b6-cb8464cd23b4",
         "union_id":"c9c60f44-a68e-4f5d-84dd-ce22faeb0ba1"
      }
   },
   "error":{
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
Was this document helpful?