Docs
# Scopes Overview
Scopes represent end user granted permissions to access specific data resources or perform specific actions. Every TikTok for Developer API requires a scope to be accessed, and sensitive fields are protected by additional scopes. For example, the scope `user.info``.basic` allows access to APIs and data related to the basic user of a TikTok user.
## Managing scopes
Scopes are available on your app page. The scope `user.info``.basic` will be added by default for all apps with Login Kit. Developers can also request additional scopes and manage existing scopes on their app page after logging in.
To add scopes to your app, do the following:
- Navigate to the section titled **Scopes** to view your scopes.
- Click the **Add Scopes **button, then add your desired scopes.
To remove a scope, click the minus button next to it.
Note: Remember that applying and being approved for a scope alone does not give you access to a user's data. Each user must also authorize your app for access to specific scopes.
## User authorization
[[[[After you are approved for certain scopes on TikTok for Developers, users will be asked to authorize and confirm your access. This is explained further in the tutorials for Login Kit on iOS](https://developers.tiktok.com/doc/login-kit-ios-login-kit-with-objective-c), Android](https://developers.tiktok.com/doc/login-kit-android), Desktop](https://developers.tiktok.com/doc/login-kit-desktop), and Web](https://developers.tiktok.com/doc/login-kit-web). Users can grant or deny the requested scopes or any subset of them, and revoke the authorization at any time on their TikTok apps.
After a user grants the requested scopes, a code will be sent to your registered callback URL. You can obtain an `access_token` and start invoking TikTok for Developers APIs to get that user's information or perform actions on the user's behalf.
[See how to manage user access tokens](https://developers.tiktok.com/doc/login-kit-manage-user-access-tokens) for `access_token` related endpoints.
## Scopes Reference
[You can find the list of available scopes and their explanation on the scopes reference page](https://developers.tiktok.com/doc/tiktok-api-scopes).
Was this document helpful?