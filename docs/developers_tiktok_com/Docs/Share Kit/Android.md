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