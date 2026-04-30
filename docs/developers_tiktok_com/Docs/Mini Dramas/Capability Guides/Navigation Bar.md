Docs
# Navigation Bar
Since it is necessary to adapt to the custom navigation bar, add it to the original configuration`style`. This allows developers to configure the style of the navigation bar. The specific config modification is as follows:
```
{
  "navbar": {
    "style": "custom", // custom: custom navigation bar, default: default navigation bar
    "bgColorLight": "#ffffff",
    "bgColorDark": "#000000",
  },
  ...
}
```

| **Parameter** | **Description** | **Values** |
| --- | --- | --- |
| style | The style of the navigation bar, default style if not set | `custom`: Custom navigation bar. Developers can customize the style of the navigation bar. `default`: The default navigation bar is provided by Minis Framework and only supports color modification. |

## TTMinis.setNavigationBarColor
Set the foreground and background colors of the navigation bar.

| **Parameter** | **Type ** | **Description ** |
| --- | --- | --- |
| frontColor | string | Foreground color value, including the color of buttons, titles, and status bars, only supports #ffffff and #000000 |
| backgroundColor | string | Background color value, valid value is hexadecimal color |

### Example
```
if (TTMinis.canIUse("setNavigationBarColor")) {
    TTMinis.setNavigationBarColor({
      frontColor: string;
      backgroundColor: string;
    }, function (res) {
      console.log(res.is_success);
    })
}
```
## TTMinis.getMenuButtonBoundingClientRect
To customize the navigation bar, you must first obtain the position of the menu button. You can then create a custom navigation bar according to the position of the menu button. The position of the capsule button provides the `TTMinis.getMenuButtonBoundingClientRect()`API to get the layout position information of the menu button (the capsule button in the upper right corner). The coordinate information is based on the upper left corner of the screen as the origin.

| **Param** | **Type** | **Comment** |
| --- | --- | --- |
| width | number | Width, unit: px |
| height | number | Height, unit: px |
| top | number | Upper boundary coordinate, unit: px |
| right | number | Right border coordinates, unit: px |
| bottom | number | Lower boundary coordinate, unit: px |
| left | number | Left boundary coordinate, unit: px |

The menu button layout is formatted as such: `capsuleButtonLayout = {"left": xx, "right": xx, "top": xx, "bottom": xx, "width": xx, "height": xx}`
**Note**: Since the coordinate information is based on the upper left corner of the screen as the origin, this api only takes effect when style == custom. When style == default, these params are all 0
### Example
```
const capsuleButtonLayout = TTMinis.getMenuButtonBoundingClientRect();

// Based on the position of the button as a reference, set the position of other elements to achieve alignment and other capabilities
```
Was this document helpful?