Docs
# Payment
## .pay(cb,opts)
### Parameters

| **Parameter** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| `trade_order_id` | `string` | ID of the order | Yes |
| `log_extra` | `Record<string, unknown>` | Expand event tracking fields | No |

### Callback

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `is_success` | `boolean` | Whether the payment was successful |
| `trade_order_id` | `string` | Order ID |
| `error` | `object` | Return when failure |

```
type PayBeansCallback = (result: Result) => void;

interface Result {
   is_success: boolean;
   error?: {
     error_code: number;
     error_msg: string;
     error_extra: Record<string, unkown>;
   };
 }
```
### Options
```
interface Options {
  trade_order_id: string;      
}
```
### Example
```
Minis.pay(（result）=>{
  if(result.is_success){
    // do something
  } else {
    // do something
  }
},{trade_order_id: "demo"})
```
## .openbalance(cb,opts)
Jump to the balance page.
### Parameter

| **Parameter** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| `type` | `'BEANS'` | Balance type | Yes |

### Callback

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `is_success` | `boolean` | Whether the opening was successful |
| `error` | `object` | Return on failure |

```
type Callback = (result: Result) => void;
interface Result {
  is_success: boolean;
   error?: {
     error_code: number;
     error_msg: string;
     error_extra: Record<string, unknown>;
   };
}
```
### Options
```
interface Options {
  type: 'BEANS'
}
```
### Example
```
TTMinis.openBalance(
```
Was this document helpful?