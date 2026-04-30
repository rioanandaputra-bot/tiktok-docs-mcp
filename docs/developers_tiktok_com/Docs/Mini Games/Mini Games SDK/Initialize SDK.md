Docs
# Initialize SDK
This guide explains how to initialize the Mini Games SDK, a JavaScript toolkit that provides access to TikTok's client-side functionalities, in your HTML runtime mini game.
**Note**: Initializing Mini Games SDK is only required if your mini game uses HTML runtime. This step is not necessary for native runtime mini games.
To use Mini Games SDK for your HTML mini game, include a piece of JavaScript code in your HTML to asynchronously load the SDK into your pages. This will not block other elements from loading on your page. Mini Games SDK does not require standalone files or downloads.
Insert the following code snippet directly after the opening `<body>` tag on each page where you want to load the basic version of the SDK with default options.
```
<script src="https://developers.tiktok.com/js/minis.js"></script>
<script>  
   TTMinis.game.init({
     clientKey: '{app-client-key}',
   });
</script>
```
This code will load and initialize the SDK. You must replace the `app-client-key` value with your app's client key, found in the **Credentials** section of your app page on Developer Portal.
## Set up Mini Games SDK for your HTML mini game
### .init(params)
The method `TTMinis.game.init()` is used to initialize and set up the SDK. All other SDK methods must be called after this one, because they won't exist until you do.
#### Parameters
```
/**
 * Init JSSDK
 * @param {Object} params - Init params
 * @param {string} params.clientKey - clientKey from https://developers.tiktok.com/apps/
 */
TTMinis.game.init(params)
```
#### Example
```
TTMinis.game.init({
  clientKey: '{app-client-key}'
});
```
### .setLoadingProgress(opts)
Informs the main framework of the loading progress of the game, and closes the main framework loading page when progress reaches a value of 1.
#### Parameters
- **Progress:** Game progress 0~1
- **Success**: Execute a successful return
```
type SuccessHandler = （）= void;
```
- **Fail**: Return the failed execution
```
type FailHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
- **Complete**: Execute the completed return
```
type CompleteHandler = （）= void;
```
#### Example
```
TTMinis.game.setLoadingProgress({
  progress: 1,
  success: () => {
  // do something when succeed
  },
  fail: (error) => {
  // do something when failed
  }
  complete: () => {
  // do something when completed
  }
})
```
After initializing and setting up the SDK, you can call any of the JavaScript APIs for mini games.
Was this document helpful?