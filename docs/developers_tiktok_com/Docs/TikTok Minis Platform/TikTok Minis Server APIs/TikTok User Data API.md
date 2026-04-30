Docs
# TikTok User Data API
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the right to only agree to a subset of scopes you requested from them.
Currently, TikTok Minis only supports `user.info``.basic` and `user.info``.open_id`. See **User Object** under the response struct.
## Get user info
[The `/v2/user/info/` endpoint returns some basic information for a given TikTok user. It must have `user.info``.basic` scope. To get the `user.info``.basic` scope, follow the explicit authorization process](https://developers.tiktok.com/doc/develop-your-mini-game).
### Endpoint
[`GET ``https://open.tiktokapis.com/v2/user/info/](https://open.tiktokapis.com/v2/user/info/)`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The set of user fields to request for | open_id,union_id,avatar_url | Yes |

### Response Struct

| **Key** | **Type** |
| --- | --- |
| data | map<string, User Object> |
| error | [Error Object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

**User Object**

| **Field** | **Type** | **Description** | **Authorized ****s****cope** |
| --- | --- | --- | --- |
| open_id | string | The unique identification of the user within the current application (a TikTok user's unique identifier) | user.info.basic |
| union_id | string | The unique identification of the user across different apps for the same developer. For example, if a partner has X number of clients, it will get X number of `open_id`for the same TikTok user, but one persistent `union_id`for the particular user | user.info.basic |
| avatar_url | string | User's profile image | user.info.basic |
| avatar_url_100 | string | User`s profile image in 100 x 100 size | user.info.basic |
| avatar_large_url | string | User's profile image with higher resolution | user.info.basic |
| display_name | string | User's profile name | user.info.basic |

### Example
```
curl -L -X GET 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url' \
-H 'Authorization: Bearer act.example12345Example12345Example'
```
If the request is successful, the response will look like the following.
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
[If the request is unsuccessful, an error response body will be returned in the response. Learn more about error handling](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling).
Was this document helpful?