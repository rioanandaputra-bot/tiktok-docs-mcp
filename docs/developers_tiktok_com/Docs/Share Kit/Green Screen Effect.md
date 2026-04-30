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