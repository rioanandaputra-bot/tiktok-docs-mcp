Docs
[There is a new version of this SDK: Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart)
# Android Quickstart
Integrating our open SDK can help you leverage TikTok's open platform capabilities, such as Login Kit, Sound Kit, sharing videos to TikTok, and more coming soon. We hope to help you enhance your app's discovery and engagement, as well as provide another location for your users to share their favorite content for the world to see.
## Getting started
Below is a quick start for you to apply the TikTok SDK to your application. You should confirm that your project has a **Minimum ****API**** level of 16: Android 4.1 (Jelly Bean)** or higher.
### Step 1: Configure TikTok App Settings for Android
Use the Developer Portal to apply for Android client_key and client_secret access. Upon application approval, the Developer Portal will provide access to these keys.
### Step 2: Install the SDK and Setup Android Project
- In Project window, switch to "Android" view tab and open Gradle Scripts > build.gradle (Project). Then add the following repository in the repositories{} section. For example:
```
repositories {
    maven { url "https://artifact.bytedance.com/repository/AwemeOpenSDK" }
}
```
- Open Gradle Scripts > build.gradle (Module: app) and add the following implementation statement to the dependencies{} section:
```
dependencies {
    implementation 'com.bytedance.ies.ugc.aweme:opensdk-oversea-external:0.2.1.2'
}
```
- Edit your Application
First you need to initialize `TikTokOpenApiFactory` by using client key in your custom Application.
```
@Override
public void onCreate() {
    super.onCreate();
    String clientKey = "[CLIENT_KEY]";
    TikTokOpenConfig tiktokOpenConfig = new TikTokOpenConfig(clientKey);
    TikTokOpenApiFactory.init(new TikTokOpenConfig(tiktokOpenConfig));
}
```
- Edit Your Manifest
- Open the **/app/manifest/AndroidManifest.xml** file.
- Register `TikTokEntryActivity` for receiving callbacks in Manifest. If you have customized an activity to receive callbacks, you may skip this step.
```
// If you have customized activity to receive callbacks, you can skip the step
<activity
    android:name=".tiktokapi.TikTokEntryActivity"
    android:exported="true">
</activity>
```
Note:
- Due to changes in Android 11 regarding package visibility, when impementing Tiktok SDK for devices targeting Android 11 and higher, add the following to the Android Manifest file:
```
<queries>
    <package android:name="com.zhiliaoapp.musically" />
    <package android:name="com.ss.android.ugc.trill" />
</queries>
```
- Excellent! Now, **sync** your project and get the latest version of SDK package.
At this point, you should already set up the basic development environment. Next please refer to the feature access doc for further integrating.
Was this document helpful?