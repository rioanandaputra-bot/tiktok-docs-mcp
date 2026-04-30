Docs
# Login Kit for iOS
This guide explains how to integrate your app with Login Kit for iOS. After successful user authentication with TikTok, your app can access basic user data, such as display name and avatar. Access to additional user data requires approval from TikTok for Developers website.
## Prerequisites
[Before proceeding, make sure you complete all of the steps in the iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart).
[Obtain the `client_key` and `client_secret` located in the **Credentials** section of your app page on the TikTok for Developers website](https://developers.tiktok.com/). Navigate to the **Products** section of your app page and click **Add products**. Then add **Login Kit**.
[[You must also register a redirect URI on the TikTok for Developers website. This redirect URI is used to verify your application, as well as to callback to your application with an authorization response. This redirect URI must be a universal link](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc) with an `https` scheme and your app must support associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains?language=objc).
## iOS integration
### Create an authorization request and handle responses
For the following steps, your app is required to maintain a strong reference to the request to receive the response callback. You can discard it once you have handled the response.
- Import the `TikTokOpenAuthSDK` module and create an authorization request, as shown in the code snippet below. In the authorization request init method, set the following parameters.
- `scopes`: The set of scopes you are requesting from the user.
- `redirectURI`: Universal link that's used to callback to your application
- Start the login by calling the `send(_:)` method on the authorization request object.
- After the user finishes authorizing, you will receive a response callback in the closure. In the authorization response object, you can find whether the authorization request succeeded or failed.
```
/* Step 1 */
import TikTokOpenAuthSDK

let authRequest = TikTokAuthRequest(scopes: ["user.info.basic",...], 
                                    redirectURI: "https://www.example.com/path")
/* Step 2 */
authRequest.send { response in
    /* Step 3 */
    let authResponse = response as? TikTokAuthResponse else { return }
    if authResponse.errorCode == .noError {
        print("Auth code: \(authResponse.code)")
    } else {
        print("Authorization Failed! 
              Error: \(authResponse.error ?? "") 
              Error Description: \(authResponse.errorDescription ?? "")")
    }
}
```
Alternatively, you can pass in a `nil` completion handler to the authorization request and create a `TikTokAuthResponse` directly from the URL sent back by TikTok in the `application(_:continue:restorationHandler:)` AppDelegate function. In this case, you do not have to maintain a strong reference to the authorization request.
### Obtain an access token
[Upload the `TikTokAuthResponse.code` returned in the callback and the `TikTokAuthRequest.pkce.codeVerifier` to your server-side and obtain a user access token. See User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management) for more information.
### Handling errors
[See Error Handling](https://developers.tiktok.com/doc/oauth-error-handling) for more information.
Was this document helpful?