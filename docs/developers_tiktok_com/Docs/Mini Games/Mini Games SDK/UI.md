Docs
# UI
This API helps align the menu button within the mini game's navigation bar.
**Note**: This API is only required for games that use HTML runtime.
## .getMenuButtonBoundingClientRect()
Get the layout position information of the menu button (capsule button in the upper right corner). Coordinate information starts from the upper left corner of the screen. Unit is in pixels (px).
### Return value
Layout position information of the menu button:

| Attribute | Type | Instructions |
| --- | --- | --- |
| width | number | Width, unit: px |
| height | number | Height, unit: px |
| top | number | Upper boundary coordinate, unit: px |
| right | number | Right boundary coordinate, unit: px |
| bottom | number | Lower boundary coordinate, unit: px |
| left | number | Left boundary coordinate, unit: px |

### Example
```
const res = TTMinis.game.getMenuButtonBoundingClientRect()

console.log(res.width)
console.log(res.height)
console.log(res.top)
console.log(res.right)
console.log(res.bottom)
console.log(res.left)
```
Was this document helpful?