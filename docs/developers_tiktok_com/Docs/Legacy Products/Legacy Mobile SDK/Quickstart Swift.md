Docs
# iOS Quickstart Swift
[There is a new version of this SDK: iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart)
Integrating our open SDK can help you leverage TikTok's open platform capabilities, such as Login Kit, Sound Kit, sharing videos to TikTok, and more coming soon. We hope to help you enhance your app's discovery and engagement, as well as provide another location for your users to share their favorite content for the world to see.
## Getting Started with the TikTok SDK for iOS
### Requirements
TikTok iOS SDK requires iOS 9.3 and Xcode 4.5 or later.
### Step 1: Configure TikTok App Settings for iOS
Go to TikTok Developer App Registration Page to create your app. After approval, you will get the Client Key and Client Secret.
### Step 2: Install the SDK
#### Via Cocoapods (Recommend)
Add the pod to your Podfile:
```
pod 'TikTokOpenSDK', '~> 5.0.15'
```
And then run:
```
pod install --repo-update
```
#### Via Manual Install
[Download TikTokOpenSDK](https://sf16-sg.tiktokcdn.com/obj/tiktok-open-platform-sg/TikTokOpenSDK.xcframework-5.0.15.zip), unzip the zip files, and you would find the SDKs called TikTokOpenSDK.framework.
Link Framework
- **Copy** or **Drag** the SDKs into your Xcode Project.
Select your Project in Project Navigator. Click "+" in `TARGETS -> Build Phases -> Link Binary With Libraries`, and then select `TikTokOpenSDK.``xc``framework` in your Project folder to add it.
- Add `WebKit.framework` and `Security.framework`.
- `WebKit.framework` - It is used to gain authorization through web-view when TikTok is not installed.
- `Security.framework` - Encryption and decryption library. We use this framework to ensure that communications are securely transmitted.
- Add Link Flag `-ObjC` in `TARGETS->Build Settings->Other Linker Flags`. Make sure the letter 'O' and 'C' are capitalized.
The correct configuration is shown below:
### Step 3: Configure Xcode Project
#### Configure Info.plist
- In Xcode, right-click your project's Info.plist file and select Open As -> Source Code.
- Here are 3 keys need to configuration:
- **LSApplicationQueriesSchemes: Use to Open TikTop App**
- **TikTokAppID: Use to config TikTok OpenSDK**
- **CFBundleURLTypes : Use TikTok App callback your App**
Insert the following XML snippet into the body of your file just before the final `</dict>` element.
```
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>tiktokopensdk</string>
    <string>tiktoksharesdk</string>
    <string>snssdk1180</string>
    <string>snssdk1233</string>
</array>
<key>TikTokAppID</key>
<string>$TikTokAppID</string>
<key>CFBundleURLTypes</key>
<array>
  <dict>
    <key>CFBundleURLSchemes</key>
    <array>
      <string>$TikTokAppID</string>
    </array>
  </dict>
</array>
```
- Replace `$TikTokAppID` with your **App's Client Key**
Note:
- `tiktokopensdk` is used for logging in.
- `tiktoksharesdk` is used for sharing.
- `snssdk1233`, `snssdk1180` are used to check if the TikTok application is installed.
- The TikTok Open SDK auto-registers your Client Key when your App launches.
#### Make sure your app has access to Photo Library
Sharing pictures requires Photo Library access. Make sure a proper Privacy - Photo Library Usage Description is added in your Info.plist.
After the configuration, your Info.plist will look like the following.
### Step 4: Connect App delegate
You need to connect your `AppDelegate` class to the `TikTokOpenSDKApplicationDelegate.h` To do this, add the following code to your `AppDelegate.m` or `AppDelegate.swift` file.
```
import TikTokOpenSDK
@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
       TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, didFinishLaunchingWithOptions: launchOptions)
       return true
    }

    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {

        guard let sourceApplication = options[UIApplication.OpenURLOptionsKey.sourceApplication] as? String,
              let annotation = options[UIApplication.OpenURLOptionsKey.annotation] else {
            return false
        }

        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(app, open: url, sourceApplication: sourceApplication, annotation: annotation) {
            return true
        }
        return false
    }

    func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, open: url, sourceApplication: sourceApplication, annotation: annotation) {
            return true
        }
        return false
    }

    func application(_ application: UIApplication, handleOpen url: URL) -> Bool {
        if TikTokOpenSDKApplicationDelegate.sharedInstance().application(application, open: url, sourceApplication: nil, annotation: "") {
            return true
        }
        return false
    }
}
```
If your application does not have a `SceneDelegate`, you are good to go! If your application makes use of the `SceneDelegate`, you will need to add the following function to your `SceneDelegate` file.
```
class SceneDelegate: UIResponder, UIWindowSceneDelegate {

  func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
      guard let url = URLContexts.first?.url else {
          return
      }
      if let appDelegate = UIApplication.shared.delegate as? AppDelegate {
          _ = appDelegate.application(UIApplication.shared, open: url, options: [:])
      }
  }

}
```
#### API Instructions
**TikTokOpenSDKApplicationDelegate**
Log Delegate
```
protocol TikTokOpenSDKLogDelegate {
    func onLog(_ logInfo: String) { }
}
```
TikTok internal log in level ERROR or Warning will callback in this method. You need to register log delegate in TikTokOpenSDKApplicationDelegate
Usage:
```
TikTokOpenSDKApplicationDelegate.sharedInstance().logDelegate = self
```
Check TikTok is installed:
```
func isAppInstalled() -> Bool
```
**BDOpenPlatformObjects**
The definition of basic classes (Request or Response) to SDK.
Was this document helpful?