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