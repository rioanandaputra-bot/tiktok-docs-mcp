Docs
# Set Up Development Configuration
On your app's **Development configuration** page, you must configure several methods to validate and restrict access to certain web endpoints, ensuring security and controlled integration.
- **Security**: Specify trusted domains for your app, as TikTok will only support requests to these trusted domains.
- **Webhooks**: Enter a callback URL for TikTok to notify your application when an event occurs, like a payment transaction using TikTok's APIs.
- **URL properties**: Verify ownership of URLs in your app configuration by domain or URL prefix.
## Add trusted domains
During runtime, your app can only initiate network requests to trusted domains that have been registered. Any domain not registered will be denied access. Therefore, all domains involved in network requests for your app must be registered here.
To add trusted domains for your app, complete the following steps:
- Click the **Security** tab on your **Development configuration** page.
- Click the **Add domain** button to enter a URL.
- Domains must start with `https://` and cannot contain wildcards or paths.
- You can add up to 20 domains.
- Click the **Save changes** button.
## Set up webhooks
When your app is ready to receive webhooks notifications, you can use this webhooks module to confirm that it will handle the request correctly. To set up webhooks for your app, complete the following steps:
- Click the **Webhooks** tab on your **Development configuration** page.
- Enter a callback URL. TikTok will push messages to this URL when a specified event occurs.
- Click the **Test URL** button to send a test event. We'll send a POST request to your callback URL when you click the **Send** button.
- Once you've verified that your application received the request correctly, click the **Save changes** button.
[Learn more about webhooks](https://developers.tiktok.com/doc/webhooks-overview).
## Verify URL ownership
You must verify URL properties for all URLs in your app configuration. Some features require URL verification before they can be used, like Link Sharing and Content Posting API. There are two cases for URL verification, depending on when the app was created.
To verify URL properties, complete the following steps:
- Click the **Webhooks** tab on your **Development configuration** page.
- Click the **Verify properties **button.
- Choose whether to verify your URL by **Domain** or **URL prefix**:
- For verification by Domain, enter your domain and subdomain name, then click **Verify**.
- For verification by URL prefix, enter your complete URL, then click **Verify**. Download the provided signature file, then upload it to your URL.
Was this document helpful?