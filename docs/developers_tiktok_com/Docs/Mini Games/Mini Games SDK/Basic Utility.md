Docs
# Basic Utility
These basic utility APIs provide core functionality for networking and checking compatibility within the Mini Game environment.
## .request
Initiate an HTTPS network request from the mini‑game runtime. Use it to call your own backend or lightweight public endpoints.

| **Field** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `url` | string | Yes | The target Developer Server Interface Address (your backend) for the request. |
| `data` | string/object | No | The data payload to send with the request (e.g., JSON or form data). |
| `header` | Object | No | Custom HTTP headers. Note: The Referer header cannot be set. Content-type defaults to application/json. |
| `timeout` | number | No | Request timeout in milliseconds. |
| `method` | string | No | HTTP request method (defaults to GET). |
| `RequestTask.abort` | _Method_ |  | Interrupts a currently running network request. |

### RequestTask
#### RequestTask.abort
Abort an in‑flight `request` task, like when the user navigates away.
```
const task = TTMinis.game.request({...});
// later
task.abort();
```
## .canIUse(schema)
An API compatibility check that determines whether a specific TikTok JavaScript API, its method, return value, or parameter is available in the user's current TikTok version. This prevents runtime errors on older clients.
Always gate new or version‑specific features before use (features available from v41.0.0).

| **Parameter** | **Description** | **Example schema** |
| --- | --- | --- |
| **API** | The base name of the API to check (for example: login, setLoadingProgress). | `TTMinis.game.canIUse('login')` |
| **method** | Checks a specific part of the API call lifecycle or object: | `TTMinis.canIUse('login.success')` |
| **param** | Used after a method to check a specific property (for example: checking if the code parameter is available in the login success return). | `TTMinis.canIUse('login.success.code')` |
| **option** | Checks if a specific enumeration value (a fixed string or number option) for a parameter is available. | `TTMinis.canIUse('onShow.callback.launch_from.anchor')` |

### API
The **API** parameter specifies the specific API name to be checked, such as `login`, `setLoadingProgress`, `getMenuButtonBoundingClientRect`, and more.
```
// Check if the login API is available
TTMinis.game.canIUse('login');

// Check if the getMenuButtonBoundingClientRect API is available
TTMinis.game.canIUse('getMenuButtonBoundingClientRect');
```
### Method
The **method** parameter specifies the calling method of the API, and valid values include the following:

| **Method** | **Description** | **Example** |
| --- | --- | --- |
| success | Callback function for successful execution | `TTMinis.canIUse('login.success')` |
| return | Return result of the synchronization method | `TTMinis.canIUse('getMenuButtonBoundingClientRect.return')` |
| callback | Callback parameters of asynchronous methods | `TTMinis.canIUse('onShow.callback')` |
| object | Validation of the request parameter object | `TTMinis.canIUse('login.object')` |

The following are example usages of each calling method:
- **success:** Callback function for successful execution check and its parameters:
```
// Original API call method
TTMinis.login({
  success: (res) => {
    console.log(res.code); // Check if res.code is available
    console.log(res.token); // Check if res.token is available
  }
});

// Using canIUse to check
TTMinis.game.canIUse('login.success'); // Check if the success callback is available
TTMinis.game.canIUse('login.success.code'); // Check if the code parameter in the success callback is available
TTMinis.game.canIUse('login.success.token'); // Check if the token parameter in the success callback is available
```
- **return**: Check the return value of the synchronization method:
```
// Original API call method
const buttonInfo = TTMinis.getMenuButtonBoundingClientRect();
console.log(buttonInfo.width);
console.log(buttonInfo.height);

// Using canIUse to check
TTMinis.game.canIUse('getMenuButtonBoundingClientRect.return'); // Check if the return value is available
TTMinis.game.canIUse('getMenuButtonBoundingClientRect.return.width'); // Check if the width property in the return value is available
TTMinis.game.canIUse('getMenuButtonBoundingClientRect.return.height'); // Check if the height property in the return value is available
```
- ** callback**: Check the callback parameters of asynchronous methods:
```
// Original API call method
TTMinis.onShow((params) => {
  console.log(params.query);
});

// Using canIUse to check
TTMinis.game.canIUse('onShow.callback'); // Check if the callback is available
TTMinis.game.canIUse('onShow.callback.query'); // Check if the query parameter in the callback is available
```
- **object**: Check the parameters of the request parameter object
```
// Original API call method
TTMinis.login({
  clientKey: 'clientKey',
  scope: 'scope'
});

// Using canIUse to check
TTMinis.game.canIUse('login.object'); // Check if the object parameter is available
TTMinis.game.canIUse('login.object.clientKey'); // Check if the clientKey parameter in the object is available
TTMinis.game.canIUse('login.object.scope'); // Check if the scope parameter in the object is available
```
### Param
The **param** parameter specifies the specific parameter or return value to be checked, and has different usages depending on the method:

| **Method** | **Description** | **Example** |
| --- | --- | --- |
| success | Callback parameters for successful API execution | `TTMinis.canIUse('login.success.code')` |
| callback | Parameters of the callback method passed in by the API | `TTMinis.canIUse('onShow.callback.query')` |
| object | Parameters of the parameter object passed in by the API | `TTMinis.canIUse('login.object.clientKey')` |
| return | Parameters of the return value from API execution | `TTMinis.canIUse('getMenuButtonBoundingClientRect.return.left')` |

### Option
The **option** parameter is used to check whether a specific enumeration value is available. In most cases, this parameter does not need to be used; it is only necessary to use this parameter to check whether a specific enumeration value is available when a parameter or return value is of a definite enumeration type.
```
// Check if the 'anchor' enumeration value for the 'launch_from' parameter in the onShow callback is available
TTMinis.game.canIUse('onShow.callback.launch_from.anchor'); // true

// Check if the 'profile' enumeration value for the 'launch_from' parameter in the onShow callback is available
TTMinis.game.canIUse('onShow.callback.launch_from.profile'); // false
```
## env
Provides read-only access to mini game runtime environment variables.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| USER_DATA_PATH | string | The path to the user's specific directory in the file system for local file storage |

Was this document helpful?