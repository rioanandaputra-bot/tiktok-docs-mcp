Docs
# Debug Your Mini Drama
This document demonstrates the steps to debug, package, and preview your TikTok Minis app before uploading it to the platform.
## Debugging preparation
Before starting the local debugging process, please ensure your development environment meets the following requirements:
### Configure networks
- Local network: Your computer and mobile testing device must be connected to the same Wi-Fi network.
- Internet access: Both devices must have active external internet access.
### Register test users
Before debugging, verify that the logged-in TikTok account on your mobile device is added to the **Test User **list for your target `clientKey`.
**Note:** If the user is not on the list, you must add them in the Developer Portal before proceeding.
- Go to the** Testing permissions** tab on your app page.
- Click the **Add test users** button.
- Connect the TikTok account that you want to add as a test user. You can add up to 30 test users.
**Tip**: If you click the **Continue** button when prompted to connect your TikTok account and nothing happens, you need to check whether your browser has blocked pop-ups. If so, you must allow pop-ups to add test users.
### Application startup scripts
The debugging tool relies on your project's startup scripts. It will automatically call `dev` or `start` to launch the TikTok Minis application. Check your `package.json` to ensure these are configured:
```
// package.json
{
  "scripts": {
    "dev": "..." // or "start"
  }
}
```
### Check SDK integration
Confirm that the TikTok Minis SDK is properly initialized in your entry HTML file. Ensure the `clientKey` used in local debugging exactly matches the one passed into `TTMinis.init`.
```
<!-- index.html -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <script src="https://connect.tiktok-minis.com/drama/sdk.js"></script>
    <script>
      TTMinis.init({
        clientKey: "YOUR_CLIENT_KEY", // Replace with your actual client key
      });
    </script>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>tiktok-minis-demo</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```
### Create configuration file
You need a `minis.config.json` file in your project root to define your development and build environments.
#### Method 1: CLI generation (Recommended)
Navigate to your project root and run the initialization script to automatically generate the config file:
```
cd path/to/your/project
minis init
```
#### Method 2: Manual configuration
Alternatively, create a `minis.config.json` file in your root directory and paste the following configuration, modifying the values to fit your project:
```
{
  "dev": {
    "port": "3000",        // The port your local dev server uses
    "host": "localhost"    // Your local host (optional)
  },
  "build": {
    "outputDir": "dist",          // The output directory after building (e.g., dist, build)
    "htmlEntry": "public/index.html" // The relative path to your index.html
  }
}
```
## Start debugging session
After you've prepared your debugging environment and completed the necessary prerequisites, you may start a debugging session:
- Open your terminal at the project root directory.
```
cd path/to/your/project/
```
- Run the start command:
```
minis dev
```
### Troubleshooting tips
Listed are potential issues you might encounter while debugging and their respective solutions:
- Initialization not completed: Ensure `TTMinis.init` is correctly executed upon load.
- Client key mismatch: The client key used by `minis dev` does not match the key used in `TTMinis.init`.
- Missing SDK: `index.html` lacks the JSSDK script tag.
- Startup script issue: `dev` or `start` is missing in `package.json`.
### Preview app on TikTok via QR code
Once the local server starts, a QR code will be generated. Use your TikTok app to scan it.
**Important**: Take note of the following tips when debugging:
- Keep the TikTok app open and active at all times. It is highly recommended to increase your phone's screen timeout setting. If the screen turns off, you must restart TikTok and scan the code again.
- Ensure the TikTok account scanning the QR code is registered as a test user.
- Manual connection: If the QR code scan fails or times out, click **Network Diagnostics** below the QR code and manually connect using the configuration displayed on the client loading interface.
## Package your TikTok Minis app
TikTok Minis applications are fundamentally web applications running within a WebView. To minimize disruption to your existing workflow, Minis uses a "post-build" pipeline.
Compile your source code into a static resource directory (`dist`, `build`) as usual, and then `minis build` performs supplementary processing (pre-checks, compression, optimization) based on the `build.outputDir` config to ensure the artifacts meet platform standards.
Complete your project build: `npm run build`.
### Recommended integration workflow
The best practice is to chain `minis build` directly after your standard build command. This ensures you only need to run `npm run build` once.
#### Example 1: Vite project
```
// package.json (Before, assuming the project originally used Vite)
{
  "scripts": {
    "build": "vite build"
  }
}

// package.json (After TikTok Minis integration)
{
  "scripts": {
    "build": "vite build && minis build"
  }
}
```
#### Example 2: Webpack project
```
{
  "scripts": {
    "build": "webpack --mode production && minis build"
  }
}
```
### Build field references
For reference, ensure your `minis.config.json` correctly outlines your build targets:
- `dev.port`: Local dev server port.
- `dev.host`: Local dev server address (optional).
- `build.outputDir`: The directory containing your standard build artifacts (such as `dist`).
- `build.htmlEntry`: The relative path to the entry HTML file in your source code.
For example:
```
{
      "dev": {
        "port": 3000,
        "host": "localhost"
      },
      "build": {
        "outputDir": "dist",
        "htmlEntry": "public/index.html"
      }
    }
```
## Platform preview
### Integrated logs (vConsole)
For on-device debugging and log viewing, you can inject `vConsole` into your application. Add the following script tags to your `index.html`:
```
<head>
  <!-- Initialize Minis SDK -->
  <script src="https://connect.tiktok-minis.com/drama/sdk.js"></script>
  <script>
    TTMinis.init({ clientKey: "YOUR_CLIENT_KEY" });
  </script>

  <!-- Inject vConsole for on-device logs -->
  <script src="https://connect.tiktok-minis.com/libs/vConsole.js"></script>
  <script>
    // vConsole mounts to `window.VConsole` by default
    var vConsole = new window.VConsole();
  </script>
</head>
```
### Code upload and preview
[Once your code package is ready, proceed to upload, preview, submit, and release your app](https://developers.tiktok.com/doc/tiktok-minis-release-your-mini-app) on the Developer Portal.
Was this document helpful?