Docs
# Introduction
[Embedded Videos enable TikTok videos to be embedded into your articles or websites. This helps to foster storytelling, and provides proper attribution by showing the video creator, video description and background sound in the form of TikTok's custom player. It also links back to the corresponding content on TikTok](https://www.tiktok.com).
## Embed from TikTok.com
Follow these steps to get the embed code from a TikTok video:
- [Open the video webpage on tiktok.com](https://www.tiktok.com)
- [Example video webpage](https://www.tiktok.com/@scout2015/video/6718335390845095173)
- You must open this webpage in the browser from a non-mobile surface
- Click the Share button (right-facing arrow icon), and then click Embed
- From the popup window, simply copy and paste the code into the destination webpage, where you wish to attach the video. Voilà, the embedded video will automatically load on the page.
[@scout2015](https://www.tiktok.com/@scout2015?refer=embed)
[[[Scramble up ur name & I’ll try to guess it😍❤️ #foryoupage](https://www.tiktok.com/tag/foryoupage?refer=embed) #petsoftiktok](https://www.tiktok.com/tag/petsoftiktok?refer=embed) #aesthetic](https://www.tiktok.com/tag/aesthetic?refer=embed)
[♬ original sound - tiff](https://www.tiktok.com/music/original-sound-6689804660171082501?refer=embed)
Embedded videos support volume control during playback and provide recommended videos at the end of each playback.
[[All buttons and texts on the embedded video are interactive. By tapping on them, the user will be linked directly to the corresponding content page on tiktok.com](https://www.tiktok.com). The "Discover more on TikTok" button at the bottom of the embedded card will either link users to the Trending Page](https://www.tiktok.com/trending) if the user is browsing on desktop, or deeplink users to the TikTok product page on the App Store / Google Play if browsing on a mobile device.
A video's availability is consistent in and outside the TikTok app, as moderation standards and results are applied to both in-app content and embedded content. For example, if a video has been removed from the TikTok app, the same video in its embedded form on the web will no longer be accessible.
Note: Some browsers in CN will forbid the use of TikTok's custom player and show the default player provided by the browser.
## Embedded for developers
Programmatically, you may convert a TikTok's video URL into embedded video markup by using the oEmbed API. It allows you to get the embed code and additional information about the video associated with the webpage link provided.
### API

| GET | /oembed | Returns the embed code and information about the video |
| --- | --- | --- |

### Parameters
**Request**

| Param | Description |
| --- | --- |
| url | The video link for embedding |

**Response**
[The response format follows the specification of https://oembed.com/](https://oembed.com/), please check it out for more details.
### Example
**Request URL**
```
https://www.tiktok.com/oembed?url=https://www.tiktok.com/@scout2015/video/6718335390845095173
```
**Response Data**
```
{
  "version": "1.0",
  "type": "video",
  "title": "Scramble up ur name & I’ll try to guess it😍❤️ #foryoupage #petsoftiktok #aesthetic",
  "author_url": "https://www.tiktok.com/@scout2015",
  "author_name": "Scout & Suki",
  "width": "100%",
  "height": "100%",
  "html": "<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@scout2015/video/6718335390845095173\" data-video-id=\"6718335390845095173\" data-embed-from=\"oembed\" style=\"max-width: 605px;min-width: 325px;\" > <section> <a target=\"_blank\" title=\"@scout2015\" href=\"https://www.tiktok.com/@scout2015?refer=embed\">@scout2015</a> <p>Scramble up ur name & I’ll try to guess it😍❤️ <a title=\"foryoupage\" target=\"_blank\" href=\"https://www.tiktok.com/tag/foryoupage?refer=embed\">#foryoupage</a> <a title=\"petsoftiktok\" target=\"_blank\" href=\"https://www.tiktok.com/tag/petsoftiktok?refer=embed\">#petsoftiktok</a> <a title=\"aesthetic\" target=\"_blank\" href=\"https://www.tiktok.com/tag/aesthetic?refer=embed\">#aesthetic</a></p> <a target=\"_blank\" title=\"♬ original sound - 𝐇𝐚𝐰𝐚𝐢𝐢𓆉\" href=\"https://www.tiktok.com/music/original-sound-6689804660171082501?refer=embed\">♬ original sound - 𝐇𝐚𝐰𝐚𝐢𝐢𓆉</a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>",
  "thumbnail_width": 720,
  "thumbnail_height": 1280,
  "thumbnail_url": "https://p16.muscdn.com/obj/tos-maliva-p-0068/06kv6rfcesljdjr45ukb0000d844090v0200010605",
  "provider_url": "https://www.tiktok.com",
  "provider_name": "TikTok"
}
```
Was this document helpful?