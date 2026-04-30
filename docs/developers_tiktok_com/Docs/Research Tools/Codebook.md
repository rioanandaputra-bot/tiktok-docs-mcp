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