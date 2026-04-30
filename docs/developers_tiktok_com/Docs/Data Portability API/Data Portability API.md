Docs
# Get Started
This guide will show you how to apply for the Data Portability API and what you need to become fully integrated and approved to use the Data Portability API functionality.
## Prerequisites
Before you start, you will need access to the following:
- A TikTok developer account on the TikTok for Developers website.
- A registered app on the TikTok for Developers website. The app must at least be in **Staging **status to generate an App ID (a numerical code that uniquely identifies your app).
- Screenshots of detailed UX mockups showing the user flow for your app's use case.
## Apply for access
- Go to the **Manage apps** page and select your app, or **Connect an app** if you don't have one yet.
- On the app page, click the **Add products** button under **Products**, then add **Data Portability API**.
- Add the **Login Kit** and **Webhooks** products to your app as well.
- On the **Data Portability API** product, view scopes, then click **Apply** to access the application for Data Portability API.
- Fill out the **Data Portability API Application** form and submit. Make sure to select all necessary scopes on the form.
- Wait for approval. You can typically expect to hear back within 3-4 weeks. You can check for scope approval status on the app page.
- Once you have received approval, you can choose which approved scopes to add to your app on the **Data Portability API** product.
- Fill out the information on the app page, including under **Login Kit** and **Webhooks**.
- Click **Submit for review**, and we will start reviewing your app.
NOTE: You may submit your app for review before your Data Portability API Application is processed.
Once you are approved for Login Kit, Webhooks, and the Data Portability API scopes, you can start using the Data Portability API functionality for your app.
## Get permission
All the scopes for calling Data Portability APIs are in the form `portability.`**<data type>**`.single`  and `portability.`**<data type>**`.ongoing`
With **<data type>** being: `all`, `activity`, `directmessages`, and `postsandprofile`. There are eight available scopes, as described below.
All data
- portability.all.single: Make a single request for all available data on the user's behalf
- portability.all.ongoing: Make ongoing requests for all available data on the user's behalf
Posts and profile
- portability.postsandprofile.single: Make a single request for posts and profile data on the user's behalf
- portability.postsandprofile.ongoing: Make ongoing requests for posts and profile data on the user's behalf
Activity
- portability.activity.single: Make a single request for activity data on the user's behalf
- portability.activity.ongoing: Make ongoing requests for activity data on the user's behalf
Direct messages
- portability.directmessages.single: Make a single request for direct message data on the user's behalf
- portability.directmessages.ongoing: Make ongoing requests for direct message data on the user's behalf
NOTE: Subsequent requests made using ongoing permission (or made with multiple one-time authorizations) will return the full data for the given scope.
[You can visit the Data Types](https://developers.tiktok.com/doc/data-portability-data-types/) page to see more detail about what information is included for each scope.
## Lifecycle of a data request
Once authorized, making a data request for a given user involves a few steps:
- Request data
- [Use the Add Data Request](https://developers.tiktok.com/doc/data-portability-api-add-data-request/) endpoint to start a data export. In your request, you should indicate the categories of data you're requesting (all_data, activity, video, profile, direct_message), which the user should have authorized permission for. If they haven't authorized permission, the response will include an error.
- (If desired) Check the status of an ongoing request
- [Use the Check Status of Data Request](https://developers.tiktok.com/doc/data-portability-api-check-status-of-data-request/) endpoint to see the status of an ongoing request.
- (If desired) Cancel an ongoing request
- [Use the Cancel Data Request](https://developers.tiktok.com/doc/data-portability-api-cancel-data-request/) endpoint to cancel a request. If the user has allowed you to make ongoing requests, you can make another request using the same token.
- [Once a request is ready, we'll send notice to the callback URL you provided in the app page via webhook](https://developers.tiktok.com/doc/webhooks-events/). We aim to provide data within a few seconds, minutes, or hours, depending on the data requested. However, this is not guaranteed, as unforeseen technical issues may cause delays.
- [Once you receive the callback, you can download the data](https://developers.tiktok.com/doc/data-portability-api-download/) with a Download request. Data will be available to download for four days after it's been prepared.
NOTE: You are not required to set up webhooks to receive notifications. Instead, you can check the status of the request and download the data once it is ready.
Was this document helpful?