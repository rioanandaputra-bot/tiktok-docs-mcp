Docs
# Enable Monetization Features
This guide covers two mandatory steps to set up monetization for your mini app.
- **Feature enablement**: Enable monetization features by accepting payment terms, then integrate with monetization APIs to configure these features in your mini app.
- **Payout setup**: After enabling at least one monetization feature, provide business, tax, and bank information to set up a payout account. Any earnings will remain in your balance until you finish setting up.
**Note**: Only registered admins of your TikTok for Developers organization account can complete monetization setup.
## Prerequisites
[To access monetization features, your business must be verified by TikTok for Developers. Learn more about verifying your business](https://developers.tiktok.com/doc/verify-your-business).
## Feature enablement process
To enable monetization features, complete the following steps for your organization on the Developer Portal:
Note: You can only enable one monetization feature at a time.
- Go to your organization's **Monetization** page.
- Go to the **Feature enablement** section on the **Overview** page.
- Click the **Enable** button for whichever feature your business scenario requires. The following features are available:
- Mini games
- In-app purchases (IAP)
- In-app ads (IAA)
- Mini dramas
- In-app purchases (IAP)
- Review and sign the terms and agreements for your specified monetization feature. You can connect with monetization APIs for your mini game and mini drama after this step.
Once TikTok has fully reviewed your submission, you will receive an email and a Developer Portal notification informing you of your submission status. This process generally takes 1-2 days.
The feature you enabled will be applied to all mini apps registered under your organization.
### Configure monetization features
After enabling monetization features, you can configure these features in your mini app by integrating with TikTok APIs.
- [In-app ads setup](https://developers.tiktok.com/doc/in-app-ads)
- [In-app purchases setup](https://developers.tiktok.com/doc/in-app-purchases)
## Complete payout setup
To receive earnings, you must submit detailed business, tax, bank information. TikTok will only use this information to verify your tax responsibility in the U.S., make payments to you, and check compliance with regulatory requirements. The required information depends on which country or region your company is registered in.
Go to the **Payout setup **section on the **Overview **page and submit the requested information.
### Business details
Provide the following information for your business:
- **Business entity name**
- **Country of registration**
- **Permanent residence address**: The official legal address of the company as filed with the government when the company is registered.
If your business is not registered within the U.S., you must submit an additional document:
- **Company registration document**: Official proof of identification of your company issued by the tax authority or government of your country of registration. The following document types are accepted.

|  | **Non-U.S. entity ** | **U.S. entity ** |
| --- | --- | --- |
| **Required information** | **Business entity name** **Country of registration** **Permanent residence address** **Company registration document** | **Business entity name** **Country of registration** **Permanent residence address** |

### Tax details
Prepare the following tax information for submission. The information you are requested to provide will be used solely for tax purposes.

|  | **Non-US entity ** | **US entity ** |
| --- | --- | --- |
| **Required information** | **Business entity name** **Country of registration ** **Business type**: Select your business type: Corporation Partnership Disregarded entity Complex trust Simple trust Tax-exempt organization Foreign government - Controlled entity Foreign government - Integral part Central bank of issue International organization Private foundation Grantor trust Estate **Foreign tax identification number**: The tax identification number for your business in the country of registration. **Permanent address**: The permanent address of the beneficiary or owner of the business. | **Business entity name** **Country of registration ** **Backup withholding status** **U.S. Employer Identification Number (EIN)** **Federal tax classification type** C corporation S corporation Partnership Trust/estate LLC Other **Type of LLC** C S P **Foreign owners or beneficiaries ** **Permanent address**: The permanent address of the beneficiary or owner. This will be used for your company's W-9 tax form. |
| **Tax form** | W-8 BEN-E | W-9 |

[Warning: Payout setup is not currently available for organizations that are subject to backup withholding](https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding).
### Bank information
You’ll receive payments for your organization to the bank account you register. Only traditional bank accounts are accepted. Virtual accounts are not supported.
Depending on your region, the required information for bank setup could be any combination of the following fields:
- **Account name**
- **Country of institution **
- **Institution name **
- **Account number**
- **Routing number**
- **SWIFT/BIC**
- **IBAN**
**Note:** Your **Account name** must match the entity name registered during business verification. Otherwise, you may be required to submit documentation that displays your bank account number and your business license number.
If your organization already has a payout account set up, your bank information will be populated. If you need to change your payout details, reach out to your TikTok operations representative.
Was this document helpful?