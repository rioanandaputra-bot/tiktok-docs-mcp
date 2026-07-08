# Embed

> Consolidated from 3 source files.



---
## SOURCE: Embed/Embed Creator Profiles.md

Docs
# Introduction
[[Creator Profile Embed allows TikTok creator profiles to be embedded into your articles or websites. With this tool you can showcase an overview of a creator's presence on TikTok, including the number of users who follow that creator, the number of users that creator follows, and the number of likes that creator has received across all of their TikTok videos. The embedded creator profile also contains a selection of up to ten of the creator's most recent videos. Like embedded videos](https://developers.tiktok.com/doc/embed-videos), most of the components in an embedded creator profile link back to the corresponding pages on TikTok.com](https://www.tiktok.com) or the app.
## Private and underage accounts
Private accounts and underage accounts cannot be embedded. In these cases, the share icon will be grayed out and won't be interactive. Accounts which are later set as "private" on TikTok will be shown as private on the embed profile card as well, as are underage accounts. Users who have not yet set their age in their TikTok profile are shown as private by default.
## Embed from TikTok.com
[You can get the embed code by visiting the creator's profile page on TikTok.com](https://www.tiktok.com). Click the share icon and select "Embed" from the dropdown.
[See https://www.tiktok.com/@scout2015](https://www.tiktok.com/@scout2015) to see this embed workflow
Once you have clicked on this button, a popup card will appear with the embed code. Click "Copy code" to copy the entire embed code to your clipboard and paste it where you wish to display the creator profile card. The embedded profile card will automatically show up on your page.
Creator Profile Embed can support a wide variety of screens. Videos will automatically play when moused over on desktop or when on-screen on mobile and can be scrolled to the side.

| - | Autoplay | Scroll |
| --- | --- | --- |
| Mobile | Whenever on-screen | Yes - tap and scroll |
| Desktop | On mouseover | Yes - mouse scroll, scrollbar |

| Desktop | Mobile |
| --- | --- |
|  |  |

[Most of the components on the embedded creator profile are interactive. By clicking or tapping on them, the user will be linked directly to the corresponding content page on TikTok.com](https://www.tiktok.com) or the app. The "Open TikTok" button at the bottom of the embedded profile card will link users to the creator’s profile page, as will the avatar, username, metrics, and user description. Video cards contained within the embedded creator profile link to their respective videos in the webpage or the app.
The same moderation standards apply to both in-app and embedded content. For example, if a video has been removed from the TikTok app, the same video in its embedded form on the web will no longer be accessible.
Note: Some browsers in China will forbid the use of TikTok's custom player and show the default player provided by the browser.
## Embed for developers
Programmatically, you may convert a TikTok creator profile URL into embedded markup by using the oEmbed API. It allows you to get the embed code and additional information about the creator profile associated with the webpage link provided.
### API

| GET | /oembed | Returns the embed code and information about the creator profile |
| --- | --- | --- |

### Parameters
**Request**

| Param | Description |
| --- | --- |
| url | The creator profile link for embedding |

**Response**
[The response format follows the specification of https://oembed.com/](https://oembed.com/), please check it out for more details.
### Example
**Request URL**
```
https://www.tiktok.com/oembed?url=https://www.tiktok.com/@scout2015
```
**Response Data**
```
{
  "version":"1.0",
  "type":"rich",
  "title":"Scout, Suki & Stella's Creator Profile",
  "author_url":"https://www.tiktok.com/@scout2015",
  "author_name":"Scout, Suki & Stella",
  "width":"100%",
  "height":"100%",
  "html":"<blockquote class=\"tiktok-embed\" cite=\"https://www.tiktok.com/@scout2015\" data-unique-id=\"scout2015\"  data-embed-type=\"creator\" style=\"max-width: 720px; min-width: 288px;\" data-embed-from=\"oembed\"> <section> <a target=\"_blank\" href=\"https://www.tiktok.com/@scout2015?refer=creator_embed\">@scout2015</a> </section> </blockquote> <script async src=\"https://www.tiktok.com/embed.js\"></script>",
  "provider_url":"https://www.tiktok.com",
  "provider_name":"TikTok"
}
```
Was this document helpful?


---
## SOURCE: Embed/Embed Videos.md

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


---
## SOURCE: Embed/Embed.md

Docs
# Embed Player
## Introduction
This embedded player consists of a TikTok post hosted inside of an inline frame (iframe) element. This player allows you to do the following:
- Customize the player by appending query parameters in the iframe URL. For example, you can display the music information of this video using the "description" parameter, or you can hide the video controls using the "controls" parameter.
- Control the player by messaging the HTML host to enable functionality like playing, pausing, muting, and more.
See more on the custom options and messaging communication below.
## Get started
First locate the TikTok post you want to embed in the player. The post URL follows this structure: www.tiktok.com/player/v1/{tiktok_post_id}.
[View the following example: https://www.tiktok.com/player/v1/6718335390845095173](https://www.tiktok.com/player/v1/6718335390845095173)
[You can find the TikTok post ID on from the post URL. For example, 6718335390845095173 is the post ID from the URL https://www.tiktok.com/@scout2015/video/6718335390845095173](https://www.tiktok.com/@scout2015/video/6718335390845095173)
## Customize the player
You can customize the player by choosing which playback interface elements should be hidden or displayed.
[For example, this URL displays the TikTok post's music info and the description: https://www.tiktok.com/player/v1/6718335390845095173?music_info=1&description=1](https://www.tiktok.com/player/v1/6718335390845095173?music_info=1&description=1)

| **Name** | **Description** | **Post type** |
| --- | --- | --- |
| controls | 1: Display the progress bar and all the control buttons, such as the playvolume control and fullscreen buttons 0: Hide the progress bar and all control buttons Default to 1 | video, image |
| progress_bar | 1: Display the progress bar 0: Hide the progress bar Default to 1 | video |
| play_button | 1: Display the play button 0: Hide the play button Default to 1 | video |
| volume_control | 1: Display the volume control button 0: Hide the volume control button Default to 1 | video, image |
| fullscreen_button | 1: Display the fullscreen button 0: Hide the fullscreen button Default to 1 | video, image |
| timestamp | 1: Display the video's current playback time and duration 0: Hide the time info Default to 1 | video |
| loop | 1: Play the current video repeatedly 0: Stop the video while it ends Default to 0 | video |
| autoplay | 1: Automatically play the video when the player loads 0: Do not start playing automatically Default to 0 | video |
| music_info | 1: Display the music info 0: Do not display the music info Default to 0 | video, image |
| description | 1: Display the video description 0: Do not display the video description Default to 0 | video, image |
| rel | 1: Show recommended videos as related videos 0: Show the current video author's videos as related video Default to 1 | video |
| native_context_menu | 1: Display the browser's native context menu 0: Hide the browser's native context menu Default to 1 | video, image |
| closed_caption | 1: Display the closed caption icon 0: Hide the closed caption icon Default to 1 | video |
| muted | 1: Set the default volume to 0 and prevent the user from changing the volume 0: Enable volume controls Default to 0 | video, image |

## Message the HTML host
[The HTML host communicates with the iframe embedded video page through the `Window::postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)` method, where the message body is defined as follows:
```
interface EmbeddedPlayerMessage<T> {
  'x-tiktok-player': boolean; // Lets you know that this is an embed message.
  value: T;
  type: string; // Defines the message types below. 
}
```
### Host to player messages

| **Method name ** **(type in ****EmbeddedPlayerMessage****)** | **Parameter type ** **(value in ****EmbeddedPlayerMessage****)** | **Value** | **Post type** | **Remarks** |
| --- | --- | --- | --- | --- |
| `play` | void | void | video, image | Use this method to play videos in video posts and to play music in image posts |
| `pause` | void | void | video, image | Use this method to pause videos in video posts and to pause music in image posts |
| `seekTo` | number | 0–(video length) | video, image | For video posts, use this method to seek the video's time, measured in seconds. For image posts, use this method to seek the music's time, also measured in seconds. |
| `mute` | void | void | video, image |  |
| `unMute` | void | void | video, image |  |
| `navigateTo` | number | 0–(number of images -1) | image | Use this method to navigate to the index of the desired image |

### Player to host messages

| **Method name ** **(type in ****EmbedMessage****)** | **Parameter type ** **(value in ****EmbedMessage****)** | **Value** | **Post type** | **Remarks** |
| --- | --- | --- | --- | --- |
| `onPlayerReady` | void | void | video, image |  |
| `onStateChange` | number | -1: init 0: ended 1: playing 2: paused 3: buffering | video, image |  |
| `onCurrentTime` | currentTime: number duration: number | 0–(video length) | video, image | The current playback time measured in seconds |
| `onMute` | boolean | True/False | video, image |  |
| `onVolumeChange` | number | 0–100 | video, image | The percentage of the volume relative to the maximum volume measured on a 0–100 scale |
| `onError`(deprecated) | number | [MediaError.code - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/MediaError/code) | video, image |  |
| `onImageChange` | number | 0–(number of images -1) | image | The index of the image currently in display |
| `onPlayerError` | errorCode: number errorType: string | Reference table below | Video, image |  |

#### Player Error Reporting
The embedded player will emit errors to the host through the `onPlayerError` interface.

| **Error Category** | **Error Code** | **Error Type** | **Description** |
| --- | --- | --- | --- |
| **Data & Validation** | **1000-1099** |  |  |
|  | 1001 | INVALID_VIDEO | Invalid Media ID, no video/photo found |
| **Network & Infrastructure** | **2000-2099** |  |  |
|  | 2001 | SERVER_ERROR | TikTok servers fail to serve the resource |
| **Player & Runtime** | **3000-3099** |  |  |
|  | 3001 | PLAYBACK_ERROR | Video/audio playback failure |
|  | 3002 | AUTOPLAY_ERROR | Video/audio fails to autoplay due to browser security policies |

### Code example
```
<html>
<body>

<h1>The iframe element</h1>

<form action="javascript:seekTo(to)">
  <label for="fname">Jump to (seconds)</label><br>
  <input type="text" id="to" name="to" value="20"><br>
</form>

<iframe height="300" width= "400" src="https://www.tiktok.com/player/v1/6718335390845095173?&music_info=1&description=1" allow="fullscreen" title="test"></iframe>
<br />

<script>
  // Receive messages 
        window.addEventListener('message', (event) => {
    // do something
  });

  // Send messages
  function seekTo(to) {
    const iframe = document.querySelector("iframe");
    iframe.contentWindow.postMessage({type: "seekTo", value: Number(to.value), "x-tiktok-player": true}, '*');
  }
</script>

</body>
</html>
```
Was this document helpful?
