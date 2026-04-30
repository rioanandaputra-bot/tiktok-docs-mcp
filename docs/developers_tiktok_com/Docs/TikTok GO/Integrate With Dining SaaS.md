Docs
# Integrate With Dining SaaS
This guide lists the key API connections for you to integrate TikTok GO Dining services with your system.
Alternatively, you can use the Merchant Portal to manage your business activities such as shops, products and sales. However, certain features are only available through API integration, such as voucher redemption management.
## Shop Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| POI Claiming | Allows you to create a new POI for a shop or outlet and query existing POIs | [[[Shop Management APIs](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Claim POI tasks](https://developers.tiktok.com/doc/shop-management#) Description | Create a new outlet → Fill in the outlet's Basic information |
| Shop Certifications Upload and Check | Allows you to upload shop certifications and check for existing certifications | [[[[Upload Shop Certifications API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Upload Shop Certification tasks](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Upload and submit certifications for your outlet |
| Shop Decoration | Allows you to upload and view detailed information and images for your shop | [[[Batch Submit Shop Decoration API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Decorate Shop API](https://developers.tiktok.com/doc/shop-management#) Description | Edit outlet information → add business information |
| Shop Basic Info | Allows you to update the basic information for your shops | [[[[Update Shop Basic Info API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Query Update Shop Basic Info tasks API](https://developers.tiktok.com/doc/shop-management#)Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Create a new outlet → Fill in the outlet's Basic information |
| Batch Query Shop Information | Allows you to query information for multiple shops in a single request | [[Batch Query Shop Information API](https://developers.tiktok.com/doc/shop-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A |

## Product Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| Product Creation and Update | Allows you to create and update the product information | [[Update/Create Product](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Create new product → fill in product information |
| National Holiday Inquiry | Allows you to query the national holiday by countries | [[National Holiday Inquiry](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A |
| Product Query | Allows you to query various product information after creation | [[[[[[Get Delist the Product API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Product Category Inquiry](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ Products Can Be Queried in Shops API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Filter listed products |
| Product Update (Exempt from Review) | Allows you to update certain product information that is exempt from review after the initial review is approved | [[Product Update (Exempt From Review) API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Edit audit-free information |
| Product Review Revocation | Allows you to withdraw a product from review | [[Product Review Revocation API](https://developers.tiktok.com/doc/product-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | Filter products under review |
| Voucher Query | Allows you to query voucher information | [Query Voucher API](https://developers.tiktok.com/doc/product-management#) Description | N/A |
| Redeem Management (Recommended) | Allows you to redeem vouchers using a QR code scanner or voucher codes | [[Redeem Voucher](https://developers.tiktok.com/doc/voucher-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A (Merchant Portal doesn't support this feature) |

## Voucher Management APIs

| **API name** | **Description** | **API implementation** | **Merchant Portal operation** |
| --- | --- | --- | --- |
| Voucher Query | Allows you to query voucher information | [Voucher Query API](https://developers.tiktok.com/doc/voucher-management#) Description | N/A |
| Redemption management (Recommended) | Allows you to redeem vouchers using QR code scanner or vouchers' code | [[Redeem Code API](https://developers.tiktok.com/doc/voucher-management#) Description _Sample Code](https://developers.tiktok.com/doc/dining-saas-sample-code#)_ | N/A (Merchant Portal doesn't support this feature) |

Was this document helpful?