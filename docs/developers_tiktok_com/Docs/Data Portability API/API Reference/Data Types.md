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