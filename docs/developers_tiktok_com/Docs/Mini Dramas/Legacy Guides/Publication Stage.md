Docs
# Publication Stage
Once you have finished building and debugging your mini app, prepare to upload your code assets then submit your mini app for review.
## Pack and upload your TikTok Minis
After completing development, debugging, and testing, pack your mini app code artifacts into a zip file that does not exceed 50 MB. Make sure your zip file contains all of the files in your directory.
Your mini app file must also meet the following requirements for code scanning:
- The **minis.config.json** file must be included.
- The **TikTok Minis SDK** must be initialized.
- The **TikTok Login API** functionality must be implemented.
- It must not contain any empty files (zero bytes).
- APIs related to navigation are disabled.
- APIs listed in the full Web API sensitivity inventory are disabled.
- Restrict the sources of **dynamically imported scripts** to prevent bypassing platform reviews and arbitrary updates.
- Limit the sources of runtime API requests. The Minis platform ensures traceability of third-party API request scopes, allowing only domains declared in the local configuration file to make valid requests.
Please be aware that if your zip file does not meet our requirements, you may be unable to upload your file to the Developer Portal.
On your app page, go to the **Code assets **section, then upload your zip file.
After uploading your mini app file, you can select how you would like to release your mini app. You must set the status of at least one version to **Production** or **Partial rollout**.
Note that only one version can be released to **Production** at a time. For **Partial rollout**, you can add target users for that specific version of the mini app.
Tip: Selecting **Partial rollout** and setting your rollout percentage to 0 effectively acts as preview mode, so only target users will be able to view your mini app.
## Import sandbox configuration to your draft app (optional)
If you have been using a sandbox for testing and plan on using its configurations for the live version of your app, you can import your sandbox's configuration to your draft app. Ensure that all of the information, assets, and settings in your sandbox are production-quality before beginning the import process. Also, make sure that you have already tested your mini app with a target user account.
In the **Sandbox **section of your app page, click the **More options** button next to the desired sandbox. Click **Import Configurations** to overwrite the existing configurations of the draft version with your sandbox configurations.
[Learn more about importing your sandbox configuration](https://developers.tiktok.com/doc/add-a-sandbox#).
## Provide submission details for app review
Perform a final check your of your draft app to ensure the mini app is ready for submission.
Before submitting for review, ensure that your mini app abides by the following guidelines.

| **Fields** | **Requirements** |
| --- | --- |
| App icon | The app icon must be a clear image. The app icon must not contain any sensitive or inappropriate content. The app icon must not be easily confused with another well-known brand icon. The app icon must be consistent with the app name or brand. |
| App name | The name should be appropriate and not contain any sensitive terminology. Examples: Any adult content, like lottery, gambling, abortion, violence, drugs, and any potentially negative or harmful content, like conspiracy theories, terrorism, and more. The name should not be, include, or be attempting to copy the name of other well-known apps. Examples: TikTok, Tik Tok, T1kTok, and use of a few characters together with Tik/Tok. The name matches the description. |
| Description | [[Apps will not be approved if they match the following: They contain sensitive terminology. They are for private or personal use. They are still in development or testing. Their end users do not fit the TikTok platform: The app targets children. The app targets users who live in: China (Mainland & Hong Kong), India, Iran, Syria, Cuba, North Korea, Crimea, Luhansk, Donetsk. They provide products or services that violate the TikTok Community Guidelines](https://www.tiktok.com/community-guidelines/en/). They violate TikTok Developer Terms of Service](https://www.tiktok.com/legal/tik-tok-developer-terms-of-service). |
| Terms of Service URL | Must be easily accessible. Must lead to a Terms of Service page. |
| Privacy Policy URL | Must be easily accessible. Must lead to a Privacy Policy page. |

Your mini app service must also meet the following:
- Must be accessible and fully developed.
- The service is relevant to the app name & description.
- Provide a good user experience without any experience design that is obviously counterintuitive to users.
Go to the **App Review** section of your app page, and provide detailed information about how your mini app works, and whether you are submitting for an initial release or an update.
After submission, your mini app status will be **In Review**. Your app will be reviewed within one to three days.
After your mini app is approved, its status will change to **Live** and online users will be able to access your mini app.
## View mini app
You can view your mini app after it has been reviewed and approved, and the app status appears as **Live** in the Developer Portal.
From the** Live** version of your app on the Developer Portal, go to the **Code assets** section. Then click the **View** button next to the version of your mini app that you want to view.
Scan the QR code with the TikTok app to view the mini app. For apps released to production, the designated percentage of TikTok users will be able to view the mini game. For partially rolled out apps, the designated percentage of TikTok users and all target users will be able to view the mini game.
## Post-publication
[After your mini app is published and publicly available as a TikTok Minis, users can submit reports to provide feedback about user experience, payment issues, or content violations. Refer to the report handling guide](https://developers.tiktok.com/doc/minis-report-handling-guide) for more details.
Was this document helpful?