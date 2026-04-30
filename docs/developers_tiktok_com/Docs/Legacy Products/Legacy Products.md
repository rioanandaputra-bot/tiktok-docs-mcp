Docs
# Migrating to our new API
Created based on feedback from our partners, our new API follows industry standards including OAuth 2.0 and provides an improved integration experience.
Our new API is hosted at `open.tiktokapis.com`. Learn more about our new API endpoints:
- [Get User Info](https://developers.tiktok.com/doc/tiktok-api-v2-get-user-info)
- [List Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-list)
- [Query Videos](https://developers.tiktok.com/doc/tiktok-api-v2-video-query)
# What's New
## New Request and Response Format
### Authentication
Users need to pass the access token returned from the authorization step to successfully call our  APIs. The access token must be put into `Authorization` header with `Bearer` type. We no longer require `open_id` for request authentication.
### Request Parameters
`GET` requests may have query parameters but no request body is allowed.
For `POST` requests, `fields` should be provided as a query parameter. All other parameters should be placed in the request body in JSON format.
Please refer to the documentation for each individual API for detailed information about the request format.
### Error Handling
[[[New APIs will return different `4xx` and `5xx` HTTP status in the response, with the name of the error and an error message in the response body. For a complete list of HTTP status and error names, please refer to our new](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling)API Error Handling document](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling)ation](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling).
Was this document helpful?