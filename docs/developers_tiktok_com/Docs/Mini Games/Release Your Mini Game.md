Docs
# Release Your Mini Game
This guide explains the process for releasing your mini game to users:
- Upload your code
- Preview your mini game in TikTok
- Submit a version for review
- Release to users
## Prerequisites
Before you begin the publication process, ensure you have completed the following prerequisites:
- [Your organization has been verified as a business](https://developers.tiktok.com/doc/verify-your-business)
- [Your organization has completed industry qualification review](https://developers.tiktok.com/doc/industry-qualification-review)
- [Your mini game's basic information](https://developers.tiktok.com/doc/basic-information-specifications) has been submitted and approved
- [You have integrated your mini game with all of the required capabilities](https://developers.tiktok.com/doc/develop-your-mini-game#)
## Upload Your Code
After you have a package of your mini game's code that integrates with TikTok functionalities and has been debugged, you are ready to upload it to the Developer Portal.
### Code scanning requirements
Package your code artifacts into a ZIP file that does not exceed 200 MB. Make sure your package contains all of the files in your directory and meets the following requirements for code scanning:
- The TikTok Login API functionality must be implemented.
- It must not contain any empty files (zero bytes).
- Restrict the sources of dynamically imported scripts to prevent bypassing platform reviews and arbitrary updates.
- Limit the sources of runtime API requests. The Minis platform ensures traceability of third-party API request scopes, allowing only domains declared in the local configuration file to make valid requests.
Please be aware that if your ZIP file does not meet our requirements, you may be unable to upload your file to the Developer Portal.
### Upload your code as a preview version
Once uploaded, the code asset will be listed as a preview version. You can have up to 30 preview versions.
Note: Your code asset file must be a ZIP file, maximum 200 MB.
- On your app page, click the **Code version** tab.
- Click the **Upload code asset** button.
- Select your code asset type and upload the file.
- You can add notes for your own reference. This is recommended if you plan to upload multiple preview versions.
- Click the **Add asset **button.
Once your code asset is uploaded, it will appear in the **Preview** section.
## Preview your app in TikTok
To preview a version of your app in TikTok, make sure you already have test users added.
- Click the **Preview** button on your code version card to display the preview QR code.
- Scan the QR code with the TikTok app. Make sure you are using the TikTok account of one of your test users.
## Submit a version for review
Before you submit your desired preview version for review, make sure you have submitted and received approval for the following prerequisites:
- Basic information
- Business verification
When you're ready, submit your desired app version:
- Click the **Submit for review** button on the code version card.
- Choose how you want to release your app version after it has been approved:
- **Release manually**: You can choose when and how to release your app after it has been approved.
- **Automatically release after approval**: The app version will be released as soon as it is approved.
- Choose the type of release.
- **Push to production**: Release the app version to all users on TikTok. If it's your first time releasing the app, you must choose the production release type.
- **Gray release**: Release the app version to a percentage of users on TikTok. To use gray release, you need to already have a version in production. Your percentage of users to release to must be greater than the current release percentage.
After you submit, your code version will move to the** In-review** section as we review your code. Your app’s Basic Information will cross-referenced during the review. Your app must be compatible with English in order to pass the review.
## Release to users
Once your app has been approved, its status will change to **Ready For Release**. You can then release it to users.
- If you selected manual release, click the **Release** button to choose the release type.
- If you selected automatic release, your app will be released as soon as it is approved.
You are allowed to have two released versions in total: one production version, and one gray release version. Note the following about release types:
- A production version must remain online to keep your app accessible. You can only release a version to production for the first-time launch.
- You can have one gray release version online, where you can configure its traffic distribution. It will share traffic with the production version.
- The release percentage of the production version will automatically adjust based on the traffic percentage assigned to the gray release version. Their combined traffic will always total 100%.
**Note**: Different regions may have different requirements for release, such as the following:
- [United States: Approval from TikTok to launch in the US. Learn more about requesting approval for US launch](https://developers.tiktok.com/doc/launch-your-app-to-us-users-minigames).
- Vietnam: G1 Online Game License from the Vietnam Ministry of Information and Communications.
Was this document helpful?