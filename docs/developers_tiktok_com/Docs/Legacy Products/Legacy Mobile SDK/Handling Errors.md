Docs
# Handling iOS Errors
When any error happens, the response will have an error code with the following mapping:

| **TikTokShareResponseErrorCode** | **Error Code** |
| --- | --- |
| Success | 0 |
| Common Error | -1 |
| User Canceled | -2 |
| Share failed | -3 |
| Share denied | -4 |
| Unsupported | -5 |

If the error code does not make it easy for you to locate a specific error, you can use 'respond.shareState` for detail message. SDK version need 2.0.8 or higher.
The following map defines the Sharing state and specific issues.

| **TikTokOpenSDKShareRespState** | **value** | **Description** |
| --- | --- | --- |
| TikTokOpenSDKShareRespStateSuccess | 20000 | Success. |
| TikTokOpenSDKShareRespStateUnknownError | 20001 | Unknown or current SDK version unclassified error. |
| TikTokOpenSDKShareRespStateParamValidError | 20002 | Params parsing error. |
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