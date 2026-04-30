Docs
# Dining SaaS Sample Code
This document provides a comprehensive sample code demo of each API module for external developers onboarding with TikTok Go Dining SaaS. You can refer to these examples when developing and testing your API integrations.
The sample code is demonstrated in **Java** and **GoLang **respectively.
## Authentication
Authentication is the first step to interacting with TikTok Local Services (TTLS) APIs. It involves obtaining an access token that must be included in the header of subsequent API calls.
### Get New Token
**Purpose:** To obtain a new access token for the first time.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.stream.Collectors;

public class GetAccessToken {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        Map<Object, Object> data = Map.of(
                "client_key", "{CLIENT_KEY}",
                "client_secret", "{CLIENT_SECRET}",
                "merchant_id", "{MERCHANT_ID}",
                "grant_type", "access_token"
        );

        String form = data.entrySet()
                .stream()
                .map(e -> e.getKey() + "=" + URLEncoder.encode(e.getValue().toString(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/merchant/oauth/token/"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .header("x-tt-target-idc", "alisg")
                .POST(HttpRequest.BodyPublishers.ofString(form))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
    "strings"
)

func main() {
    apiURL := "https://open.tiktokapis.com/merchant/oauth/token/"

    data := url.Values{}
    data.Set("client_key", "{CLIENT_KEY}")
    data.Set("client_secret", "{CLIENT_SECRET}")
    data.Set("merchant_id", "{MERCHANT_ID}")
    data.Set("grant_type", "access_token")

    req, err := http.NewRequest("POST", apiURL, strings.NewReader(data.Encode()))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
    req.Header.Set("x-tt-target-idc", "alisg")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Refresh Access Token
**Purpose:** To obtain a new access token using a refresh token when the current access token expires.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.stream.Collectors;

public class RefreshAccessToken {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        Map<Object, Object> data = Map.of(
                "client_key", "{CLIENT_KEY}",
                "client_secret", "{CLIENT_SECRET}",
                "merchant_id", "{MERCHANT_ID}",
                "grant_type", "refresh_token",
                "refresh_token", "{REFRESH_TOKEN}"
        );

        String form = data.entrySet()
                .stream()
                .map(e -> e.getKey() + "=" + URLEncoder.encode(e.getValue().toString(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/merchant/oauth/token/"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .header("x-tt-target-idc", "alisg")
                .POST(HttpRequest.BodyPublishers.ofString(form))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.outprintln("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
    "strings"
)

func main() {
    apiURL := "https://open.tiktokapis.com/merchant/oauth/token/"

    data := url.Values{}
    data.Set("client_key", "{CLIENT_KEY}")
    data.Set("client_secret", "{CLIENT_SECRET}")
    data.Set("merchant_id", "{MERCHANT_ID}")
    data.Set("grant_type", "refresh_token")
    data.Set("refresh_token", "{REFRESH_TOKEN}")

    req, err := http.NewRequest("POST", apiURL, strings.NewReader(data.Encode()))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
    req.Header.Set("x-tt-target-idc", "alisg")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
## Shop Management
This section covers APIs for managing shops, including claiming, certification, decoration, and querying shop information.
### POI Claiming
**Purpose:** To claim a Point of Interest (POI) on TikTok and link it to a merchant's shop.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PoiClaiming {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "shop_name_local": "Toko Kue Enak",
                    "shop_name_en": "Delicious Cake Shop",
                    "shop_address_local": "Jl. Merdeka No. 1, Jakarta",
                    "shop_address_en": "1 Merdeka Street, Jakarta",
                    "business_status": 1,
                    "type_code": "722511",
                    "latitude": "-6.2088",
                    "longitude": "106.8456"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/poi/batch_claim/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/poi/batch_claim/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "shop_name_local": "Toko Kue Enak",
                "shop_name_en": "Delicious Cake Shop",
                "shop_address_local": "Jl. Merdeka No. 1, Jakarta",
                "shop_address_en": "1 Merdeka Street, Jakarta",
                "business_status": 1,
                "type_code": "722511",
                "latitude": "-6.2088",
                "longitude": "106.8456"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Upload Shop Certifications
**Purpose:** To submit certification documents for a shop, such as business licenses or other required legal documents.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UploadShopCertifications {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "industry_license_url": "https://example.com/license.pdf"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_submit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_cert/batch_submit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "industry_license_url": "https://example.com/license.pdf"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Shop Decoration
**Purpose:** To update a shop's decorative information, such as photos, opening hours, and average price.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ShopDecoration {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "phone": "+621234567890",
                    "average_price": {
                        "amount": "100000",
                        "currency": "Rp"
                    },
                    "opening_time": [
                        {
                            "day": 1,
                            "time_periods": [
                                {
                                    "start_time": "09:00",
                                    "end_time": "22:00"
                                }
                            ]
                        }
                    ],
                    "images": [
                        {
                           "is_main": true,
                           "index": 1,
                           "origin_url": "https://example.com/shop_image.jpg"
                        }
                    ]
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_decoration/batch_submit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_decoration/batch_submit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "phone": "+621234567890",
                "average_price": {
                    "amount": "100000",
                    "currency": "Rp"
                },
                "opening_time": [
                    {
                        "day": 1,
                        "time_periods": [
                            {
                                "start_time": "09:00",
                                "end_time": "22:00"
                            }
                        ]
                    }
                ],
                "images": [
                    {
                       "is_main": true,
                       "index": 1,
                       "origin_url": "https://example.com/shop_image.jpg"
                    }
                ]
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Update Shop's Basic Info
**Purpose:** To update a shop's basic information, such as name, address, and business category.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UpdateShopBaseInfo {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "data": [
                {
                    "third_shop_id": "{THIRD_SHOP_ID}",
                    "shop_name_local": "Toko Roti Baru",
                    "shop_name_en": "New Bakery Shop"
                }
            ]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_base_info/batch_update/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_base_info/batch_update/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "data": [
            {
                "third_shop_id": "{THIRD_SHOP_ID}",
                "shop_name_local": "Toko Roti Baru",
                "shop_name_en": "New Bakery Shop"
            }
        ]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Task Query for Shop Operations
**Purpose:** To query the status of asynchronous tasks submitted for POI claiming, shop certification, shop decoration, and shop basic info updates.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class QueryShopTasks {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "task_id_list": [12345, 67890]
        }
        ''';

        // Example for POI task query
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/poi_task/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    // Example for POI task query
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/poi_task/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "task_id_list": [12345, 67890]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Batch Query Shop Information
**Purpose:** To retrieve detailed information for multiple shops in a single request.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class BatchQueryShopInfo {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_shop_ids": ["{THIRD_SHOP_ID_1}", "{THIRD_SHOP_ID_2}"]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/shop_info/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_shop_ids": ["{THIRD_SHOP_ID_1}", "{THIRD_SHOP_ID_2}"]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Webhook Overview for Shop-Related Events
**Purpose:** To receive real-time notifications about the status of shop-related operations.
**Implementation Notes:**
- **Retry Logic:** Your webhook endpoint should be prepared to handle retries from TikTok's servers in case of network issues or non-2xx responses.
- **Idempotency:** Implement idempotency checks on your end to prevent duplicate processing of the same event. The `create_time` field can be used for this purpose.
**Event Names:**
- `ttls.merchant.poi_claiming_task.result`: For POI claiming tasks.
- `ttls.merchant.upload_shop_certifications_task.result`: For shop certification tasks.
- `ttls.merchant.shop_decoration_task.result`: For shop decoration tasks.
- `ttls.merchant.update_shop_base_info_task.result`: For shop basic info update tasks.
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the details of the task. The structure of this JSON will correspond to the task type (e.g., `PoiClaimTask`, `ShopCertificationTask`). Key fields to inspect are:
- `task_id`: The ID of the task.
- `task_status`: The status of the task (e.g., `2` for Success, `3` for Failed).
- `reject_reason`: If the task failed, this field will contain the reason for rejection.
## Product Management
This section details the APIs for managing products, including creating, updating, and querying product information.
### Save Product
**Purpose:** To create a new product or update an existing one. This is a comprehensive endpoint that requires all product attributes to be provided.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class SaveProduct {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "category_id": "722511",
            "product_type": 2,
            "attr_key_value_map": {
                "rec_person_num": "\"1\"",
                "shop_id": "[\"{SHOP_ID}\"]",
                "commodity_set": "2",
                "commodity": "[{\"i18n_group_mame\":{\"default_text\":\"Pizza Group\"},\"total_count\":1,\"option_count\":1,\"item_list\":[{\"i18n_name\":{\"default_text\":\"Large Pizza\"},\"price\":\"100000\",\"currency\":\"Rp\",\"count\":1}]}]",
                "product_name": "{\"default_text\":\"Pizza Voucher\"}",
                "image_list": "[{\"outer_url\":\"https://example.com/pizza.jpg\"}]",
                "origin_amount": "150000",
                "actual_amount": "100000",
                "local_currency": "Rp",
                "stock_info": "{\"stock_num\":100,\"stock_qty_limit_type\":1}",
                "sold_time_type": 2,
                "use_type": 1,
                "use_date": "{\"use_date_type\":2,\"day_duration\":30}",
                "use_time": "{\"use_time_type\":1}",
                "consumption_convention": "{\"consumption_method\":3}"
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/save/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/save/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "category_id": "722511",
        "product_type": 2,
        "attr_key_value_map": {
            "rec_person_num": "\"1\"",
            "shop_id": "[\"{SHOP_ID}\"]",
            "commodity_set": "2",
            "commodity": "[{\"i18n_group_mame\":{\"default_text\":\"Pizza Group\"},\"total_count\":1,\"option_count\":1,\"item_list\":[{\"i18n_name\":{\"default_text\":\"Large Pizza\"},\"price\":\"100000\",\"currency\":\"Rp\",\"count\":1}]}]",
            "product_name": "{\"default_text\":\"Pizza Voucher\"}",
            "image_list": "[{\"outer_url\":\"https://example.com/pizza.jpg\"}]",
            "origin_amount": "150000",
            "actual_amount": "100000",
            "local_currency": "Rp",
            "stock_info": "{\"stock_num\":100,\"stock_qty_limit_type\":1}",
            "sold_time_type": 2,
            "use_type": 1,
            "use_date": "{\"use_date_type\":2,\"day_duration\":30}",
            "use_time": "{\"use_time_type\":1}",
            "consumption_convention": "{\"consumption_method\":3}"
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Update (Free Audit)
**Purpose:** To update a product's stock and price information without requiring a review. This allows for real-time changes to inventory and pricing.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class UpdateFreeAudit {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "product_free_audit": {
                "local_currency": "Rp",
                "actual_amount": "95000",
                "stock_qty_limit_type": 1,
                "stock_num": 50
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/update_free_audit/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/update_free_audit/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "product_free_audit": {
            "local_currency": "Rp",
            "actual_amount": "95000",
            "stock_qty_limit_type": 1,
            "stock_num": 50
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Delist Product
**Purpose:** To take a product offline, making it unavailable for purchase.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class DelistProduct {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/offline"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/offline"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Withdraw Product Audit
**Purpose:** To withdraw a product from the audit process before it is completed.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class WithdrawProductAudit {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_product_id": "{THIRD_PRODUCT_ID}"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/withdraw_audit"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/withdraw_audit"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_product_id": "{THIRD_PRODUCT_ID}"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Batch Query Products
**Purpose:** To retrieve a list of products based on various filter criteria.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class BatchQueryProducts {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "product_type_list": [2],
            "list_tab": 1,
            "pagination": {
                "page_size": 10,
                "page_no": 1
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/batch_query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "product_type_list": [2],
        "list_tab": 1,
        "pagination": {
            "page_size": 10,
            "page_no": 1
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Query Product Details
**Purpose:** To retrieve detailed information about a single product, including its online and under-review versions.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class QueryProductDetails {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "third_product_id": "{THIRD_PRODUCT_ID}",
            "merchant_id": "{MERCHANT_ID}",
            "online": true
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product/query/"

    jsonBody := []byte(`{
        "third_product_id": "{THIRD_PRODUCT_ID}",
        "merchant_id": "{MERCHANT_ID}",
        "online": true
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product Category Query
**Purpose:** To retrieve the available product categories for a merchant.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ProductCategoryQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "language": "en"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product_opt_category/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product_opt_category/query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "language": "en"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product-Available Shops Query
**Purpose:** To retrieve a list of shops where a product can be made available.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ProductAvailableShopsQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "language": "en",
            "pagination": {
                "page_size": 10,
                "page_no": 1
            }
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/product_opt_shops/query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/product_opt_shops/query/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "language": "en",
        "pagination": {
            "page_size": 10,
            "page_no": 1
        }
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### National Holiday Query
**Purpose:** To retrieve a list of national holidays for specified countries.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class NationalHolidayQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "countries": ["ID"],
            "language": "en"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/holiday/batch_query/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/holiday/batch_query/"

    jsonBody := []byte(`{
        "countries": ["ID"],
        "language": "en"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Product Status Webhook Overview
**Purpose:** To receive real-time notifications about changes in product status.
**Event Name:**
- `ttls.product.status_update.result`
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the following key fields:
- `third_product_id`: The unique ID of the product in the third-party system.
- `product_id`: The TikTok product ID.
- `product_status`: The new status of the product (e.g., `1` for Listed, `3` for Rejected).
- `action_type`: The type of action that triggered the status change.
## Redeem Management
This section covers APIs for managing voucher redemption.
### Voucher Query
**Purpose:** To query the details of a voucher using its code or a QR code.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class VoucherQuery {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "merchant_id": "{MERCHANT_ID}",
            "third_shop_id": "{THIRD_SHOP_ID}",
            "code_list": ["123456789012"]
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/fulfill/get_code_item_list/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/fulfill/get_code_item_list/"

    jsonBody := []byte(`{
        "merchant_id": "{MERCHANT_ID}",
        "third_shop_id": "{THIRD_SHOP_ID}",
        "code_list": ["123456789012"]
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### Voucher Redeem
**Purpose:** To redeem a voucher, marking it as used.
**Java Example (JDK 11+):**
```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class VoucherRedeem {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String jsonBody = '''
        {
            "third_shop_id": "{THIRD_SHOP_ID}",
            "code_list": ["123456789012"],
            "shop_order_id": "{SHOP_ORDER_ID}",
            "merchant_id": "{MERCHANT_ID}",
            "locale": "id-ID"
        }
        ''';

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://open.tiktokapis.com/v2/localservice/saas/fulfill/redeem_code/"))
                .header("Authorization", "Bearer {ACCESS_TOKEN}")
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response Body: " + response.body());
    }
}
```
**Golang Example:**
```
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    apiURL := "https://open.tiktokapis.com/v2/localservice/saas/fulfill/redeem_code/"

    jsonBody := []byte(`{
        "third_shop_id": "{THIRD_SHOP_ID}",
        "code_list": ["123456789012"],
        "shop_order_id": "{SHOP_ORDER_ID}",
        "merchant_id": "{MERCHANT_ID}",
        "locale": "id-ID"
    }`)

    req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(jsonBody))
    if err != nil {
        fmt.Println("Error creating request:", err)
        return
    }

    req.Header.Set("Authorization", "Bearer {ACCESS_TOKEN}")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        fmt.Println("Error sending request:", err)
        return
    }
    defer resp.Body.Close()

    body, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading response body:", err)
        return
    }

    fmt.Println("Status Code:", resp.StatusCode)
    fmt.Println("Response Body:", string(body))
}
```
### After-sale Webhook Overview
**Purpose:** To receive real-time notifications about after-sale events, such as refunds.
**Event Name:**
- `ttls.fulfill.after_sale.result`
**Payload Focus:**
The `content` field of the webhook payload will contain a JSON string with the following key fields:
- `after_sale_event_type`: The type of after-sale event (e.g., `AFTER_SALE_SUCCESS`).
- `shop_order_id`: The ID of the order.
- `item_ids`: A list of item IDs that were refunded.
- `after_sale_order_id`: The ID of the after-sale order.
Was this document helpful?