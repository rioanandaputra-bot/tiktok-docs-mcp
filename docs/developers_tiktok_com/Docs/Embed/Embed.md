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