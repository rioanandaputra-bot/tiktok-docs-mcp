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