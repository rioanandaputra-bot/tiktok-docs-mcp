# Share Kit

> Consolidated from 3 source files.



---
## SOURCE: Share Kit/Android.md

Docs
# Share Kit for Android
### Overview
Share Kit, part of our OpenSDK, enables third party apps to integrate directly with TikTok, providing creator's an ability to edit photos and videos in apps they love and seamlessly share content to TikTok. Using Share Kit and adding TikTok to your app's share sheet has these additional benefits:
- Ease of use in integrating with TikTok as we provide the boilerplate code in this guide. Seamless sharing straight from your app's sharesheet.
- Include your app's hashtag in content shared to TikTok. By engaging with the TikTok SDK, third party platforms will not only provide a new channel for their users to share their creations, but also expand the reach of their own platform through specified** partner hashtags**, as shown in the user journey below.
- We show a toast to creators to return to your app after sharing content to TikTok.
- [Third party apps can leverage creative effects such as sharing a single image or video as a green screen background](https://developers.tiktok.com/doc/green-screen-kit/).
This guide demonstrates how to enable sharing videos and images from your app to TikTok.
### Prerequisites
[Before sharing videos to TikTok from your app, you must complete all the steps in Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart).
[Obtain the `client_key` located in the **Appdetails** section of your app on the TikTok for Developers website](https://developers.tiktok.com/). Then add Share Kit to your app by navigating to the **Manage apps** page, and clicking **+ Add products**.
### Send a share request
- Create a `ShareApi` to send a share request.
- Build share content for images and videos into the `MediaContent` model.
- Create a `ShareRequest` object and set the required parameters. You can use the `shareFormat` field in the share request object to share images or videos with TikTok in different formats.
- `Format.DEFAULT`: The default share format. This format allows your app to share images or videos, as is, with TikTok.
- [`Format.GREEN_SCREEN`: See Green Screen](https://developers.tiktok.com/doc/green-screen-kit) for more details.
- Call the `Share()` method in `ShareApi` .
```
/* Step 1 */
shareApi = ShareApi(
    activity = [your_activity],
)

/* Step 2 */
val mediaContent = MediaContent(
    mediaType = if (isSharingImage) MediaType.IMAGE else MediaType.VIDEO, 
    mediaPaths = mediaUrls, // a list of selected media paths
)
// use Share.Format.GREEN_SCREEN for green screen share and Share.Format.DEFAULT for default share
val shareFormat = shareFormat = if (greenScreenEnabled) { 
    Format.GREEN_SCREEN
} else {
    Format.DEFAULT
}

/* Step 3 */
val request = ShareRequest(
    clientKey = clientKey,
    mediaContent = mediaContent,
    shareFormat = shareFormat,
    packageName = [package name of your activity which will receive share result intent from TikTok, e.g com.bytedance.sdk.demo.share],
    resultActivityFullPath = [full class path of your activity which will receive share result intent from TikTok, e.g com.bytedance.sdk.demo.share.ShareActivity]
)

/* Step 4 */
shareApi.share(request);
```
[[[If you want to share a file with the `file:///``Uri](https://developer.android.com/reference/android/net/Uri.html)` path, follow Android's FileProvider instruction](https://developer.android.com/reference/androidx/core/content/FileProvider) to create `content://``Uri](https://developer.android.com/reference/android/net/Uri.html)` for the file first, and then share it with TikTok.
Make sure you also grant TikTok access permission to your content Uri:
```
context.grantUriPermission("com.zhiliaoapp.musically", your_content_uri, 
    Intent.FLAG_GRANT_READ_URI_PERMISSION)
context.grantUriPermission("com.ss.android.ugc.trill", your_content_uri, 
    Intent.FLAG_GRANT_READ_URI_PERMISSION)
```
After a successful sharing session, a dialog will prompt the user to either go back to their app or stay in TikTok.
If you want to receive callbacks when users stay in TikTok, register to receive a broadcast.
```
public static final String ACTION_STAY_IN_TT = "com.aweme.opensdk.action.stay.in.dy";
```
### Receive callbacks
Provide the package name and the activity full path in the `ShareRequest` and then the response will be sent to your activity.
Make sure you have set `android:exported="true"` for your activity so that it can receive messages from sources outside its application.
```
<activity
    android:name="You activity which is gonna receive the sharing result intent from TikTok"
    ....
    android:exported="true">
</activity>
```
Parse `ShareResponse` from `intent` with `ShareApi.getShareResponseFromIntent`.
```
shareApi.getShareResponseFromIntent(intent)?.let { 
    val isSuccess = it.isSuccess
    val errorCode = it.errorCode
    val subErrorCode = it.subErrorCode
    val errorMsg = it.errorMsg
}
```
### Requirements for media
- For video sharing:
- The minimum video duration is 1 second.
- The maximum video duration is 360 seconds.
- The supported video media type is `.mp4`.
- The maximum frame size is 1100 px.
- For multi-videos, the maximum number of videos is 35.
- For image sharing:
- The number of images should be more than 1 and up to 35.
- For green screen sharing:
- The number of images and videos should only be 1.
- [You must be authorized to use any brand logos and watermarks. See TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal) for more details.
### Error handling
If you receive an error sharing response, refer to the table below for error handling and debugging.

| **Error Code** | **Sub****Error Code** | **Error Message** |
| --- | --- | --- |
| 0 | 0 | Success. |
| -1 | -1 | Unknown error. |
| -3 | 20002 | Parameters parsing error. |
| -3 | 10011 | App certificate does not match configurations。 |
| -4 | 20005 | TikTok has no album permissions. |
| -12 | 20006 | TikTok Network error. |
| -5 | 20008 | Photo doesn't meet requirements. |
| -5 | 20010 | Processing photo resources failed. |
| -5 | 20012 | Video format is not supported. |
| -2 | -2 | Sharing canceled. |
| -4 | 20016 | Users store shared content for draft or user accounts are not allowed to post videos. |
| -1 | -1 | Share Denied. |

If you don't want to integrate using the share kit for now, your app can also share to TikTok in another way.
# **Share with TikTok by using Intents**
[Developers can use Intent to share content with TikTok without using our Share Kit. However, using our Share Kit to share content provides additional benefits for our partners and their users with ease of use as mentioned above](#overview).
## **Overview**
This guide details how to enable sharing from your app to TikTok by using a intents. TikTok supports sharing video, multi-video and multi-image currently.
## **Sharing on Android**
For all types of sharing, create an intent to send simple data to TikTok:
- Set `Intent.ACTION_SEND`/`ACTION_SEND_MULTIPLE` for Intent's action.
- Set the appropriate MIME type. For example `image/*` for sharing images and `video/mp4` for sharing video.
- Place a URI / a list of URIs pointing to the content in the extra `EXTRA_STREAM`.
Here is the example for sharing single-video:
```
val intent = Intent()
intent.action = Intent.ACTION_SEND
intent.putExtra(Intent.EXTRA_STREAM, uriToImage)
intent.type = "video/*"
yourActivity.startActivityForResult(intent, resultCode)
```
Sharing multi-image:
```
val imageUris = mutableListOf<Uri>()
imageUris.add(imageUri1) // Add your image URIs here
imageUris.add(imageUri2)
...

val intent = Intent()
intent.action = Intent.ACTION_SEND_MULTIPLE
intent.putExtra(Intent.EXTRA_STREAM, imageUris)
intent.type = "image/*"
shareIntent.setType("image/*")
yourActivity.startActivityForResult(intent, resultCode)
```
- Note: When sharing multi-image with TikTok, TikTok will make a slideshow.
Sharing multi-video:
```
val videoUris = mutableListOf<Uri>()
videoUris.add(videoUri1) // Add your video URIs here
videoUris.add(videoUri2)
...

val intent = Intent()
intent.action = Intent.ACTION_SEND_MULTIPLE
intent.putExtra(Intent.EXTRA_STREAM, videoUris)
shareIntent.setType("video/mp4")
yourActivity.startActivityForResult(intent, resultCode)
```
- Note: When sharing multi-video with TikTok, TikTok will stitch into a long video. Users can edit the long video in TikTok.
If your shared images or videos are stored in internal storage of your app, then other apps can not access your files. When you want to share files with TikTok, you should grant permissions for these files by calling
`intent.flag = Intent.FLAG_GRANT_READ_URI_PERMISSION`
## **PackageName for TikTok**
If you don't want to call Intent.createChooser(). You can set packageName to share directly to TikTok.
```
String TIKTOK_M_PACKAGE = "com.zhiliaoapp.musically";
String TIKTOK_T_PACKAGE = "com.ss.android.ugc.trill";
...//set packagename

shareIntent.setPackage(TikTokConstant.Share.TIKTOK_M_PACKAGE);
shareIntent.setPackage(TikTokConstant.Share.TIKTOK_T_PACKAGE);
```
Was this document helpful?


---
## SOURCE: Share Kit/Green Screen Effect.md

Docs
# Overview
TikTok OpenSDK now provides a seamless experience for your users to share content from your app as a green screen background using TikTok's famous green-screen effect. The green-screen effect lets users record a video with an image or video in the background and the creator's face in the forefront. Previously, creators would need to go through many steps to apply a green screen background with content from your app, but with the new release of our OpenSDK, your app can accomplish this by configuring a single field on our share request.
# iOS
### Prerequisites
[Before proceeding, make sure you complete all of the steps in the iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart).
### Green Screen Usage
To enable this feature, we provided a new field, `shareFormat`, in the share request object. To share content as a green screen background, set `shareFormat` equal to `.greenScreen`. If `shareFormat` is not set, it will be `.normal` by default.
- Import the `TikTokOpenShareSDK` module and create a share request, as shown in the code snippet below. In the share request object, set the following parameters:
- `localIdentifiers`: List of media. Media can either be all videos or all images.
- `mediaType`: The type of media you want to share.
- `redirectURI`: Universal link that's used to callback to your application
- On the share request, set the `shareFormat` equal to `.greenScreen`.
- Start the share request by calling the `send(_:)` method on the share request object.
- After the user finishes sharing, you will receive a response callback in the closure. In the share response object, you can find whether the share succeeded or failed.
```
/* Step 1 */
import TikTokOpenShareSDK
let shareRequest = TikTokShareRequest(localIdentifiers: [...], // Must be single video
                                           mediaType: .video, 
                                           redirectURI: "https://www.example.com/path")
/* Step 2 */
shareRequest.shareFormat = .greenScreen 
/* Step 3 */
shareRequest.send { response in
    /* Step 4 */
    let shareResponse = response as? TikTokShareResponse else { return }
    if shareResponse.errorCode == .noError {
        print("Share succeeded!")
    } else {
        print("Share Failed! 
               Error Code: \(shareResponse.errorCode.rawValue) 
               Error Message: \(shareResponse.errorMessage ?? "") 
               Share State: \(shareResponse.shareState)")
    }
}
```
Note that:
- This only applies to single video or image sharing. If multiple videos or images are shared, this field is ignored.
- For videos, an extra step is presented to users to trim the shared video if needed before the recording. This is the same experience we have when the Green Screen effect is used with a video background.
- If TikTok fails to apply the Green Screen effect, we'll present a dialog for users to continue with regular sharing.
# Android
### Prerequisites
[Before proceeding, make sure you complete all of the steps in the Android Quickstart](https://developers.tiktok.com/doc/mobile-sdk-android-quickstart).
### Green Screen Usage
To enable this feature, we provided a new field, `shareFormat`, in the share request. By default, it will be the regular video or image sharing we had previously. If the Green Screen enum value (`GR``EEN_SCREEN` on Android) is provided for single video or image sharing, TikTok will try to apply the Green Screen effect automatically and use the shared video or image as the Green Screen background. Your users can start recording the video seamlessly.
- Create a `ShareApi` to send a share request.
- Build share content for images and videos into the `MediaContent` model.
- Create a `ShareRequest` object and set the required parameters with `shareFormat` equal to `Format.GREEN_SCREEN`.
- Call the `Share()` method in `ShareApi`.
```
/* Step 1 */
shareApi = ShareApi(
    activity = [your_activity],
)

/* Step 2 */
val mediaContent = MediaContent(
    mediaType = if (isSharingImage) MediaType.IMAGE else MediaType.VIDEO, 
    mediaPaths = mediaUrls, // a list of selected media paths
)

/* Step 3 */
val request = ShareRequest(
    clientKey = clientKey,
    mediaContent = mediaContent,
    shareFormat = Format.GREEN_SCREEN,
    packageName = [package name of your activity which will recive share result intent from TikTok, e.g com.bytedance.sdk.demo.share],
    resultActivityFullPath = [full class path of your activity which will recive share result intent from TikTok, e.g com.bytedance.sdk.demo.share.ShareActivity]
)

/* Step 4 */
shareApi.share(request);
```
[See the **Receive callbacks** section in Share Kit for Android](https://developers.tiktok.com/doc/share-kit-android-quickstart-v2) to handle share responses
Note that:
- This only applies to single video or image sharing. If multiple videos or images are shared, this field is ignored.
- For videos, an extra step is presented to users to trim the shared video if needed before the recording. This is the same experience we have when the Green Screen effect is used with a video background.
- If TikTok fails to apply the Green Screen effect, we'll present a dialog for users to continue with regular sharing.
Was this document helpful?


---
## SOURCE: Share Kit/Share Kit.md

Docs
# Share Kit for iOS
This guide explains how to integrate your app with Share Kit. Long videos with a duration of up to ten minutes can be shared. The allowed duration may vary based on the region.
## Prerequisites
[Before proceeding, you must complete all the steps in iOS Quickstart](https://developers.tiktok.com/doc/mobile-sdk-ios-quickstart).
[Obtain the `client_key` located in the **App** **details** section of your app on the TikTok for Developers website](https://developers.tiktok.com/). Then add Share Kit to your app by navigating to the **Manage apps** page, and clicking **+ Add products**.
Your app must have access to the user's photo library to successfully share videos to TikTok.
## Create a share request and handle responses
For the following steps, your app is required to maintain a strong reference to the request to receive the response callback. You can discard it once you have handled the response.
- Import the `TikTokOpenShareSDK` module and create a share request, as shown in the code snippet below. In the share request object, set the following parameters:
- `localIdentifiers`: List of media. Media can either be all videos or all images.
- `mediaType`: The type of media you want to share.
- `redirectURI`: Universal link that's used to callback to your application
- Start the share by calling the `send(_:)` method on the share request object.
- After the user finishes sharing, you will receive a response callback in the closure. In the share response object, you can find whether the share succeeded or failed.
```
/* Step 1 */
import TikTokOpenShareSDK

let shareRequest = TikTokShareRequest(localIdentifiers: [...], 
                                      mediaType: .video, 
                                      redirectURI: "https://www.example.com/path")
/* Step 2 */
shareRequest.send { response in
    /* Step 3 */
    let shareResponse = response as? TikTokShareResponse else { return }
    if shareResponse.errorCode == .noError {
        print("Share succeeded!")
    } else {
        print("Share Failed! 
               Error Code: \(shareResponse.errorCode.rawValue) 
               Error Message: \(shareResponse.errorMessage ?? "") 
               Share State: \(shareResponse.shareState)")
    }
}
```
Alternatively, you can pass in a `nil` completion handler to the share request and create a `TikTokShareResponse` directly from the URL sent back by TikTok in the `application(_:continue:restorationHandler:)` AppDelegate function. In this case, you do not have to maintain a strong reference to the authorization request.
After a successful sharing session, a dialog will prompt the user to either go back to their app or stay in TikTok.
## Share formats
You can use the `shareFormat` field in the share request object to share images or videos to TikTok in different formats. If `shareFormat` is not set, it will be `.normal` by default
- `.normal`: The default share format. This format allows your app to share images or videos, as is, to TikTok.
- [`.greenScreen`: See Green Screen](https://developers.tiktok.com/doc/green-screen-kit) for more details.
---
Note:
- The aspect ratio of images or videos should be between 1/2.2 and 2.2.
- A maximum of 35 images can be shared.
- A maximum of 12 videos can be shared.
- [You must be authorized to use any TikTok brand logos and watermarks. See TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal) for more details.
## Handling errors
When an error occurs, the response will have an error code with the following mapping:

| **Error Code** | **Description** |
| --- | --- |
| 0 | Shared success. |
| -1 | Common error type e.g. network error. |
| -2 | User Canceled share in TikTok. |
| -3 | User publish content failed. |
| -4 | Share denied. |
| -5 | Unsupported. |

Below is a mapping of the `shareState` which provides a more detailed explanation of the error:

| **Share state** | **Description** |
| --- | --- |
| 20000 | Success. |
| 20001 | Unknown or current SDK version unclassified error. |
| 20002 | Params parsing error. |
| 20003 | Permission not granted |
| 20004 | User not logged in. |
| 20005 | TikTok has no album permissions. |
| 20006 | TikTok Network error. |
| 20007 | Video length doesn't meet requirements. |
| 20008 | Photo doesn't meet requirements. |
| 20009 | Time stamp check failed. |
| 20010 | Processing photo resources failed. |
| 20011 | Video resolution doesn't meet requirements. |
| 20012 | Video format is not supported. |
| 20013 | Sharing canceled. |
| 20014 | Another video is currently uploading. |
| 20015 | User saved the shared content as a draft |
| 20016 | Posting failed |
| 21001 | Downloading from iCloud failed. |
| 21002 | Internal params parsing error. |
| 21003 | Media resources do not exist. |

Was this document helpful?
