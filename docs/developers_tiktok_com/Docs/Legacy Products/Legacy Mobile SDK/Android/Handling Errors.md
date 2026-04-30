Docs
# Handling Android Errors
In the table below, each row represents error code. For further information please see the `CommonConstants`.

| **ErrorCode** | **Description** |
| --- | --- |
| 0 | Success. |
| -1 | Unknown error. |
| -2 | User cancelled. |
| -3 | Send failed. |
| -4 | Auth denied. |
| -5 | Unsupported. |
| -12 | Network not connected. |
| -13 | Network connection timed out. |
| -14 | Network Timeout. |
| -15 | Network IO error. |
| -16 | Network unknown host error. |
| -21 | Network ssl error. |
| -30 | User cancel login or login failure. |

### For Share errors
If the error code does not make it easy for you to locate a specific error, you can use 'response.subErrorCode' for detail message. SDK version needs to be 0.0.1.5 or higher and TikTok version needs to be 14.4.0 or higher.

| **response.subErrorCode** | **Description** |
| --- | --- |
| 20002 | Params parsing error. |
| 20003 | Not enough permissions to operation. |
| 20004 | User not login. |
| 20005 | TikTok has no album permissions. |
| 20006 | TikTok Network error. |
| 20007 | Video length doesn't meet requirements. |
| 20008 | Photo doesn't meet requirements. |
| 20010 | Processing photo resources failed. |
| 20011 | Video resolution doesn't meet requirements. |
| 20012 | Video format is not supported. |
| 20013 | Sharing canceled. |
| 20015 | Users store shared content for draft or user accounts are not allowed to post videos. |
| 22001 | Unsupported resolution. |

### For Authentication errors
#### Universal

| **ErrorCode** | **Description** |
| --- | --- |
| 0 | Success. |
| 2100004 | The system is busy. Please try again later. |
| 2100005 | Invalid parameter. |
| 2100007 | No permission operation. |
| 2100009 | The user is banned from using this operation. |
| 2190001 | Quota has been used up. |
| 2190004 | The application has not obtained this ability. Please register for it on developer portal. |
| 2190015 | Request parameter access_token openid does not match. |

#### OAuth

| **ErrorCode** | **Description** |
| --- | --- |
| 10002 | Parameter error. |
| 10003 | Illegal application configuration. |
| 10004 | Illegal authorization scope. |
| 10005 | Missing parameters. |
| 10006 | Illegal redirection URI needs to be consistent with the "authorized callback domain" in the app configuration. |
| 10007 | Authorization code expired. |
| 10008 | Illegal call credentials. |
| 10009 | Illegal parameter. |
| 10010 | Refresh_token expired. |
| 10011 | The application package name is inconsistent with the configuration. |
| 10012 | App is under review and cannot be authorized. |
| 10013 | Client key or client secret error. |
| 10014 | The authorized client key is inconsistent with the access token obtained. |
| 10015 | Application type error, such as using the client_key of APP application for PC application. |
| 10017 | Authorization failed, the signature information needs to be completed. |
| 2190002 | Invalid access_token. |
| 2190003 | The user has not authorized the api. |
| 2190008 | Access_token expired, please refresh or re-authorize. |
| 6007061 | TikTok app version is too low. To continue, update to the latest version of the app. |
| 6007062 | This feature is not available for your account due to the age restriction. Try using another account. |

Was this document helpful?