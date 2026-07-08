# TikTok Minis Platform

> Consolidated from 12 source files.



---
## SOURCE: TikTok Minis Platform/Configure Localization.md

Docs
This guide explains how to configure localization for your mini game, if you plan to release your mini game to multiple global regions. English is the default language for your app and will be configured automatically.
## Set up additional languages
If you want to release your mini game in different languages, you must configure localization on your mini game's app page.
- On your mini game's app page, click the **Localization** tab.
- Click the **Add language** button.
- Select your desired language then click the **Add** button.
- Enter your app's basic information in the new language you selected, then click **Submit**.
After you submit the new language setting, TikTok will review it. Upon approval, your new language setting will go live.
The languages selected will match the user's language settings in the TikTok App:
- **Online**: For a language that has been configured and is **Online**, the app name, app icon, app description, Terms of Service URL, and Privacy Policy URL will be displayed in the language that matches the user's TikTok language settings.
- **Offline**: If a language has not been configured or the language status is **Offline**, then the app name, app icon, app description, Terms of Service URL, and Privacy Policy URL will be displayed in the default language.
## Supported languages
The following additional languages are supported:
- Albanian
- Arabic
- Azerbaijani
- Bengali
- Bulgarian
- Burmese
- Catalan
- Cebuano
- Chinese (Simplified)
- Chinese (Traditional)
- Croation
- Czech
- Danish
- Dutch
- English (UK)
- English (US)
- Estonian
- Filipino
- Finnish
- French
- French (Canada)
- German
- Greek
- Hebrew
- Hindi
- Hungarian
- Icelandic
- Indonesian
- Irish
- Italian
- Japanese
- Javanese
- Kazakh
- Khmer
- Korean
- Latvian
- Lithuanian
- Malay
- Norwegian
- Polish
- Portugueseweath
- Portuguese (Brazil)
- Romanian
- Russian
- Slovenian
- Spanish
- Spanish (Latin America)
- Swahili
- Swedish
- Thai
- Turkish
- Ukrainian
- Urdu
- Uzbek
- Vietnamese
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/Industry Qualification Review.md

