Docs
# Add a Sandbox
**Sandbox** mode is a restricted environment that allows you to try out integrations without having to submit your app for review. You can create multiple sandboxes for your app to experiment with different configurations without compromising the live version of your app. You can create up to 5 sandboxes.
## Prerequisites
Before registering your app, do the following:
- [Create a TikTok developer account from our signup page](https://developers.tiktok.com/signup) using your email.
- [Create or join an organization](https://developers.tiktok.com/doc/working-with-organizations/) representing the owning group of the app. This step is highly recommended but not required.
[You will also need access to a URL decoder to authorize target users](#authorize_target_users_with_login_kit).
## Create a Sandbox
This workflow demonstrates how to create your first sandbox.
- Go to the **Manage apps** page, then select an app or **Connect an app** if you don't have one yet.
- On the app page, switch the toggle next to your app's name to **Sandbox**.
- Click the **Create Sandbox **button, then enter a name. You can choose to clone an existing configuration from your app's production versions or another sandbox.
- Click **Confirm** to create the sandbox.
- Configure the sandbox as desired by editing **App details** and adding products.
Note: Sandbox mode does not offer access to Content Posting API for public videos or Data Portability API.
- Click **Apply changes** to save changes and make your configuration take effect.
To create another sandbox, click the [**+**] button (**Create Sandbox**) in the left navigation panel.
## Manage target users
Adding target users to a sandbox allows them to try out your sandbox configurations. To add a TikTok account that you own as a target user, you must provide its login credentials. You can add up to 10 accounts.
- Go to **Sandbox settings** on the app page.
- Under **Target users**, click **Add account**. You will be redirected to log in to a TikTok account.
- Log in to the TikTok account and agree to the TikTok Developer Terms of Service.
Your target users will be displayed on your app page after they have been added. Results may take up to an hour to show after you refresh the page.
### Authorize target users with Login Kit
[After you add target users, you may authorize them if you want to use Login Kit and the other products dependent on it. Authorization workflows for Web, Desktop, iOS, and Android are available in the Login Kit documentation](https://developers.tiktok.com/doc/login-kit-overview).
## Import your Sandbox configuration
You can import a sandbox's configuration to a **Draft** of your app in production. Doing so will overwrite the draft's existing configuration with the chosen sandbox configuration.
Note: You can only import a sandbox configuration to a **Draft **in **Production **mode.
- On the app page, switch the toggle next to your app's name to **Production**.
- Click **Draft** in the left navigation panel.
- Click **Import**, then select the sandbox you want to import from.
If you have a version of the app that has been approved and is live, you can revert back to that configuration by clicking **Revert to Live version **in the** Import **dropdown.
[[When you are ready to submit your app](https://developers.tiktok.com/doc/getting-started-create-an-app#submit_your_app_for_review), make sure that it follows our app review guidelines](https://developers.tiktok.com/doc/app-review-guidelines).
[For further inquiries or assistance, contact us through our Support form](https://developers.tiktok.com/support?topic=sandbox).
Was this document helpful?