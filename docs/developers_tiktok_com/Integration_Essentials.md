# Integration Essentials

> Consolidated from 10 source files.



---
## SOURCE: Integration Essentials/Android.md

Docs
# TikTok OpenSDK for Android - Quickstart
[TikTok OpenSDK for Android is a Gradle project that allows you to integrate with native TikTok app functions. With OpenSDK, you can enable your users to log into your app with TikTok, and then share images and videos to their TikTok profiles. Checkout tiktok/tiktok-opensdk-android](https://github.com/tiktok/tiktok-opensdk-android) on GitHub!
## Getting started
The minimum system requirement is an API level of 21: Android 5.0 (Lollipop) or later.
### Step 1: Configure TikTok app settings for Android
[Register your app on the TikTok for Developers website](https://developers.tiktok.com/).
You must provide your MD5 and SHA256 certificate fingerprint during the app registration process.
- [If your app uses app signing by Google Play](https://support.google.com/googleplay/android-developer/answer/7384423), copy the MD5 and SHA-256 fingerprint from the app signing page of the Play Console.
- If your app is using self-signing, you can follow the instructions below to use Keytool or Gradle's Signing Report to get your MD5 and SHA-256.
- Using Keytool
Open a terminal and run the `keytool` utility to get the MD5 and SHA-256 fingerprint of the certificate.
```
keytool -list -v \
-alias <your-key-name> -keystore <path-to-production-keystore>
```
```
MD5: 75:C8:69:FC:D5:6E:EB:1D:02:79:A9:3F:91:BD:5E:5B
SHA1: EE:26:47:EC:59:83:6A:91:3C:7A:E1:61:14:56:6D:D8:90:B7:BA:3E
SHA-256: 6C:CF:15:C0:17:2E:EF:3E:48:2F:7E:E8:ED:6D:06:CB:CB:52:A4:CF:AD:CE:42:0B:80:9D:D5:D9:DE:DA:4C:7D
```
- Using Gradle's Signing Report
```
./gradlew signingReport
```
The signing report includes the signing information for each of your app's variants. Copy the MD5 and SHA-256 of the release variant.
```
Store: <your_keystore_location>
Alias: <your_keystore_alias>
MD5: 75:C8:69:FC:D5:6E:EB:1D:02:79:A9:3F:91:BD:5E:5B
SHA1: EE:26:47:EC:59:83:6A:91:3C:7A:E1:61:14:56:6D:D8:90:B7:BA:3E
SHA-256: 6C:CF:15:C0:17:2E:EF:3E:48:2F:7E:E8:ED:6D:06:CB:CB:52:A4:CF:AD:CE:42:0B:80:9D:D5:D9:DE:DA:4C:7D
```
- Provide the MD5 and SHA-256 for your app on the TikTok for Developers website.
- In the **App signature** field, remove the colon ( : ) from your MD5 string and provide the 32-character signature.
- In the **Signing certificate fingerprints** field, provide your SHA-256 string directly.
### Step 2: Install the SDK and set up the Android project
- In the **Project** window, switch to the **Android view** tab.
- Open **Gradle**** Scripts** and locate `build.gradle` (Project).
- Add the following repository in the `repositories{}` section:
```
repositories {
    maven { url "https://artifact.bytedance.com/repository/AwemeOpenSDK" }
}
```
- Open** ****Gradle**** Scripts** and locate `build.gradle` (Module: app).
- Add the following implementation statement to the `dependencies{}` section.
```
dependencies {
    implementation 'com.tiktok.open.sdk:tiktok-open-sdk-core:latest.release'
    implementation 'com.tiktok.open.sdk:tiktok-open-sdk-auth:latest.release'   // to use authorization api
    implementation 'com.tiktok.open.sdk:tiktok-open-sdk-share:latest.release'    // to use share api
}
```
[You can find the latest release here](https://github.com/tiktok/tiktok-opensdk-android/releases).
Note:
Due to package visibility changes in Android 11, the implementation of TikTok SDK for devices targeting Android 11 and later requires you to add the following to the Android manifest file.
```
<queries>
    <package android:name="com.zhiliaoapp.musically" />
    <package android:name="com.ss.android.ugc.trill" />
</queries>
```
Sync your project and get the latest version of the SDK package.
At this point, the basic development environment setup is complete.
Was this document helpful?


---
## SOURCE: Integration Essentials/Integration Essentials.md

Docs
# TikTok OpenSDK for iOS - Quickstart
[TikTok OpenSDK is a framework that enables your app's users to log in with their TikTok accounts and share images and videos to TikTok. This SDK is available for download through Swift Package Manager and CocoaPods. Checkout tiktok/tiktok-opensdk-ios](https://github.com/tiktok/tiktok-opensdk-ios) on GitHub!
## Getting started
The following are the minimum system requirements:
- iOS version 11.0 or later
- XCode version 9.0 or later
### Register your app with the TikTok for Developers website
- [Sign up for a developer account on the TikTok for Developers website](https://developers.tiktok.com/).
- Create a new app, add the required details, and submit it for review.
Upon approval, you will be provided with a client key and client secret that is unique to your app which you can view on the TikTok for Developers website.
### Install the SDK
#### Swift Package Manager
Add the library to your XCode project as a Swift Package:
- In XCode, click `File -> Add Packages...`
- Paste the repository URL: `https://github.com/tiktok/tiktok-opensdk-ios`
- [Select `Dependency Rule` -> `Up to Next Major Version` and input the major version you want (i.e. `2.``2``.0` You can find the latest release here](https://github.com/tiktok/tiktok-opensdk-ios/releases).)
- Select `Add to Project` -> Your project
- Click `Copy Dependency` and select the libraries you need (`TikTokOpenAuthSDK`, `TikTokOpenSDKCore`, `TikTokOpenShareSDK`)
#### Podfile
- Add the following to your Podfile:
```
pod 'TikTokOpenSDKCore'
pod 'TikTokOpenAuthSDK'
pod 'TikTokOpenShareSDK'
```
- Run `pod install --repo-update`.
### Configure your Xcode project
- Open your `Info.plist` file and add or update the following key-value pairs:
- Add the following values to `LSApplicationQueriesSchemes`:
- `tiktokopensdk` for Login Kit.
- `tiktoksharesdk` for Share Kit.
- `snssdk1233` and `snssdk1180` to check if TikTok is installed on your device.
- Add `TikTokClientKey` key with your app's client key, obtained from the TikTok for Developers website, as the value.
- Add your app's client key to `CFBundleURLSchemes`.
```
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>tiktokopensdk</string>
    <string>tiktoksharesdk</string>
    <string>snssdk1180</string>
    <string>snssdk1233</string>
</array>
<key>TikTokClientKey</key>
<string>$TikTokClientKey</string>
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>$TikTokClientKey</string>
    </array>
  </dict>
</array>
```
- Add the following code to your app's `AppDelegate`:
```
import TikTokOpenSDKCore

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ app: UIApplication,open url: URL, 
                     options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
        if (TikTokURLHandler.handleOpenURL(url)) {
            return true
        }
        return false
    }
    
    func application(_ application: UIApplication, 
                     continue userActivity: NSUserActivity, 
                     restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
        if (TikTokURLHandler.handleOpenURL(userActivity.webpageURL)) {
            return true
        }
        return false
    }

}
```
- If your application makes use of the `SceneDelegate`, you will need to add the following code to your `SceneDelegate` file.
```
import TikTokOpenSDKCore
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

    func scene(_ scene: UIScene, 
               openURLContexts URLContexts: Set<UIOpenURLContext>) {
        if (TikTokURLHandler.handleOpenURL(URLContexts.first?.url)) {
            return
        }
    }

}
```
Was this document helpful?


---
## SOURCE: Integration Essentials/Server API/Error Handling.md

Docs
# Error Handling
Starting with TikTok API 2.0, error responses include error codes represented as readable strings with detailed error messages and a log ID. When contacting TikTok support team, these details must be provided.
### Error Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| code | string | The error category in string |
| message | string | The detailed error description |
| log_id | string | The unique id associated with every request for debugging purporse |

### All Error Codes
The following list provides v2 error codes, their corresponding HTTP status codes, and a description of the error including guidance on how to handle the issue. Error codes are sorted alphabetically.

| **Error code** | **Description ** | **HTTP status code** |
| --- | --- | --- |
| access_token_invalid | The access token is invalid or not found in the request. Please refresh the token and retry. | 401 |
| internal_error | This is the generic error code for TikTok internal errors. _Please refer to the error message for details and notify TikTok support._ | 500 |
| invalid_file_upload | The uploaded file does not meet API specifications. Please correct the file and try again. | 400 |
| invalid_params | One or more fields in request is invalid. _Please refer to the error message for details._ | 400 |
| rate_limit_exceeded | The API rate limit was exceeded. Please try again later. | 429 |
| scope_not_authorized | The user did not authorize the scope required for completing this request. Please ask the user to authorize and then retry. | 401 |
| scope_permission_missed | Access token is invalid, some fields need additional scopes. _Please refer to the error message for more details._ | 400 |

## Error Example
```
{
   "code":"access_token_invalid",
   "message":"Access token is invalid, please refresh token and retry",
   "log_id":"20220829194722CBE87ED59D524E727021"
}
```
Was this document helpful?


---
## SOURCE: Integration Essentials/Server API/Server API.md

Docs
# Rate Limits on API Requests
TikTok API limits the number of requests you can send in a given timeframe. Limits for each API are set and enforced separately. Default limits are provided below.

| **API** | **Limit** |
| --- | --- |
| /v2/user/info/ | 600 |
| /v2/video/query/ | 600 |
| /v2/video/list/ | 600 |

Request rate calculation is based on a one minute sliding window. If the number of requests exceeds the threshold, new requests will be throttled and a response will be returned with HTTP status `429` and error code `rate_limit_exceeded`.
[If your application needs higher limits, please contact us using our Support Page](https://developers.tiktok.com/support/). We will review your request. If approved, rate limits will be increased.
Was this document helpful?


---
## SOURCE: Integration Essentials/Server API/OAuth/Client Access Token Management.md

Docs
# Client Access Token Management
[[Client access token is a type of access token that does not need user authorization. This is typically used by clients to access resources about themselves or a TikTok application, rather than to access a user's resources. The use cases are to access Research API](https://developers.tiktok.com/products/research-api/) and Commercial Content API](https://developers.tiktok.com/products/commercial-content-api/).
### Endpoint
_POST_ https://open.tiktokapis.com/v2/oauth/token/
### Headers

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | String | The unique identification key provisioned to the partner. |
| client_secret | String | The unique identification secret provisioned to the partner. |
| grant_type | String | Its value should always be set as `client_credentials`. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| access_token | String | The generated client access token. |
| expires_in | Int64 | The expiration for the `access_token`in seconds. **It****is valid for 2 hours after the initial issuance**. |
| token_type | String | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'grant_type=client_credentials'
```
If the request is successful, the response will look like the following:
```
{
    "access_token": "clt.example12345Example12345Example",
    "expires_in": 7200,
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following:
```
{
    "error": "invalid_request",
    "error_description": "Client secret is missed in request.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
[[At the time of this writing, this guide is applicable to Research API](https://developers.tiktok.com/doc/research-api-get-started) and Commercial Content API](https://developers.tiktok.com/doc/commercial-content-api-getting-started).
Was this document helpful?


---
## SOURCE: Integration Essentials/Server API/OAuth/Error Handling.md

Docs
# Error Handling
In the new generation of the TikTok Login Kit, OAuth error responses include an error code represented as readable strings with a detailed error message and log ID. When contacting the TikTok support team, these details must be provided.
### Error struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| error | String | The error category in string. |
| error_description | String | The detailed error description. |
| log_id | String | The unique ID associated with every request for debugging purposes. |

### Error categories
The `error` property can be one of the following values:

| **Error** | **Description ** |
| --- | --- |
| access_denied | The resource owner or authorization server denied the request. |
| invalid_client | Client authentication failed (for example, unknown client, no client authentication included, or unsupported authentication method). |
| invalid_grant | The provided authorization grant (for example, authorization code or resource owner credentials) or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client. |
| invalid_request | The request misses a required parameter or is otherwise malformed. |
| invalid_scope | The requested scope is invalid, unknown, or malformed. |
| unauthorized_client | The client is not authorized to request an authorization code using this method. |
| unsupported_grant_type | The authorization grant type is not supported by the authorization server. |
| unsupported_response_type | The authorization server does not support obtaining an authorization code using this method. |
| server_error | Other internal server errors. |
| temporarily_unavailable | Service is temporarily unavailable. |

Was this document helpful?


---
## SOURCE: Integration Essentials/Server API/OAuth/OAuth.md

Docs
# Endpoints
## 1. Fetch an access token using an authorization code
Once the authorization code callback is handled, you can use the code to retrieve the user's access token.
#### Endpoint
_POST_ https://open.tiktokapis.com/v2/oauth/token/
#### Headers

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

#### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| client_secret | string | The unique identification secret provisioned to the partner. |
| code | string | The authorization code from the web, iOS, Android or desktop authorization callback. The value should be **URL****decoded**. |
| grant_type | string | Its value should always be set as `authorization_code`. |
| redirect_uri | string | Its value must be the same as the `redirect_uri`used for requesting code. |
| code_verifier | string | **Required for mobile and desktop app only.**Code verifier is used to generate code challenge in PKCE authorization flow. |

#### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier. |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize. |
| access_token | string | The access token for future calls on behalf of the user. |
| expires_in | int64 | The expiration of `access_token`in seconds. It is valid for 24 hours after initial issuance. |
| refresh_token | string | The token to refresh `access_token`. It is valid for 365 days after the initial issuance. |
| refresh_expires_in | int64 | The expiration of `refresh_token`in seconds. |
| token_type | string | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
#### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'code=CODE' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'redirect_uri=REDIRECT_URI'
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "afd97af1-b87b-48b9-ac98-410aghda5344",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "Redirect_uri is not matched with the uri when requesting code.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## 2. Refresh an access token using a refresh token
Although the fetched `access_token` expires within 24 hours, it can be refreshed without user consent. The developer's back-end server can schedule background jobs to keep tokens up to date.
#### Endpoint
_POST_ https://open.tiktokapis.com/v2/oauth/token/
#### Headers

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

#### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| client_secret | string | The unique identification secret provisioned to the partner. |
| grant_type | string | Its value should always be set as `refresh_token`. |
| refresh_token | string | The user's refresh token. |

#### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The partner-facing user ID. |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize. |
| access_token | string | The new token for future calls on behalf of the user. |
| expires_in | int64 | The expiration of the access token in seconds. |
| refresh_token | string | The token to refresh a user's `access_token`. Note: The returned `refresh_token`may be different than the one passed in the payload. You must use the newly-returned token if the value is different than the previous one. |
| refresh_expires_in | int64 | The expiration for `refresh_token`in seconds. |
| token_type | string | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
#### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=REFRESH_TOKEN'
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "asdf-12345c-1a2s3d-ac98-asdf123as12as34",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## 3. Revoke access
When a user wants to disconnect your application from TikTok, you can revoke their tokens so the user will no longer see your application on the **Manage app permissions** page of the TikTok for Developers website.
#### Endpoint
_POST_ https://open.tiktokapis.com/v2/oauth/revoke/
#### Headers

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

#### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| client_secret | string | The unique identification secret provisioned to the partner. |
| token | string | The `access_token`that bears the authorization of the TikTok user. |

#### Response struct
If the request is successful, the response struct will be empty.
#### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/revoke/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'token=ACCESS_TOKEN'
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
Was this document helpful?


---
## SOURCE: Integration Essentials/Webhooks/Events.md

Docs
# Webhook Events
[Webhooks let you subscribe to events and receive notice when an event occurs. For more information about how to set up a webhook subscription, see Webhooks Overview](https://developers.tiktok.com/doc/webhooks-overview).
By default, you are subscribed to all events when a callback URL is configured in the TikTok Developer Portal.
## Webhook Structure
### Request Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | The unique identification key provisioned to the partner. |
| event | string | Event name. |
| create_time | int64 | The time in which the event occurred. UTC epoch time is in seconds. |
| user_openid | string | The TikTok user's unique identifier; obtained through `/oauth/access_token/`. |
| content | string | A serialized JSON string of event information. |

## Event types
### authorization.removed
Fired when the user's account deauthorized from your application.
The `access_token` for the user will have been already revoked when you receive the disconnect callback message. Developers can persist this information for clean-up purposes.

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| reason | int | 0 = Unknown 1 = User disconnects from TikTok app 2 = User's account got deleted 3 = User's age changed 4 = User's account got banned 5 = Developer revoke authorization |

#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "authorization.removed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content": "{\"reason\": 1 }"
}
```
### video.upload.failed
[Fired when the video uploaded from Video Kit](https://developers.tiktok.com/doc/web-video-kit-with-web) fails to upload in TikTok.
#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "video.upload.failed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content":"{\"share_id\":\"video.6974245311675353080.VDCxrcMJ\"}"
}
```
### video.publish.completed
[Fired when the video uploaded from Video Kit](https://developers.tiktok.com/doc/web-video-kit-with-web) has been published by the user in TikTok.
#### Example payload
```
{
    "client_key": "bwo2m45353a6k85",
    "event": "video.publish.completed",
    "create_time": 1615338610,
    "user_openid": "act.example12345Example12345Example",
    "content":"{\"share_id\":\"video.6974245311675353080.VDCxrcMJ\"}"
}
```
## portability.download.ready
[Fired when data requested via from the Data Portability API](https://developers.tiktok.com/products/data-portability-api/) is in the `downloading` state.
Example payload:
```
{
    "client_key": "developer_client_key",
    "event": "portability.download.ready",
    "create_time": 1615338610,
    "content":"{\"request_id\":123123123123123}"
}
```
Note: `content` is a JSON object marshalled as a string
```
{
    "request_id": 123123123123123
}
```
### Payload content

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API | 123123123123 |

Was this document helpful?


---
## SOURCE: Integration Essentials/Webhooks/Verification.md

Docs
# Check the signature
TikTok webhooks are sent with a signature the destination server can use to verify that the event came from TikTok and not a third party or malicious system. It is _strongly recommended_ that webhook consumers verify these signatures before processing each webhook event.
## Verify Message Signature
To protect your  app against man-in-the-middle and replay attacks, you should verify the signature of messages sent to your application. Since this timestamp is part of the signed payload, an attacker cannot change the timestamp without invalidating the signature. If the signature is valid but the timestamp is too old, you can have your application reject the payload.
The signature is included as `TikTok-Signature` in the header.
### Example of TikTok-Signature
```
"Tiktok-Signature": "t=1633174587,s=18494715036ac4416a1d0a673871a2edbcfc94d94bd88ccd2c5ec9b3425afe66"
```
### Signature Verification
#### Step 1: Extract the timestamp and signatures from the header
Split the header, using the `,` character as the separator, to get a list of elements. Next, split each element, using the `=` character as the separator, to get a prefix and value pair.
The value for the prefix `t` corresponds to the timestamp, and `s` corresponds to the signature.
#### Step 2: Signature Generation
`signed_payload` can be created by concatenating:
- The timestamp as a string
- The character `.`
- The actual JSON payload (request body)
An HMAC with the SHA256 hash function is computed with your `client_secret` as the key and your `signed_payload` string as the message.
#### Step 3: Signature Generation
Compare the signature in the header to the generated signature. In the case they are equal, compute the difference between the current timestamp and the received timestamp in the header. Use this to decide whether the difference is tolerable.
Was this document helpful?


---
## SOURCE: Integration Essentials/Webhooks/Webhooks.md

Docs
# TikTok Webhooks
## Overview
Webhook is a subscription that notifies your application via a callback URL when an event happens in TikTok. Rather than requiring you to pull information via API, you can use webhooks to get information on events that occur. Notifications are delivered via HTTPS POST in JSON format to the callback url configured for your app in the Developer Portal. This information can be used to update your system or to trigger business processes.
## Requirements and Limitations
In order to receive a webhook message, callback URL should be registered in the client application on TikTok Developer Portal. This callback url can be configured either during the initial application or after the client key has been provisioned by updating the application.
The callback URL must do the following:
- Immediately respond with a 200 HTTP status code to acknowledge the receipt of the event notification.
- The callback URL endpoint must require HTTPS.
If a 200 HTTP status code is not returned, TikTok assumes that the delivery was unsuccessful. TikTok retries the delivery of event notification for up to 72 hours using exponential backoff. After 72 hours, the notification is discarded and not sent again.
TikTok makes a best effort for "at least once delivery" of webhooks. Webhook endpoints might receive the same event more than once. There should be a guard against duplicated event receipts by making your event processing idempotent.
Was this document helpful?
