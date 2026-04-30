Docs
# Video Kit with Objective-C
[There is a new version of this SDK: Share Kit for iOS](https://developers.tiktok.com/doc/share-kit-ios-quickstart-v2)
## Introduction
Video Kit allows users to share videos and photos from your app to TikTok. Make sure your app has access to Photo Library.
Now we support long video sharing (> 1min) for up to 10 mins. Actual supported video duration may vary based on region.
## Preparation
[Before you start sharing, you need to complete all of the configurations listed in Getting Started](https://developers.tiktok.com/doc/getting-started-ios-quickstart-objective-c) with the TikTok SDK for iOS.
You can complete the sharing step by step：
### Step 1 : Import Header
Import TikTokOpenSDKShare.h
```
#import <TikTokOpenSDK/TikTokOpenSDKShare.h>
```
### Step 2 : Construct a Share Request
Construct a share request.
```
TikTokOpenPlatformShareRequest *req = [[TikTokOpenPlatformShareRequest alloc] init];
```
### Step 3 : Required Parameters
Set the shared resource type. Currently we support images and videos.
```
req.mediaType = TikTokOpenSDKShareMediaTypeImage;
//Or
req.mediaType = TikTokOpenSDKShareMediaTypeVideo;
```
---
Set share localIdentifiers as PHAsset.
e.g
```
NSMutableArray<NSString *> *mediaLocalIdentifiers = [NSMutableArray array];
for (PHAsset *asset in self.selectedAssets) {
    [mediaLocalIdentifiers addObject:asset.localIdentifier];
}
req.localIdentifiers = [mediaLocalIdentifiers copy];
```
Note:
- The aspect ratio of the images or videos should between: [1/2.2, 2.2]
- If mediaType is Image:
- The number of images should be more than one and up to 12.
- If mediaType is Video:
- Total video duration should be longer than 1 seconds.
- No more than 12 videos can be shared
- Videos with brand logo or watermark will lead to the videos being deleted or the respective accounts disabled. Make sure your application shares content without a watermark.
### Step 4 : Optional Parameters
**State**
You can customize a string to identify a share. The same state will be present in the respond.
You can bind you information with this ShareID.
```
req.state = @"a47e57c6c559acb88a9569da66ee5f65e0f779c9";
```
### Step 5 : Send Share Request
Call `-[``TikTokOpenSDKShareRequest`` sendShareRequestWithCompleteBlock:]` method to send the share request .
It will open the TikTok app and publish the content. Users can stay in TikTok or go back to your App after sharing.
If the user goes back to your app, you can receive a callback in CompleteBlock.
When any error happens, the response will have an error code with the following mapping:

| **TikTokOpenSDKErrorCode** | **errorCode** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKSuccess | 0 | Shared success. |
| TikTokOpenSDKErrorCodeCommon | -1 | Common error type e.g. network error. |
| TikTokOpenSDKErrorCodeUserCanceled | -2 | User Canceled share in TikTok. |
| TikTokOpenSDKErrorCodeSendFailed | -3 | User publish content failed. |
| TikTokOpenSDKErrorCodeAuthDenied | -4 | Auth denied. |
| TikTokOpenSDKErrorCodeUnsupported | -5 | Unsupported. |

If the error code does not make it easy for you to locate a specific error, you can use 'respond.shareState` for detail message. SDK version need 2.0.8 or higher.
The following map defines the Sharing state and specific issues.

| **TikTokOpenSDKShareRespState** | **value** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKShareRespStateSuccess | 20000 | Success. |
| TikTokOpenSDKShareRespStateUnknownError | 20001 | Unknown or current SDK version unclassified error. |
| TikTokOpenSDKShareRespStateParamValidError | 20002 | Params parsing error, media resource type difference you pass. |
| TikTokOpenSDKShareRespStateSharePermissionDenied | 20003 | Not enough permissions to operation. |
| TikTokOpenSDKShareRespStateUserNotLogin | 20004 | User not logged in. |
| TikTokOpenSDKShareRespStateNotHavePhotoLibraryPermission | 20005 | TikTok has no album permissions. |
| TikTokOpenSDKShareRespStateNetworkError | 20006 | TikTok Network error. |
| TikTokOpenSDKShareRespStateVideoTimeLimitError | 20007 | Video length doesn't meet requirements. |
| TikTokOpenSDKShareRespStatePhotoResolutionError | 20008 | Photo doesn't meet requirements. |
| TikTokOpenSDKShareRespTimeStampError | 20009 | Timestamp check failed. |
| TikTokOpenSDKShareRespStateHandleMediaError | 20010 | Processing photo resources failed. |
| TikTokOpenSDKShareRespStateVideoResolutionError | 20011 | Video resolution doesn't meet requirements. |
| TikTokOpenSDKShareRespStateVideoFormatError | 20012 | Video format is not supported. |
| TikTokOpenSDKShareRespStateCancel | 20013 | Sharing canceled. |
| TikTokOpenSDKShareRespStateHaveUploadingTask | 20014 | Another video is currently uploading. |
| TikTokOpenSDKShareRespStateSaveAsDraft | 20015 | Users store shared content for draft or user accounts are not allowed to post videos. |
| TikTokOpenSDKShareRespStatePublishFailed | 20016 | Post share content failed. |
| TikTokOpenSDKShareRespStateMediaInIcloudError | 21001 | Downloading from iCloud failed. |
| TikTokOpenSDKShareRespStateParamsParsingError | 21002 | Internal params parsing error. |
| TikTokOpenSDKShareRespStateGetMediaError | 21003 | Media resources do not exist. |

Was this document helpful?