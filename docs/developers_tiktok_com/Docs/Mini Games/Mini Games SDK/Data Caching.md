Docs
# Data Caching
## .setStorage(opts)
Used to store data in the Client Local Cache. If the key name already exists, update its corresponding value.
### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | Specified key in local caching | Yes |
| data | any | Content to be stored. Only native types, date, and objects that can be serialized via`JSON.stringify`are supported. | Yes |

- **Success: **Callback function for successful interface call
```
type SuccessHandler = () => void
```
- **Fail**: Return the failed execution
```
type FailHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
### Example
```
TTMinis.game.setStorage({
  key: "gameLocalData",
  data: {
    a: 1,
    b: 2,
    c: 3
  },
  success: () => {
  // Do something when succeeded
  },
  error: (error) => {
  // Do something when failed
  }
  complete: () => {
  // Do something when completed
  }
})
```
## setStorageSync(string key, any data)
Stores data in the specified key within local caching. This will overwrite the original content corresponding to that key
### Parameters

| Field | Type | Description |
| --- | --- | --- |
| key | string | The specified key in local caching |
| data | any | Content to be stored. Only native types, Date, and objects that can be serialized via`JSON.stringify`are supported. |

### Example
```
try {
  TTMinis.game.setStorageSync('key', 'value');
} catch (e) { }
```
## .getStorage(opts)
Used to get Local Cache data, when a key is passed, the value of the key will be returned; if the data for the key does not exist in the Client cache, `null` is returned.
### Parameters

| Field | Type | Description |
| --- | --- | --- |
| key | string | The specified key in local caching |

- **Success**: Execute a successful return
```
type SuccessHandler = (result: {
  data?: unknown;
}) => void
```
- **Fail**: Return the failed execution
```
type ErrorHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
- **Complete**: Callback for execution completion (including success and failure).
```
type CompleteHandler = () => void;
```
### Example
```
TTMinis.game.getStorage({
  key: "gameLocalData",
  success: (result) => {
    let data = result.data;
    // do something with data
  },
  error: (error) => {
    // do something with error
  },
})
```
## .getStorageSync(opts)
Synchronously retrieves the content of the specified key from local caching.
### Parameter

| Field | Type | Description |
| --- | --- | --- |
| key | string | The specified key in local caching |

Return Value: Content corresponding to key
### Example
```
try {
  var value = TTMinis.game.getStorageSync('key')
  if (value) {
```
## .removeStorage(opts)
Used to remove cached data stored locally in the Client, the developer passes in the key that needs to remove the cache. After successful execution, the corresponding cache will be removed.
### Parameters

| Field | Type | Description |
| --- | --- | --- |
| key | string | The specified key in local caching |

- **Success**: Execute a successful return
```
type SuccessHandler = () => void
```
- **Fail**: Return the failed execution
```
type ErrorHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
- **Complete**: Callback of execution completion (including success and failure)
```
type CompleteHandler = () => void;
```
### Example
```
TTMinis.game.removeStorage({
  key: "gameLocalData",
  success: () => {
  // do something when succeed
  },
  error: (error) => {
  // do something when failed
  }
  complete: () => {
  // do something when completed
  }
})
```
## removeStorageSync(string key)
Remove the specified key from local caching.
### Parameter

| Field | Type | Description |
| --- | --- | --- |
| key | string | The specified key in local caching |

### Example
```
try {
  wx.removeStorageSync('key')
} catch (e) {
  // Do something when catch error
}
```
## .clearStorage(opts)
Used to remove the local cache of the current mini-game based on setStorage storage.
### Parameters
- **Success**: Execute a successful return
```
type SuccessHandler = () => void
```
- **Fail**: Return the failed execution
```
type ErrorHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
- **Complete**: Callback of execution completion (including success and failure)
```
type CompleteHandler = () => void;
```
### Example
```
TTMinis.game.clearStorage({
  success: () => {
  // Do something when succeeded
  },
  error: (error) => {
  // Do something when failed
  }
  complete: () => {
  // Do something when completed
  }
})
```
## .clearStorageSync()
Clears all cached data synchronously.
### Example
```
try {
  TTMinis.game.clearStorageSync();
} catch (e) {
  // Do something when error is caught
}
```
## .getStorageInfo
Note: This API is supported starting from SDK version 0.8.0. Lower versions must be adjusted for compatibility.
Asynchronously obtain relevant information about the current storage.
### Parameters
Object object

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

### object.success callback function
Object object

| Field | Type | Description |
| --- | --- | --- |
| keys | Array.<string> | All keys in the current storage |
| currentSize | number | Currently occupied space size, unit: KB |
| limitSize | number | Limited space size, unit: KB |

### Example
```
TTMinis.game.getStorageInfo({
```
## .getStorageInfoSync
Note: This API is supported starting from SDK version 0.8.0. Lower versions must be adjusted for compatibility.
Synchronously obtain relevant information about the current storage.
### Parameters
Object object

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| keys | Array.<string> | All keys in the current storage |
| currentSize | number | Currently occupied space size, unit: KB |
| limitSize | number | Limited space size, unit: KB |

### Example
```
try {
  const res = TTMinis.game.getStorageInfoSync()
  console.log(res.keys)
  console.log(res.currentSize)
  console.log(res.limitSize)
} catch (e) {
```
Was this document helpful?