Docs
# Industry Qualification Review
Industry qualification is a one-time review that confirms your organization is a legitimate mini dramas or mini games publisher. This process protects the platform and users by verifying that app developers are authentic and compliant before your app goes live. After submitting a link to representative work and supporting materials, your organization will be approved to launch your app.
## Prerequisite
[Before starting the industry qualification review process, your organization must have already completed business verification](https://developers.tiktok.com/doc/verify-your-business) on the Developer Portal.
**Note**: The entity approved through business verification will be referenced during industry qualification review.
## Required materials
For industry qualification, you must provide the following items, depending on whether your company is a mini games or mini dramas publisher.

| **Mini dramas** | **Mini games** |
| --- | --- |
| **Company introduction: **A summary of the company's basic information, including the company's date of establishment, main business dealings, personnel composition, company website, supplementary materials, and more. **Drama link**: A playable link to representative work (a mini drama) from another app platform. **Proof of identity**: Supporting proof that the entity that owns the drama link matches the business entity verified by TikTok. Only required if the entity that owns the drama link differs from your verified business entity. **Your TikTok Customer Manager:**If you have already established contact with a Customer Manager from TikTok for Business, please provide their email address. | **Game link**: A playable link to representative work (a mini game) from another app platform. **Proof of identity**: Supporting proof that the entity that owns the game link matches the business entity verified by TikTok. Only required if the entity that owns the game link differs from your verified business entity. |

### Company introduction
Provide an introduction to your company, including but not limited to the following:
- Date of establishment
- Summary of main business dealings
- Personnel composition (total headcount, role types, number of employees per role)
- Company's official website
- Supplementary materials
The more detailed the information you provide, the more it will assist our team in conducting a thorough assessment.
### Links to representative work
Refer to the information below for directions on how to retrieve a playable link to your representative work: a mini drama, or a mini game. If your representative work is on a platform not shown below, you must provide a playable link after it has been launched on that platform.
#### Google Play
On the app details page, click the more options icon in the upper righthand corner. Then copy the link from the ensuing pop-up window.
#### App Store
On the app details page, tap the share icon in the top-right corner, and then copy the link from the ensuing pop-up window.
#### WeChat Mini App
Enter the mini drama or mini game and then tap the button in the upper righthand corner. Copy the link from the ensuing pop-up window.
#### Douyin Mini App
Enter the mini drama or mini game and then tap the button in the upper righthand corner. Tap "Share" in the ensuing pop-up window to obtain the link.
### Proof of identity
If the mini drama or mini game link you provide belongs to an entity that is different from your verified business, you must submit supporting proof of identity. Listed are possible scenarios that require proof of identity:
- The link belongs to an entity that is registered in a different country from your verified business.
- The link belongs to an entity that develops dramas or games, while your verified business is an entity that publishes dramas or games.
There are two acceptable forms of proof of identity. Choose one that fits your business scenario:
- **Business registration documents for both entities**: If the legal representative is the same for both the entity that owns the link and your verified business entity, they can submit the registration documents for both entities.
- **Authorization letter**: This authorization letter must be issued by the app developer entity, stating that your verified business entity is authorized to publish and operate its mini drama or mini game on TikTok. The authorization letter must be stamped with your entity's official seal.
Upload one PDF with your proof of identity. The file size must not exceed 10 MB and 30 pages. You may only upload one file.
### Your TikTok Customer Manager
If you have an established TikTok for Business Customer Manager, please provide their email address. Only an official email address from "@bytedance.com" will be accepted.
## Complete industry qualification form
To verify your business, you must submit a short form with links to representative works and, if needed, supporting proof. Go to the Developer Portal and complete the following steps:
**Note**: Only registered organization admins can view the Business page and complete this industry qualification.
- Find **My organizations** and select your desired organization.
- Go to the **Business** page then click the** Industry qualification** tab.
- Click the **Apply** button.
- Provide the following information:
- Company introduction: Summary of your company's basic information (mini dramas only)
- Work link: A playable link to your mini drama or mini game from another app platform
- Proof of identity: Supporting proof that the publishing entity matches the business entity verified by TikTok
- Your TikTok Customer Manager: The email address of your TikTok for Business Customer Manager (mini dramas only)
## Industry qualification review and completion
After you submit your verification form, TikTok will review your verification request within 1-3 business days. You can track the status of your request on your organization's **Industry qualification **page. You may receive one of the following results.
- **Approved**: Your industry qualification was successfully verified. You can now launch your mini game.
- **Couldn't verify**: Due to certain issues with your request, TikTok could not complete industry qualification verification. You may need to edit and resubmit the form.
- [**Rejected**: Your business verification was rejected. Contact your TikTok representative or submit a support ticket](https://developers.tiktok.com/support).
Once verified, your information will be stored and associated with your organization. Only an organization admin or owner can edit verification information.
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/Set Up Development Configuration.md

Docs
# Set Up Development Configuration
On your app's **Development configuration** page, you must configure several methods to validate and restrict access to certain web endpoints, ensuring security and controlled integration.
- **Security**: Specify trusted domains for your app, as TikTok will only support requests to these trusted domains.
- **Webhooks**: Enter a callback URL for TikTok to notify your application when an event occurs, like a payment transaction using TikTok's APIs.
- **URL properties**: Verify ownership of URLs in your app configuration by domain or URL prefix.
## Add trusted domains
During runtime, your app can only initiate network requests to trusted domains that have been registered. Any domain not registered will be denied access. Therefore, all domains involved in network requests for your app must be registered here.
To add trusted domains for your app, complete the following steps:
- Click the **Security** tab on your **Development configuration** page.
- Click the **Add domain** button to enter a URL.
- Domains must start with `https://` and cannot contain wildcards or paths.
- You can add up to 20 domains.
- Click the **Save changes** button.
## Set up webhooks
When your app is ready to receive webhooks notifications, you can use this webhooks module to confirm that it will handle the request correctly. To set up webhooks for your app, complete the following steps:
- Click the **Webhooks** tab on your **Development configuration** page.
- Enter a callback URL. TikTok will push messages to this URL when a specified event occurs.
- Click the **Test URL** button to send a test event. We'll send a POST request to your callback URL when you click the **Send** button.
- Once you've verified that your application received the request correctly, click the **Save changes** button.
[Learn more about webhooks](https://developers.tiktok.com/doc/webhooks-overview).
## Verify URL ownership
You must verify URL properties for all URLs in your app configuration. Some features require URL verification before they can be used, like Link Sharing and Content Posting API. There are two cases for URL verification, depending on when the app was created.
To verify URL properties, complete the following steps:
- Click the **Webhooks** tab on your **Development configuration** page.
- Click the **Verify properties **button.
- Choose whether to verify your URL by **Domain** or **URL prefix**:
- For verification by Domain, enter your domain and subdomain name, then click **Verify**.
- For verification by URL prefix, enter your complete URL, then click **Verify**. Download the provided signature file, then upload it to your URL.
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Platform.md

Docs
# Prepare Your Developer Account
This guide explains how to kickstart the mini game integration process by preparing the following items in the Developer Portal with your TikTok for Developers account:
- An organization that represents your business
- An app that represents your mini app
## Prerequisite
[Before you start, you will need a TikTok developer account on the TikTok for Developers website. Sign up for an account](https://developers.tiktok.com/signup) if you haven't already.
## Create an organization
First, you must create an organization on the Developer Portal that represents your business:
- Click **Developer Portal** in the navigation bar of the TikTok for Developers website.
- Click **My organizations**.
- Click **Create organization**.
- Name your organization using the full name of your business entity. This information will be displayed to TikTok users.
**Note**: You cannot change the organization name after you create it.
### Add members to your organization
Once you've created your organization, you can add members who will be able to access and work on the apps owned by your organization. Certain settings are restricted to organizational admins. As the creator of the organization, your account automatically has admin access.
- Click the **Members** tab on your organization's page.
- Click the **Invite member **button.
- Enter the member's email address to send an invitation.
- Select the member's role type:
- **Member**: Can access the organization's apps and resources. No permission to manage the organization or its members.
- **Admin**: Can manage the organization's members, apps, and resources.
[Learn more about working with organizations](https://developers.tiktok.com/doc/working-with-organizations).
### Verify your organization as a business
Verify your organization's identity as a registered business by providing TikTok with detailed documentation and certifications. This helps ensure a more secure experience for developers.
Business verification is also mandatory for monetization. Only organization admins can complete business verification.
[Learn how to verify your business.](https://developers.tiktok.com/doc/verify-your-business)
## Create an app
Create an app in the Developer Portal that represents your mini app. You will use this app to register information, configure basic settings, upload code packages, and manage operations.
- Click **Developer Portal** in the navigation bar of the TikTok for Developers website.
- Click **Manage apps**.
- Click the **Connect an app** button.
- Select your organization as the app's owner.
- Enter your mini app's name as the **App name**.
- Select your app type.
## Next step: Configure your app's basic information
[After you've created an organization and an app that represents your mini game or mini drama, you can begin configuring your app. Learn more about how to add basic information about your app](https://developers.tiktok.com/doc/basic-information-specifications).
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/U.S. and E.U. Launch Approval.md

Docs
# U.S. and E.U. Launch Approval
If you intend on launching your app to users in the U.S. and E.U., you must provide details about your company and its data usage in an approval request form on the Developer Portal. After receiving your request, TikTok may conduct a full third-party risk management (TPRM) analysis to assess whether your company meets our compliance standards for data usage.
This analysis allows TikTok to ensure that vendor relationships remain secure, legally sound, and aligned with our obligations under U.S. and E.U. law and internal standards. Your participation is essential to maintaining a trusted partnership.
## Process for launching your app to U.S. and E.U. users
To receive approval to launch your app to users in the U.S., you must complete the following:
- **Submit the launch approval request**: Fill out the approval request form on the Developer Portal to determine eligibility for launch in the U.S. and E.U. There are two parts:
- **Organization details**: Provide your company's business and operations information.
- **Data requirements**: Indicate what type of data is required for your operations.
- **Complete the TPRM questionnaire**: If you indicated that you need access to sensitive data in your approval request form, you will receive a TPRM questionnaire in the next 7-10 days. If your submission is approved, you may launch your app to users in the U.S. and E.U.
- **Sign agreement**: You must sign a data security agreement for your scope to take effect.
## U.S. launch approval request
To start the approval request process, you must first complete the U.S. launch approval request form on the Developer Portal. This requires you to provide information about your company's operations and intended data usage.
### Organization details
In the request form, you must provide information about the following:
- Country where your company is registered
- Your company's majority stakeholders (only those with a controlling interest of 25% or more), and their countries of residence and citizenship
- All locations of the teams that will support your U.S. launch, operations, and customer support in any way
- Location of primary data centers where U.S. user data will be stored
### Data requirements
TikTok requires you to indicate which type of data you intend to use for reporting and operations purposes. Depending on what data type you select, some features may not be available. Two data types are considered:
- **Excepted data**: The aggregated data of your U.S. users. For excepted data, any category of U.S. user data being examined requires a minimum of 1,000 unique users.
- **Sensitive data**: Detailed, individual-level user data that will be available regardless of the number of unique U.S. users. If your company's ownership, personnel, service and support locations, and necessary fourth parties are affiliated or supported from restricted countries, this data type will not be available to you.

|  | **Excepted data** | **Sensitive data** |
| --- | --- | --- |
| Scale | Aggregated | Individual |
| Data availability | Data reporting only available once the app reaches 1000 unique U.S. & E.U. users | Data reporting available without restriction on unique U.S. & E.U. users |
| Regional restrictions | Available to all companies, potential feature restrictions apply | Unavailable to companies affiliated with restricted countries or regions |
| Inaccessible features | In-App Ads | None |
| TPRM screening | Not required | Required |
| Example | The aggregated number of clicks on a video from at least 1,000 U.S. users | The duration of a video an individual U.S. user has watched |

Fill out the pre-selection questions to help you determine what data type is required.
- If your app only requires In-App Purchases, **Excepted data** is recommended.
- If your app requires both In-App Purchases and In-App Ads, **Sensitive data** is required.
- If your business operations require detailed, individual-level user data, **Sensitive data** is required.
## Third-Party Risk Management questionnaire
[If you indicate that your company requires sensitive data, a representative from the TikTok U.S. Data Security Inc. (USDS) will email you an additional questionnaire. TikTok USDS is an organization tasked with managing TikTok's business functions that require access to U.S. user data. Learn more about TikTok USDS](https://usds.tiktok.com/what-is-usds).
### Vendor compliance review process
To align with TikTok USDS's data protection requirements, you must complete a **Vendor Compliance Questionnaire (VCQ)** through our TPRM platform.
This review covers key risk areas, including the following:
- **Ultimate Beneficial Ownership (UBO)**
- **Headquarters and workforce locations**
- **Service and support geography**
- **Data access, processing, and storage practices**
- **Use of subcontractors and fourth parties**
**Important**: Incomplete responses may delay approval. TikTok's TPRM analysts will review your submission and follow up with any clarification requests. Based on the findings, we will proceed as follows:
- If compliant, you are cleared to proceed, while subject to legal agreement terms from TikTok USDS.
- If there are risks, we’ll work with you to assess mitigation options or alternative arrangements.
Your cooperation in this process helps ensure a secure and trusted partnership for both our organizations.
### Compliance review definitions and requirements
More information about the compliance review's key risk areas is listed below.
#### Ultimate Beneficial Ownership (UBO)
UBO refers to the individuals or entities who ultimately own or control your company. Even if ownership is indirect or layered through holding companies, the ultimate decision makers must be disclosed.
**Note:** Vendors with a UBO holding ≥20% ownership interest located in a restricted country may not access, process, or store TikTok USDS protected data.
#### Headquarters and workforce locations
Your personnel who support TikTok U.S. users—whether employees, contractors, or subcontractors—must not be based in a restricted country. This restriction applies regardless of employment classification or whether the personnel support us directly or indirectly.
#### Service and support location restrictions
All technical support and operational services related to TikTok USDS must be performed outside restricted countries. This includes the following:
- Hosting environments
- Development teams
- Customer support personnel
Failure to comply with this requirement may lead to disqualification or reassessment of the vendor relationship.
#### Data handling locations
TikTok USDS data cannot be accessed, processed, modified, or stored in a restricted country.
Please confirm your cloud and infrastructure configurations before completing the VCQ, especially if your services use auto-scaling or globally distributed environments.
#### Fourth-party disclosure requirements
If your organization relies on other entities (cloud providers, IT subcontractors, for example) to support your TikTok USDS engagement, those are considered fourth parties. Disclosure is required if these parties engage in the following:
- Host, transmit, or process USDS data
- Provide core infrastructure for your services
- Offer necessary services for your operational delivery to TikTok
## Approval request results
After completing the approval request process, you may receive one of the following results.
- **Approved**: You may launch your app in the U.S. without restrictions. No aggregation is required for data reporting.
- **Approved with restrictions**: You may launch your app in the U.S., but access to certain features is restricted. Aggregation is required for data reporting.
- **Not approved**: You may not launch your app in the U.S. Contact your TikTok operations representative for support.
If you have any questions, please reach out to the TikTok USDS TPRM team at TPRM@tiktokusds.com.
## Sign agreement to access sensitive data
If you requested access to sensitive data, you must sign a data security agreement after your request has been approved for the data scope to take effect.
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/Verify Your Business.md

Docs
# Verify Your Business
When you create an account for your organization on the Developer Portal, you must verify your organization's identity and provide detailed documentation and certifications. This helps ensure a more secure experience for developers.
**Note**: Business verification is mandatory for publishing mini games and mini dramas and accessing monetization features.
## Prepare your verification documents
To complete verification, you are required to electronically submit the following documents:
- Your company's business certification
- A government-issued photo ID of your primary or legal representative
- Proof of representation for your primary representative
The documents listed below are accepted.
### Business certificate
This document must be issued by the competent government authority in the country or region where your business is registered. Your document must contain the following information.
- Full legal business name (in both English and the local language)
- Business registration number
- Address
- Legal representative's name (if not on the business certificate, upload supplementary documentation)
The following documents are accepted for verification.
- Business license
- Certificate of incorporation or registration
- Extract from commercial registry
- Tax registration or certificate
**Tip**: If your document doesn't contain all of the required information, you can combine multiple documents into one PDF. For example:
- Business certificates in some regions don't include the legal representative's information, but registration certificates usually do. You can combine them into one PDF to upload.
- Business certificates in some regions are only available in the local language, without an English name. Usually the bank account opening certificate of the same entity includes an English name. You can combine them into one PDF to upload.
### Photo ID of your primary or legal representative
This representative will act as the main point of contact between TikTok and your business. They must be officially authorized to act on behalf of the company in legal, financial, and administrative matters. You can choose between your company's legal representative or someone who handles communications and project management, such as director or general manager.
**Tip**: Your primary or legal representative is usually listed on the company's registration documents.
You must provide the representative's government-issued photo ID that includes the following information:
- Issuing country or region
- Representative's full legal name
- ID number
- Nationality and/or full address
- Date of birth
- Date of expiry (if available)
Some commonly accepted forms of identification include the following.
- Driver's license
- Passport
- Permanent resident card
- State identification card
### Proof of representation
You must provide documentation proving that the stated individual is the primary representative of the business. The document must contain the following information:
- Representative's full name
- Company name
Check what type of document you should submit as proof of representation:
- Representative's full name **is** on the business registration document: Re-submit the original business registration document as proof of representation.
- Representative's full name** is not** on the business registration document: Upload any other file that includes the representative's full name and company name.
- No existing files satisfy requirements: Provide a Letter of Authorization following the provided template.
Before starting the verification process, ensure that the certification documents you provide meet the following requirements:

| **Requirement** | **Description** |
| --- | --- |
| Accepted file formats | JPEG, PNG, PDF, JPG |
| Certification type | Business and personal documents must be electronic versions of acceptable official documents issued by the local government. |
| File size | 10 MB maximum per file |
| Image quality | All four corners and edges of the document must be fully visible. No portion of the document should be cut off or cropped. The document should be flat and not folded or wrinkled in ways that obscure critical information. There should be no third-party watermark on the document. There should be no blurriness, pixelation, or distortion that impairs readability. Black-and-white copies are not acceptable. |
| Resolution | 480 x 480 pixels minimum per file |
| Validity period | Documents must be currently valid and not expiring within 30 days |

**Note**: Depending on your business situation, we may ask you to submit additional certification.
## Complete verification form
To verify your business, you must complete a verification form with information about your business, primary or legal representative, and designated point of contact. To complete the form, go to the Developer Portal and complete the following steps:
**Note**: Only registered organization admins can view the Business page and complete verification.
- Find **My organizations** and select your desired organization.
- Go to the **Business** page then click the **Start verification **button**.**
- Fill out all sections of the verification form and upload certification documents.
- Business details: upload certification
- Primary representative: upload certification
- Operational representative: register and verify an email address
- Submit the verification form for review. You can expect to hear back in 1-3 business days.
**Note**: If you're unable to find the entry point for business verification on your organization's Overview page, you may need to first connect an app with the mini game app type. Follow the steps below.
If connecting an app to your organization for the first time, you can follow this flow:
- On the Developer Portal, click **Manage apps**.
- Click the **Connect an app** button if you're creating a mini game for the first time.
- Select **Organization** as the ownership type.
- Enter the name of your mini game, then select **Mini game** as the app type.
- Go to the Developer Portal, then click **My organizations**. Click your organization. You should see the business verification card on the **Overview** page.
### Fill in business details
Complete the business details section as indicated.

| Field | Remarks |
| --- | --- |
| Country of registration | Select your company registration country or region. If you do not see your company's country listed, contact your TikTok operations representative. **Note**: If you select Hong Kong, after business verification, your business will not be able to publish apps in the U.S. and can only launch them in countries other than the US. |
| Business certificate | [Enterprise qualification certificate. Refer to the business certificate specifications](https://developers.tiktok.com/doc/verify-your-business#business_certificate). |
| Full legal business name in the local language | Full company name in the local language |
| Full legal business name in English | Full company name in English |
| Business registration number | Company registration number as stated on the business certificate |
| Incorporation registered address | Company registered address |
| Date of expiry of business certificate | Period during which the document is valid. If the document has no stated expiration date, you may indicate so. |

**Note**: For businesses registered in Hong Kong, businesses operating for less than one year may provide the NNC1 document, while those operating for one year may provide the NAR1 document.
### Fill in primary representative details
Complete the primary representative details section as indicated. They will act as the main point of contact between TikTok and your business and must be officially authorized to act on behalf of your business.
You can choose between your company's legal representative or someone who handles communications and project management, such as director or general manager.

| Field | Remarks |
| --- | --- |
| Proof of identity | [Government-issued photo identification of the primary or legal representative, which must include full name, date of birth, and nationality or address. **Note**: For identity documents from regions that do not include nationality or address fields, submit the representative's passport as proof of identity. Refer to the photo ID document specifications](#share-Dowjd5SUZo950qxNTE2uWoqdsQc). |
| Issuing country or region | [Issuing country or region stated on the document. If you do not see your company's country listed, contact your TikTok operations representative or submit a support ticket](https://developers.tiktok.com/portal/support). |
| Full legal name | Representative's full name (in the original language) |
| ID number | Identification number as stated on the document |
| Which of the following is displayed on the uploaded document? | Country or region, address, or both |
| Date of birth | Date of birth of the representative as stated on the document |
| Date of expiry on proof of identity | Period during which the document is valid. If the document has no stated expiration date, you may indicate so. |
| Proof of representation status | [Documentation proving that the stated individual is the primary representative of the business. Documents must state the name of the representative. Refer to the proof of representation document specifications](#share-QlRfdS6FEoH9HzxvXbsunUWYspb). |

### Designate an operational representative
Provide the name and email address of your main operational representative. Registering the email requires CAPTCHA verification.
After verifying that all of the information is correct, click the **Submit** button to complete the form.
## Developer verification review and completion
After you submit your verification form, TikTok will review your verification request within 1-3 business days. You can track the status of your request on your organization's **Overview** and **Business **pages. You may receive one of the following results.
- **Verified**: Your business was successfully verified.
- **Couldn't verify**: Due to certain issues with your request, TikTok could not verify your business. You may need to edit and resubmit the verification form.
- [**Information needed**: TikTok requires you to submit additional information](#share-DbYPdccFYoZB1AxxlQhu2cUhsSf) to verify your business.
- [**Rejected**: Your business verification was rejected. Contact your TikTok representative or submit a support ticket](https://developers.tiktok.com/support) for support.
**Warning**: To access monetization features and publish your mini game or mini drama, your business must be verified.
Once verified, your certification documents will be stored and associated with your organization. Only an organization admin or owner can edit verification information.
## Submit additional information
TikTok may request that you provide additional information for your primary representative. In this case, submit the following document by the indicated deadline. The document must meet the same formatting and image quality requirements as the other certification documents.
### Proof of address for your primary or legal representative
Proof of your representative's address must include this information:
- Issuing agency
- Representative's full name
- Address
- Issuance or statement date
- Document must be dated within the last 6 months
Some commonly accepted forms of identification include the following. You can upload any one or more of these documents:
- Valid government ID (drivers license, national ID card, or permanent residence card)
- Utility bill
- Bank statement
- Credit card statement
- Lease or rental agreement
- Property tax statement
- Insurance policy document
- Letter from a government agency
- Employer letter
- Pay stub
- Mortgage statement
To submit supplementary information when necessary, do as indicated:
- Go to the **Verification** tab of your organization's** Business **page
- Click the **Add additional information **button.
- Upload and submit the proof of address.
## Troubleshooting developer identity verification
If your verification request was unsuccessful, it may have been due to the following reasons:
- The required information was missing or invalid.
- The type of document submitted is not accepted.
- The document submitted did not meet image quality requirements.
- You must provide supplementary information.
To troubleshoot developer verification, consider the following:
- Check that you've submitted acceptable document types.
- Check that the business license or certificate number matches the one in your document.
- Ensure all of the text on your document is clearly displayed and the business license or certification number is visible.
- If you are photographing your document, place it on a dark background and ensure that all text is legible.
[If your document is still not approved, try submitting a different acceptable document. If you continue to encounter issues after having completed the troubleshooting steps listed above, please contact your TikTok representative or submit a support ticket](https://developers.tiktok.com/support).
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/Error Codes.md

Docs
# Error Codes
TikTok Minis APIs return errors in three categories: System Errors (server-side issues), Invalid Parameter Errors (request validation failures), and Business Errors (payment/subscription domain constraints). Use the error code and `log_id` to trace issues.
## System Error

| Code | Description | Action |
| --- | --- | --- |
| 50001000 | TikTok Internal Error | Retry or do nothing |

## Invalid Param Error

| Code | Description | Action |
| --- | --- | --- |
| 40001000 | Invalid Parameters | Check your request parameters |

## Business Errors

| Code | Description | Action |
| --- | --- | --- |
| 20011002 | Order not existed | Verify client key, trade order ID, and user ID |
| 20021001 | Submerchant ID invalid | Contact TikTok to enable payment capabilities |
| 20021002 | Outer order ID existed | Your external order ID is a duplicate |
| 20001003 | Tier ID invalid | Check the tier ID |
| 20021101 | Subscription is active | Cannot create a new one |
| 20021102 | Subscription is canceled | Can only reactivate, not create a new one |
| 20021103 | Subscription is on hold | Guide user to handle their current subscription |
| 20021108 | Change subscription unfinished | Wait 1 hour between change requests |
| 20021111 | Subscription too close to renewal | Cannot be changed within 24 hours of renewal |

Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/OAuth for TikTok Minis.md

Docs
# OAuth for TikTok Minis
TikTok OAuth v2 flow manages the token life cycle, allowing you to integrate authentication flows directly in your TikTok Minis or mini game. A successful authorization flow grants you refreshable access tokens. Those tokens enable you to perform endpoint access with user permissions.
[Note: OAuth for TikTok Minis has the same structure as User Access Token Management](https://developers.tiktok.com/doc/oauth-user-access-token-management), with the exception of omitting `redirect_uri` and `code_verifier` in the request body parameters for fetching an access token.
## Fetch an access token using an authorization code
Once the authorization code callback is handled, you can use the code to retrieve the user's access token.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/token/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| code | string | The authorization code from the web, iOS, Android or desktop authorization callback. The value should be URL decoded. |
| grant_type | string | A fixed value that should always be set as `authorization_code` |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize |
| access_token | string | The access token for future calls on behalf of the user |
| expires_in | int64 | The expiration of `access_token`in seconds. It is valid for 24 hours after initial issuance. |
| refresh_token | string | The token to refresh `access_token`. It is valid for 365 days after the initial issuance. |
| refresh_expires_in | int64 | The expiration time of `refresh_token`in seconds |
| token_type | string | A fixed value that should be set to `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'code=CODE' \
--data-urlencode 'grant_type=authorization_code' \
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "afd97af1-b87b-48b9-ac98-410aghda5344",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request is missing a required parameter.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## Refresh an access token using a refresh token
Although the fetched `access_token` expires within 24 hours, it can be refreshed without user consent. The developer's backend server can schedule background jobs to keep tokens up to date.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/token/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| grant_type | string | A fixed value that should always be set as `refresh_token` |
| refresh_token | string | The user's refresh token |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| open_id | string | The TikTok user's unique identifier |
| scope | string | A comma-separated list (,) of the scopes the user has agreed to authorize |
| access_token | string | The new token for future calls on behalf of the user |
| expires_in | int64 | The expiration of the access token in seconds |
| refresh_token | string | The token to refresh a user's `access_token`. Note: The returned `refresh_token`may be different than the one passed in the payload. You must use the newly-returned token if the value is different than the previous one. |
| refresh_expires_in | int64 | The expiration for `refresh_token`in seconds. |
| token_type | string | The value should be `Bearer`. |

Make sure to store these values on your back end as they are needed to persist access.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=REFRESH_TOKEN'
```
If the request is successful, the response will look like the following.
```
{
    "access_token": "act.example12345Example12345Example",
    "expires_in": 86400,
    "open_id": "asdf-12345c-1a2s3d-ac98-asdf123as12as34",
    "refresh_expires_in": 31536000,
    "refresh_token": "rft.example12345Example12345Example",
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
}
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
## Revoke access
When a user wants to disconnect your application from TikTok, you can revoke their tokens so the user will no longer see your application on the **Manage apps **page of the TikTok for Developers website.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/oauth/revoke/`
### Authorization header

| **Key** | **Value** |
| --- | --- |
| Content-Type | application/x-www-form-urlencoded |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| client_key | string | Your app's unique client key, obtained from your app page on the Developer Portal |
| client_secret | string | Your app's unique client secret, obtained from your app page on the Developer Portal |
| token | string | The `access_token`that bears the authorization of the TikTok user |

### Response struct
If the request is successful, the response struct will be empty.
### Example
```
curl --location --request POST 'https://open.tiktokapis.com/v2/oauth/revoke/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cache-Control: no-cache' \
--data-urlencode 'client_key=CLIENT_KEY' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'token=ACCESS_TOKEN'
```
If the request is not successful, an error response body will be returned in the response, like the following.
```
{
    "error": "invalid_request",
    "error_description": "The request parameters are malformed.",
    "log_id": "202206221854370101130062072500FFA2"
}
```
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/Payment APIs.md

Docs
# Payment APIs
These APIs manage transactions using the platform's currency, Beans.
## Get recharge tiers
You need to first get the ID of the tiers you want to show on your recharge page.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/utility/get_tier_infos/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| tier_ids | list<string> | The list of IDs for tiers you want to get detail information of |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TierInfos | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TierInfos**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| tier_infos | map<string, TierInfoObject> | The TikTok user's unique identifier. The key in the map is `tier_id`. |

**TierInfoObject**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| tier_id | string | The ID of the tier |
| tier_name | string | The name of the tier |
| token_type | string | The type of token contained in the tier. For now, this field can only be `"BEANS"` |
| token_amount | int | The amount of token contained in the tier. For now, this filed implies the amount of Beans |
| price | string | The price of the tier |
| currency | string | The currency of the price, which follows the ISO 4217 standard. Example: `"USD"`for US Dollars |
| symbol | string | The symbol of the price. Example: `"$"`for USD. |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "tier_ids": ["1731381720000100"]
}
```
**Response**
```
{
    "data": {
        "tier_infos": {
            "1731381720000100": {
                "tier_id": "1731381720000100",
                "tier_name": "pd_beans_showcase_100",
                "token_amount": 100,
                "token_type": "BEANS",
                "price": "1.19",
                "currency": "USD",
                "symbol": "$"
            }
        }
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_od": "202411190743174589DAA30620D104990F",
    }
}
```
## Create an order
You need to pass the information of the order created in your system to TikTok to generate a trade order on TikTok's server, which is a necessary step in the pay and refund process.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/trade_order/create/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through `/oauth/access_token/`. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| token_amount | int | The amount of token contained in this order. For now, this field implies the amount of Beans. |
| order_info | OrderInfoObject | The order info from partner's side |

**OrderInfoObject**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| order_id | string | The ID of your order created in your system |
| order_url | string | The URL to the order information page in your system |
| product_name | string | The name of the product user intended to purchase |
| product_id | string | The ID of the product user intended to purchase |
| quantity | int | Number of products contained in this order |
| quantity_unit | string | Unit of the product, for example, `"episode"` |
| image_url | string | URL of the cover image of the order. We'd recommded using the poster of the drama in this field. Users can see this image on their order history page |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TradeOrderInfo | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TradeOrderInfo**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "token_amount": 100,
    "order_info": {
        "order_id": "external_order_id_003",
        "product_name": "Wake up dad! wedding time",
        "product_id": "external_product_id",
        "order_url": "/profile/order_history/external_product_id",
        "quantity": 1,
        "quantity_unit": "episode", // Pass in the unit of the item being sold based on the actual situation, such as 'episode' for a drama series unit
        "iamge_url": "https//your.domain/pics/wake_up_dad.jpg"
    }
}
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Query an order
You can track the status of the trade order by calling this API.
### Endpoint
_POST_` ``https://open.tiktokapis.com/v2/minis/trade_order/query/`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The type of token you want to get tier Info for. For now, there is only one type, `"BEANS"`. Please only use `"BEANS"`in this field. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | TradeOrderInfo | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TradeOrderInfo**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |
| trade_order_status | string | The status of the trade order. Available values are: `"PENDING"`and `"SUCCESS"` |

### Example
**Request**
```
{
    "trade_order_id": "TOID1732533244259"
}
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259",
        "trade_order_status": "PENDING"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "202411251312430B89D17FDCB31F26244A"
    }
}
```
## Check redeem amounts
You need to make sure all the products you are trying to sell follow the correct pricing policy under TikTok's restriction. You must first check if the price you've settled on each product is legal by calling this API.
### Endpoint
_POST_ https://open.tiktokapis.com/v2/minis/utility/check_redeem_amounts/
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | TRUE |

### Request body parameters

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| token_type | string | The type of token you want to get tier info for. For now, there is only one type: `"BEANS"`. Please only use `"BEANS"`in this field. |
| token_amounts | list<int> | The list of token amount you want to get detail information of. |

### Response struct

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| data | CheckResponse | The response data |
| error | ErrorStruct | The common error structure returned by TikTok Open API |

**TierInfos**

| **Key** | **Type** | **Description** |
| --- | --- | --- |
| valid | bool | True if all amounts are valid |

### Example
**Request**
```
{
    "token_type": "BEANS",
    "token_amounts": [11, 19, 999, 2999]
}
```
**Response**
```
{
    "data": {
        "valid": true
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_od": "202411190743174589DAA30620D104990F",
    }
}
```
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/Subscription APIs.md

Docs
# Subscription APIs
## Create a subscription
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/create/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| tier_id | string | Tier ID of the subscription product | Yes |
| order_info | OrderInfoObject | The order info from partner's side | Yes |

**OrderInfoObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| order_id | string | The ID of your order created in your system | Yes |
| product_name | string | The name of the product user intended to purchase | Yes |
| order_url | string | The URL to the order information page in your system | No |
| order_detail | string | Detailed info of the order info, if any | No |

### Response data struct

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID. | Yes |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/create/' \
--header 'Authorization: Bearer {AccessToken}' 
--header 'Content-Type: application/json' \
--data '{
    "tier_id": "sandbox_499_1M",
    "order_info": {
        "order_id": "wsf_test_6",
        "product_name": "ttt1",
        "order_detail": "",
        "order_url": ""
    }
}'
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Reactivate subscription
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/reactivate/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| subscription_id | string | ID of user's current active subscription | Yes |
| order_info | OrderInfoObject | The order info from partner's side | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/reactivate' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "subscription_id": "784647171844-B",
    "order_info": {
        "order_id": "reactivate_test_wsf7",
        "product_name": "reactivate",
        "order_detail": "",
        "order_url": ""
    }
}'
```
**Response**
```
{
    "data": {
        "trade_order_id": "TOID1732533244259"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Get active subscription list
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_active_list/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscriptions | list<ThirdPartyUserSubscriptionObject> | List of active subscriptions |

**ThirdPartyUserSubscriptionObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| subscription_id | string | ID of the subscription | Yes |
| tier_id | string | ID of the subscription product | Yes |
| is_subscription_rights_valid | bool | indicate whether this right is still valid | Yes |
| is_renewal_normal | bool | indicate whether the renew is normal, false if renew is failed/onold | Yes |
| trade_order_id | string | the latest trade_order_id related to this subscription | Yes |
| begine_time | int64 | beginning time of this subscription | No |
| end_time | int64 | end time of this subscription | No |
| next_duduct_time | int64 | time of the next deduct | No |
| pay_type | string | IAP or WEB; IAP=Google/Apple Store, WEB=PayPal | No |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_active_list' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json'
```
**Response**
```
{
    "data": {
        "subscriptions": [
            {
                "subscription_id": "tb4ML0ZVim",
                "tier_id": "xohs4Jojay",
                "is_subscription_rights_valid": true,
                "is_renewal_normal": false,
                "trade_order_id": "ggG7luEdWt",
                "is_sandbox": true,
                "begin_time": 8054018414209391465,
                "end_time": 1061662930613089341,
                "next_duduct_time": 2184276991229817160,
                "pay_type": "IAP"
            }
        ]
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Get subscription Info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_subscription_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription | ThirdPartyUserSubscriptionObject | List of active subscriptions |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_subscription_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "trade_order_id": ""
}'
```
**Response**
```
{
   "data": {
        "subscription": {
            "subscription_id": "H36qTi1gNU",
            "tier_id": "iqBaXsMxHh",
            "is_subscription_rights_valid": true,
            "is_renewal_normal": false,
            "trade_order_id": "SbUgvLyKj5",
            "is_sandbox": true,
            "begin_time": 7564558100036318910,
            "end_time": 5659157601114497266,
            "next_duduct_time": 953443659701638510,
            "pay_type": "IAP"
        }
    },
    "error": {
        "code": "gvlXZLamY7",
        "message": "2xuw0XIUIr",
        "log_id": "uPnqDeYu1S"
    }
}
```
## Get trade order Info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_trade_order_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | The ID of order created by TikTok. Please store this ID since you can only query the order status through this ID | Yes |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription_tiers_info | SubscriptionTradeOrderInfoObject | List of active subscriptions |

**SubscriptionTradeOrderInfoObject**

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| trade_order_id | string | same as the requested trade_order_id | Yes |
| subscription_id | string | ID of the subscription | Yes |
| trade_order_status | string | indicate the status of the trade order: SUCCESS, PENDING,REFUNDED | Yes |
| is_sandbox | bool | Is sandbox order | No |
| begine_time | int64 | beginning time of the subscription related to this trade order | No |
| end_time | int64 | end time of the subscription related to this trade order | No |
| next_duduct_time | int64 | Happen time of the next deduction of the subscription related to this trade order | No |
| pay_type | string | IAP or WEB | No |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_trade_order_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "trade_order_id": ""
}'
```
**Response**
```
{
    "data": {
        "trade_order_id": "UIlpZZ1TIc",
        "subscription_id": "iSjgkQ9rei",
        "trade_order_status": "BRM1MQac3i",
        "is_sandbox": true,
        "begin_time": 162780036655460135,
        "end_time": 7326223299323173385,
        "actually_end_time": 7143902738493296646,
        "pay_type": "IAP"
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
## Get subscription tier info
### Endpoint
`POST ``https://open.tiktokapis.com/v2/minis/subscription/get_subscription_tier_info/`
### Authorization header

| **Field** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Request body parameters

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| tier_ids | list<string> | The list of tier_ids of the target subscription product. For sandbox, these `tier_ids`can be used: sandbox_499_1M $4.99/Monthly sandbox_1347_3M $13.47/QUARTERLY sandbox_699_1M $6.99/Monthly sandbox_1887_3M $18.87/QUARTERLY |
| device_platform | string | Indicate user's device platform Optional value: `android`, `iphone` If this field is empty or other value, we will use `iphone`as the default value. You can determine whether a device is running IOS or Android by analyzing the User-Agent in HTTP request |

### Response data struct

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| subscription_tiers_info | map<string, SubscriptionTradeOrderInfoObject> | List of active subscriptions |

**SubscriptionTierInfoObject**

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| tier_id | string | Same as the requested `trade_order_id` |
| deduct_cycle | string | Length of each deduction cycle. Possible values are: WEEKLY MONTHLY BIMONTHLY QUARTERLY SEMIANNYALLY ANNUALLY |
| deduct_type | string | indicate the deduction type. Possible values are: one_time auto_renew |
| price | string | Price to deduct for each cycle |
| currency | string | Currency of price to deduct for each cycle |
| symbol | string | Symbol of currency of price to deduct for each cycle |

### Example
**Request**
```
curl --location 'https://open.tiktokapis.com/v2/minis/subscription/get_subscription_tier_info/' \
--header 'Authorization: Bearer {AccessToken}' \
--header 'Content-Type: application/json' \
--data '{
    "tier_ids": ["awcnbwhfvvf9tmey_1347_3M"]
}'
```
**Response**
```
{
    "data": {
        "subscription_tiers_info": {
            "zqrPo2cIEE": {
                "tier_id": "IdohVeNqMX",
                "deduct_cycle": "I6Sj9ICBaW",
                "deduct_type": "CfuHfLeMoH",
                "price": "MrofV8f93l",
                "currency": "QiWeEc4YoU",
                "symbol": "uPk6QRdtsv"
            }
        }
    },
    "error": {
        "code": "ok",
        "message": "",
        "log_id": "20241125114034036EE8AEADBAF91D5E93"
    }
}
```
Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/TikTok Minis Server APIs.md

Docs
**TikTok Minis Server APIs **(open.tiktokapis.com) is a secure, backend-only suite of endpoints that manages identity and commerce for TikTok Minis (mini apps and mini games) via OAuth v2 and scope-based permissions. It provides OAuth token retrieval, scope-gated user info retrieval, order creation and management, and pricing. Your backend stores and manages tokens and trade orders.
TikTok Minis Server API serves both mini apps (such as mini dramas) and mini games use cases.

| **Category** | **Function** | **Description** |
| --- | --- | --- |
| [OAuth for TikTok Minis](https://developers.tiktok.com/doc/minis-oauth) | Fetch an access token using an authorization code | Exchanges the temporary `code`(received from the client-side `.login()`or `.authorize()`calls) for the permanent user tokens |
| Refresh an access token using a refresh token | Obtain a new `access_token`when the current one expires (after 24 hours), without requiring the user to log in again |
| Revoke access | Disconnects your application from a user's TikTok account |
| [TikTok User Data API](https://developers.tiktok.com/doc/minis-user-data) | Get user info | Retrieve basic profile information for an authorized TikTok user |
| [Payment APIs](https://developers.tiktok.com/doc/minis-payment-apis) | Get recharge tiers | Query the details and pricing of available BEANS recharge packages (tiers) offered by TikTok |
| Create an order | Register an upcoming payment order in your system with the TikTok server to generate a secure `trade_order_id`for the transaction |
| Query an order | Track the status of a specific payment order created on the TikTok server |
| Check redeem amounts | Verify if a list of requested Beans amounts (prices) for their products complies with TikTok's current pricing policy and restrictions |

Was this document helpful?


---
## SOURCE: TikTok Minis Platform/TikTok Minis Server APIs/TikTok User Data API.md

Docs
# TikTok User Data API
Most endpoints provided by TikTok for Developers require direct consent from TikTok users before you can invoke them. The permissions are granted on a scope level. Users have the right to only agree to a subset of scopes you requested from them.
Currently, TikTok Minis only supports `user.info``.basic` and `user.info``.open_id`. See **User Object** under the response struct.
## Get user info
[The `/v2/user/info/` endpoint returns some basic information for a given TikTok user. It must have `user.info``.basic` scope. To get the `user.info``.basic` scope, follow the explicit authorization process](https://developers.tiktok.com/doc/develop-your-mini-game).
### Endpoint
[`GET ``https://open.tiktokapis.com/v2/user/info/](https://open.tiktokapis.com/v2/user/info/)`
### Authorization header

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /oauth/access_token/. | Bearer act.example12345Example12345Example | Yes |

### Query parameters

| **Key** | **Type** | **Description** | **Example** | **Required** |
| --- | --- | --- | --- | --- |
| fields | string | The set of user fields to request for | open_id,union_id,avatar_url | Yes |

### Response Struct

| **Key** | **Type** |
| --- | --- |
| data | map<string, User Object> |
| error | [Error Object](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling) |

**User Object**

| **Field** | **Type** | **Description** | **Authorized ****s****cope** |
| --- | --- | --- | --- |
| open_id | string | The unique identification of the user within the current application (a TikTok user's unique identifier) | user.info.basic |
| union_id | string | The unique identification of the user across different apps for the same developer. For example, if a partner has X number of clients, it will get X number of `open_id`for the same TikTok user, but one persistent `union_id`for the particular user | user.info.basic |
| avatar_url | string | User's profile image | user.info.basic |
| avatar_url_100 | string | User`s profile image in 100 x 100 size | user.info.basic |
| avatar_large_url | string | User's profile image with higher resolution | user.info.basic |
| display_name | string | User's profile name | user.info.basic |

### Example
```
curl -L -X GET 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url' \
-H 'Authorization: Bearer act.example12345Example12345Example'
```
If the request is successful, the response will look like the following.
```
{
   "data":{
      "user":{
         "avatar_url":"https://p19-sign.tiktokcdn-us.com/tos-avt-0068-tx/b17f0e4b3a4f4a50993cf72cda8b88b8~c5_168x168.jpeg",
         "open_id":"723f24d7-e717-40f8-a2b6-cb8464cd23b4",
         "union_id":"c9c60f44-a68e-4f5d-84dd-ce22faeb0ba1"
      }
   },
   "error":{
      "code":"ok",
      "message":"",
      "log_id":"20220829194722CBE87ED59D524E727021"
   }
}
```
[If the request is unsuccessful, an error response body will be returned in the response. Learn more about error handling](https://developers.tiktok.com/doc/tiktok-api-v2-error-handling).
Was this document helpful?
