Docs
# Login Kit for Android
[This guide explains how to integrate with Login Kit for Android using Kotlin. Once authenticated users authorize your app, you can access their basic TikTok profile data, including their display name and avatar. Additional data access may require approval for additional scopes. Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
## Prerequisites
[Before proceeding, make sure you complete all of the steps in the Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart).
[Obtain the `client_key` and `client_secret` located in the **Credentials** section of your app page on the TikTok for Developers website](https://developers.tiktok.com/). Navigate to the **Products** section of your app page and click **Add products**. Then add **Login Kit**.
## Android integration
### Create an authorization request
- Create an instance of `AuthApi`.
- Create an `AuthRequest` instance and set the following required parameters:
- `clientKey = your_client_key`: Use the client key that you obtain on the TikTok for Developers website.
- `scope = ``user.info``.basic`: If you are approved for additional scopes, include them using a comma-separated list.
- `redirectUri = your_redirectUri`: Redirect URI determines how TikTok sends back the response to your app. The value must match one of the authorized redirect URIs that you provide for your Android Login Kit and follow an `https` scheme.
- `codeVerifier = your_codeverifier`: Generate a code verifier with `PKCEUtils`.
- Call the `authorize()` method on your instance of `AuthApi` .
```
// STEP 1: Create an instance of AuthApi
val authApi = AuthApi(
    activity = [your_activity]
)

// STEP 2: Create an AuthRequest and set parameters
val request = AuthRequest(
    clientKey = clientKey,
    scope = "user.info.basic",
    redirectUri = redirectUri, 
    codeVerifier = codeVerifier
)

// STEP 3: Invoke the authorize method
authApi.authorize(
    request = request,
    authMethod = AuthMethod.TikTokApp / AuthMethod.ChromeTab
);
```
After successful authorization, the user will be brought back to your app via the activity associated with `redirectUri`.
### Receive callbacks
```
// the actvity which will receive the authorization response from TikTok
<activity>
    ...
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        // Note that VIEW action, and DEFAULT & BROWSAbLE categories are necessary.
        <data android:scheme="your_redirect_uri_scheme" />
        <data android:host="your_redirect_uri_host"/>
    </intent-filter>
</activity>
```
Parse the AuthResponse from intent with `authApi.getAuthResponseFromIntent`. Refer to `MainActivity` in the `demo-auth` package as an example.
```

authApi.getAuthResponseFromIntent(intent, [your_redirect_uri])?.let { 
    val authCode = it.authCode // The auth code will be used to obtain access token
    val grantedPermissions = it.grantedPermissions // Granted scopes
            
    // Please refer to the Handling Errors for more detail.
    val authError = it.authError
    val authErrorDescription = it.authErrorDescription
    ...
}
```
### Obtain an access token
[Upload the `code` returned in the callback and your `code_verifier` to your server-side and obtain a user access token. See User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management) for more information.
### Handling errors
[See Error Handling](https://developers.tiktok.com/doc/oauth-error-handling) for more information.
Was this document helpful?