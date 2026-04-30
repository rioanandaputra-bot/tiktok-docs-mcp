Docs
# Error Handling
In the new generation of the TikTok Login Kit, OAuth error responses include an error code represented as readable strings with a detailed error message and log ID. When contacting the TikTok support team, these details must be provided.
### Error struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| error | String | The error category in string. |
| error_description | String | The detailed error description. |
| log_id | String | The unique ID associated with every request for debugging purposes. |

### Error categories
The `error` property can be one of the following values:

| **Error** | **Description ** |
| --- | --- |
| access_denied | The resource owner or authorization server denied the request. |
| invalid_client | Client authentication failed (for example, unknown client, no client authentication included, or unsupported authentication method). |
| invalid_grant | The provided authorization grant (for example, authorization code or resource owner credentials) or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client. |
| invalid_request | The request misses a required parameter or is otherwise malformed. |
| invalid_scope | The requested scope is invalid, unknown, or malformed. |
| unauthorized_client | The client is not authorized to request an authorization code using this method. |
| unsupported_grant_type | The authorization grant type is not supported by the authorization server. |
| unsupported_response_type | The authorization server does not support obtaining an authorization code using this method. |
| server_error | Other internal server errors. |
| temporarily_unavailable | Service is temporarily unavailable. |

Was this document helpful?