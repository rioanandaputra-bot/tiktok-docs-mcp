Docs
[There is a new version of this SDK: Share Kit for Android](https://developers.tiktok.com/doc/share-kit-android-quickstart-v2)
# Video Kit with Android
### Overview
This guide details how to enable sharing from your app to TikTok. After sharing successfully to TikTok, users will see your app's name in TikTok feed.
Note: The minimum TikTok version supporting sharing is 11.3.0.
Now we support long video sharing (> 1min) for up to 10 mins. Actual supported video duration may vary based on region.
### Prerequisites
Before you can share to TikTok from your App, make sure you have obtained a Client Key from TikTok and installed the TikTok SDK to your Android project. For details on these requirements, see Getting started.
[We recommend that developers targeting Android 7.0 and above use FileProvider to share. For more details, please refer to the document](https://developers.tiktok.com/doc/video-kit-android-android-fileprovider).
### Detailed Steps
[Follow the steps mentioned in the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-android-quickstart)
#### Send Share Request
- Create a `TiktokOpenApi` to send share request.
- Build share content for images/videos into the `TikTokMediaContent` model.
- Create Share.Request instance and set required parameters: `request.mMediaContent = [TikTokMediaContent]`.
- Call method `Share()` in `TiktokOpenApi` .
```
// 1.create TiktokOpenApi
TiktokOpenApi tiktokOpenApi= TikTokOpenApiFactory.create(this);

Share.Request request = new Share.Request();
// initialize the resource path, please provide absolute path
ArrayList<String> mUri = new ArrayList<>();
mUri.add ...

// 2.build share content for photos/videos into TikTokMediaContent
VideoObject videoObject = new VideoObject();
videoObject.mVideoPaths = mUri;
MediaContent content = new MediaContent();
content.mMediaObject = videoObject;

// 3.set required parameters
request.mMediaContent = content;

// or share multi-picture，here the size of mUri must >=2
ImageObject imageObject = new ImageObject();
imageObject.mImagePaths = mUri;
MediaContent mediaContent = new MediaContent();
mediaContent.mMediaObject = imageObject;
request.mMediaContent = mediaContent;


// 4.start share
tiktokOpenApi.share(request);
```
After a successful sharing session, a Dialog will prompt for the user to choose `Back to your App` or `Stay in TikTok`.
If you want to receive callbacks when people stay in TikTok , please register to receive a broadcast :
```
public static final String ACTION_STAY_IN_TT = "com.aweme.opensdk.action.stay.in.dy";
```
**Parameters in Share.Request**

| **Parameter** | **Usage** |
| --- | --- |
| mMediaContent | You can build share content for videos or photos using following models: 1. multi-Image: see `ImageObject`model. Note: The size of Images must be > 1 and <= 12. 2. single-video\multi-video: see `VideoObject`model. Then assign required parameter as `request.mMediaContent = [MediaContent]`; |
| callerLocalEntry | Set customized callback Activity by using `request.callerLocalEntry = "com.xxx.xxx...activity";`If this parameter is not set, TikTok will callback `TikTokEntryActivity`in default. |

#### Receive Callbacks
We provides two ways for you to receive the callback data from TikTok.
- Create new activity named "TikTokEntryActivity" in your app and implement TikTokApiEventHandler interface.
**Note**: The path of the activity should be your "package name" + .tiktokapi.TikTokEntryActivity. For example, "com.tiktok.opensdk.tiktokapi.TikTokEntryActivity".
The following example shows how to use TikTokEntryActivity to receive the callback data.
```
class TikTokEntryActivity extends Activity implements IApiEventHandler {

   TiktokOpenApi ttOpenApi;
   @Override
   public void onCreate(@Nullable Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       ttOpenApi= TikTokOpenApiFactory.create(this);
       ttOpenApi.handleIntent(getIntent(),this); // receive and parse callback
   }
   @Override
   public void onReq(BaseReq req) {
   }
   @Override
   public void onResp(BaseResp resp) {
       if (resp.getType() == TikTokConstants.ModeType.SHARE_CONTENT_TO_TT_RESP)  {
           Share.Response response = (Share.Response) resp;
           Toast.makeText(this, " code：" + response.errorCode + " errorMessage：" + response.errorMsg, Toast.LENGTH_SHORT).show();
       }
   }
   @Override
   public void onErrorIntent(@Nullable Intent intent) {
       Toast.makeText(this, "Intent Error", Toast.LENGTH_LONG).show();
   }
}
```
- You can also customize your own activity to receive the callback; just implement the interface `IApiEventHandler` and set your activity path by using parameter "callerLocalEntry".
```
// request.callerLocalEntry = "com.xxx.xxx...activity";
```
### Requirements for Media
- For Video:
- Minimum video duration must be 3 seconds.
- Supported video media type: .mp4.
- The minimum of the frame size should be no more than 1100.
- For multi-Video:
- The number of Videos can be no more than 12.
- For multi-Image:
- The number of images should be more than 1 and up to 12.
- Videos cannot contain brand logos or watermarks. Violating this guideline will lead to videos being deleted or accounts being banned. Make sure your applications share content without watermarks or brand logos.
#### Handling Errors
[For error handling and debugging, check out the list of Error Codes](https://developers.tiktok.com/doc/getting-started-android-handling-errors)
Was this document helpful?