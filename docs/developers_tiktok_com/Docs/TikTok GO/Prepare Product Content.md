Docs
# Prepare Product Content
This guide demonstrates how to configure your products. There are two methods to create and manage product content: via the Merchant Portal, or SaaS APIs.
## Create a product via Merchant Portal
- Log into the Merchant Portal.
- Click on the **Products** tab.
- Click the **Create Product** button.
- When prompted to create a new product, select the relevant category and type. **Discount voucher** will be selected by default. Click the **Next** button.
- Upload an image of the product and input the product's name. Click the **Confirm **button.
- The newly created product will be listed with the status **Under review**.
You can view, edit, withdraw, or offline each product using the icons next to the listed product.
## Create a product via SaaS APIs
[You can also use SaaS APIs to create products. Refer to the parameter details and implementation in the Create Product API reference](https://developers.tiktok.com/doc/product-management#).
### Product creation example
**API Request**
_Please refer to the detailed API page for compulsory fields as well as format_
```
curl --location 'https://open.tiktokapis.com/v2/localservice/saas/product/save/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer mat.sjhBhSeKr6rC3lYgEJ4a0I9IazsQh0vVlGiwAuxTljjE61DCOOHVJQayqKpH.s1' \
--header 'x-tt-env: ppe_ttls_se_portal' \
--header 'x-use-ppe: 1' \
--data '{
    "merchant_id": "100983406680068",
    "third_product_id": "test_portal_1736",
    "category_id": "24020301",
    "product_type": 2,
    "
```
**API Response**
```

{
    "data": {
        "product_id": "19271577661700"
    },
    "error": {
        "code": "0",
        "message": "success",
        "log_id": "202512201737102D104F5A72E94ABB401A"
    }
}
```
Was this document helpful?