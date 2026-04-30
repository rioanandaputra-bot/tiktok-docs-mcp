Docs
# Get Started
TikTok Minis SDK allows authentication from your web app to TikTok.
To use TikTok Minis SDK, include a piece of JavaScript code in your HTML to asynchronously load the SDK into your pages. This will not block other elements from loading on your page. TikTok Minis SDK does not require standalone files or downloads.
Insert the following code snippet directly after the opening `<body>` tag on each page where you want to load the basic version of the SDK with default options.
```
<script src="https://connect.tiktok-minis.com/drama/sdk.js"></script>
<script>  
   TTMinis.init({
     clientKey: '{app-client-key}',
   });
</script>
```
This code will load and initialize the SDK. You must replace the `app-client-key` value with your app's client key, found in the **Credentials** section of your app page on Developer Portal.
## Set up TikTok Minis SDK
### init(params)
The method `TTMinis.init()` is used to initialize and set up the SDK. All other SDK methods must be called after this one, because they won't exist until you do.
**Parameters**
```
/**
 * Init JSSDK
 * @param {Object} params - Init params
 * @param {string} params.clientKey - clientKey from https://developers.tiktok.com/apps/
 */
TTMinis.init(params)
```
**Example**
```
TTMinis.init({
  clientKey: '{app-client-key}'
});
```
After initializing and setting up the SDK, you can call any of the JavaScript APIs for TikTok Minis.
Was this document helpful?