Docs
# Debug Your Mini Game
After you've developed your mini game and integrated Mini Games SDK to access TikTok capabilities, you can debug your mini game using **DevTool**, TikTok's mini game developer tool. Once you've completed debugging, you are ready to upload your code package to the Developer Portal.
**Note**: Before performing local debugging, please ensure that your mobile phone and computer are on the same network and can access the extranet environment normally.
## Manage test users
Test users are TikTok accounts that you approve to debug and preview your app. Test users can also access the partial rollout version of your app, if you choose grey release.
If you plan to release your mini game to multiple global regions, we recommend having at least one TikTok test account per region.
Add test users to your app page in the Developer Portal:
- Go to the** Testing permissions** tab on your app page.
- Click the **Add test users** button.
- Connect the TikTok account that you want to add as a test user. You can add up to 30 test users.
**Tip**: If you click the **Continue** button when prompted to connect your TikTok account and nothing happens, you need to check whether your browser has blocked pop-ups. If so, you must allow pop-ups to add test users.
## Required items for debugging
To complete the debugging process, you will need the following items and environments:

| **Required item** | **Description** |
| --- | --- |
| Access to Developer Platform | Run `curl ``https://developers.tiktok.com`to determine whether you have access to the TikTok Developer Platform. This step is used to verify whether the terminal has successfully connected to the network proxy, preventing subsequent debugging link exceptions caused by the inability to access relevant interfaces of the developer platform. |
| DevTool | Command-line interface tool for local development and debugging of TikTok mini games. You must install DevTool to debug your mini game. |
| Exported game directory | When exporting your mini game code package from a third party game engine, choose a mainstream platform as the export type. TikTok native mini games are compatible with mainstream platforms, such as WeChat or Douyin. |
| Google Chrome | DevTool provides a development and debugging environment based on the Google Chrome. Make sure Google Chrome is installed on the device you will use for debugging. |
| NodeJS | [DevTool is developed based on the NodeJS environment. Therefore, you must have NodeJS installed](https://nodejs.org/en/download). Your Node version must not be lower than v20, otherwise you will encounter an error when trying to install DevTool. We recommend installing v20.19.5. |
| Single wifi network | Local debugging on mobile phones and computers requires them to be on the same network. |
| Test users | Local debugging can only be carried out after TikTok test users have been registered in the **Testing permissions **section of your app page. Otherwise, scanning the code will result in an error. |
| TikTok app | You must have the TikTok app installed on the device you will use for debugging. |
| Trusted domains | [Your domain name must be registered under your app's **Development Configuration](https://developers.tiktok.com/doc/set-up-development-configuration)**section. During runtime, mini-games can only initiate network requests to registered domains. Any domain not on the allowlist will be denied access. Therefore, all domains involved in network requests within mini games must be registered in advance. |

## Debug your mini game
To debug your mini game, you will need to have completed code development and integration with TikTok's features:
- Exported your mini game's code package from the game engine you used
- Completed integration with TikTok's Mini Games SDK and required dependencies
The following steps explain how to install and use TikTok's developer debug tool to debug your mini game.
**Note**: Before performing local debugging, please ensure that your mobile phone and computer are on the same network and can access the extranet environment normally.
### Install debug tool
To install TikTok's debug tool (DevTool), run the following command:
**Note**: You must use a Node.js environment. Check in advance if your Node version is >=20. If it is an earlier version, you must upgrade it before proceeding.
```
npm install @ttmg/cli -g

ttmg -v
```
### Complete local login
Functions provided by the debug tool, such as viewing game details and uploading the code package to the Developer Platform, require developers to log in to their TikTok for Developers account on the local endpoint before they can be used. We recommend that you complete the account login first and then proceed with subsequent debugging operations.
```
ttmg login
```
### Initiate debugging session
Enter the game directory with the path to your game project:
```
cd path/to/your-game-project
```
Then start up the debugging environment. You will only be asked to enter your app's client key once, during the first debugging session. It will be stored for subsequent debugging sessions.
```
ttmg dev
```
Before running your mini game's code exported by the game engine, TikTok will perform a compilation of the game artifact against its runtime framework. The mini game is then run based on this compiled artifact, ensuring consistent performance.
The compilation process will perform necessary pre-verification on the game atifact to help developers identify issues in advance. The verification includes the following:
- `game.json` configuration: Is it configured? (Required)
- `subpackages` in `game.json`: If present, is the configuration correct?
- `main` file: Does it exist, and is it correct?
- `root` directory: Does it exist, and is it correct?
- Game package size: Does it meet platform requirements? (This will show as a warning during local debugging, but will cause an error during platform deployment):
- The entire game package size cannot exceed 30 MB.
- The main game package size cannot exceed 4 MB.
- The size of an independent subpackage cannot exceed 4 MB.
### Select debug mode
There are two primary methods for testing and debugging your mini game: The debug mode type determines where the game's core logic is executed and how you access debugging tools.

| **Mode** | **Where logic runs** | **Description** | **Usage** |
| --- | --- | --- | --- |
| **Mobile device** | Game logic executes on the physical mobile device (TikTok app = Client). | Use the vConsole (an in-app, on-screen console) to view logs. This is the most authentic way to test visual and performance effects. | Best used when your local network condition is poor, as this mode is less reliant on continuous PC-to-browser communication. |
| **Remote browser** | Game logic executes on the local PC browser (Chrome). | Allows advanced debugging (breakpoints, watching variables) using Chrome's DevTool. The mobile device synchronously mirrors the screen. | Best used when you need powerful, flexible breakpoint debugging and access to full browser development tools. |

**Tip**: If you require more flexibility, you can also create a new custom startup mode to meet specific debugging and preview requirements.
### Scan the QR code to debug
Note: Before scanning the code, confirm whether the current TikTok version supports native mini games. If unsupported, a 404 page will appear after scanning.
- Use TikTok to scan the QR code on the webpage.
- TikTok may require a VPN to be accessed normally.
- Before scanning the QR code, you need to log in using a test account.
- Wait for the TikTok app to verify whether the currently logged-in TikTok user has debugging permissions for this application.
- If authorized, the TikTok app will enable the debugging environment.
- If unauthorized, check the following:
- Open `project.config.json` and check if the `appid` is consistent with the game ID on the Developer Portal.
- Check whether the `appid` in `project.config.json` has already added test users on the Developer Portal.
- After completing debugging of user authentication, the debugging tool will start uploading the game package to TikTok app. After the upload is completed, it will start loading the game.
- The browser interface displays the upload progress, and after the upload is completed, the TikTok app starts the game.
- After the TikTok app completes the game startup, operate the game within the TikTok app and enter the module you want to debug.
- Use the browser Console to view your logged messages or debug your JavaScript.
- When you need to modify the code during debugging, you can select the same export path in the game engine export process.
- The local debugging service will monitor changes to the game's original code package and automatically perform pre-compilation.
- The debugging page will notify via a pop-up window after the modified code is compiled.
## Modify debugging settings
You can modify debugging settings depending on the scenario you want to test.
- After enabling domain verification, only domains configured on the platform will be allowed to make requests.
- After enabling ad mock debugging, when calling JavaScript APIs for In-App Ads, it will enter the mock environment to help you debug various boundary scenarios.
- After enabling payment mock debugging, when calling JavaScript APIs for In-App Purchases, it will enter the mock environment to help you debug various boundary scenarios.
## Set debug startup mode
During mini game development, internal logic is usually differentiated based on different traffic entry sources, and function customization can be achieved by selecting different scenario entry points.
If your mini game supports independent subpackages, you can also choose a specific subpackage as the code package at startup for debugging purposes.
Additionally, in scenarios related to advertising placement, developers often need to customize startup parameters for internal technical attribution within the game.
You can obtain these custom parameters by accessing the `TTMinis.game.getLaunchOptionsSync` method and use them in subsequent technical processes.
### Custom startup package
- Game main package startup: Load and start the game using the game entry file `game.js`
- Independent subpackage startup: Start, load, and debug the game using the independent subpackage entry file
### Select to enter the scene
Simulate different traffic scenarios within the TikTok app to launch mini-games, enabling the development and debugging of subsequent processes
### Add startup parameters
`TTMinis.game.getLaunchOptionsSync` method retrieves these custom parameters and uses them in subsequent technical processes.
## Local code pre-check
Below is a list of what content to check:
- **Package size check**
- The size of the entire game package must be contained within 30 MB, the size of the main package cannot exceed 4 MB, and the size of independent subpackages cannot exceed 4 MB.
- **Required connection capability check**
- Check if the game has integrated the necessary API capabilities to ensure that the mini game has better user experience and conversion effects on TikTok.
- **Configuration file check**
- `game.json`: Ensure that the configuration of the subpackage file paths is correct, all paths can be accessed normally, and avoid subsequent loading failures.
- `project.config.json`: Confirm that the `appid` has been filled in and is a valid value; otherwise, local debugging will not run properly.
#### Explanation of package sizes
**Note**: Be aware of package size verification. During local development, failure to meet the requirements will only trigger an alert. During the upload to the platform, if the requirements are not met, the upload will fail.

| Type | Restriction | Description |
| --- | --- | --- |
| Total project size | Source file size does not exceed 30 MB (before compression) | Size of the game project exported from the game engine |
| Game main package size | The main package size does not exceed 4 MB (before compression) | All files in the game project, except those under `subpackages/*`, will be counted within the size range of the main game package |
| Independent subpackage size | The main package size does not exceed 4 MB (before compression) | The size of the package body defined as `independent: true`in the game subpackages |

#### Required connection capabilities

| Required capabilities | Frontend interface | Reasons for mandatory connection |
| --- | --- | --- |
| User silent login | `TTMinis.game.login` | Ensure data consistency and traceability after user return |
| Incentive ad video | `TTMinis.game.createRewardedVideoAd` | Core monetization methods, providing a stable monetization path Deeply integrated with incentive-based gameplay (such as stamina, revival, double rewards, acceleration, and more) to improve user retention and session duration |
| Home screen shortcut | Add to home screen:`TTMinis.game.addShortcut` Receive reward:`TTMinis.game.getShortcutMissionReward` | Improve next-day and multi-day follow-up: Direct desktop access shortens the startup path, significantly boosting return and activity Support platform retention and growth tasks, which require standardized creation and claiming processes to ensure compliance in awarding prizes |
| Open profile sidebar | Jump to the sidebar of the home page:`TTMinis.game.startEntranceMission` Receive reward:`TTMinis.game.getEntranceMissionReward` | Utilize the platform entry position to increase exposure and natural traffic conversion, and promote user attention and return visit Coordinate with the platform's "entry tasks/sidebar tasks" to distribute rewards, thereby enhancing the depth of interaction and task completion rate |

#### Configuration file instructions

| Configuration file | Verification content | Post script |
| --- | --- | --- |
| `game.json` | Is the subpackages configuration valid? | If the configured subpackage information is incorrect, an error will be reported directly, and the compilation process will be interrupted |
| `game.js` | Entry file of the game | -- |
| `project.config.json` | Does the `appid`in the game configuration file exist and is it valid? | Under the local debugging environment, it has a strong dependency. If the configured `appid`is invalid, it will affect debugging. |

## Upload local code to the Developer Portal
During mini game development, developers can use DevTool to upload local game code packages to the Developer Portal for testing or debugging.
This feature allows developers to directly select the code package to be uploaded and push it to the Developer Portal after completing code writing and packaging locally.
This process helps developers quickly verify the content of different versions or sub-packages, enhancing the flexibility of development and debugging.
## Next step: Release your mini game
[After debugging your code, you are ready to upload, preview, submit for review, and release to users](https://developers.tiktok.com/doc/submit-your-app-for-review).
Was this document helpful?