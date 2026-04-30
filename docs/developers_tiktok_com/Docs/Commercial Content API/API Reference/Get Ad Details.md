Docs
# Get Ad Details
Use POST /v2/research/adlib/ad/detail/ to get ad details.

| **HTTP ****URL** | https://open.tiktokapis.com/v2/research/adlib/ad/detail/ |
| --- | --- |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

# Request
## Headers

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

## Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The requested fields: ad.id ad.first_shown_date ad.last_shown_date ad.status ad.status_statement ad.videos ad.image_urls ad.reach advertiser.business_id advertiser.business_name advertiser.paid_for_by advertiser.follower_count advertiser.avatar_url advertiser.profile_url ad_group.targeting_info | ad.id,ad.first_shown_date,ad.last_shown_date | true |

## Body

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| ad_id | i64 | The ad ID. | 104836593772645 | false |

## Request example
```
curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/detail/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
-H 'Authorization: Bearer clt.example12345Example12345Example' \
-H 'Content-Type: application/json'
--data-raw '{
   "ad_id": 104836593772645
}'
```
# Response

| **Key** | **Type** | **Example** |
| --- | --- | --- |
| data | AdDetailData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

## Response example
```
{
   "data": {
      "ad": {
         "first_shown_date": 20210101,
         "id": 1923845247192304,
         "image_urls": [
            "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf"
         ],
         "last_shown_date": 20210101,
         "status": "active",
         "videos": [
            {"url": "https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4"},
            {"url": "https://asdfcdn.com/..../1kmeidhfb38u21nd82hsk389fd/?mime_type=video_mp4"}
         ],
         "reach": {
            "unique_users_seen": "30K",
            "unique_users_seen_by_country": {
               "GB": "18K",
               "IT": "12K"
            }
         },
         "rejection_info": {
             "affected_countries": ["FR", "IT"] 
         }
      },
      "ad_group": {
         "target" {
            "number_of_users_targeted": "50K",
            "country": ["IT", "GB"],
            "age": {
               "13-17": false,
               "18-24": false,
               "25-34": false,
               "35-44": true,
               "35-44": true,
               "55+": true,
            },
            "gender": {
               "female": true,
               "male": true,
               "other_genders": true
            },
            "audience_targeting": "No",
            "video_interactions": "Entertainment",
            "creator_interactions": "Talent",
            "interest": "News & Entertainment, Business Services"
         }
      },
      "advertiser": {
          "business_id": 1755645247067185,
          "business_name": "Awesome Co.",
          "country_code": "US",
          "paid_by": "Awesome Co.",
          "tiktok_account": {
            "avatar_url": "https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600\u0026x-signature=asdf",
            "follower_count": 26374,
            "profile_url": "https://www.tiktok.com/@awesome_co"
          }
      }
   },
   "error": {
      "code": "ok",
      "http_status_code": 200,
      "log_id": "202207280326050102231031430C7E754E",
      "message": ""
   }
}
```
## Data structures
### GetAdDetailData

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| advertiser | Advertiser | The advertiser metadata. |  |
| ad_group | AdGroup | The ad group metadata. |  |
| ad | Ad | The ad metadata. |  |

### Advertiser

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| business_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business_name | string | The advertiser's business name. | Awesome Co. |
| country_code | string | The advertiser's country in the format of a two-letter code defined in ISO 3166-1. | US |
| paid_by | string | The advertiser's funding source. | Awesome Co. |
| tiktok_account | TikTokAccount | The advertiser's TikTok account information. | See example in TikTokAccount table |

### TikTokAccount

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| profile_url | string | The advertiser's TikTok profile link. | https://www.tiktok.com/@awesome_co |
| avatar_url | string | The advertiser's TikTok avatar link. | https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600&x-signature=asdf |
| follower_count | i64 | The advertiser's TikTok follower count. | 26374 |

### AdGroup

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| targeting_info | TargetingInfo | The targeting of this ad group. | See example in Targeted table |

### TargetingInfo

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| number_of_users_targeted | string | The total number of users targeted. | "20K" |
| country | list<string> | The targeted countries. | ["FR", "GB"] |
| age | map<string,bool> | The targeted ages. | { "13-17": false, "18-24": false, "25-34": false, "35-44": true, "35-44": true, "55+": true, } |
| gender | map<string,bool> | The targeted genders. | { "female": true, "male": false, "unknown": true } |
| audience_targeting | string | A flag that indicates if the user is part of an audience list uploaded by the advertiser. | "Yes" |
| video_interactions | string | The list of video categories that the user engaged with | "Entertainment" |
| creator_interactions | string | The list of creator categories based on how the user followed or viewed creators | "Talent" |
| interest | string | The list of interest categories that the viewers of this ad were grouped into | "News & Entertainment, Business Services" |

### Ad

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| id | i64 | The ad ID. | 1923845247192304 |
| first_shown_date | string | The first day when this ad was shown. | 20210101 |
| last_shown_date | string | The last day when this ad was shown. | 20210101 |
| status | string | The audit status of this ad: active or inactive. | active |
| ad_videos | list<AdVideo> | The list of videos. |  |
| image_urls | list<string> | The image URL list of this ad. | [ "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf" ] |
| reach | Reach | The audience of this ad group. | See example in Reach table |
| rejection_info | RejectionInfo |  | See example in RejectionInfo |

### AdVideo

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| url | string | The video url of this ad. | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4 |

### Reach

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| unique_users_seen | string | The total number of unique users who have seen this ad. | 10K |
| unique_users_seen_by_country | map<string,string> | The total number of unique users who have seen this ad in each country. | { "GB": "13K", "IT": "12K" } |

### ErrorStructV2

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| code | string | The error category in string. | ok |
| message | string | The detailed error description. |  |
| log_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http_status_code | i32 | The http status code. | 200 |

### RejectionInfo

| **Key** | **Type** | **Description** | **Example** |
| --- | --- | --- | --- |
| reasons | list<string> | The reason that an ad has been rejected, when applicable. | ["The product/service promoted on the ad/landing page belongs to a prohibited industry of the targeted location(s) in your ad when we take our own business evaluation, user experience and the value of advertisement impact, etc. into consideration."] |
| affected_countries | list<string> | The affected region(s), if any, where the listed rejection reasons may apply to the ad. If an ad is rejected but no affected regions are specified, it may be rejected in all applicable regions. | ["Austria", "Belgium"] |
| reporting_source | string | The reporting or detection source that led to the ad's rejection(s), when applicable. | Users and third parties can report policy violations to us. We have detected this policy violation based on a report that the content violated our Advertising Policies. |
| automated_notice | string | The notice that describes when TikTok's moderation decision relied on automated measures. This field returns a null value if the decision was based on a manual review. | We have used automated measures in making this decision. |

Was this document helpful?