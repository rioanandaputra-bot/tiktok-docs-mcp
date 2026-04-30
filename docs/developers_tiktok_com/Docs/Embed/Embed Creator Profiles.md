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