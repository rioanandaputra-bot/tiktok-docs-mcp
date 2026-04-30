Docs
# Error Handling
Starting with TikTok API 2.0, error responses include error codes represented as readable strings with detailed error messages and a log ID. When contacting TikTok support team, these details must be provided.
### Error Struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| code | string | The error category in string |
| message | string | The detailed error description |
| log_id | string | The unique id associated with every request for debugging purporse |

### All Error Codes
The following list provides v2 error codes, their corresponding HTTP status codes, and a description of the error including guidance on how to handle the issue. Error codes are sorted alphabetically.

| **Error code** | **Description ** | **HTTP status code** |
| --- | --- | --- |
| access_token_invalid | The access token is invalid or not found in the request. Please refresh the token and retry. | 401 |
| internal_error | This is the generic error code for TikTok internal errors. _Please refer to the error message for details and notify TikTok support._ | 500 |
| invalid_file_upload | The uploaded file does not meet API specifications. Please correct the file and try again. | 400 |
| invalid_params | One or more fields in request is invalid. _Please refer to the error message for details._ | 400 |
| rate_limit_exceeded | The API rate limit was exceeded. Please try again later. | 429 |
| scope_not_authorized | The user did not authorize the scope required for completing this request. Please ask the user to authorize and then retry. | 401 |
| scope_permission_missed | Access token is invalid, some fields need additional scopes. _Please refer to the error message for more details._ | 400 |

## Error Example
```
{
   "code":"access_token_invalid",
   "message":"Access token is invalid, please refresh token and retry",
   "log_id":"20220829194722CBE87ED59D524E727021"
}
```
Was this document helpful?