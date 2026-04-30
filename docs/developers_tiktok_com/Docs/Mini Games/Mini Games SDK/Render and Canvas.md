Docs
# Render and Canvas
## Canvas
### .createCanvas
Creates a canvas object. The first call creates the primary on-screen canvas; subsequent calls create off-screen canvases for background rendering. Returns a Canvas object.
#### Return value

| Field | Type | Description |
| --- | --- | --- |
| width | number | Width of the canvas |
| height | number | Height of the canvas |
| getContext | function | Gets the drawing context of the canvas object |
| toDataURL | function | Returns the content drawn on the canvas in the format of a string. After enabling the open data domain, all canvases in the main domain cannot call this interface. |

### .createImage
Creates an image object, used for loading and drawing images onto a canvas. Returns an Image object with `src`, `width`, `height`, and event listener methods.
#### Return value
The return value is Image, which is of type object. The detailed parameter descriptions are as follows:

| Field | Type | Description |
| --- | --- | --- |
| src | string | URL of the image, base64 content, or ArrayBuffer data |
| width | number | True width of the image |
| height | number | True height of the image |
| addEventListener | function | Add event listener |
| removeEventListener | function | Remove event listener |

### Canvas object
#### .getContext(enum contextType)
Returns the drawing context (`2d` or `webgl`) for the canvas.
##### Parameter
[When the parameter is 2D, the return value `CanvasRenderingContext2D` implements  most of the properties and methods defined by the HTML Canvas 2D Context](https://html.spec.whatwg.org/multipage/), and the features **not** currently supported are as listed:
- `CanvasRenderingContext2D.clip`
- `CanvasRenderingContext2D.lineDashOffset`
- `CanvasRenderingContext2D.isPointInPath`
- `CanvasRenderingContext2D.isPointInStroke`
[When the parameter is `webgl`, the return value WebGLRenderingContext implements all attributes, methods, and constants defined by WebGL 1.0](https://www.khronos.org/registry/webgl/specs/latest/1.0/).

| Field | Default Value | Value | Description | Required |
| --- | --- | --- | --- | --- |
| contextType | None | 2d/webgl | Context type | Yes |

##### Return value

| Type | Description |
| --- | --- |
| object | Canvas context object |

#### .toDataURL
Returns canvas content as a data URI string.
##### Return value
String in data URI format
## Frame Rate
Note: Frame Rate JavaScript APIs are supported starting from SDK version 0.6.0. Lower versions must be adjusted for compatibility.
### .setPreferredFramesPerSecond
The rendering frame rate can be modified. The default rendering frame rate is 60 frames per second. After modification, the callback frequency of requestAnimationFrame will change.
#### Parameter

| Field | Type | Description |
| --- | --- | --- |
| fps | number | Frame rate, valid range 1 - 60. |

## Font
### .loadFont
Loads a custom font and returns its font‑family name or `null`.
#### Parameter

| Field | Type | Description |
| --- | --- | --- |
| path | string | Font file path. Supports local paths and code package paths |

#### Return value

| Type | Description |
| --- | --- |
| string | If the font is successfully loaded, return the font family value; otherwise, return null |

## Was this document helpful?