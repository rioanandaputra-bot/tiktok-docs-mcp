Docs
# Android Support for FileProvider
## Getting started
## Step 1: Integrate the fileprovider SDK
```
// Add the following to gradle：
repositories {
    maven { 
        url 'https://dl.bintray.com/aweme-open-sdk-team/public'
    }
} 
    
dependencies {
    implementation 'com.bytedance.ies.ugc.aweme:opensdk-oversea-external:0.1.4.1'
}
```
## Step 2: Integration
- In the Application onCreate，initialize TikTokOpenApiFactory
```
@Overridepublic void onCreate() {
 super.onCreate();
    String clientkey = "[Client Key]";
    TikTokOpenApiFactory.init(new TikTokOpenConfig(clientkey));
}
```
- Add permissions to your Android Manifest, and setup callback to your activity
```
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" /> 
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
// If you have a custom activity to receive callback, you can skip this step
<activity     android:name=".tiktokapi.TikTokEntryActivity"               
  android:launchMode="singleTask"
  android:taskAffinity="[Your package name]" 
  android:exported="true">
</activity>
```
TikTok 12.5.0 and above supports FileProvider. Below are the instructions to support FileProvider.
## FileProvider Usage
- Settings
In your app's AndroidManifest.xml, add the following settings as follows:
```
<provider  android:name="android.support.v4.content.FileProvider"
  android:authorities="${applicationPackageName}.fileprovider"
  android:exported="false"
  android:grantUriPermissions="true">
  <meta-data
    android:name="android.support.FILE_PROVIDER_PATHS"
    android:resource="@xml/file_provider_paths" />
</provider>
```
In res/xml (please create the directory if it doesn't exist), add a file file_provider_paths.xml with the content:
```
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-files-path name="sharedata" path="shareData/"/>
</paths>
```
external-files-path represents the files in the root of your app's external storage area. The root path of this subdirectory is the same as the value returned by Context.getExternalFilesDir(null)
You can also support other paths for example:
```
<files-path name="name" path="path" /> // Subdirectory returned by Context.getFilesDir()
<cache-path name="name" path="path" /> // Subdirectory returned by Contextget.CacheDir()
```
[For more information, check out this page](https://developer.android.com/reference/androidx/core/content/FileProvider).
- Using the FileProvider API
FileProvider converts a path file a content://URI format
```
public String getFileUri(Context context) {
     String filePath = context.getExternalFilesDir(null).p + "/shareData/test.png";
    // The filePath needs conforms to the path in the xml/file_provider_path file in order to be sharable
    File file = new File(filePath);
    // Use contentPath for sharing
    String contentPath = getFileUri(context, file);
 // The package name here must be consistent with what was provided in the AndroidManifest.xml's authorities.
    Uri contentUri = FileProvider.getUriForFile(context, 
        "com.example.app.fileprovider",file);
    // Authorize permission for TikTok build variants
    context.grantUriPermission("com.zhiliaoapp.musically",  
        contentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
    context.grantUriPermission("com.ss.android.ugc.trill",  
        contentUri, Intent.FLAG_GRANT_READ_URI_PERMISSION);
    return contentUri.toString(); // contentUri.toString() should be prefixed with "content://"
}
```
- Sharing photos
```
TiktokOpenApi tiktokOpenApi = TikTokOpenApiFactory.create(this);
if (tiktokOpenApi.isShareSupportFileProvider() &&
        android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
    ArrayList<String> images = new ArrayList<>();
    images.add(xxx);  // Pass FileProvider formatted list here
    Share.Request request = new Share.Request();
    ImageObject imageObject = new ImageObject();
    imageObject.mImagePaths = images;
    MediaContent mediaContent = new MediaContent();
    mediaContent.mMediaObject = imageObject;
    request.mMediaContent = mediaContent;
    tiktokOpenApi.share(request);
} else {
    Toast.makeText(TestFileProviderActivity.this, "Unsupported version", Toast.LENGTH_LONG).show();
}
```
- Sharing videos
```
if (tiktokOpenApi.isShareSupportFileProvider() &&
        android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.N) {
 
    ArrayList<String> videos = new ArrayList<>();
    videos.add("video path"); // Pass FileProvider formatted list here
    Share.Request request = new Share.Request();
    VideoObject videoObject = new VideoObject();
    videoObject.mVideoPaths = videos;
    MediaContent content = new MediaContent();
    content.mMediaObject = videoObject;
    request.mMediaContent = content;
    tiktokOpenApi.share(request);
} else {
    Toast.makeText(TestFileProviderActivity.this, "Unsupported version", Toast.LENGTH_LONG).show();
}
```
Was this document helpful?