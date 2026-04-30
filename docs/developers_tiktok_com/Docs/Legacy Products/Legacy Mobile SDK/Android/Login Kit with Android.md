Docs
[There is a new version of this SDK: Login Kit for Android](https://developers.tiktok.com/doc/login-kit-android-quickstart-v2)
# Login Kit for Android
## Overview
[This guide explains how to integrate with Login Kit for Android using Swift. Once authenticated users authorize your app, you can access their basic TikTok profile data including their display name and avatar. Additional data access may require approval for additional Scopes. Learn more on Scopes Overview](https://developers.tiktok.com/doc/scopes-overview).
## Prerequisites
[[Obtain a client key and client secret by logging in to Developer Portal](https://developers.tiktok.com/apps/) and selecting your app. Refer to the Quickstart Guide](https://developers.tiktok.com/doc/getting-started-android-quickstart) for detailed steps. You must also provide a signing key for your Android app, as described below.
### Android App Signing Key
While registering your app for the Android platform on Developer Portal, you'll be asked to submit a signing key for your Android app. That signing key is the MD5 hex digest of your installed release app which will be used as the signature. It looks similar to something like: `114326e82c81e639a52e5c023100f12a`.
There are 2 methods for obtaining the signature of the Android installation package:
- Obtained in the code, but you must know the package name of the installation package.
```
PackageManager manager = getPackageManager();
/** Get the package information of the specified package name including the signature through the package manager **/
PackageInfo packageInfo = null;
try {
    packageInfo = manager.getPackageInfo("your package name", PackageManager.GET_SIGNATURES);
} catch (PackageManager.NameNotFoundException e) {
    e.printStackTrace();
}

/** Get the signature array through the returned package information **/
Signature[] signatures = packageInfo.signatures;
String ss = MD5.hexdigest(signatures[0].toByteArray());
if(ss != null) {
    Toast.makeText(this, "signature" + ss, Toast.LENGTH_LONG).show();
} else {
    Toast.makeText(this, "No signature", Toast.LENGTH_LONG).show();
}

/** Create an MD5 tool class **/
public class MD5 {
    private static final char[] hexDigits = { 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102 };

    public static String hexdigest(String paramString) {
        try {
            String str = hexdigest(paramString.getBytes());
            return str;
        } catch (Exception localException) {
        }
        return null;
    }

    public static String hexdigest(byte[] paramArrayOfByte) {
        try {
            MessageDigest localMessageDigest = MessageDigest.getInstance("MD5");
            localMessageDigest.update(paramArrayOfByte);
            byte[] arrayOfByte = localMessageDigest.digest();
            char[] arrayOfChar = new char[32];
            int i = 0;
            int j = 0;
            while (true) {
                if (i >= 16)
                    return new String(arrayOfChar);
                int k = arrayOfByte[i];
                int m = j + 1;
                arrayOfChar[j] = hexDigits[(0xF & k >>> 4)];
                j = m + 1;
                arrayOfChar[m] = hexDigits[(k & 0xF)];
                i++;
            }
        } catch (Exception localException) {
        }
        return null;
    }
}
```
- Inside of a terminal, enter the directory where *.jks is located, then enter into the command line:
```
keytool -list -v -keystore [xxx] -keypass [xxx]
```
Get the output MD5 value, then remove the ":" to obtain the required 32-character signature.
## Android Integration
### Request User Authorization
- Create an instance of `TiktokOpenApi`.
- Create an `Authorization.Request` instance and set the following required parameters:
- `request.scope = ``user.info``.basic`. If you are approved additional scopes , include them using comma-separated list.
- `request.state = "xxx"` . This is used to maintain the status of your request and callback. Verify that the `state` parameter returned in the callback matches what you sent earlier.
- Call the method `authorize()` on your instance of `TiktokOpenApi` .
```
// STEP 1: Create an instance of TiktokOpenApi
TiktokOpenApi tiktokOpenApi= TikTokOpenApiFactory.create(this);

// STEP 2: Create an instance of Authorization.Request and set parameters
Authorization.Request request = new Authorization.Request();
    request.scope = "user.info.basic";
    request.state = "xxx";
    return tiktokOpenApi.authorize(request);

// 3. Invoke the authorize method
tiktokOpenApi.authorize(request);
```
After successful authorization, the user will be brought back to your app via the `TikTokEntryActivity`.
### Receive Callbacks
We provide two ways for you to receive the callback data from TikTok:
- Create new activity named `TikTokEntryActivity` in your Android app and implement the `TikTokApiEventHandler` interface.
- **Note**: The path of the activity should be in the format: `{your-p``ackage``-``name``}``.tiktokapi.TikTokEntryActivity`. For example, `com.``mycoolapp``.tiktokapi.TikTokEntryActivity`.
The following example demonstrates how to use the `TikTokEntryActivity` to receive the callback data:
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
       if (resp instanceof Authorization.Response)  {
          Authorization.Response response = (Authorization.Response) resp;
          Toast.makeText(this, " code：" + response.errorCode + " errorMessage：" + response.errorMsg, Toast.LENGTH_SHORT).show();
      }
   }
   @Override
   public void onErrorIntent(@Nullable Intent intent) {
       Toast.makeText(this, "Intent Error", Toast.LENGTH_LONG).show();
   }
}
```
- Alternatively, you can customize your own activity to receive the callback. To do this, implement the interface `IApiEventHandler` and set your activity path by using parameter `callerLocalEntry`.
```
// request.callerLocalEntry = "com.xxx.xxx...activity";
```
To receive callbacks when people stay in TikTok, please register to receive a broadcast:
```
public static final String ACTION_STAY_IN_TT = "com.aweme.opensdk.action.stay.in.dy";
```
### Obtain Access Token
[Upload the `code` returned in the callback to your server-side and obtain a user access token. See Manage User Access Tokens](https://developers.tiktok.com/doc/legacy-user-access-guide) for more information.
### Handling Errors
[See Error Codes](https://developers.tiktok.com/doc/getting-started-android-handling-errors) for error handling and debugging.
Was this document helpful?