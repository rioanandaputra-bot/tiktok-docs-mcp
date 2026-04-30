Docs
# Login Kit with Objective-C
[There is a new version of this SDK: Login Kit for iOS](https://developers.tiktok.com/doc/login-kit-ios-quickstart)
### Overview
[This guide explains how to integrate with Login Kit for iOS using Objective-C. Once authenticated users authorize your app, you can access their basic TikTok profile data including their display name and avatar. Additional data access may require approval for additional Scopes. Learn more on Scopes Overview](https://developers.tiktok.com/doc/scopes-overview).
### Prerequisites
[[Obtain a client key and client secret by logging in to Developer Portal](https://developers.tiktok.com/apps/) and selecting your app. Refer to the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-ios-quickstart-objective-c) for detailed steps.
### iOS Integration
#### Authorization Request
- Create a `TikTokOpenSDKAuthRequest` and set `permissions` equal to the set of scopes you are requesting from the user. For example, `user.info``.basic,video.list`.
- Send the authorization request.
- If user authorization was successful, a `code` will be provided in the response.
- [Upload this `code` to your server-side and obtain a user access token. See Manage User Access Tokens](https://developers.tiktok.com/doc/legacy-user-access-guide) for more information.
These steps are demonstrated in the following code snippet:
```
#import <TikTokOpenSDK/TikTokOpenSDKAuth.h>

/* STEP 1: Create the request and set permissions */
NSArray *scopes = @"user.info.basic,video.list"; // list your scopes;
NSOrderedSet *scopesSet = [NSOrderedSet orderedSetWithArray:scopes];
TikTokOpenSDKAuthRequest *request = [[TikTokOpenSDKAuthRequest alloc] init];
request.permissions = scopesSet;

/* STEP 2: Send the request */
__weak typeof(self) ws = self;
[request sendAuthRequestViewController:self
                completion:^(TikTokOpenSDKAuthResponse *_Nonnull resp) {
    __strong typeof(ws) sf = ws;

    /* STEP 3: Parse and handle the response */
    if (resp.errCode == 0) {
        NSString *responseCode = resp.code;
        // Upload response code to your server and obtain user access token
        ... 
    } else {
        // User authorization failed. Handle errors
    }
}];
```
#### Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-ios-handling-errors) for error handling and debugging.
Was this document helpful?