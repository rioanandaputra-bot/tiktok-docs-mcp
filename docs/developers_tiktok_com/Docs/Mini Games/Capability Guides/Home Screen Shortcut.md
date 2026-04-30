Docs
# Home Screen Shortcut
The home screen shortcut is a capability that allows users to add a shortcut to your mini game on their device's home screen. The purpose of this capability is to boost retention, especially for mini games with advertising campaigns.
**Note**: Integration with this capability is mandatory for mini games.
## Guidelines for implementation
For optimal usage, we recommend adhereing to the following guidelines when implementing the mandatory home screen shortcut capability.
- Timing and placement
- The earlier the better: When prompting the user to add the home screen shortcut, try to display the guidance as early as possible. For example, right after the user enters the game for the first time. If the game requires a novice tutorial first, then directly present the "Add to Home Screen" revisit activity after tutorial completion to ensure that user education is completed at the earliest stage possible.
- Prominent location: Display the icon on the game's first screen as a primary entry point, and also provide an "Add to Home Screen" entry point on the login screen;
- Benefit settings
- High rewards: Provide 2 or more benefits (all in-game hard currency—currency, stamina, or equipment, for example) to ensure a rich reward system and increase user appeal
- Significant reward investment: Since the home screen can generate more revenue from returning users later, it is recommended that the rewards for this re-engagement activity be higher than other entry points, such as increasing the quantity or quality of rewards, to enhance user awareness of this entry point
- Copywriting guidance: Optional. Provide a separate "Add to Home Screen" guidance icon to inform users of the detailed steps
- Post-completion guidance
- Daily check-in: High priority recommendation. Set up "daily rewards," allowing users to receive corresponding rewards daily by entering the game from the home screen (rewards can be lower than the initial addition), strengthening user awareness of this entry point and cultivating return visit habits. If subsequent internal verification shows this entry point is highly valuable to the game, higher-level rewards can be used to reinforce the guidance.
- Icon retention: After the user completes adding to the home screen or claims the daily entry reward, the "Add to Home Screen" icon reminder remains, reinforcing user awareness of this entry point.
- Exit guidance: Provide "Add Now" guidance after the user exits the game (platform mechanism, check if your game has this feature).
- Other possible directions: Add home screen shortcut guidance to in-game tasks or check-in tasks, with rewards upon completion.
## Access scheme recommendations
### 7-day check-in tiered incentive
- "Add to home screen" shortcut display appears immediately after the newbie guide ends
- The rewards are highly generous, all being in-game hard currency and the reward tiers tend to be above average
- Keep the "Add to home screen" icon entry prompt after adding the home screen is completed
- Set the "Daily Reward", with the reward content being half of the first addition, to enhance users' subsequent revisit to the home screen
- Prompt "Add to home screen subscription" when exiting the game
- 7-day event: Log in via home screen launch to receive tiered rewards
### Daily fixed incentive
- The game's first screen displays a primary entry point for "Add for Rewards", clearly indicating that adding to the home screen can earn relevant rewards
- The rewards are highly generous, all being in-game hard currency and the reward tiers tend to be above average
- Prompt "Add to home screen subscription" after exiting the game
- Keep the "Add to home screen" prompt even after the "Add to home screen" guide is completed
- After logging in daily, you can claim fixed rewards through the in-game "Add to home screen" event entry
## Technical integration
[This flow allows users to receive a reward after adding a shortcut to their mini game on their home screen. For more details, see the revisit incentive JavaScript APIs](https://developers.tiktok.com/doc/mini-games-sdk-revisit-incentives).
**Note:** These APIs require **TikTok version 41.0.0** or higher. Always use `canIUse()` first to check compatibility.
- Before calling the API, check if the function is available in the current TikTok version with `canIUse`.
```
if (TTMinis.game.canIUse("addShortcut")) {
    // Proceed to call the API
}
```
- Execute the `addShortcut` function. This will typically trigger a system-level prompt asking the user for permission to add the icon.
```
TTMinis.game.addShortcut({
  success: () => {
    // Log or handle the success (User confirmed and shortcut was added)
    console.log("Shortcut successfully added to home screen");
  },
  fail: (error) => {
    // Log or handle the failure (User declined or an error occurred)
    console.log("Failed to add shortcut", error);
  },
  complete: () => {
    // Cleanup or final actions
  }
});
```
- After the shortcut has been added, the game can check and award the user.
- Check reward status: Call the `getShortcutMissionReward` API. This API checks the user's status for the "add-to-home-screen" mission.
- Handle success: The success callback should check the returned boolean value, `canReceiveReward`, to determine the next action.
```
TTMinis.game.getShortcutMissionReward({
  success: ({ canReceiveReward }) => {
    if (canReceiveReward) {
      // If true, grant the reward (coins, items, etc.) in your game logic
      console.log("User is eligible for the shortcut mission reward");
    } else {
      console.log("User is not currently eligible for the reward");
    }
  },
  fail: (error) => {
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
- Set the startup mode of the home screen shortcut entry:
- Scan the QR code to simulate the shortcut entry and start debugging the reward distribution results**.**
```
TTMinis.game.getShortcutMissionReward({
  success: ({ canReceiveReward }) => {
    console.log("success", canReceiveReward);
  },
  fail: (error) => {
    console.log("fail", error);
  },
  complete: () => {
    console.log("complete");
  }
})
```
Was this document helpful?