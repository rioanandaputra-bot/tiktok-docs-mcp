Docs
# TikTok Webhooks
## Overview
Webhook is a subscription that notifies your application via a callback URL when an event happens in TikTok. Rather than requiring you to pull information via API, you can use webhooks to get information on events that occur. Notifications are delivered via HTTPS POST in JSON format to the callback url configured for your app in the Developer Portal. This information can be used to update your system or to trigger business processes.
## Requirements and Limitations
In order to receive a webhook message, callback URL should be registered in the client application on TikTok Developer Portal. This callback url can be configured either during the initial application or after the client key has been provisioned by updating the application.
The callback URL must do the following:
- Immediately respond with a 200 HTTP status code to acknowledge the receipt of the event notification.
- The callback URL endpoint must require HTTPS.
If a 200 HTTP status code is not returned, TikTok assumes that the delivery was unsuccessful. TikTok retries the delivery of event notification for up to 72 hours using exponential backoff. After 72 hours, the notification is discarded and not sent again.
TikTok makes a best effort for "at least once delivery" of webhooks. Webhook endpoints might receive the same event more than once. There should be a guard against duplicated event receipts by making your event processing idempotent.
Was this document helpful?