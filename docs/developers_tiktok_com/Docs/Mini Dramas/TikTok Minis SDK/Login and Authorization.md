Docs
# Login and Authorization
These APIs manage the user's login status and data permissions.
## .login(opts)
Engages the **silent login** feature. This attempts to log the user in and get their basic access credentials (`code`) without showing an authorization screen. Used for IAP and basic identification.
### Parameters

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| **success** | SuccessHandler | Returns a temporary code which must be sent to your backend server to exchange for the permanent `open_id`and `access_token` |
| **fail** | FailHandler | Executed if silent login fails (for example, if the user is completely unauthorized) |
| **complete** | CompleteHandler | Executed upon completion |

- **success**: Callback for successful execution
```
type SuccessHandler = （result：{
  code: string;
}）= void;
```
- **fail**: Callback for execution failure
```
type FailHandler = (result: {
  error: {
    error_code: number;
    error_msg: string;
    error_extra: Record<string, unknown>;
  }
}) => void;
```
- **complete**: Callback for execution completion
```
type CompleteHandler = （）= void;
```
### Example
```
TTMinis.login({
  success: (result) => {
  // The user has logged in and authorized the application
  // You can get the code and send it to the backend in exchange for open_id, access_token, and more
   let code = result.code;
  },
  fail: (error) => {
  // Other errors or deauthorization code is null
  },
  complete: () => {
   //  Both success and failure will trigger this callback
  }
});
```
## .authorize(opts)
Engages the **explicit authorization** process, which prompts the user with an authorization screen to grant your app specific data permissions. This is needed for data beyond basic ID, like username and avatar.
```
TTMinis.authorize(callback, options): void
```
By default, calling `TTMinis` attempts to verify the user's basic permissions (avatar, display name, open ID, and union ID).
If you need one or more additional permissions, use the `scope` parameter, call `TTMinis` login, and set the `scope` parameter with a comma-separated list of permissions.
- For account binding, please apply for this scope on the Developer Portal: **user.info****.basic - Login Kit**.
- When you call `TTMinis.login`, please refer to the following examples.
### Parameters

| **Parameter** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| `scope` | `string` | Authorization scope, default `user.info.basic` | No |
| `returnScopes` | `boolean` | Whether to include the authorized scope in the return result | No |

### Callback

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `authResponse.code` | `string` | Authorization Code |
| `authResponse.grantedScopes` | `string` | Actual authorized scope, available when `returnScopes`is enabled |
| `error` | `object` | Return when failed |

```
TTMinis.authorize({
  scope: "user.info.basic"
  success: (result) => {
  // The user has logged in and authorized the application
  // You can get the code and send it to the backend in exchange for open_id, access_token, and more
   let code = result.code;
  },
  fail: (error) => {
  // Other errors or deauthorization code is null
  },
  complete: () => 
   //  Both success and failure will trigger this callback
  }
});
```
Was this document helpful?