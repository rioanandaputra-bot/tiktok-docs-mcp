Docs
# Mini Games SDK Changelog
This changelog describes updates to the Mini Games SDK base library version and the corresponding TikTok app version.
## SDK 0.19.0 / Client 44.7.0 (March 26, 2026)
### New Content/Features
- Added new APIs related to screen brightness and always-on:
- `setKeepScreenOn` (Set the always-on state of the screen)
- `getScreenBrightness` (Get the current screen brightness)
- `setScreenBrightness` (Set the screen brightness)
## SDK 0.18.0 / Client 44.6.0 (March 26, 2026)
- Added new APIs`FileSystemManager.appendFile`, `FileSystemManager.appendFileSync` to append content to the end of the file
- Added new APIss`FileSystemManager.truncate`, `FileSystemManager.truncateSync` to truncate a file to a specified length
- Added new APIs`FileSystemManager.ftruncate`, `FileSystemManager.ftruncateSync` to truncate an opened file to a specified length
- Added new APIs`FileSystemManager.readCompressedFile`,`FileSystemManager.readCompressedFile` to read compressed file
- Added new APIs `FileSystemManager.readZipEntry` to read file entries within a ZIP package
- Added new network status management series of APIs which support developers to perceive changes in the network environment and optimize the user experience in weak network scenarios:
- `getNetworkType` (Get the current network type)
- `onNetworkWeakChange` (Listen for changes in weak network status)
- `offNetworkWeakChange` (Cancel listening for weak network status)
## SDK 0.17.0 / Client 44.5.0 (March 24, 2026)
No change s
## SDK 0.16.0 / Client 44.4.0 (March 18, 2026)
### What's new
- Added new APIs`FileSystemManager.stat`,`FileSystemManager.statSync` to get file status information
- Added new APIs`FileSystemManager.fstat`,`FileSystemManager.fstatSync` to get status information of an opened file
- Added new APIs`FileSystemManager.rename`, `FileSystemManager.renameSync` to rename files
- Added new APIs `FileSystemManager.getFileInfo` to get file information
- Added new APIs`FileSystemManager.saveFile`, `FileSystemManager.saveFileSync` to save files locally
- Added new APIs`FileSystemManager.getSavedFileList` to get the list of saved files
- Added new APIs`FileSystemManager.removeSavedFile` to delete saved files
## SDK 0.15.0 / Client 44.3.0 (March 11, 2026)
### What's new
- Added new APIs`FileSystemManager.open`,`FileSystemManager.openSync` - Open File
- Added new APIs`FileSystemManager.close`,`FileSystemManager.closeSync` - Close File
- Added new APIs`FileSystemManager.read`,`FileSystemManager.readSync` - Read File
- Added new APIs`FileSystemManager.write`, `FileSystemManager.writeSync` - Write to File
- Added new APIs`FileSystemManager.rmdir`, `FileSystemManager.rmdirSync` - Remove Directory
- Added new APIs`FileSystemManager.readdir`, `FileSystemManager.readdirSync` - Read Directory
- Added new APIs`FileSystemManager.unlink`, `FileSystemManager.unlinkSync` - Delete File
## SDK 0.14.0 / Client 44.2.0 (March 4, 2026)
No changes
## SDK 0.13.0 / Client 44.1.0 (February 24, 2026)
No changes
## SDK 0.12.0 / Client 44.0.0 (February 24, 2026)
No changes
## SDK 0.11.0 / Client 43.9.0 (February 24, 2026)
### Bug fixes
- Fixed the issue where downloading fails due to spaces in the URL of `TTMinis.game.downloadFile`
## SDK 0.10.0 / Client 43.8.0 (January 27, 2026)
### What's new
- Added APIs `TTMinis.game.vibrateLong` and `TTMinis.game.vibrateShort`, which can make the phone vibrate
## SDK 0.9.0 / Client 43.7.0 (January 22, 2026)
### Improvements
- Updated the error code fields for interstitial ads and rewarded ads, renaming `errorMsg` to `errMsg` to align with the rest of the API
### Bug fixes
- Fixed an issue where `TTMinis.game.getStorageSync` and `TTMinis.game.setStorageSync` could throw exceptions when a non-string key was passed
## SDK 0.8.0 / Client 42.6.0 (January 19, 2026)
### What's new
- Added API `TTMinis.game.getStorageInfo`、`TTMinis.game.getStorageInfoSync` to get the storage info
### Improvements
- Updated API `TTMinis.game.login` error codes to pass through client and server error codes
### Bug fixes
- Fixed an issue where passing both `defaultValue` and `maxLength` to the API `TTMinis.game.showKeyboard` on Android caused an error
## SDK 0.7.0 / Client 43.5.0 (January 15, 2026)
No changes
## SDK 0.6.0 / Version 43.4.0 (December 30, 2025)
### What's new
- Added support for loading Wasm files using `TTWebAssembly`
- Added API `TTMinis.game.showKeyboard`, `TTMinis.game.hideKeyboard` to use keyboard-related features
- Added API `TTMinis.game.setPreferredFramesPerSecond` to modify rendering frame rate
## SDK 0.5.0 / Version 43.1.0 (December 19, 2025)
### What's new
- Added support for game engine plugins
### Bug fixes
- Fixed API `fileSystem.writeFile` to support writing `ArrayBuffer` type
## SDK 0.4.0 / Version 43.0.0 (December 4, 2025)
### What's new
- Added API `TTMinis.game.connectSocket` to create a websocket connection
- Added API `TTMinis.game.reportEvent` for event reporting capability
## SDK 0.3.0 / Version 42.9.0 (November 27, 2025)
### What's new
- Added API `TTMinis.game.getMenuButtonBoundingClientRect` to get the layout position information of the menu button (top-right capsule button)
- Added API `fileSystemManager.unzip` to decompress files
- Added API `TTMinis.game.createInterstitialAd` to create an interstitial ad component
### Improvements
- Updated API `TTMinis.game.shareAppMessage` to support `query` and `path` parameters
## SDK 0.2.0 / Version 42.8.0 (November 20, 2025)
### What's new
- Added API `TTMinis.game.getWindowInfo` to get window information
### Improvements
- Updated API `TTMinis.game.request` to support passing the `arraybuffer` type as a parameter
- Updated APIs `TTMinis.game.getSystemInfo` and `TTMinis.game.getSystemInfoSync` to support fetching the `statusBarHeight` and `safeArea` fields
## SDK 0.1.0 / Version 42.7.0 (November 18, 2025)
### Bug fixes
- Fixed vConsole format logic to prevent JS OOM (Out Of Memory)
- Fixed API `TTMinis.game.request` issue where the default content-type was not `application/json`
Was this document helpful?