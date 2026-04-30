Docs
# Video Object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Unique identifier for the TikTok video. Also called "item_id" |
| create_time | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. |
| cover_image_url | string | A CDN link for the video's cover image. The image is static. Due to our trust and safety policies, the link has a **TTL****of 6 hours.** |
| share_url | string | A shareable link for this TikTok video. Note that the website behaves differently on Mobile and Desktop devices. |
| video_description | string | The description that the creator has set for the TikTok video. Max length: 150 |
| duration | int32 | The duration of the TikTok video in seconds. |
| height | int32 | The height of the TikTok video. |
| width | int32 | The width of the TikTok video. |
| title | string | The video title. Max length: 150 |
| embed_html | string | HTML code for embedded video |
| embed_link | string | Video embed link of tiktok.com |
| like_count | int32 | Number of likes for the video |
| comment_count | int32 | Number of comments on the video |
| share_count | int32 | Number of shares of the video |
| view_count | int64 | Number of views of the video |

Was this document helpful?