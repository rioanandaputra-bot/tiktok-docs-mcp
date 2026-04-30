Docs
# Sharing
Enable users to share content to stories, send direct messages to contacts, or customize the metadata attached to copied links.
## .shareToStory
Allow users to share the TikTok Minis to their TikTok story.
### Parameters
Object object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| title | string | Share title | No |
| desc | string | Share description | No |
| imageUrl | string | Share image | No |
| query | string | Share custom query | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

## .shareAppMessage
Actively initiate sharing via direct message and enter the contact selection interface.
### Parameters
Object object

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| title | string | Forward title | No |
| imageUrl | string | Forward the link to the displayed image | No |
| query | string | Query string. After entering from this forwarded message, you can obtain the query in the launch parameters through the `TTMinis.game.getLaunchOptionsSync()`function or the `TTMinis.game.onShow()`function. | No |
| subtitle | string | Subtitle | No |
| templateType | string | Template style, 1 | 2 | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

## .onCopyUrl
Function listener: Listen for the event triggered when the user clicks the "Copy link" button in the menu.
### Parameter
Object res

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| title | string | Share title | No |
| desc | string | Share description | No |
| imageUrl | string | Share image | No |
| query | string | Share custom query | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

### Example
```
// Bind sharing parameters
  TTMinis.game.onCopyUrl(() => {return { query: 'a=1&b=2' }})
  // Unbind sharing parameters
  TTMinis.game.offCopyUrl()
```
## .offCopyUrl
Remove all the listener functions for the event triggered when the user clicks the "Copy Link" button in the menu.
### Example
```
// Bind sharing parameters
  TTMinis.game.onCopyUrl(() => {return { query: 'a=1&b=2' }})
  // Unbind sharing parameters
  TTMinis.game.offCopyUrl()
```
Was this document helpful?