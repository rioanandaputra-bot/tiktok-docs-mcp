Docs
# Rate Limits on API Requests
TikTok API limits the number of requests you can send in a given timeframe. Limits for each API are set and enforced separately. Default limits are provided below.

| **API** | **Limit** |
| --- | --- |
| /v2/user/info/ | 600 |
| /v2/video/query/ | 600 |
| /v2/video/list/ | 600 |

Request rate calculation is based on a one minute sliding window. If the number of requests exceeds the threshold, new requests will be throttled and a response will be returned with HTTP status `429` and error code `rate_limit_exceeded`.
[If your application needs higher limits, please contact us using our Support Page](https://developers.tiktok.com/support/). We will review your request. If approved, rate limits will be increased.
Was this document helpful?