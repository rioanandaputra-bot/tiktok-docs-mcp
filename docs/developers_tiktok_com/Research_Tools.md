# Research Tools

> Consolidated from 32 source files.



---
## SOURCE: Research Tools/Codebook.md

Docs
# Codebook
## Introduction
TikTok supports independent research about our platform. TikTok's Research Tools allow qualifying researchers who conduct research on a not-for-profit basis to study public data about TikTok content and accounts. This document describes the Research Tools functionality provided to researchers by TikTok.
## Eligibility and Data Access
[To check your eligibility and determine the process to get access to this data, check our product page](https://developers.tiktok.com/products/research-api/).
## Content Made Available for Research
### Videos
#### Unit of Analysis
A public TikTok video posted by a public creator (who is aged 18 and over), who wants to expose their videos to all users of TikTok
#### Scope
All the videos from TikTok that are:
- made public by a creator who is aged 18 and over;
- AND, are posted in the regions of US, Europe and Rest of the World;
- AND do not belong to Canada.
[**Note**: Our research tools return all public videos on the platform including videos which are not eligible for recommendation to the For You feed](https://www.tiktok.com/community-guidelines/en/fyf-standards) or that may be in the review by fact-checkers.
#### Details
- **ID**: The unique identifier of the TikTok video. This is also called "item_id" or "video_id".
- **Create Time**: This is the time when the video was created.
- **User****n****ame****:** This is the username of the video creator.
- [**Region Code**: A two digit code for the country where the video creator registered their account. Click here](https://developers.tiktok.com/doc/research-api-specs-query-videos/) to learn more about the region codes returned.
- **Video Description****:** This is the description of the video.
- **Music ID**: This is the music_id used in the video.
- **Like Count****:** The total number of likes on a TikTok video, created by users by clicking the “Heart” icon.
- **Comment Count**: This is the total number of comments posted on a video.
- **Share Count**: The total number of times a TikTok video has been shared by clicking the "Share" button with the video.
- **View Count****:** This is the total number of views for a video on TikTok.
- **Effect_IDs**: The list of effects applied on the video.
- **Video ID**: This is a unique video ID for each video posted on TikTok. This is a number that can be used to reconstruct the URL link to access the video.
- **Hashtags**: The list of hashtags used in the video.
- **Hashtag_id**:  Returns the unique hashtag_ids for each hashtag.
- **Hashtag_description**: Returns a description for a hashtag_name if one exists.
- **Video_mention_list**: Returns the other tagged users in a video.
- **Video_label**: Returns any labels applied to a video such as "election labels" (Ex: Get info on the U.S elections)
- **Playlist_ID**: The ID of the playlist that the video belongs to.
- **Voice_to_text**: Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated)
- **Is_stem_verified**: Whether the video has been verified as being high quality STEM content.
- **Video_duration**: The duration of the video in seconds.
- **Favorites_count**: The number of favorites a video receives.
### Comments
#### Unit of Analysis
A comment OR a reply to a comment posted for a public video on TikTok.
#### Scope
The information provided here includes text extracted from comments and a serial number (i.e. comment IDs) that help identify original comments posted on a video and any replies to comments. To protect the privacy of our users, other information is removed.
#### Details
- **Create Time**: This is the time when the comment was posted on a video.
- **ID**: This is the unique comment ID for a comment posted on a video.
- **Like Count**: The total number of likes for a comment under a video, created by users by clicking the “Heart” icon.
- **Parent Comment ID**: This is the unique ID of the parent comment when the user responds to another user's comment. If the comment was directly entered for a video, this ID is the same as the Video ID.
- **Reply Count**: This is the total number of replies on a particular comment.
- **Text****:** This is the actual text of the comment entered on a video. To protect the privacy of our users, other information is removed.
- **Video_ID**: This is the video ID for which the comment was entered.
### Users
#### Unit of Analysis
User information of all TikTok users that have set their account to public and are aged 18 and over.
#### Scope
The public details of a public user who is aged 18 and over can be accessed via this particular API.
#### Details
- **Following Count**: This is the number of people that a public user follows.
- **Likes Count**:  This is the total number of likes accumulated by the user.
- **Video Count**: This is the total number of videos that the user has posted on their TikTok account.
- **Bio Description**: This is the description in the bio of the user. If the user does not have a description, this will be returned blank.
- **Display Name**: This is the user's profile name that is found under the username.
- **Follower Count**: This is the total number of followers that follow the user.
- **Avatar**** ****URL**: This is the URL of the user's profile picture.
- **Is Verified**:  This returns the information on whether the user has been verified. All verified users will have "blue tick" next to their username. If the user has a blue tick, this variable will return a "true" in the response.
- **Bio_URL**: The public URL in the user's bio will be shared here.
### Liked Videos
#### Unit of Analysis
Liked video details of a TikTok user that has set their account to public and is aged 18 and over.
#### Scope
The liked video details of a public user who is aged 18 and over can be accessed via this particular API.
#### Details
- **ID**: The unique identifier of the TikTok video. This is also called "item_id" or "video_id".
- **Create Time**: This is the time when the video was created.
- **User****n****ame**: This is the unique username of the video creator.
- [**Region Code**: A two digit code for the country where the video creator registered their account. Click here](https://developers.tiktok.com/doc/research-api-specs-query-videos/) to learn more about the region codes returned.
- **Video Description**: This is the description of the liked video.
- **Music ID**: This is the music_id used in the video.
- **Like Count**: The total number of likes on a TikTok video, created by users by clicking the “Heart” icon.
- **Comment Count**: This is the total number of comments posted on a video.
- **Share Count**: The total number of times a TikTok video has been shared by clicking the "Share" button with the video.
- **View Count**: This is the total number of views for a video on TikTok.
- **Hashtag Names**: The list of hashtags used in the video.
- **Hashtag_id**:  Returns all the unique hashtag_ids for each hashtag.
- **Hashtag_description**: Returns a description for a hashtag_name if one exists.
- **Video_mention_list**: Returns the other tagged users in a video.
- **Video_label**: Returns any labels applied to a video such as "election labels" (Ex: Get info on the U.S elections)
- **Is_stem_verified**: Whether the video has been verified as being high quality STEM content.
- **Video_duration**: The duration of the video in seconds.
- **Favorites_count**: The number of favorites a video receives.
### Reposted Videos
#### Unit of Analysis
Reposted video details of a TikTok user that has set their account to public and is aged 18 and over.
#### Scope
The reposted video details of a public user who is aged 18 and over can be accessed via this particular API.
#### Details
- **ID**: The unique identifier of the TikTok video. This is also called "item_id" or "video_id".
- **Create Time**: This is the time when the video was created.
- **User****n****ame**: This is the unique username of the video creator.
- [**Region Code**: A two digit code for the country where the video creator registered their account. Click here](https://developers.tiktok.com/doc/research-api-specs-query-videos/) to learn more about the region codes returned.
- **Video Description**: This is the description of the liked video.
- **Music ID**: This is the music_id used in the video.
- **Like Count**: The total number of likes on a TikTok video, created by users by clicking the “Heart” icon.
- **Comment Count**: This is the total number of comments posted on a video.
- **Share Count**: The total number of times a TikTok video has been shared by clicking the "Share" button with the video.
- **View Count**: This is the total number of views for a video on TikTok.
- **Hashtag Names**: The list of hashtags used in the video.
- **Hashtag_id**:  Returns all the unique hashtag_ids for each hashtag.
- **Hashtag_description**: Returns a description for a hashtag_name if one exists.
- **Video_mention_list**: Returns the other tagged users in a video.
- **Video_label**: Returns any labels applied to a video such as "election labels" (Ex: Get info on the U.S elections)
- **Is_stem_verified**: Whether the video has been verified as being high quality STEM content.
- **Video_duration**: The duration of the video in seconds.
- **Favorites_count**: The number of favorites a video receives.
### Pinned Videos
#### Unit of Analysis
Pinned video details of a TikTok user that has set their account to public and is aged 18 and over.
#### Scope
The pinned video details of a public user who is aged 18 and over can be accessed via this particular API.
#### Details
- **ID**: The unique identifier of the TikTok video. This is also called "item_id" or "video_id".
- **Create Time**: This is the time when the video was created.
- **User****n****ame**: This is the username of the video creator.
- [**Region Code**: A two digit code for the country where the video creator registered their account. Click here](https://developers.tiktok.com/doc/research-api-specs-query-videos/) to learn more about the region codes returned.
- **Video Description**: This is the description of the pinned video.
- **Music ID**: This is the music_id used in the video.
- **Like Count**: The total number of likes on a TikTok video, created by users by clicking the “Heart” icon.
- **Comment Count**: This is the total number of comments posted on a video.
- **Share Count**: The total number of times a TikTok video has been shared by clicking the "Share" button with the video.
- **View Count**: This is the total number of views for a video on TikTok.
- **Hashtag Names**: The list of hashtags used in the video.
- **Hashtag_id**:  Returns all the unique hashtag_ids for each hashtag.
- **Hashtag_description**: Returns a description for a hashtag_name if one exists.
- **Video_mention_list**: Returns the other tagged users in a video.
- **Video_label**: Returns any labels applied to a video such as "election labels" (Ex: Get info on the U.S elections)
- **Is_stem_verified**: Whether the video has been verified as being high quality STEM content.
- **Video_duration**: The duration of the video in seconds.
- **Favorites_count**: The number of favorites a video receives.
### Query Followers List
The followers list of a TikTok user that has set their account to public and is aged 18 and over.
#### Scope
The followers list of a public user who is aged 18 and over can be accessed via this particular API.
#### Details
- **Display Name**: This is the profile name of the follower who follows the queried user.
- **User****n****ame**: This is the username of the follower who follows the queried user.
### Query Following List
The following list of a TikTok user that has set their account to public and is aged 18 and over. Further, the public user should also have made their following list public.
#### Scope
The following list of a public user who is aged 18 and over and has made this list public can be accessed via this particular API.
#### Details
- **Display Name**: This is the profile name of the user who the queried user follows.
- **User****n****ame**: This is the username of the user who the queried user follows.
### Query Playlist Info
The public playlists from accounts to get information on all videos that are part of a playlist.
#### Scope
The playlist details of a playlist ID that is publicly visible to all users can be accessed via this particular API.
#### Details
- **Playlist_ID**: The unique ID of the playlist.
- **Playlist_item_total**:  Provides the total number of items in a playlist.
- **Playlist_last_updated**: Provides info on when the playlist was last updated.
- **Playlist_name**: The name of the playlist.
- **Playlist_Video_IDs**: Provides a list of all video IDs in a playlist.
Was this document helpful?


---
## SOURCE: Research Tools/Frequently Asked Questions.md

Docs
# Frequently Asked Questions
- **What data is available as part of the Research ****Tools****?**
[More information about public data accessible via our Research Tools can be found here](https://developers.tiktok.com/products/research-api/).
[For detailed information on the data returned via our tools, check out the codebook](https://developers.tiktok.com/doc/research-api-codebook/).
- **How do I know if I qualify for access to TikTok's Research Tools ?**
[Applicants must fulfill our criteria described here](https://developers.tiktok.com/products/research-api/) to be eligible for access to Research Tools.
- **How do I apply for Research ****Tools**** access?**
[[If you meet the eligibility criteria described here](https://developers.tiktok.com/products/research-api/) and have prepared a research proposal, click here](https://developers.tiktok.com/application/research-api) to apply.
- **Can I work with a group of researchers to collaborate on a research topic? How do I ensure we all get access to the Research Tools  in order to collaborate on our approved project?**
We support lab-level access to Research Tools. The application form should be submitted by the project's principal researcher. Once the application is approved, the principal researcher can log in and view the approved "Organization" on the TikTok for Developers (TT4D) home page. Here, the principal researcher will have the ability to manage access, including adding and removing collaborators.
The principal researcher can add up to 9 collaborators to work together on a research topic. It is preferable that the principal researchers submit the details of all anticipated collaborators during the application process. TikTok will review any collaborators that are invited to join an approved research project prior to granting them access. Further, it is the responsibility of the principal researcher to remove and revoke access to collaborators who are no longer working on the approved research project.
If the collaborators are from a different research entity, an application should be submitted with a list of collaborators for each research entity.
The collaborators need to ensure that they have setup their TT4D account in advance prior to getting an invite.
The approved data limits will be shared across the organization.
- **When will TikTok's Research Tools be available in my country?**
[TikTok is committed to supporting researchers and we hope to expand eligibility to additional regions soon. Please check this page](https://developers.tiktok.com/products/research-api/) for updates.
- **I am a creator, advertiser, or commercial user. Am I eligible for access to the Research ****Tools****?**
[No. Click here](https://developers.tiktok.com/) to learn more about our other API access opportunities.
- **What are the daily quota limits? Can I request an increase in the quota limit? **
Currently, the daily limit is set at 1000 requests per day, allowing you to obtain up to 100,000 records per day across our APIs. (Video and Comments API can return 100 records per request). The daily quota gets reset at 12 AM UTC.
For the Followers and Following lists API, you can obtain up to 2M records per day by making up to 20,000 calls per day. You get a maximum of 100 records in each call. The daily quota gets reset at 12 AM UTC.
If you are approved for access to the Virtual Compute Environment (VCE), then you can access up to 5,000 records per day in the "Test Stage".
If you believe a quota limit increase is necessary for your research, please email us at               Research-API@tiktok.com. We can't grant exceptions, but we're eager to better understand use cases from the research community to evaluate and take your requests into account for the future.
- **I have a developer account with ****TikTok****. Can I start using Research ****Tools****?**
Your developer account alone is not sufficient to grant you access to Research Tools. In order to access our Research Tools, you will need to meet our eligibility requirements, submit an application, and be approved for a specific research project.
## Research API Usage FAQs
- **Why is my access token invalid? **
Access tokens are set to expire every two hours. If you experience an invalid token error within two hours of generating it, please submit a support ticket to us with your token and client key, and we will investigate the issue.
- **Why did I receive a response back with code: "scope_not_authorized" and message: "The user did not authorize the scope required for completing this request?" **
[[[This indicates that you have not yet submitted your research application for our review and have not passed the necessary approval evaluations. If you are interested in accessing our Research Tools, visit our Research](https://developers.tiktok.com/products/research-api/)Tools](https://developers.tiktok.com/products/research-api/)](https://developers.tiktok.com/products/research-api/)page to learn more, check eligibility requirements and apply for access.
- **Why is the query video data (view_count, comment_count, like_count, share_count) significantly inaccurate, often showing lower numbers than what is live at the moment? **
The User info API only retrieves data for an individual user, so we use online data. However, the video query API searches for the full dataset, so we use archived data instead of the current online data. New videos take up to 48 hours to be added to the search engine, and statistics such as view count and follower count can take up to 10 days to update.
Was this document helpful?


---
## SOURCE: Research Tools/Getting Started - Research API.md

Docs
# Getting Started
This guide will show you how to use the Research API. Learn how to use the Research API to query video data and fetch public TikTok account data in the following use case example.
# View your client registration
[Once your application is approved, a research client will be generated for your project. You can view your approved projects on your **Research projects](https://developers.tiktok.com/research/)** page. Select a project from the list to see the research client details.
The provided **Client key** and **Client secret** are required to connect to the Research API endpoints. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).
Warning: The client secret is a credential used to authenticate your connection to TikTok's APIs. Do not share this with anyone!
# Obtain a client access token
[Once you have obtained the client key and secret for your project, generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Research API endpoints.
# Query TikTok public content data
The cURL command below shows an example of how you can query the TikTok ID and like count of videos created in the US or Canada with the keyword `hello world` in the video description.
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 100,
    "cursor": 0,
    "start_date": "20181207",
    "end_date": "20181207",
    "is_random": false}
'
```
## Query condition
Similar to the WHERE clause in SQL, a condition can be used to filter data returned in a query operation. The above request is equivalent to the following SQL query:
```
 SELECT id,like_count FROM video_table WHERE region_code IN ["US", "CA"] AND create_date > 20220615
```

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| field_name | string | The field name this condition is restricting | "region_code" | Yes |
| operation | string | The comparison logic of this condition. One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" | "GT" | Yes |
| field_values | list[string] | A list of values to be compared with | ["US", "IN"] | Yes |

**Note**: Approximate string matching (or fuzzy string searching) is used to match conditions.
### field_name
The following are the `field_name` values:
- `keyword`
- `create_date`
- `username`
- `region_code`
- `video_id`
- `hashtag_name`
- `music_id`
- `effect_id`
- `video_length`
### operation
The following are the `operation` values:
- `IN`: Tests if an expression matches any value in a list of values.
- `EQ`: Tests if an expression matches the specified value.
- `GT`: Tests if an expression is strictly greater than the specified value.
- `GTE`: Tests if an expression is greater than or equal to the specified value.
- `LT`: Tests if an expression is strictly less than the specified value.
- `LTE`: Tests if an expression is less than or equal to the specified value.
### AND, OR or NOT
Conditions are grouped by the following boolean operators:
- `AND`: Displays a record if all the conditions separated by `AND` are `TRUE`.
- `OR`: Displays a record if any of the conditions separated by `OR` is `TRUE`.
- `NOT`: Displays a record if all the conditions separated by `NOT` are `FALSE`.
## Pagination
If the total number of videos that match the query criteria is larger than the max number of videos that can be returned in a single request, the response data will be returned with different requests.

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| max_count | number | The max count of TikTok videos in response. default: 10, max: 100 | 12 | No |
| cursor | number | The starting index of TikTok videos in response. default: 0 | 100 | No |
| search_id | string | The ID of a previous search to provide sequential calls for paging | "7167072234702738478" | No |

### First page
When you send the first request, you do not need to set the `search_id` or `cursor` in the request body. In the http response, `cursor` and `search_id` are returned, which are used in the subsequent requests. Try out this request:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 100,
    "cursor": 0,
    "start_date": "20181207",
    "end_date": "20181207",
    "is_random": false}
'
```
The following example data is returned from the response.
```
{
    "data": {
        "cursor": 10,
        "has_more": true,
        "search_id": "7160776277492814854",
        "videos": [
            ...
        ]
    },
    "error": {
        ...
    }
 }
```
### Next page
With the cURL command below, you can get the next page of query results.
```
curl --location 'https://open.tiktokapis.com/v2/research/video/query/?fields=id%2Clike_count' \
--header 'authorization: bearer abcdefg' \
--header 'Content-Type: application/json' \
--data '{
  "query": {
              "and": [
                   { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
                   { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
               ]
          }, 
  "max_count": 10,
          "cursor": 10,
          "start_date": "20220615",
          "end_date": "20220628",
          "search_id": "7160776277492814854"
}
'
```
The following example data is returned from the response.
```
{
    "data": {
        "cursor": 20,
        "has_more": true,
        "search_id": "7160776277492814854",
        "videos": [
            ...
        ]
    },
    "error": {
        ...
    } 
}
```
# Query TikTok public account information
With the cURL command below, you can query public TikTok account information by a TikTok handle.
```
curl --location --request POST 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
--header 'Authorization: bearer {{access_token}}' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "username": "example_username"
}'
```

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | TikTok user's username | "example_username" | No |

The following example data is returned from the response.
```

{
    "data": {
        "username": "example_username",
        "video_count": 64,
        "avatar_url": "https://my-awesome-avatar",
        "display_name": "joe 1234567",
        "follower_count": 111,
        "likes_count": 4146,
        "bio_description": "joe joe",
        "following_count": 103,
        "is_verified": false
    },
    "error": {
        ...
    }
}
```
### Was this document helpful?


---
## SOURCE: Research Tools/Getting Started - VCE.md

Docs
# Getting Started
This guide shows you how to access and use the Virtual Compute Environment (VCE), a secure space that allows you to query and analyze public data.
# How does the Virtual Compute Environment work?
The VCE allows you to access and analyze TikTok's public data in two stages. These stages are meant to protect user privacy and help organize your data analysis.
- **Test Stage**: Query the data using TikTok's query software development kit (SDK). The VCE will return random sample data based on your query, limited to 5,000 records per day. The data here is limited to data of users who have at least 25,000 followers.
- **Execution Stage**: Submit a script to execute against all public data. TikTok provides a powerful search capability that allows data to be paginated in increments of up to 100,000 records. TikTok will review the results file to make sure the output is **aggregated**.
- **NOTE**: Please ensure that the scripts submitted are looking to get aggregated outputs. Scripts that request individual data will be rejected.
- Examples of Acceptable Outputs:
- Descriptive statistics (for example, mean, standard deviation, skewness)
- Inferential statistics (for example, Z-scores, regression coefficients)
- Topic model results or word clouds
Note: TikTok only reviews the results to ensure that there is no identifiable individual information extracted out of the platform. All aggregated results will be shared as a downloadable link to the approved primary researcher's email.
# View your client registration
[[Once your application is approved, a research client will be generated for your project. You can view your approved research projects on your **Research projects](https://developers.tiktok.com/research/)** page](https://developers.tiktok.com/research/). Select a project from the list to view the research client details.
The provided **Client key** and **Client secret** are required to access the VCE. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).
Note: The client secret is a credential used to authenticate your connection to TikTok's Research Tools. Do not share this with anyone!
# Log in to the Virtual Compute Environment
[First, go to the Virtual Compute Environment login page](https://research.tiktok.com/virtual-compute-environment/hub/).
Then, sign in using your **Client key** as the **Username** and your **Client secret** as the **Password**.
# Use the Virtual Compute Environment
## Test Stage: Query TikTok's public data
In the Test Stage, you will submit a query to access random sample public data about videos, comments, and users. You can retrieve up to 5000 records per day from creators who have at least 25,000 followers.
Note: If you want to analyze all public user data, you must submit a script to the VCE, as explained later in this guide.
### Install query SDK
After logging into the VCE, click the **New Launcher** [**+**] button. Then open a new notebook, choosing the **Python 3 (ipykernel)** option.
Copy and paste the following code into the terminal, then run the code to install the query SDK from TikTok.
```
!pip install \
-U --index-url https://us-west2-python.pkg.dev/research-platform-prod/jupyterlab-extensions-prod/simple/ \
pyrqs
```
### Set query parameters
You must structure your query according to the following guidelines. Use the query structure example code below as a framework for formatting your query.
#### Data category
Indicate what `category` of data you want to query. The available data categories are described in the respective reference pages:
- [Query Profiles](https://developers.tiktok.com/doc/vce-query-profiles/)
- [Query Videos](https://developers.tiktok.com/doc/vce-query-videos/)
- [Query Video Comments](https://developers.tiktok.com/doc/vce-query-video-comments/)
#### Condition groups
Create your query `condition_groups` using the listed field names, operations, and boolean operators.
**Field names**
The following are the `field_name` values:
- `create_time`
- `display_name`
- `region_code`
- `id`
- `video_description`
- `hashtag_name`
- `music_id`
- `like_count`
- `comment_count`
- `share_count`
- `view_count`
- `effect_ids`
- `hashtag_names`
- `playlist_id`
- `voice_to_text`
- `duration_type`
- `video_length`
**Operations**
The following are the `operation` values:
- `IN`: Tests if an expression matches any value in a list of values
- `EQ`: Tests if an expression matches the specified value
- `GT`: Tests if an expression is strictly greater than the specified value
- `GTE`: Tests if an expression is greater than or equal to the specified value
- `LT`: Tests if an expression is strictly less than the specified value
- `LTE`: Tests if an expression is less than or equal to the specified value
- `LIKE`: Available for video_description, returns the rows if it contains a specified value
- `CONTAINS`: Available for `effect_ids` and `hashtag_names`, returns the rows if they contain the specified `effect_ids` or `hashtag_names`
**Boolean operators**
Conditions are grouped by the following boolean operators:
- `AND`: Displays a record if all the conditions separated by `AND` are `TRUE`
- `OR`: Displays a record if any of the conditions separated by `OR` is `TRUE`
- `NOT`: Displays a record if all the conditions separated by `NOT` are `FALSE`
#### Fields, limit, and client
Specify the `fields` to be returned in the query results, and a `limit` indicating the maximum number of records to return. Create a `client`, such as RQSClient, to interact with the query service.
### Query structure example
Below is a complete sample command that can be executed in the VCE. This example defines a data variable and prints the data received by the query to display it on the VCE.
**Example code**
```
from pyrqs import rqs

category = 'video'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "like_count",
                "operator": "gte",
                "field_values": ["10"]
            }
        ]
    }
]
fields = 'username,video_description,create_time,id'
limit = 10
client = rqs.RQSClient()
data = client.query(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
The data from this sample code should be displayed on the VCE, as below.
## Execution Stage: Submit script to analyze data
After you have queried the data and understood the metadata structure, you can run a script to analyze all TikTok's public data. Please make sure that the output of your script at this stage does not contain individual-level data.
To submit a script to the VCE, do the following:
- Click the shield icon on the right sidebar.
- Select your script file in the right sidebar, then click the upload button.
- When prompted to submit a job to Data Clean Room, click the **Ok** button.
- Once submitted, your script will run in a trusted execution environment to analyze and prepare the results file.
- TikTok will review the results to verify that results are aggregated and do not contain individual data.
- After the results are verified, TikTok will send an email to the primary researcher to download the approved results file.
Was this document helpful?


---
## SOURCE: Research Tools/Research Tools.md

Docs
# About Research Tools
TikTok's Research Tools allow independent and academic researchers who conduct research on a non-for-profit basis to access certain data.
The types of public information that is available via the Research Tools include:
- **Videos -** Videos that can be watched by "Everyone", and for such videos, the total number of likes, total number of comments, voice-to-text, subtitles, the time of creation and video length.
- **Comments - **Comment text, and total number of likes, replies, and the time the comment was posted.
- **Accounts - **Bios, profile pictures, liked videos, reposted videos, pinned videos, the total number of followers and the number of people who are followed by the account. The response also returns information on the followers and people followed by the account.
[[The Research Tools support research in areas such as misinformation, disinformation, violent extremism, social trends, and community building. In order to obtain access to TikTok's Research Tools, researchers must submit an application, be approved, and adhere to our Community Guidelines](https://www.tiktok.com/community-guidelines/en-GB) and TikTok Research Tools Terms of Service](https://www.tiktok.com/legal/page/global/terms-of-service-research-api/en).
[Additional information about TikTok's Research Tools can be found on TikTok for Developers](https://developers.tiktok.com/products/research-api/).
## Vetted Researchers Data Sharing
The EU Digital Services Act (DSA) requires platforms such as TikTok to share certain data with certain qualifying researchers granted vetted researcher status by a Digital Services Coordinator (DSC) under the DSA (known as "Vetted Researchers").
[In accordance with the DSA, Vetted Researchers may be eligible to access data for the purposes of conducting research that contributes to the detection, identification and understanding of systemic risks in the EU and the measures taken to mitigate them by platforms such as TikTok. See more information on the Vetted Researcher Data Access page](https://developers.tiktok.com/products/research-api/vetted-researcher-data-access).
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/API Reference.md

Docs
# Query Videos
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/video/query/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Content-Type | string | Indicate the original media type of the resource. | "application/json" | Yes |
| Authorization | string | The client access token which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields. Choose from the Video Object's fields. | Complete list: id,video_description,create_time, region_code,share_count,view_count,like_count,comment_count, music_id,hashtag_names, username,effect_ids,playlist_id,voice_to_text, is_stem_verified, favorites_count, video_duration,hashtag_info_list, sticker_info_list, effect_info_list, video_mention_list,video_label,video_tag | Yes |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| query | Query object (See the definition below) | A JSON object that contains three types of children: `and`, `or`, and `not`, each of which is a list of conditions. An valid query must contain at least one non-empty `and`, `or`or `not`condition lists | { "and":[ { "operation":"IN", "field_name":"region_code", "field_values":[ "JP", "US" ] }, { "operation":"EQ", "field_name":"keyword", "field_values":["animal"] } ], "not":[ { "operation":"LT", "field_name":"create_date", "field_values":["20230101"] } ] } | Yes |
| start_date | string | The lower bound of video creation time in UTC | "20210102" | Yes |
| end_date | string | The upper bound of video creation time in UTC The end_date must be no more than 30 days after the start_date | "20210123" | Yes |
| max_count | int64 | The number of videos in response. Default is 20, max is 100. It is possible that the API returns less videos than the max count due to reasons such as videos deleted/marked as private by users etc. | 20 | No |
| cursor | int64 | Retrieve video results starting from the specified index | 100 | No |
| search_id | string | The unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "7201388525814961198" | No |
| is_random | bool | The flag that indicates whether to return results in a random order. If set to true, then the API returns 1 - 100 videos in random order that matches the query. If set to false or not set with any value, then the API returns results in the decreasing order of video IDs. | true | No |

##### Query

| **Key** | **Type** | **Description ** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

##### Condition

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| field_name | string | The name of the field this condition is restricting One of: ["create_date", "username", "region_code", "video_id", "hashtag_name", "keyword", "music_id", "effect_id", "video_length", "view_count", "comment_count"] |
| operation | string | One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" |
| field_values | list<string> | A list of restriction values |

##### Condition fields

| **Field Name** | **Description ** | **Example** |
| --- | --- | --- |
| create_date | The video creation date in UTC, presented in the format YYYYMMDD | "20220910" |
| username | The username of the video creator | "cookie_love_122" |
| region_code | A two digit code for the country where the video creator registered their account | "FR", "TH", "MM", "BD", "IT", "NP", "IQ", "BR", "US", "KW", "VN", "AR", "KZ", "GB", "UA", "TR", "ID", "PK", "NG", "KH", "PH", "EG", "QA", "MY", "ES", "JO", "MA", "SA", "TW", "AF", "EC", "MX", "BW", "JP", "LT", "TN", "RO", "LY", "IL", "DZ", "CG", "GH", "DE", "BJ", "SN", "SK", "BY", "NL", "LA", "BE", "DO", "TZ", "LK", "NI", "LB", "IE", "RS", "HU", "PT", "GP", "CM", "HN", "FI", "GA", "BN", "SG", "BO", "GM", "BG", "SD", "TT", "OM", "FO", "MZ", "ML", "UG", "RE", "PY", "GT", "CI", "SR", "AO", "AZ", "LR", "CD", "HR", "SV", "MV", "GY", "BH", "TG", "SL", "MK", "KE", "MT", "MG", "MR", "PA", "IS", "LU", "HT", "TM", "ZM", "CR", "NO", "AL", "ET", "GW", "AU", "KR", "UY", "JM", "DK", "AE", "MD", "SE", "MU", "SO", "CO", "AT", "GR", "UZ", "CL", "GE", "PL", "CA", "CZ", "ZA", "AI", "VE", "KG", "PE", "CH", "LV", "PR", "NZ", "TL", "BT", "MN", "FJ", "SZ", "VU", "BF", "TJ", "BA", "AM", "TD", "SI", "CY", "MW", "EE", "XK", "ME", "KY", "YE", "LS", "ZW", "MC", "GN", "BS", "PF", "NA", "VI", "BB", "BZ", "CW", "PS", "FM", "PG", "BI", "AD", "TV", "GL", "KM", "AW", "TC", "CV", "MO", "VC", "NE", "WS", "MP", "DJ", "RW", "AG", "GI", "GQ", "AS", "AX", "TO", "KN", "LC", "NC", "LI", "SS", "IR", "SY", "IM", "SC", "VG", "SB", "DM", "KI", "UM", "SX", "GD", "MH", "BQ", "YT", "ST", "CF", "BM", "SM", "PW", "GU", "HK", "IN", "CK", "AQ", "WF", "JE", "MQ", "CN", "GF", "MS", "GG", "TK", "FK", "PM", "NU", "MF", "ER", "NF", "VA", "IO", "SH", "BL", "CU", "NR", "TP", "BV", "EH", "PN", "TF", "RU" |
| video_id | The unique identifier of the video | 6978662169214864645 |
| hashtag_name | The hashtag associated with the video | "arianagrande", "celebrity" |
| keyword | The keyword in the video description | "tiktok" |
| music_id | The music ID of the video. | "8978345345214861235" |
| effect_id | The effect ID of the video. | "3957392342148643476" |
| video_length | The duration of the video SHORT: <15s MID: 15 ~60s LONG: 1~5min EXTRA_LONG: >5min | "SHORT", "MID", "LONG", "EXTRA_LONG" |
| view_count | The number of video views the video has received | 10 |
| comment_count | The number of comments the video has received | 10 |

## Example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json' \
--data-raw '{
    "query": {
        "and": [
            {
                "operation": "IN",
                "field_name": "region_code",
                "field_values": ["JP", "US"]
            },
            {
                "operation":"EQ",
                "field_name":"hashtag_name",
                "field_values":["animal"]
            }
        ],
        "not": [
          {
                "operation": "EQ",
                "field_name": "video_length",
                "field_values": ["SHORT"]
           }
        ]
    },
    "max_count": 100,
    "cursor": 0,
    "start_date": "20230101",
    "end_date": "20230115"
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | QueryVideoResponseData | { "videos": [...], "cursor": 100, "has_more": true, "search_id": "" } |
| error | ErrorStruct | Error object |

## Data Structures
### QueryVideoResponseData

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| videos | list<Video Object> | A list of video objects that match the query |
| cursor | int64 | Returns video results from the given index. |
| has_more | bool | Whether there are more videos or not. |
| search_id | string | A search_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. |

##### Video Object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | Unique identifier for the TikTok video. Also called "item_id" or "video_id" |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The video's author's username |
| "region_code" | string | A two digit code for the country where the video creator registered their account |
| "video_description" | string | The description of the video, also known as the title |
| "music_id" | int64 | The music_id used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of video views the video has received |
| "effect_ids" | list<string> | The list of effect ids applied on the video |
| "hashtag_names" | list<string> | The list of hashtag names that the video participates in |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists. |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_url". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video . |
| "video_label" | Struct | Returns any information and labels associated with a video. |
| "playlist_id" | int64 | The ID of playlist that the video belongs to |
| "voice_to_text" | string | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) |
| is_stem_verified | bool | Whether the video has been verified as being high quality STEM content. |
| video_duration | int64 | The duration of the video, in seconds. |
| favorites_count | int64 | The number of favorites that a video receives. |
| video_tag | Struct | "type" and "number" returned here Definitions: "number" = 1, and "type" = AIGC Type indicates "Creator Labelled as AI-Generated" "number" = 2, and "type" = AIGC Type indicates "AI-Generated" "number" = 1, and "type" = Branded Type indicates "Paid Partnership" "number" = 7, and "type" = Branded Type indicates "Creator Earns Commission" |

## Example
```
{
    "data": {
        "videos": [
            {
                "hashtag_names": [
                    "avengers",
                    "pov"
                ],
                "region_code": "CA",
                "create_time": 1633823999,
                "effect_ids": [
                    "0"
                ],
                "video_id": 702874395068494965,
                "music_id": 703847506349838790,
                "video_description": "lol #pov #avengers",
                "view_count": 1050,
                "comment_count": 2
            },
            ...
        ],
        "cursor": 100,
        "search_id": "7201388525814961198",
        "has_more": true
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20230113024658F0D7C5D6CA3A9B79C5B9"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Batch Compliance APIs.md

Docs
# Create a batch compliance task
## Request to create a batch compliance task

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/validation_task/create/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters
Need form-data in Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| file_data | File | A text file that contains video ids or comment ids. The max IDs users can submit is 10,000 per time. |  | Yes |
| category | Text | Category that the file contains. Video or comment. | video | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task/create/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefg' \
--form 'file_data=@"/****/****/****/test file.txt"' \
--form 'category="video"'
```
## Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | struct | The task id associated with the task. |
| error | ErrorStructV2 | Error object |

### Example
```
{
    "data": {
        "task_id": 12345678910987654321
    },
    "error": {
        "code": "ok",
        "http_status_code": 200,
        "log_id": "987654321",
        "message": "ok."
    }
}
```
# Get a batch compliance task status
## Request to get a batch compliance task status

| **HTTP URL** | https://open.tiktokapis.com/v2/research/validation_task_status/get/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Task id created by the create batch compliance api | 12345678910 | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task_status/get/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 1234567891011' \
--data '{
    "task_id":12345678910
}'
```
## Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | struct | Current task status. Completed/Processing/Failed |
| error | ErrorStructV2 | Error object |

### Example
```
{
    "data": {
        "task_status": "Completed"
    },
    "error": {
        "code": "ok",
        "http_status_code": 200,
        "log_id": "12345678910",
        "message": "ok."
    }
}
```
# Download a completed batch compliance task
## Request to download a batch compliance task

| **HTTP URL** | https://open.tiktokapis.com/v2/research/validation_task/download/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Body Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Task id created by the create batch compliance api | 12345678910 | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/validation_task_status/get/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 1234567891011' \
--data '{
    "task_id":12345678910
}'
```
## Response
Click Send and Download, a text file with valid IDs will be download automatically.
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query Playlist Info.md

Docs
# Query Playlists
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/playlist/info/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Request Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| playlist_id | int64 | The unique ID of the playlist | 1234569763387255595 | Yes |
| cursor | int64 | Retrieve video results starting from the specified index | 15 | No |
| max_count | int64 | Max number of videos can be returned in one playlist | 10 | No |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/playlist/info/?fields=playlist_id' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer abcdefghijklmn' \
--data '{
   "playlist_id": 12345677654321,
    "max_count":100,
    "cursor":0
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | PlayListInfoObject | The returned playlist info data |
| error | ErrorStructV2 | Error object |

### PlayListInfoObject

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| playlist_id | int64 | The unique ID of the playlist |
| playlist_item_total | int64 | Provides the total number of items in a playlist |
| playlist_last_updated | int64 | Provides info on when the playlist was last updated |
| playlist_name | string | The name of the playlist |
| playlist_video_ids | list<i64> | Provides a list of all video IDs in a playlist |
| has_more | bool | Whether there are more videos in the playlist or not |
| cursor | int64 | Next available videos start index |

### Example
```
{
    "data": {
        "playlist_item_total": 10,
        "playlist_last_updated": 12345678,
        "playlist_name": "example name",
        "playlist_video_ids": [
            12345678910,
            10987654321
        ],
        "cursor": 10,
        "has_more": true,
        "playlist_id": 12345678910
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "12345678899abcdefg"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query TikTok Shop Info.md

Docs
# Query Shop Details
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/shop/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Shop Info Object below for a full list of values. | **Complete list**: shop_name,shop_rating,shop_review_count,item_sold_count,shop_id | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| shop_name | string | shop_name as the unique identifier | "Test Shop" |
| limit | int | Max data can be returned at one time (max 10 for TTS related data) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/shop/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2.example' \
--data '{
    "shop_name": "TEST SHOP",
    "fields":"shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value",
    "limit": 10
}'

curl --location 'https://open.tiktokapis.com/v2/research/tts/shop/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2' \
--data '{
    "shop_name": "test shop",
    "fields":"shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value",
    "limit": 1
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Shop Info Object | The returned shop info for shops operating in the EU. |
| error | ErrorStructV2 | Error object |

## Shop Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "shop_name" | string | The name of the shop |
| "shop_rating" | String | The rating of the shop |
| "shop_review_count" | int64 | The number of reviews the shop has received |
| "item_sold_count" | int64 | The number of items the shop has sold |
| "shop_performance_value" | int64 | The value of shop performance (Ex: 90) |

## Example
```
{
    "data": {
        "shop_data": [
            {
                "item_sold_count": 1216959,
                "shop_id": 123456789,
                "shop_name": "Test Name",
                "shop_rating": "4.5",
                "shop_review_count": 12345
            }
        ]
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query TikTok Shop Products.md

Docs
# Query Product Info
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/product/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Product Info Object below for a full list of values. | **Complete list**: product_id,product_sold_count,product_description,product_price,product_review_count,product_name,product_rating_1_count,product_rating_2_count,product_rating_3_count,product_rating_4_count,product_rating_5_count | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| shop_id | int | shop_id as the unique identifier | "127878967" |
| page_start | int | The start page for the products in the shop (start with 1) | 1 |
| page_size | int | The size of data on the page (max 10) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/product/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.2.' \
--data '{
    "shop_id": 12345678910,
    "fields": "product_id,product_sold_count,product_review_count,product_rating",
    "page_start": 1,
    "page_size": 5
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Product Info Object | The returned product info data for products available for purchase in the EU. |
| error | ErrorStructV2 | Error object |

## Product Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "product_name" | string | The name of the product |
| "product_id" | int64 | The unique ID of the product |
| "product_price" | list | The price of the product |
| "product_rating" | string | The rating of the product |
| "product_review_count" | int64 | The number of reviews of the product |
| "product_rating_5_count" | int64 | The number of ratings of 5-stars the product has received |
| "product_rating_4_count" | int64 | The number of ratings of 4-stars the product has received |
| "product_rating_3_count" | int64 | The number of ratings of 3-stars the product has received |
| "product_rating_2_count" | int64 | The number of ratings of 2-stars the product has received |
| "product_rating_1_count" | int64 | The number of ratings of 1-star the product has received |
| "product_sold_count" | int64 | The number of items sold since this item was listed on TikTok shop, including items that have been returned |
| "product_description" | string | The description of the product |
| "shop_name" | string | The name of the "Shop" the product is under |

## Example
```
{
    "data": {
        "product_data": [
            {
                "product_description": "test Description",
                "product_id": 123456789,
                "product_name": "test Name",
                "product_price": [
                    "20.79GBP"
                ],
                "product_rating_1_count": 116,
                "product_rating_2_count": 47,
                "product_rating_3_count": 112,
                "product_rating_4_count": 353,
                "product_rating_5_count": 2693,
                "product_review_count": 3321,
                "product_sold_count": 37741
            }
        ]
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query TikTok Shop Reviews.md

Docs
# Query Reviews Info
# Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/tts/review/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Review Info Object below for a full list of values. | **Complete list**: product_name,review_text,review_like_count,create_time,review_rating | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| product_id | string | product_id as the unique identifier | "1234590980980" |
| page_start | int | The start page for the products in the shop (start with 1) | 1 |
| page_size | int | The size of data on the page (max 10) | 10 |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/tts/review/' \
--header 'Authorization: Bearer clt.2.example*0' \
--header 'Content-Type: application/json' \
--data '{
    "product_id": 12345678910,
    "fields": "product_name,review_text,display_name,review_like_count,create_time,review_rating",
    "page_start": 2,
    "page_size": 1
}'
```
# Response
## Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | Review Info Object | The returned review info data for reviews given on products available for purchase in the EU. |
| error | ErrorStructV2 | Error object |

### Product Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "review_text" | string | The text within the review |
| "review_like_count" | int64 | The number of likes a review has |
| "create_time" | int64 | The unix timestamp that the review was created on |
| "product_name" | string | The product that this review is for |
| "review_rating" | string | The rating of the product |

### Example
```
{
    "data": {
        "review_data": [
            {
                "create_time": 1722879716021,
                "product_name": "Test Product Name",
                "review_like_count": 1,
                "review_rating": "FIVE",
                "review_text": " test Text"
            }
        ]
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Followers.md

Docs
# Query User Followers
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/followers/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of followers that can be returned in this response. Default is 20; max is 100. | 100 | No |
| cursor | int64 | Followers followed on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://platform.tiktokapis.com/v2/research/user/followers/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.test123test123test123' \
--data '{
    "username": "test_user",
    "max_count":3,
    "cursor": 12347764
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserFollowerData | The list of the followers of the user |
| error | ErrorStructV2 | Error object |

### UserFollowerData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_followers | list<UserInfo> | A list of user info objects that match the query |
| cursor | int64 | Followers that followed this user on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. |
| has_more | bool | Whether this user has more followers or not |

### User Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "display_name" | string | The profile name of the follower of this user |
| "username" | string | The username of the follower of this user |

### Example
```
{
    "data": {
        "cursor": 1706837834,
        "has_more": true,
        "user_followers": [
            {
                "display_name": "test user",
                "username": "test_username"
            },
            {
                "username": "test user 2",
                "display_name": "test_username2"
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "123499999999999999999999999999"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Following.md

Docs
# Query User Following
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/following/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of accounts the user follows returned in a single response. Default is 20, max is 100. | 100 | No |
| cursor | int64 | Accounts the user started following on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://open-platform.tiktokapis.com/v2/research/user/following/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.test123temp123test123test123' \
--data '{
    "username": "test_user",
    "max_count":3,
    "cursor": 1685544251
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserFollowingData | The list of the accounts this user is following |
| error | ErrorStructV2 | Error object |

### UserFollowingData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_following | list<UserInfo> | A list of user info objects that match the query |
| cursor | int64 | Accounts the user started following on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. |
| has_more | bool | Whether there are more accounts this user is following or not |

### User Info Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "display_name" | string | The profile name of the account that the user is following |
| "username" | string | The username of the account that the user is following |

### Example
```
{
    "data": {
        "has_more": true,
        "user_following": [
            {
                "display_name": "test user",
                "username": "test_username"
            },
            {
                "display_name": "test user 2",
                "username": "test_username2"
            },
            {
                "display_name": "test user 3",
                "username": "test_username3"
            }
        ],
        "cursor": 1650642422
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "202499999999999999999999999999999"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Info.md

Docs
# Query User Info
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/user/info/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See User Info Object below for a full list of values. | **Complete list**: display_name, bio_description, avatar_url, is_verified, follower_count, following_count, likes_count, video_count,bio_url | Yes |

### Body Parameters

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| username | string | username as the unique identifier | "joe11235" |

### Example
```
curl -L 'https://open.tiktokapis.com/v2/research/user/info/?fields=display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type:application/json' \
-d '{"username": "joe123456"}'
```
# Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | User Info Object | The returned user info data |
| error | ErrorStructV2 | Error object |

User Info Object

| Field name | Type | Description |
| --- | --- | --- |
| "display_name" | string | The user's display name / nickname |
| "bio_description" | string | The user's bio description |
| "avatar_url" | string | The url to a user's profile picture |
| "is_verified" | bool | The user's verified status. True if verified, false if not |
| "following_count" | int | The number of people the user is following |
| "follower_count" | int | The number of followers the user has |
| "video_count" | int | The number of videos the user has posted |
| "likes_count" | int | The total number of likes the user has accumulated |
| "bio_url" | string | The url in user's bio when shared |

### Example
```
{
    "data": {
        "bio_description": "my_bio",
        "is_verified": false,
        "likes_count": 27155089,
        "video_count": 44,
        "avatar_url": "https://some_cdn.com/my_avatar",
        "follower_count": 232,
        "following_count": 45,
        "display_name": "my nick name"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202207280326050102231031430C7E754E",
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Liked Videos.md

Docs
# Liked Videos
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/liked_videos/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query Parameters

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Video Object below for a full list of values. | Complete list: id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names, is_stem_verified, favourites_count, video_duration,hashtag_info_list, sticker_info_list, effect_info_list, ,video_mention_list,video_label,video_tag | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of liked videos in a single response. Default is 20, max is 100. It is possible that the API returns fewer videos than the max count due to content moderation outcomes, videos being deleted, marked as private by users, or more. | 20 | No |
| cursor | int64 | Videos created on or before this time will be returned. It is a Unix timestamp in UTC seconds. Default value is set as the time this request was made. | 1706833705 | No |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/user/liked_videos/?fields=id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.testtemp123testtemp123' \
--data '{
    "username": "test_username",
    "max_count": 1,
    "cursor" : 1706457540000,
}'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | UserLikedVideosData | The returned list of liked video objects |
| error | ErrorStructV2 | Error object |

### UserLikedVideosData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_liked_videos | list<Video> | A list of video objects that match the query |
| cursor | int64 | Retrieve liked videos starting from the specified Unix timestamp in UTC seconds |
| has_more | bool | Whether there are more liked videos or not |

### Video Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | The unique identifier of the TikTok video |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The username as the unique identifier of the video creator |
| "region_code" | string | A two digit code for the country where the video creator registered their account. |
| "video_description" | string | The description of the liked video |
| "music_id" | int64 | The music ID used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of views the video has received |
| "hashtag_names" | list<string> | The list of hashtags used in the video |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists. |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_URI". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video |
| "video_label" | Struct | Returns any information and labels associated with a video. |
| "video_duration" | int64 | The duration of the video, in seconds. |
| "is_stem_verified" | bool | Whether the video has been verified as being high quality STEM content. |
| "favorites_count" | int64 | The number of favorites that a video receives. |
| video_tag | Struct | "video_tag_type" and "video_tag_number" returned here Definitions: "video_tag_number" = 2, and "video_tag_type" = AIGC Type indicates "Creator Labelled as AI-Generated" "video_tag_number" = 1, and "video_tag_type" = AIGC Type indicates "AI-Generated" "video_tag_number" = 7, and "video_tag_type" = Branded Type indicates "Creator Earns Commission" "video_tag_number" = 1, and "video_tag_type" = Branded Type indicates "Paid Partnership" |

### Example
```
{
    "data": {
        "cursor": 1706457371000,
        "has_more": true,
        "user_liked_videos": [
            {
                "share_count": 1,
                "view_count": 1586,
                "comment_count": 6,
                "hashtag_names": [
                    "song",
                    "Viral"
                ],
                "id": 123123123123123123123,
                "music_id": 454545454545454545
            },
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "20240299999999999993FCB68B8B13"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Pinned Videos.md

Docs
# Pinned Videos
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/pinned_videos/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query Parameters

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Video Object below for a full list of values. | Complete list: id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names, is_stem_verified, favorites_count, video_duration,hashtag_info_list, sticker_info_list, effect_info_list, video_mention_list,video_label,video_tag | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/user/pinned_videos/?fields=id,share_count,view_count,comment_count,like_count' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.testtemp123test123test123' \
--data '{
    "username": "test_username"
    }'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | PinnedVideosData | The returned pinned videos list |
| error | ErrorStructV2 | Error object |

### PinnedVideosData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| pinned_videos_list | list<Video> | A list of video objects that match the query |

### Video Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | The unique identifier of the TikTok video |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The username as the unique identifier of the video creator |
| "region_code" | string | A two digit code for the country where the video creator registered their account. |
| "video_description" | string | The description of the pinned video |
| "music_id" | int64 | The music ID used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of views the video has received |
| "hashtag_names" | list<string> | The list of hashtags used in the video |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists. |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_URI". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video |
| "video_label" | Struct | Returns any information and labels associated with a video. |
| "video_duration" | int64 | The duration of the video, in seconds. |
| "is_stem_verified" | bool | Whether the video has been verified as being high quality STEM content. |
| favorites_count | int64 | The number of favorites that a video receives. |
| video_tag | Struct | "video_tag_type" and "video_tag_number" returned here Definitions: "video_tag_number" = 2, and "video_tag_type" = AIGC Type indicates "Creator Labelled as AI-Generated" "video_tag_number" = 1, and "video_tag_type" = AIGC Type indicates "AI-Generated" "video_tag_number" = 7, and "video_tag_type" = Branded Type indicates "Creator Earns Commission" "video_tag_number" = 1, and "video_tag_type" = Branded Type indicates "Paid Partnership" |

### Example
```
{
    "data": {
        "pinned_videos_list": [
            {
                "like_count": 6205646,
                "share_count": 15864,
                "view_count": 44199736,
                "comment_count": 15597,
                "id": 7777777777777777777
            },
            {
                "share_count": 6630,
                "view_count": 16171042,
                "comment_count": 6830,
                "id": 3333333333333333333,
                "like_count": 1464523
            },
            {
                "comment_count": 2685,
                "id": 9999999999999999999,
                "like_count": 189552,
                "share_count": 4796,
                "view_count": 1305777
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "202499999999999999999999999"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query User Reposted Videos.md

Docs
# Reposted Videos
## Request

| **HTTP URL** | https://open.tiktokapis.com/v2/research/user/reposted_videos/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (required) |

### Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/ | Bearer clt.example12345Example12345Example | Yes |
| Content-Type | string | The original media type of the resource | application/json | Yes |

### Query Parameters

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | Field names for desired data to be returned. It is a comma separated list. See Video Object below for a full list of values. | Complete list: id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favourites_count, video_duration, hashtag_info_list, sticker_info_list, effect_info_list, video_mention_list, video_label,video_tag | Yes |

### Body

| **Key** | **Type ** | **Description** | **Example Value** | **Required** |
| --- | --- | --- | --- | --- |
| username | string | The username as the unique identifier | "test_username" | Yes |
| max_count | int64 | The maximum number of reposted videos returned in a single response. Default is 20, max is 100. It is possible that the API returns fewer videos than the max count due to content moderation outcomes, videos being deleted, marked as private by users, or more. | 20 | No |
| cursor | int64 | Retrieve video results starting from the specified index | 15 | No |

### Example
```
curl --location 'https://open.tiktokapis.com/v2/research/user/reposted_videos/?fields=id,create_time,region_code,music_id,like_count,comment_count,share_count,view_count,hashtag_names' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer clt.test123test123temp123test123' \
--data '{
    "username": "test_username",
    "max_count": 6
    }'
```
## Response
### Body

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| data | RepostedVideosData | The returned list of reposted video objects |
| error | ErrorStructV2 | Error object |

### RepostedVideosData

| **Key** | **Type ** | **Description** |
| --- | --- | --- |
| user_reposted_videos | list<Video> | A list of video objects that match the query |
| cursor | int64 | Retrieve reposted videos starting from the specified index |
| has_more | bool | Whether there are more reposted videos or not |

### Video Object

| **Field Name** | **Type** | **Description** |
| --- | --- | --- |
| "id" | int64 | The unique identifier of the TikTok video |
| "create_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted |
| "username" | string | The username as the unique identifier of the video creator |
| "region_code" | string | A two-digit code for the country where the video creator registered their account |
| "video_description" | string | The description of the reposted video |
| "music_id" | int64 | The music ID used in the video |
| "like_count" | int64 | The number of likes the video has received |
| "comment_count" | int64 | The number of comments the video has received |
| "share_count" | int64 | The number of shares the video has received |
| "view_count" | int64 | The number of views the video has received |
| "hashtag_names" | list<string> | The list of hashtags used in the video |
| "hashtag_info_list" | Struct | "hashtag_id" and "hashtag_description". Returns all the unique hashtag_ids for each hashtag_name and a "hashtag_description" when one exists |
| "sticker_info_list" | Struct | "sticker_id" and "sticker_name". Returns the interactive sticker details when available for a video. |
| "effect_info_list" | Struct | "effect_id", "effect_name" and "effect_photo_URI". Returns further details of effects when used in a video. |
| "video_mention_list" | list<string> | Returns other users tagged in a video |
| "video_label" | Struct | Returns any information and labels associated with a video |
| "video_duration" | int64 | The duration of the video, in seconds |
| "is_stem_verified" | bool | Whether the video has been verified as being high quality STEM content |
| favorites_count | int64 | The number of favorites that a video receives |
| video_tag | Struct | "video_tag_type" and "video_tag_number" returned here Definitions: "video_tag_number" = 2, and "video_tag_type" = AIGC Type indicates "Creator Labelled as AI-Generated" "video_tag_number" = 1, and "video_tag_type" = AIGC Type indicates "AI-Generated" "video_tag_number" = 7, and "video_tag_type" = Branded Type indicates "Creator Earns Commission" "video_tag_number" = 1, and "video_tag_type" = Branded Type indicates "Paid Partnership" |

### Example
```
{
    "data": {
        "cursor": 7,
        "has_more": true,
        "reposted_videos": [
            {
                "comment_count": 64,
                "create_time": 1706442860,
                "id": 7777777777777777777,
                "like_count": 11169,
                "music_id": 1111111111111111111,
                "region_code": "MD",
                "share_count": 27,
                "view_count": 148105
            },
            {
                "like_count": 717,
                "share_count": 4,
                "comment_count": 12,
                "hashtag_names": [
                    "fyp",
                    "example",
                    "trainingseason",
                    "newsong"
                ],
                "music_id": 9999999999999999999,
                "region_code": "DO",
                "view_count": 56416,
                "create_time": 1706355306,
                "id": 3333333333333333333
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "202402000999900909990909090999999"
    }
}
```
Was this document helpful?


---
## SOURCE: Research Tools/API Reference/Query Video Comments.md

Docs
# Query Video Comments
# Request

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/video/comment/list/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

## Headers

| **Key** | **Type** | **Description** | **Example Value** |
| --- | --- | --- | --- |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example |
| Content-Type | string | Content type for the return data | application/json |

## Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields. Choose from the Comment Object fields. | **Complete list**: id, video_id, text, like_count, reply_count, parent_comment_id, create_time | Yes |

### Body Parameters
**Note**: In your query, you must request either `video_id` or `comment_id` depending on what data you want to retrieve. You may only request one or the other; both cannot be requested at the same time.
- Requesting `video_id` will return data for the specified video's comments.
- Requesting `comment_id` will return data for the specified comment's replies.

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| video_id | int64 | The ID of the video that the comments are made to | Yes |
| comment_id | int64 | The ID of the comment that the replies are made to | Yes |
| max_count | int64 | The number of comments in response. Default is 10, max is 100. It is possible that the API returns less comments than the max count due to reasons such as comments deleted by users etc. | No |
| cursor | int64 | The starting index of the comments in the response. | No |

### Example
`video_id`:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/comment/list/?fields=id%2Ctext' \
--header 'Authorization: Bearer clt.abcdefg' \
--header 'Content-Type: application/json' \
--data '{
   "video_id": 12345678901,
   "max_count": 100,
   "cursor":0
}'
```
`comment_id`:
```
curl --location 'https://open.tiktokapis.com/v2/research/video/comment/list/?fields=id%2Ctext' \
--header 'Authorization: Bearer clt.abcdefg' \
--header 'Content-Type: application/json' \
--data '{
   "comment_id": 1234,
   "max_count": "100",
   "cursor":0
}'
```
# Response
### Body

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | ResearchVideoCommentsData | A list of comment objects for a given video |
| error | ErrorStructV2 | Error object |

##### ResearchVideoCommentsData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| comments | CommentObject | The metadata of a comment. | See example below |
| cursor | int64 | The cursor of the next page. | 1050 |
| has_more | bool | Whether there are more videos or not. | true |

##### Comment Object

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| id | int | The unique ID for the comment |
| text | string | The text within the comment |
| video_id | int | The ID of the video or item that the comment is under |
| parent_comment_id | int | The ID of the comment's parent comment, if any |
| like_count | int | The number of likes a comment has |
| reply_count | int | The number of replies a comment has |
| create_time | int | The unix timestamp that the comment was created on |

### Example
`video_id`:
```
{
    "data": {
        "comments": [
            {
                "text": "AWEEEEEE 🥰🥰🥰",
                "video_id": 1234563451201523412,
                "create_time": 1671491598,
                "id": 12345616934634134,
                "like_count": 50,
                "parent_comment_id": 1234561201524010,
                "reply_count": 10
            },
            ...
        ],
        "has_more": true,
        "cursor": 300
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202207280326050102231031430C7E754E"
    }
}
```
`comment_id`:
```
{
    "data": {
        "has_more": false,
        "comments": [
            {
                "parent_comment_id": 1234567876543,
                "reply_count": 0,
                "text": "Lalalaa",
                "create_time": 1740510402,
                "display_name": "test",
                "id": 12345678909876
            }
        ],
        "cursor": 1
    },
    "error": {
        "code": "ok",
        "message": "ok",
        "log_id": "20123456789876543"
    }
}
```
**Personal information (phone number, email and credit card account, etc) in the comments will be redacted. See the example below.**
Comment (original): "Could you please contact me? 4059233930 is my number. Hi Edmond, email Mwen numerow at acharles@emortgagecapital.com, epi map relew. Download “Temu” make an account then search up 23216471 then click accept."
Comment (returned by the API): "Could you please contact me? 40******30 is my number.
Hi Edmond, email Mwen numerow at a*******@********************, epi map relew.
Download “Temu” make an account then search up ****6471 then click accept."
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Data Refresh For comment_wi.md

Docs
# Query comment_wi
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | comment_wi | Yes |
| condition_groups | object | Specifications for what data should be returned and processed | condition_groups = [ { "operator": "and", "conditions": [ { "field": "like_count", "operator": "gte", "field_values": ["3"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, text, parent_comment_id, like_count, reply_count, create_time, display_name | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, text, parent_comment_id, like_count, reply_count, create_time |

## Query Video Comment Data from Tiktok via SDK
Example code
```
from pyrqs import rqs

category = 'comment_wi'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "like_count",
                "operator": "gte",
                "field_values": ["3"]
            }
        ]
    }
]

fields = 'like_count'
limit = 10
client = rqs.RQSClient()
data = client.query(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Data Refresh For video_wi.md

Docs
# Query video_wi
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | video_wi | Yes |
| condition_groups | object | Specifications for what data should be returned and processed | condition_groups = [ { "operator": "and", "conditions": [ { "field": "like_count", "operator": "gte", "field_values": ["1000"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | display_name, country_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_date, duration_type, favorites_count, stem_verified, hashtag_info_list, effect_info_list, sticker_text,video_label,video_mention_list,video_tags | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, text, parent_comment_id, like_count, reply_count, create_time |

## Query Video Comment Data from Tiktok via SDK
Example code
```
from pyrqs import rqs

category = 'video_wi'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "like_count",
                "operator": "gte",
                "field_values": ["1000"]
            }
        ]
    }
]

fields = 'video_description'
limit = 10
client = rqs.RQSClient()
data = client.query(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query Playlist Info.md

Docs
# Query Playlists
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | playlists | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "playlist_id" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "playlist_id", "operator": "eq", "field_values": ["7145179763387255595"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | playlist_id, playlist_name, playlist_video_ids, playlist_last_updated, and playlist_item_total | No |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfully cancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | playlist_id, playlist_name, playlist_video_ids, playlist_last_updated, and playlist_item_total. |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Playlists from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'playlists'
fields = 'playlist_id, playlist_name, playlist_video_ids, playlist_last_updated, playlist_item_total'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "playlist_id",
                    "operator": "EQ",
                    "field_values": ["7145179763387255595"]
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query TikTok Shop Info.md

Docs
# Query TikTok Shop Info
## User Interaction - Shop API endpoint
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned. As the scripting language is the same across various data categories, this value will help determine what data to fetch. | tiktok_shop_info | Yes |
| condition_groups | object | Specifications for what data should be used for querying. | condition_groups = [``{``"operator": "and",``"conditions": [``{``"field": "shop_name",``"operator": "eq",``"field_values": ["tiktok_shop"]``}``]``}``] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | shop_name,shop_rating,shop_review_count,item_sold_count,shop_id | No |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 10, and the maximum value is 5000 per day across end points. (The value is low here as researchers can see the data and we want to keep this data to a low sample count only) **Execution Stage** The default value is 100, and the maximum value is 1000 in one query. If there are less than 1,000 results, that number will be returned in one go. (This is where researchers get access to all data and hence the increments are maximized based on performance possible) |  | No |

### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here for shops actively listed in the EU. | shop_name,shop_rating,shop_review_count,item_sold_count,shop_id,shop_performance_value |

Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query TikTok Shop Products.md

Docs
# Query TikTok Shop Products
## User Interaction - Products API endpoint
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned. As the scripting language is the same across various data categories, this value will help determine what data to fetch. | tiktok_shop_products | Yes |
| condition_groups | object | Specifications for what data should be used for querying. The data can be: product_name,shop_id, shop_name | condition_groups = [``{``"operator": "and",``"conditions": [``{``"field": "shop_id",``"operator": "eq",``"field_values": ["12345678910"]``}``]``}``] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | shop_name,product_id,product_sold_count,product_description,product_price,product_review_count,product_name,product_rating_1_count,product_rating_2_count,product_rating_3_count,product_rating_4_count,product_rating_5_count | No |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 10, and the maximum value is 5000 per day across end points. (The value is low here as researchers can see the data and we want to keep this data to a low sample count only) **Execution Stage** The default value is 100, and the maximum value is 1000 in one query. If there are less than 1,000 results, that number will be returned in one go. (This is where researchers get access to all data and hence the increments are maximized based on performance possible) |  | No |

### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here for products sold in the EU. | shop_name,product_id,product_sold_count,product_description,product_price,product_review_count,product_name,product_rating_1_count,product_rating_2_count,product_rating_3_count,product_rating_4_count,product_rating_5_count |

Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query TikTok Shop Reviews.md

Docs
# Query TikTok Shop Reviews
## User Interaction - Reviews API endpoint
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned. As the scripting language is the same across various data categories, this value will help determine what data to fetch. | tiktok_shop_reviews | Yes |
| condition_groups | object | Specifications for what data should be used for querying. The data can be: product_name, product_id, shop_name | condition_groups = [ { "operator": "and", "conditions": [ { "field": "product_id", "operator": "eq", "field_values": ["1234567810"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | product_name,review_text,review_like_count,create_time,review_rating | No |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 10, and the maximum value is 5000 per day across end points. (The value is low here as researchers can see the data and we want to keep this data to a low sample count only) **Execution Stage** The default value is 100, and the maximum value is 1000 in one query. If there are less than 1,000 results, that number will be returned in one go. (This is where researchers get access to all data and hence the increments are maximized based on performance possible) |  | No |

### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here foe reviews given for products sold in the EU. | product_name,review_text,review_like_count,create_time,review_rating |

Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Followers.md

Docs
# Query User Followers
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | followers_list | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": ["test user"] } ] }``] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | display_name, username | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | display_name, username |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Followers Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'followers_list'
fields = 'display_name, username'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Following.md

Docs
# Query User Following
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | following_list | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": ["test user"] } ] }``] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | display_name, username | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | display_name, username |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Following List from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'following_list'
fields = 'display_name, username'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Info.md

Docs
# Query User Info
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | profile | Yes |
| condition_groups | object | Specifications for what data should be returned and processed | `condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": [ "test user" ] } ] } ]` | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | username, bio_description, avatar_uri, is_verified, following_count, follower_count, video_count, likes_count, bio_url | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |
| bio_url | string | The user's bio url | EQ IN |  |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query Condition Fields and Operators

| Field | Description | Type | Allowed Operator |
| --- | --- | --- | --- |
| username | The unique user name on TikTok | string | EQ IN |
| bio_description | The user's bio description | string | EQ IN |
| avatar_uri | The url to a user's profile picture | string | EQ IN |
| is_verified | The user's verified status. True if verified, false if not | int64 | EQ |
| following_count | The number of people the user is following | int64 | EQ IN GT GTE LT LTE |
| follower_count | The number of followers the user has | int64 | EQ IN GT GTE LT LTE |
| video_count | The number of videos the user has posted | int64 | EQ IN GT GTE LT LTE |
| likes_count | The total number of likes the user has accumulated | int64 | EQ IN GT GTE LT LTE |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | username, bio_description, avatar_uri, is_verified, following_count, follower_count, video_count, likes_count |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Profile Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs

category = 'profile'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "username",
                "operator": "eq",
                "field_values": ["test user"]
            }
        ]
    }
]

fields = 'username, bio_description, avatar_uri, is_verified, following_count, follower_count'
limit = 1000
client = rqs.RQSClient()
data = client.query(category=category, condition_groups=condition_groups, fields=fields, limit=limit)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Liked Videos.md

Docs
# Query User Liked Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | liked_videos | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": ["test user"] } ] }``] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfully cancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | list | Data fields returned from the query. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag |

#### Example
```
from pyrqs import rqs
from datetime import datetime, timedelta
import json
category = 'liked_videos'
fields = 'id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["userc9mxbi9hyp"]
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Liked Videos Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'liked_videos'
fields = 'id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names,is_stem_verified,favorites_count'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Pinned Videos.md

Docs
# Query User Pinned Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | pinned_videos | Yes |
| condition_groups | object | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username", "operator": "eq", "field_values": ["test user"] } ] } ] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Pinned Videos Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'pinned_videos'
fields = 'id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names,is_stem_verified,favorites_count'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query User Reposted Videos.md

Docs
# Query User Reposted Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | reposted_videos | Yes |
| condition_groups | list | Specifications for what data should be returned and processed NOTE: "username" is the only query able parameter. "EQ" is the only operator. | condition_groups = [ { "operator": "and", "conditions": [ { "field": "username, "operator": "eq", "field_values": ["test user"] } ] } ] | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | string | The `and`conditions specify that all the conditions in the list must be met | No |
| or | string | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | string | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfully cancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | list | Data fields returned from the query. Interface will only return the fields listed here. | id, create_time, username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, hashtag_names, is_stem_verified, favorites_count, hashtag_info_list, effect_info_list, sticker_info_list, video_label, video_mention_list, video_tag |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Reposted Videos Data from TikTok via SDK
**Example code**
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json
category = 'reposted_videos'
fields = 'id,create_time,username,region_code,video_description,music_id,like_count,comment_count,share_count,view_count,hashtag_names,is_stem_verified,favorites_count'
limit = 60
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "username",
                    "operator": "EQ",
                    "field_values": ["test_user"] #enter a valid user name
                }
            ]
        }
]
data = client.query(category=category, fields = fields, condition_groups=condition_groups, limit=limit)
print(data)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/Query Video Comments.md

Docs
# Query VideoComments
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | comment | Yes |
| condition_groups | list | Specifications for what data should be returned and processed | condition_groups = [ { "operator": "and", "conditions": [ { "field": "id", "operator": "eq", "field_values": ["7347705421577563079"] } ] } ] | No |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | id, video_id, text, parent_comment_id, like_count, reply_count, create_time, display_name | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query  Condition Fields and Operators

| **Field** | **Description** | **Type** | **Allowed Operator** |  |
| --- | --- | --- | --- | --- |
| id | The unique ID for the comment | string | EQ IN |  |
| text | The text within the comment | string | EQ IN |  |
| video_id | The ID of the video or item that the comment is under | string | EQ IN |  |
| parent_comment_id | The ID of the comment's parent comment, if any | string | EQ IN |  |
| like_count | The number of likes a comment has | string | EQ IN GT GTE LT LTE |  |
| reply_count | The number of replies a comment has | string | EQ IN GT GTE LT LTE |  |
| create_time | The unix timestamp that the comment was created on | string | EQ IN GT GTE LT LTE |  |
| display_name | User's display name who post the comment | string | EQ IN |  |

#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | No |

### Check Query Task Sample Code
#### Example
```
status = client.check_query_task_status(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | id, video_id, text, parent_comment_id, like_count, reply_count, create_time |

### Get Query Task Sample Code
#### Example
```
data = client.get_query_task_result(task_id)
```
## Query Video Comment Data from Tiktok via SDK
Example code
```
from pyrqs import rqs

category = 'comment'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "video_id",
                "operator": "eq",
                "field_values": ["7347705421577563079"]
            }
        ]
    }
]

fields = 'id, video_id, text, parent_comment_id, like_count, reply_count, create_time'
limit = 100
client = rqs.RQSClient()
task_id = client.create_query_task(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
status = client.check_query_task_status(task_id)
```
Was this document helpful?


---
## SOURCE: Research Tools/VCE Reference/VCE Reference.md

Docs
# Query Videos
## Create Query Task
### Query
#### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| category | string | The data category for which the analysis is planned | video | Yes |
| condition_groups | list<Condition> | Specifications for what data should be returned and processed | `condition_groups = [ { "operator": "and", "conditions": [ { "field": "like_count", "operator": "gte", "field_values": ["1000"] } ] } ]` | Yes |
| fields | string | Data fields to be returned. Interface will only return the fields listed here. | username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_time, duration_type, favorites_count, stem_verified, hashtag_info_list, effect_info_list, sticker_text, video_label, video_mention_list, video_tags | Yes |
| limit | int | The maximum number of records that will be returned. **Test Stage** The default value is 100, and the maximum value is 5000 per day. **Execution Stage** The default value is 1000, and the maximum value is 100,000 in one query. | 200 | No |

#### Query Condition

| **Key** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| and | list<Condition> | The `and`conditions specify that all the conditions in the list must be met | No |
| or | list<Condition> | The `or`conditions specify that at least one of the conditions in the list must be met | No |
| not | list<Condition> | The `not`conditions specify that none of the conditions in the list must be met | No |

#### Query Condition Fields and Operators

| **Field** | **Description** | **Type** | **Allowed Operator** |
| --- | --- | --- | --- |
| id | Unique identifier for the TikTok video. Also called "item_id" or "video_id" | string | EQ IN |
| create_time | UTC Unix epoch (in seconds) of when the TikTok video was posted. (Inherited field from TNS research API) | string | EQ IN GT GTE LT LTE |
| username | The video creator's username | string | EQ IN |
| region_code | A two digit code for the country the video was posted in | string | EQ IN |
| video_description | The description of the video, also known as the title | string | EQ IN LIKE |
| music_id | The music_id used in the video | int64 | EQ IN |
| like_count | The number of likes the video has received. | string | EQ IN GT GTE LT LTE |
| comment_count | The number of comments the video has received. | string | EQ IN GT GTE LT LTE |
| share_count | The number of shares the video has received. | string | EQ IN GT GTE LT LTE |
| view_count | The number of video views the video has received. | int64 | EQ IN GT GTE LT LTE |
| effect_ids | The list of effect ids applied on the video | list<string> | CONTAINS |
| hashtag_names | The list of hashtag names that the video participates in | list<string> | CONTAINs |
| playlist_id | The ID of playlist that the video belongs to | string | EQ IN |
| voice_to_text | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) | string | EQ IN |
| duration_type | The duration of the video, in seconds. | int | EQ IN GT GTE LT LTE |
| hashtag_id | Hash tag id which is associated with the video. | string | EQ IN |
| hashtag_name | Hash tag name which is associated with the video. | string | EQ IN |
| hashtag_description | Hashtag description which is associated with the video. | string | EQ IN |
| effect_id | Effect ID that the video used | string | EQ IN |
| effect_name | Effect name that the video used | string | EQ IN |
| effect_photo_url | Effect photo url that the video used | string | EQ IN |
| sticker_text | Sticker text that the video has | string | EQ IN |
| video_label | Video label that the video contains | list<string> | CONTAINs |
| video_mention_list | People who are mentioned in the video | list<string> | CONTAINs |
| video_tags | Video tags that the video contains | list<string> | CONTAINs |

#### Create Query Task Sample Code
This interface will create a query task at TikTok, and it will return a task id. Users can use this id to check the status, get the result and cancel the result in the future.
#### Example
```
from pyrqs import rqs

category = 'video'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "region_code",
                "operator": "eq",
                "field_values": ["NL"]
            }
        ]
    }
]

fields = 'username,region_code,video_description,music_id,like_count'
limit = 1000
client = rqs.RQSClient()
task_id = client.create_query_task(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
```
#### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 |

## Check Query Task Status
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| status | string | Data query job task status | Created AnalysisFailed Processing Completed Cancelled Validating | Yes |

### Check Query Task Result Code Sample
#### Example
```
data = client.get_query_task_result(task_id)
```
## Cancel Query Task
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| success | bool | Whether the request was successfullycancelled | True |

### Cancel Query Task Sample Code
#### Example
```
result = client.cancel_query_task(task_id)
```
## Get Query Task Result
### Query Parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| task_id | int | Data query job task identifier | 12345 | Yes |

#### Get_query_task_result_example
##### Example
```
data = client.get_query_task_result(task_id)
```
### Response

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| result | string | Data fields returned from the query. Interface will only return the fields listed here. | username, region_code, video_description, music_id, like_count, comment_count, share_count, view_count, effect_ids, hashtag_names, playlist_id, voice_to_text, id, create_time, duration_type, favorites_count, and stem_verified. |

## Query Video Data from Tiktok via SDK
Example code
```
from pyrqs import rqs
import time
from datetime import datetime, timedelta
import json

category = 'video'
fields = 'username,like_count,hashtag_info_list,video_sticker_id,video_mention_list,video_label'
limit = 100
client = rqs.RQSClient()
condition_groups = [
        {
            "operator": "and",
            "conditions": [
                {
                    "field": "video_description",
                    "operator": "LIKE",
                    "field_values": ["%tiktok%"]
                },
                {
                    "field": "hashtag_names",
                    "operator": "CONTAINS",
                    "field_values": ["tiktok"]
                }
            ]
        }
]
data = client.query(category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
Was this document helpful?
