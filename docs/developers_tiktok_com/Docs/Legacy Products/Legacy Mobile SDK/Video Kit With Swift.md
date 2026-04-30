Docs
# Video Kit with Swift
[There is a new version of this SDK: Share Kit for iOS](https://developers.tiktok.com/doc/share-kit-ios-quickstart-v2)
This guide explains how to integrate your app with Video Kit in Swift. Long videos with a duration of up to ten minutes can be shared. The allowed duration may vary based on the region.
## Preparation
[[You are required to configure your app on TikTok for Developers website](https://developers.tiktok.com/). See Getting Started with TikTok SDK for iOS](https://developers.tiktok.com/doc/getting-started-ios-quickstart-swift) for more information.
Your app must have access to the user's photo library to successfully share videos to TikTok.
## Create a Share Request
Import the TikTokOpenShareSDK module and create a share request, as shown in the code snippet below.
Your app object is required to maintain a strong reference to the request to successfully receive the response callback. You can discard it once you have handled the response.
Set the following fields in the share request object:
- `localIdentifiers`: List of media. Media can either be all videos or all images.
- `mediaType`: The type of media you want to share.
- `shareFormat`:  Refer to the Share Formats section in this guide.
```
import TikTokOpenShareSDK

let shareRequest = TikTokShareRequest()
shareRequest.localIdentifiers = [...]
shareRequest.mediaType = .video
shareRequest.shareFormat = .normal
shareRequest.send { response in
    let shareResponse = response as? TikTokShareResponse else { return }
}
```
## Share Formats
You can use the `shareFormat` field in the share request object to share images or videos to TikTok in different formats.
- `.normal`: The default share format. This format allows your app to share image(s) or video(s), as is, to TikTok.
- `.greenScreen`: The green screen format provides a seamless experience for users to apply a video or image directly to the background of the green screen effect. Green screen videos use one video or image as the background and the creator's figure is in the front.
- The green screen feature is supported only on TikTok version 25.0.0 and later.
- The `.greenScreen` field applies only when sharing a single video or single image. If multiple videos or images are shared, then the `shareFormat` field will be ignored.
- If the application of the green screen effect fails on the TikTok app, the user is prompted to continue with regular sharing.
**Note:**
- The aspect ratio of images or videos should be between: [1/2.2, 2.2]
- A maximum of 35 images can be shared.
- A maximum of 12 videos can be shared.
- [You must be authorized to use any TikTok brand logos and watermarks. See TikTok Brand and Use Guidelines](https://tiktokbrandbook.com/d/HhXfjVK1Poj9/legal) for more details.
## Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-ios-handling-errors) for more details.
Was this document helpful?