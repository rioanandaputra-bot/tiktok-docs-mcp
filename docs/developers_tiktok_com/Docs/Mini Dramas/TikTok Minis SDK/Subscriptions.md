Docs
# Subscriptions
Note: Subscriptions JavaScript APIs are supported starting from TikTok version 40.3.0. Please use `.canIUse` for version compatibility before using them.
## .canIUse(schema)
```
const result = TTMinis.canIUse('createSubscription');

if (result) {
  TTMinis.createSubscription((res: Result) => {
      // xxx
  }, options: Options)
} else {
  // xxx
}
```
### Schema
```
schema: string
TTMinis.canIUse(`${api}.${method}.${param}.${option}`);
- api: API name
- method: call mode, valid values are return, object, callback
- params: parameter or return value
- options: valid values of parameters or attributes of return values
```
## .createSubscription(cb,opts)
```
TTMinis.createSubscription((res: Result) => {
  // xxx
}, options: Options)

interface Options {
  trade_order_id: string;
}

interface Result {
  is_success: boolean;
  trade_order_id: string;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Options
```
interface Options {
  trade_order_id: string;      
}
```
### Callback
TTMinis.subscribe(callback, options)
```
interface Result {
  is_success: boolean;
  trade_order_id: string;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Example
```
TTMinis.createSubscription((result) => {
  if(result?.is_success) {
    // do something
  } else {
    // do something
  }
}, {
  trade_order_id: 'your-trade-order-id',
})
```
### ErrorCode

| **errorCode** | **errorMsg** |
| --- | --- |
| 116101 | Required params empty |
| 116502 | Client Internal Error |
| 116600 | User Error |
| 116601 | User Cancel |
| 116602 | Third party error |
| 116302 | create subscription timeout |

## .changeSubscription(cb,opts)
Change subscription.
## .reactivateSubscription(cb,opts)
### Parameter

| **Parameter** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| `trade_order_id` | `string` | Associated order ID | Yes |

```
TTMinis.reactivateSubscription((res: Result) => {
  // xxx
}, options: Options)

interface Options {
  trade_order_id: string;
}

interface Result {
  is_success: boolean;
  trade_order_id: string;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Options
```
interface Options {
  trade_order_id: string;      
}
```
### Callback
TTMinis.subscribe(callback, options)

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `is_success` | `boolean` | Whether it is successful |
| `trade_order_id` | `string` | Order ID |
| `subscription_id` | `string` | Subscription ID |
| `error` | `object` | Return on failure |

```
interface Result {
  is_success: boolean;
  trade_order_id: string;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Example
```
TTMinis.activateSubscription((result) => {
  if(result?.is_success) {
    // do something
  } else {
    // do something
  }
}, {
  trade_order_id: 'your-trade-order-id',
})
```
### ErrorCode

| **errorCode** | **errorMsg** |
| --- | --- |
| 118101 | Required params empty |
| 118502 | Client Internal Error |
| 118600 | User Error |
| 118601 | User Cancel |
| 118602 | Third party error |
| 118302 | reactivate subscription timeout |

## .showSurfaceCoupon(cb)
[This API is used to display the prompt page for users who have received the initial subscription discount.  The timing for the call can refer to the `Create new subscription](https://bytedance.sg.larkoffice.com/docx/Lq7BdpLgkos2BtxX0m6lmFEOghd#share-C1OSdkv4oolkNpxKARDlPUqdgxh)` section of the flowchart, specifically before displaying the product list page. The API currently does not display the style effect during the integration. A return value of **success** indicates success.
Illustrated below is what a user sees when they receive a coupon:
Shown below is an example of a product listing page, where the pinned ribbon at the top is implemented by TikTok and requires the user to manually close it or your platform to call `hiddenRibbon` to close it when the user exits the product page.
```
TTMinis.showSurfaceCoupon((res: Result) => {
  // xxx
})

interface Result {
  is_success: boolean;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Callback
TTMinis.showSurfaceCoupon(callback)
```
interface Result {
  is_success: boolean;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Example
```
TTMinis.showSurfaceCoupon(function({ is_success }) => {
   if (is_success) {
      // Display successful
   }
})
```
## .hideRibbon(cb)
When users receive a coupon, TikTok will display a pinned ribbon at the top of the product page showing the discount. This ribbon must be hidden when the user leaves the product list page.
There are two ways to hide it:
- The user can click the 'x' on the ribbon to close it
- Call the `hiddenRibbon` API to close it when the product list page is closed
```
TTMinis.hideRibbon((res: Result) => {
  // xxx
})

interface Result {
  is_success: boolean;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Callback
TTMinis.hideRibbon(callback)

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `is_success` | `boolean` | Whether it is successful |
| `error` | `object` | Return on failure |

```
interface Result {
  is_success: boolean;
  error?: {
    error_code: string;
    error_msg: string;
  }
}
```
### Example
```
TTMinis.hideRibbon(function({ is_success }) => {
   if (is_success) {
      // Closed successfully 
   }
})
```
Was this document helpful?