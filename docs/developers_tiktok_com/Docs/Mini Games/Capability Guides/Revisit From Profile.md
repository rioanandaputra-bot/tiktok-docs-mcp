Docs
# Revisit From Profile
This capability encourages users to collect a reward after reopening the mini game from the sidebar on their TikTok profile page. The purpose of this capability is to boost retention, especially for mini games with advertising campaigns.
**Note**: Integration with this capability is mandatory for mini games.
## Precautions
If you have accessed the mini games but the entry point still doesn't appear, it's usually because your account's region is not in the regions where the mini game function is currently available (such as US, JP, ID). You can troubleshoot using the following steps:
- Check your account's region: You can check your account's region by going to your profile page, tapping the **More options** icon in the upper corner, tapping **Settings and privacy**, going to **Account**, then tapping **Account information**. If the region is not displayed, it is likely defaulted to the IP address of your most recent login.
- Create an account in the target region: Taking the US as an example, if you have an App Store account in the US region, it is recommended to log in directly with that account. If you need to create a new account, you need to use a US SIM card and a US VPN node to complete the account registration.
- If none of the above methods solve the problem, please try logging in with another device that meets the requirements.
## Guidelines for implementation
For optimal usage, we recommend adhereing to the following guidelines when implementing the mandatory home screen shortcut capability.
- Timing and placement
- The earlier the better: The guidance should appear early in the user's login process, such as on the first screen after entering the game. If the game requires a new user tutorial, the return visit activity prompt should appear immediately after completion, ensuring user education is completed early on.
- Prominent location: Display the icon on the game's first screen as a primary entry point.
- Benefit settings: Provide two or more benefits (all in-game hard currency—currency, stamina, or equipment, for example) to ensure a rich reward system and increase user appeal. If only one reward is offered, it should be of medium to high quality to ensure attractiveness and variety.
- Guidance tips
- Static guidance: Guide the user through 3 steps (click the sidebar → click to enter the game → claim rewards) with finger icon prompts, ensuring smooth transitions and guiding the user back to the game;
- Dynamic guidance: Use dynamic animation to demonstrate the sidebar entry process, ensuring smooth transitions and guiding the user back to the game;
- Post-completion guidance
- Daily check-in: High priority recommendation. If the user accesses the mini-game from the sidebar for at least 3 days within 7 days, a highlighted bubble prompt will be triggered on the profile page (retained for 60 days), further enhancing user awareness.
- Set up "daily rewards," allowing users to receive corresponding rewards daily by entering the game from the sidebar daily (rewards can be lower than the initial addition), strengthening user awareness of this entry point and cultivating return visit habits. If subsequent internal verification shows this entry point is highly valuable to the game, higher-level rewards can be used to reinforce the guidance.
- Icon retention: After the user completes the activity or claims the daily entry reward, the icon reminder remains, reinforcing user awareness of this entry point.
- Other possible directions: Add profile sidebar guidance to in-game tasks or check-in tasks, with rewards upon completion.
## Access scheme recommendations
### Newcomer guidance period
- After the initial walkthrough, an entrance activity guide appears, and a guide appears at the primary entrance.
- The guide provides detailed steps and uses finger icons to indicate the specific entry location, and rewards can be claimed after completing the operation and returning.
- Game rewards provide mid to high-level equipment to attract users.
### Daily fixed incentive
- After the initial walkthrough, an entrance activity guide appears, and a guide appears at the primary entrance.
- The guide provides detailed steps and uses finger icons to indicate the specific entry location, and rewards can be claimed after completing the operation and returning.
- Benefits settings: Provide two in quantity and are relatively high-value.
- When adding a reward for the first time, provide in-game hard currency (currency and stamina).
- Set up daily revisit rewards, using rare characters and stamina as incentives, to cultivate users' revisit habits.
- The entry prompt remains after the follow-up visit guidance activity is completed.
- If a user accumulates at least three days of access from the sidebar within seven days, a highlighted guiding bubble will be separately generated on the personal page to attract clicks and further improve the conversion rate of the entry point.
### Multilingual adaptation
It is recommended to adapt the language for users in different regions. The following is the copy reference, and developers can adjust it according to the actual in-game design:
- **English**:
- Pop-up title: Revisit Reward
- Educational copywriting:
- Tap the menu icon in Profile
- Open [TikTok Minis Name]
- Get your reward
- Jump button: Get started
- Reward claim button: Get reward
- **Japanese**:
- Pop-up title: Return Visit Reward
- Educational copywriting:
- Please tap the menu icon in the profile
- Open [TikTok Minis Name]
- Get your reward
- Jump button: Start
- Reward claim button: Obtain Rewards
- **Indonesian**:
- Popup Title: Revisit Reward
- Educational copywriting:
- Tap the menu icon in Profile
- Buka [TikTok Minis Name]
- Dapatkan hadiahmu
- Jump button: Get started
- Reward claim button: Get reward
## Technical integration
[This flow allows users to receive a reward after opening the mini game from their profile sidebar. For more details, see the revisit incentive JavaScript APIs](https://developers.tiktok.com/doc/mini-games-sdk-revisit-incentives).
**Note:** These APIs require **TikTok version 41.0.0** or higher. Always use `canIUse()` first to check compatibility.
- Before calling the API, check if the function is available in the current TikTok version with `canIUse`.
```
if (TTMinis.game.canIUse("startEntranceMission")) {
    // Proceed to call the API
}
```
- Execute the `startEntranceMission` function. This navigates the user to the TikTok profile sidebar, effectively completing the follow-up education task.
```
TTMinis.game.startEntranceMission({
  success: () => {
    // Log or handle the successful navigation to the sidebar
    console.log("Successfully jumped to the sidebar of the home page");
  },
  fail: () => {
    // Handle failure to jump
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
- After the user has completed the entrance/sidebar mission (usually by visiting the sidebar via Step 1), the game can award them.
- Check reward status: Call the `getEntranceMissionReward` API. This checks the user's eligibility for the reward associated with the sidebar revisit mission.
- Handle success: Check the `canReceiveReward` boolean in the success callback.
```
TTMinis.game.getEntranceMissionReward({
  success: ({ canReceiveReward }) => {
    if (canReceiveReward) {
      // If true, grant the reward (coins, items, etc.) in your game logic
      console.log("User is eligible for the entrance mission reward");
    } else {
      console.log("User is not currently eligible for the reward");
    }
  },
  fail: () => {
    // Handle failure to check status
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
## Debug the reward results
[When debugging your mini game, use TikTok's DevTool to debug the home screen shortcut function. Learn more about the debugging process](https://developers.tiktok.com/doc/debug-your-mini-game).
- Let `ttmg dev` open the debugging environment:
```
cd path/to/your/game

ttmg dev
```
- Select the new launch mode:
- Set the startup mode of the profile revisit entry (select "Revisit From Profile" as the entry scene)
- Scan the QR code to simulate the shortcut entry and start debugging the reward distribution results**.**
```
TTMinis.game.getEntranceMissionReward({
  success: ({ canReceiveReward }) => {
    console.log("success", canReceiveReward);
  },
  fail: () => {
    console.log("fail");
  },
  complete: () => {
    console.log("complete");
  }
})
```
Was this document helpful?