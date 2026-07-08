# Data Portability API

> Consolidated from 8 source files.



---
## SOURCE: Data Portability API/Data Portability API.md

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


---
## SOURCE: Data Portability API/Data Portability Application Guidelines.md

Docs
# Data Portability Application Guidelines
[To ensure a successful submission to the Data Portability API, please review these guidelines for each question carefully, including the FAQ](https://developers.tiktok.com/doc/data-portability-api-faq/). If your application does not meet the criteria below, you may be required to resubmit your application or be requested to provide more details, which may delay your application's review.
**Application details**
- **Applicant name**
_Enter the name of your representative or employee, rather than a business/organization name. TikTok may reach out to this person about your application via the email provided below. _
- **Applicant email address**
_Use an email address that matches your business/organization domain. TikTok may reach out to this person about the application. _
- **Organization name**
_Please ensure that your business/organization is accurately entered._
- **Organization website **
_Please check that your website is live and working as expected, and is not a holding page or otherwise incomplete website. _
- **TikTok representative email**
_Optional: If you have a contact at TikTok you already work with, you can enter their email address here. We may reach out to them if there are issues with your application. _
- **App ID**
_Please ensure your App ID is correct and matches the app that you intend to make a submission for (if you have multiple apps). To view a list of your apps and their corresponding App IDs, log in to your TikTok for Developers account, click the profile icon, then click Manage apps. _
**Data scope & use case**
- **Data scope(s) required**
_This selection must clearly match the description and UX mockups you provide._
- **Provide a detailed explanation about how the requested data scope(s) will be used for your use case**
_Explain in detail how your data scope is appropriate for the intended use case. Describe exactly how the UX flow demonstrated in your uploaded mockups matches your data scope(s). _
- **Upload high-fidelity UX mockups**
_Your upload must match your previous answers and demonstrate the end-to-end user journey,. This includes showing four distinct screens that clearly illustrate each step outlined below. _
_Your app must clearly inform users what data will be transferred to TikTok and for what purpose. By requiring high-fidelity UX mockups, TikTok aims to ensure that users are being provided with adequate information before proceeding with a transfer._

|  | **TikTok connection page ** Show the initial option(s) where users can see "Connect to TikTok", or similar. Demonstrate where your users can select TikTok to connect it to your product or service. |
| --- | --- |
|  | **Connecting to TikTok ** Display to users that your service is connecting to TikTok. Give users the ability to "Proceed", "Go back", or similar. Clearly explain to the user what is happening, including an outline of the data being shared and an explanation of why this data is being requested. |
|  | **Confirmation of connection ** Show TikTok's login authorization page. This is TikTok's page that cannot be modified. However, please include this page in your UX mockups to demonstrate when it is expected to appear in the user journey. |
|  | **Final output / result ** Demonstrate confirmation that your app successfully connected to TikTok. If applicable, this page can also show the user output (synced data, complied data, and more). |

**GDPR & Data subject requests**
- **Describe how you enable and respond to users making data subject requests**
_Provide a detailed response that clearly outlines how users can make requests for their data and get a copy of it from your business/organization. Alternatively, you may provide a link to a page where this information is already outlined, such as your privacy policy._
- **Do you wish to upload any supporting evidence or documents for data subject requests?**
_Optional: For example, if you wish to upload a PDF version of your privacy policy to support your prior answer, you may do so here. _
**Data protection policy and processes**
- **Outline or provide links to relevant documentation that explain your data protection policy and processes**
_Please provide a detailed response or a link to a page where this information is already outlined, such as your privacy policy._
- **Do you wish to upload any supporting evidence or documents for data policy or processes?**
_Supplement your application with additional information, such as relevant legal or policy documents._
Was this document helpful?


---
## SOURCE: Data Portability API/Data Portability FAQ.md

Docs
# Data Portability FAQ
### General
- **Why do I need to fill out the Data Portability API Application form?**
TikTok needs to assess each application to ensure that requests are valid and are made by genuine companies or services. This is to ensure the privacy and security of user data.
- **How does the Data Portability API Application differ from App Review?**
[The Data Portability API is a functionality that developers can add to their apps. To protect user data privacy, developers must complete an application form and receive approval. App Review is a separate review of the developer app itself, to ensure that the app is eligible to integrate with our services. Learn more about the App Review process](https://developers.tiktok.com/doc/our-guidelines-developer-guidelines/).
### Data Portability API Application
- **What languages do you support on the application?**
Please submit your entire application in English, including the UX mockups and any other uploads.
- **Can I apply for the Data Portability API before I submit my app or website for review?**
Yes, you can submit an application for the Data Portability API while your app is in Draft status.
- **What if I cannot supply all the information being requested?**
You must complete all required fields to submit your application.
- **What happens after I submit my application?**
TikTok will review your application, which may take 3 to 4 weeks from the application submission date. You will receive a notification email after your application is processed.
- **Will a TikTok representative contact me about my application?**
A TikTok representative will assess your application, and if applicable, may reach out to request follow-up information with the email that you provide on your application form.
- **What happens if I am not approved?**
If you are not approved, you can reapply at any time. Click the **View scopes** button under the **Data Portability API** product on the app page to access the application form.
- **What should I do if I made a mistake or need to resubmit my application?**
[Please submit a support ticket](https://developers.tiktok.com/support/) and select **Data Portability API** as the **Topic**.
- **What happens after I go live with Data Portability API? **
TikTok reserves the right to periodically check that your application continues to match your app or website, and may revoke access if application terms are breached.
- **What are the daily quota limits? Can I request an increase in the quota limit?**
Currently, the daily limit is set at 1000 requests per minute, allowing you to make up to 1000 requests of any given type per minute for the Data Portability API.
[If you believe a quota limit increase is necessary for your application, please contact us via Support](https://developers.tiktok.com/support/) and we'll take your request into consideration.
- **Can I get a copy of my application?**
We are unable to supply a copy of your application and recommend that you make your own copy of the information that you provide for your reference.
Was this document helpful?


---
## SOURCE: Data Portability API/API Reference/API Reference.md

Docs
# Add Data Request
Use POST request to create a data download request.

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/add/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: request_id | request_id | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| data_format | string | Format in which the individual data files will be returned. Valid values are: text json | "text" | Yes |
| category_selection_list | list<string> | Type of data that is to be returned. See <Data Categories>. Valid values are: all_data video profile activity direct_message | ["profile", "activity"] | Yes |

#### Scopes required for categories

| **Data Categories** | **Required Scopes** |
| --- | --- |
| activity | portability.activity.single, portability.activity.ongoing |
| video, profile | portability.postsandprofile.single, portability.postsandprofile.ongoing |
| direct_message | portability.directmessages.single, portability.directmessages.ongoing |
| all_data, activity, video, profile, direct_message | portability.all.single, portability.all.ongoing |

Notes:
- If "all_data" is sent as a parameter in `category_selection_list`, it will take precedence over other categories.
- For any `portability.*.single` scope, **Add Data Request** can only be called once to create a new request.
- For cases where multiple `portability.*.single` scopes are authorized by the user:
Example:
If scopes `portability.all.single` and `portability.activity.single` are authorized by the user and a request with `"category_selection_list" : ["activity", "video"]` is made.
The only scope consumed will be `portability.all.single`, as it has access to all the categories.
After making the request, the current access token will contain the scope `portability.activity.single` and a new request for the category `activity` can be made after the current request is fulfilled without reauthorizing the access token from the user.
### Request Example
```
curl --location 'https://open.tiktokapis.com/v2/user/data/add/?fields=request_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemp123.e1' \
--data '{
    "data_format": "text",
    "category_selection_list": ["profile","direct_message"]
}'
```
## Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | AddUserDataResponseData | See the response example below |
| error | ErrorStructV2 | See the response example below |

### AddUserDataResponseData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This will be a required query parameter to get request status, cancel request, and download the data. | 123451234512345 |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string | ok |
| message | string | The detailed error description |  |
| log_id | string | The unique ID associated with every request for debugging | 1010xyz10101asdf1010101010100a12abc24 |

### Response Example
```
{
    "data": {
        "request_id": 123451234512345
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "1010xyz10101asdf1010101010100a12abc24"
    }
}
```
Was this document helpful?


---
## SOURCE: Data Portability API/API Reference/Cancel Data Request.md

Docs
# Cancel Data Request
Use POST request to cancel the data download request

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/cancel/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | string | The requested fields: request_id | request_id | Yes |

### Request Example
```
curl --location 'https://open.tiktokapis.com/v2/user/data/cancel/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemp123.e1' \
--data '{
    "request_id": 123451234512345
}'
```
## Response
A successful cancellation request will return an "ok" message in the error response. In case of failure, a verbose error message will be returned

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| error | ErrorStructV2 | See the response example below |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string | ok |
| message | string | The detailed error description |  |
| log_id | string | The unique ID associated with every request for debugging | 1010xyz10101asdf1010101010100a12abc24 |

### Response Example
```
{
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "2023242526272829300000000000001111"
    }
}
```
Was this document helpful?


---
## SOURCE: Data Portability API/API Reference/Check Status of Data Request.md

Docs
# Check Status of Data Request
Use POST request to check the status of a data download request

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/check/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: request_id apply_time collect_time status data_format category_selection_list | request_id,status,apply_time | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API. | "text" | Yes |

### Request Example
```
curl --location 'https://open-platform.tiktokapis.com/v2/user/data/check/?fields=request_id,status,apply_time,collect_time,data_format,category_selection_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer act.testTemp123testtemo123!5328.e2' \
--data '{
    "request_id": 123451234512345
}'
```
## Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | GetUserDataResponseData | See the response example below |
| error | ErrorStructV2 | See the response example below |

### GetUserDataResponseData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| request_id | int64 | The `request_id`for which the status is requested | 123451234512345 |
| apply_time | int64 | UTC Unix timestamp at which the data collection was requested | 1703186989 |
| collect_time | int64 | UTC Unix timestamp at which the data collection was started | 1703187862 |
| status | string | Current status of the data which was requested to be collected. Valid values are: pending : Indicates the data is still being collected and not yet ready for download. downloading : Indicated the data is ready for download. expired : The Download User Data API can no longer fetch this information as it is expired. Request expires within 4 days from when it was ready to be downloaded. cancelled : The caller cancelled this request using the Cancel User Data API | "downloading" |
| data_format | string | Format requested in the initial Add Data Request API. Valid values are: json text | "text" |
| category_selection_list | list<string> | Type of data that was requested in the initial Add Request API. Valid values are: all_data profile activity video direct_message | ["profile", "activity"] |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string | ok |
| message | string | The detailed error description |  |
| log_id | string | The unique ID associated with every request for debugging | 1010xyz10101asdf1010101010100a12abc24 |

### Response Example
```
{
    "data": {
        "apply_time": 1703186989,
        "category_selection_list": [
            "profile",
            "video",
            "direct_messages"
        ],
        "collect_time": 1703187862,
        "data_format": "text",
        "request_id": 123451234512345,
        "status": "downloading"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "2023242526272829300000000000001111"
    }
}
```
Was this document helpful?


---
## SOURCE: Data Portability API/API Reference/Data Types.md

Docs
# Data Types
## Overview
TikTok's Data Portability API allows users to designate your app to receive one-time or ongoing transfers of their data. Your app can request transfers of a user's full data archive to enable backup and synchronizing use cases, or request specific categories of data. This page will document the data types included in the exports, including an overview of the fields included in a full export.
[If you have any feedback on the categories of data provided by the Data Portability API, you can contact support](https://developers.tiktok.com/support).
## Categories of Data
Your app can request permission to transfer specific categories of data, or export the user's full data archive.
### Posts and Profile
Provides access to:
- A user's profile information, including their follower and following list
- The posts they've made on TikTok
For Posts, we offer a URL that your app can access to download .mp4 or .jpg files, depending on the format of the post.
Data included:

| **Category** | **Fields** |
| --- | --- |
| Profile Information | Username |
| Email address (if provided and verified) |
| Telephone number (if provided and verified) |
| Date of birth |
| Likes |
| Bio (if present) |
| Profile photo / profile video (if provided) |
| Following List | Date |
| Username |
| Follower List | Date |
| Username |
| Posts | Date |
| Video Link |
| Title |
| Who can view |
| Allow comments |
| Allow stitches |
| Allow duets |
| Allow stickers |
| Allow sharing to story |
| Content disclosure |
| AI-generated content |
| Location |
| Sound |

### Activity
Provides access to data about a user's activity on TikTok.
NOTE: If data is not present for a given user, then that file or section will be empty or not present. For example, some features like Most Recent Location Data are not launched in all regions.

| **Category** | **Fields** |
| --- | --- |
| Comments | Date |
| Comment content |
| Favorite Effects | Date |
| Effect landing page link |
| Favorite Hashtags | Date |
| Hashtag landing page link |
| Favorite Sounds | Date |
| Sounds landing page link |
| Favorite Videos | Date |
| Video landing page link |
| Purchase History | Date |
| Price |
| Gifts | Date |
| Gift amount |
| Username |
| Hashtag | Hashtag Name |
| Hashtag landing page Link |
| Like List | Date |
| Video landing page link |
| Browsing History | Date |
| Video landing page link |
| Search History | Date |
| Search Term |
| Most Recent Location Data* | [Not available in most countries, file may be missing or empty] |
| Location Reviews | Location name |
| Date and Time of review created |
| Review content |
| Review status |
| Review interactions |

### Direct Messages
Provides access to the user's direct message history on TikTok.

| **Folder** | **Category** | **Fields** |
| --- | --- | --- |
| Direct Messages | Chat History | Date, from, content |

### Full Archive
The full data archive contains further categories of data. TikTok may launch new features from time to time, and we'll do our best to keep this documentation up to date.
Not all features are available in all regions. If a feature isn't live for a user, or a user doesn't have data, than the relevant file may be empty or missing from the archive.

| **Folder** | **Category** | **Fields** |
| --- | --- | --- |
| Profile | Profile Information | Username |
| Email address (if provided) |
| Telephone number (if provided) |
| Date of birth |
| Likes |
| Bio (if present) |
| Profile photo / profile video (if provided) |
| Linked Third-party Platform Name |
| Linked Third-party Account Profile Photo |
| Linked Third-party Account Name |
| Linked Third-party Account Description |
| App Settings | Settings | Allow Others to find me |
| Private Account |
| Personalized Ads |
| Who can comment on your videos |
| Who can view your liked videos |
| Who can Duet with your videos |
| Who can send you direct message |
| Who can Stitch with you |
| Allow your videos to be downloaded |
| Filter Comments |
| Ads Based on Data Received from Partners |
| Ads From Third-party Ad Networks |
| Content preferences: Interests, Video languages, Filter Video Keywords in For You feeds, Filter Video Keywords in Following feeds |
| Push notification settings: Desktop notification, New fans push notification, New Likes on my videos push notification, New Comments on my video push notification |
| Language: App Language Web language |
| Block List | Date |
| username |
| Posts | Posts | Date |
| Video Link |
| Title |
| Who can view |
| Allow comments |
| Allow stitches |
| Allow duets |
| Allow stickers |
| Allow sharing to story |
| Content disclosure |
| AI-generated content |
| Location |
| Sound |
| Comments | Comments | Date |
| Comment content |
| Direct Messages | Chat History | Date |
| From |
| Content |
| Activity | Favorite Effects | Date |
| Effect landing page link |
| Favorite Hashtags | Date |
| Hashtag landing page link |
| Favorite Sounds | Date |
| Sounds landing page link |
| Favorite Videos | Date |
| Video landing page link |
| Purchase History | Date |
| Price |
| Gifts | Date |
| Gift amount |
| Username |
| Hashtag | Hashtag Name |
| Hashtag landing page Link |
| Like List | Date |
| Video landing page link |
| Following List | Date |
| Username |
| Follower List | Date |
| Username |
| Browsing History | Date |
| Video landing page link |
| Login History | Date |
| IP address |
| Device Model |
| Device System |
| Network Type |
| Carrier |
| Status | Screen Resolution: 1280 x 720 |
| App Version |
| IDFA |
| GAID |
| Android ID |
| IDFV |
| WebID |
| Share History | Date |
| Shared Content |
| Link |
| Method |
| Search History | Date |
| Search Term |
| Most Recent Location Data* | [Not available in most countries, file may be missing or empty] |
| Ads and data | Off-TikTok Activity | Date |
| Source |
| Event |
| Ad Interests | Ad Interest Categories |
| TikTok Shopping* *Note: Not available in all countries; files may be missing or contain no data | Product browsing history | Date |
| Product name |
| Shop name |
| Shopping cart list | Creation date |
| Product information: {Name(title)/Quantity} |
| Shop name |
| Vouchers | Date received |
| Voucher ID |
| Voucher name |
| Discount details |
| Voucher status |
| Order history | Order date |
| Order number |
| Product information: {Name(title, parameter)/Quantity} |
| Total price (including shipping fee) |
| Customer note |
| Order status |
| Receiver's name |
| Receiver's phone number (partially masked) |
| Receiver's address |
| Fulfillment logistics provider |
| Fulfillment logistics tracking number |
| Product reviews | Post date |
| Order number |
| Product information: {Name(title, parameter)} |
| Shop name |
| Reviews |
| Returns and refunds history (Refund only) | Request date |
| Request date |
| Request number |
| Order number |
| Request type: Only refund |
| Reasons |
| Customer Note |
| Customer note attachment //Download link |
| Refund amount |
| Refund method: Card Association type (last 4-digit) |
| Request status |
| Returns and refunds history (Refund and Return) | Request date |
| Request number |
| Order number |
| Request type: Return and Refund |
| Returns logistics provider |
| Returns logistics tracking number |
| Reasons |
| Customer note |
| Customer note attachment //Download link |
| Refund amount |
| Refund method: Card Association type (last 4-digit) |
| Request status |
| Current payment information | Linked credit card |
| Linked date |
| Card number (last 4 digits) |
| Card type (card association) |
| Expiry date |
| Cardholder's name |
| Saved address information | Name |
| Phone number (partially masked) |
| Address |
| Customer support history | Request date |
| Request number |
| Topic |
| Description |
| Attachment download links |
| Order dispute history | Request date |
| Request number |
| Order number |
| Issue type |
| Description |
| Communication with shops | Shop name |
| {[Conversation Timestamp] Speaker: Detailed Content} |
| TikTok LIVE | Go LIVE History | LIVE Duration: start time - end time (duration mins) |
| Room ID |
| LIVE Cover |
| LIVE Title |
| Video Quality Settings |
| Replay Videos (download link) |
| Total Views |
| Total Gifters |
| Total Earnings |
| Total Likes Received |
| Fully Muted Accounts in this LIVE: Mute Time/Username |
| GO LIVE settings | LIVE Moderators |
| LIVE Gifts Settings |
| Rankings Settings |
| LIVE Comments Settings |
| Filter Spam or Offensive Comments Settings |
| Comment Keyword Filter |
| Q&A Settings |
| Allow Co-host Invites Settings |
| Allow Invites from Suggested LIVE Hosts |
| Allow Guest Request Settings |
| Agency Invitation Settings |
| Watch LIVE History | Watch LIVE History (inc. LIVE list, comments list, Q&A list) |
| Watch LIVE settings | LIVE video quality web settings |
| LIVE video quality app settings |
| POI Review | Location Reviews | Location name |
| Date and Time of review created |
| Review content |
| Review status |
| Review interactions |
| Income+ Wallet | Transaction History | Transaction_type: Earnings |
| Date |
| Currency |
| Amount |
| Status |
| Transaction_ID |
| others e.g.: {"source":"creator fund", "cash out type":"paypal"} |

Was this document helpful?


---
## SOURCE: Data Portability API/API Reference/Download.md

Docs
# Download
Use POST request to download the requested data. The response is streamed as an HTTP data zip file.

| **HTTP URL** | https://open.tiktokapis.com/v2/user/data/download/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | portability.all.single, portability.all.ongoing, portability.activity.single, portability.activity.ongoing, portability.directmessages.single, portability.directmessages.ongoing, portability.postsandprofile.single, portability.postsandprofile.ongoing, |

## Request
### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| request_id | int64 | The unique ID generated to track the download data request. This value can be obtained from the Add Data Request API. | 123123123123 | Yes |

## Response
The response is streamed as HTTP zip file, and must be converted to a zip file to get the correct data.
This Python script can be used to POST a successful request and get data in a readable format
```
import requests
import json

url = "https://open.tiktokapis.com/v2/user/data/download/"

# The request_id returned from the `Add Data Request` API
request_id = <REQUEST ID>

# Request JSON structure
payload = json.dumps({
  "request_id": request_id
})

# Necessary headers
# Authorization must have the token obtained from the /v2/oauth/token/ API
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'AUTHORIZATION_TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

zip_file_path = f'./{request_id}.zip'

# Open the zip file in write-binary mode
with open(zip_file_path, 'wb') as zip_file:
    # Write the content of the response to the zip file
    zip_file.write(response.content)
```
### Success Example
`.zip` must be added to streamed data to make it a zip file. The data itself, viewed as unicode will not be human-readable.
### Failure Example
In case a Download Request is unsuccessful, the following response will be returned
```
{
    "data": {},
    "error": {
        "code": "invalid_params",
        "http_status_code": 400,
        "log_id": "20240125230933D4C4606E87F0A61BE502",
        "message": "Incorrect `request_id`. Please validate the request."
    }
}
```
Was this document helpful?
