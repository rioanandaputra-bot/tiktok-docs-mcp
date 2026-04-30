Docs
# Manage User Access Tokens with OAuth v2
TikTok Login Kit manages the token life cycle, allowing you to integrate login and authentication flows directly in your application. A successful authorization flow grants you refreshable access tokens. Those tokens enable you to perform endpoint access with user permissions.
## Authorization scopes
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the rights to only agree to a subset of scopes you requested from them.
The following are some example scopes:
- **user.info****.basic** gives read-only access to a user's avatar and display name.
- **video.list** gives read-only access to a user's public TikTok videos.
[Learn more about scopes](https://developers.tiktok.com/doc/scopes-overview).
## Token security
Tokens must be handled with caution. It is recommended that you store and manage all tokens on the server side.
- Access token is a user authorization token that can be used to directly access user information in the TikTok ecosystem.
- Refresh token is used to renew the access token.
## Endpoints for web
[If you have already registered a redirect URI for your web app and use `https://www.tiktok.com/v2/auth/authorize/` to authorize, please refer to the new generation user access token management API guide](https://developers.tiktok.com/doc/oauth-user-access-token-management).
[[If you are an existing client, have not registered a redirect URI for your web app and use `https://www.tiktok.com/auth/authorize/` to authorize, please refer to the legacy user access token management API guide](https://developers.tiktok.com/doc/legacy-user-access-guide). To register a redirect URI, go to the Manage apps](https://developers.tiktok.com/apps/) page of the TikTok for Developers website and migrate to the new endpoints as soon as possible.
## Endpoints for mobile
[[[**Preferred: **If you are using the new Android](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart) or iOS](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart) TikTok OpenSDK, please refer to the new user access token management guide](https://developers.tiktok.com/doc/oauth-user-access-token-management).
[[[**Legacy: **If you are using the old Android](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart) or iOS](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart) TikTok OpenSDK, please refer to the legacy user access token management guide](https://developers.tiktok.com/doc/legacy-user-access-guide).
## Endpoints for desktop
[You must register a redirect URI for your desktop app and use `https://www.tiktok.com/v2/auth/authorize/` to authorize. Please refer to the new generation user access token management API guide](https://developers.tiktok.com/doc/oauth-user-access-token-management) to manage the user access token.
Was this document helpful?