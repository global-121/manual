---
title: Payments
hide:
  - toc
---
The Payment page provides an overview of all payments made and disbursed to registrations in the program. It allows you to track the payment status for each registration, including any completed, processing, or failed transactions, and processes new payments.

!!! Important "Who can perform actions in this page?"
    All standard roles can view the Payments page. CVA Manager and Finance Manager can create payments. Only the team members set as approvers for the program can approve them. Only the Finance Manager can start (send) payments. See [Create and approve payments](./create-approve-payment.md) for details. [Learn more about Roles & Permissions](../users/description-roles.md)

![Payments page](../assets/img/PaymentsPage.png)

## Create new payment requests

You can create new payment requests by clicking **Create new payment** in the top-right corner. This allows you to begin sending cash assistance to registrations included in the program. [To start creating payment, you can follow the guidelines on this page.](./create-approve-payment.md)

## Proceed with payments

The 121 platform offers **two different methods for processing payments**:

- **Send and Reconcile manual payments by exporting a payment instructions file**. You pre-process the payment within 121 by including the selected registration list in the payment round, then download the payment instructions to share to the FSP and later reconcile the payment data. Further instructions on the [manual payment page](./issue-payment-fsp-portal.md) and [manual reconciliation page.](./manual-payment-reconciliation.md)
- Process an **instant payment** directly within the 121 platform. A direct integration with the FSP automates the payment and reconciliation. Further instructions on [this page.](./payment-integrated-fsp.md)


## Overview of payment status

You can view a summary of all payments made in the course of your program and to registrations included in the program. This overview is especially useful for:

- Having clear insights of all disbursements made along the program up to date.
- Finance Manager and Finance Officer to keep track of payment statuses, including successful, processing and failed ones.
- CVA Manager and CVA Officer to keep informed and follow whether or not a registration is receiving cash aid support.
- For donors that may want to view the ongoing payment processes and deadlines as required.

Find out more about the payment and registration's statuses on [this page.](./list-status-payment-page.md)

---

## Export payment reports

For **financial audit**, financial and payment reporting for all transactions can be exported as an Excel file. You can track and trace any successful, processing and failed payments, and also share the reporting to donors that may require additional information about the running Cash Program.

Find out more about the payment reporting and activity on [this page.](./payment-reporting.md)

!!! Info "TIPS: Only download Excel files when required and delete after exporting / using"
    Excel files should only be downloaded when required to ensure personal data is kept secure. After use, Excel files should be deleted from your computer to keep personal data secure and prevent mistakes using old files. This way, you will always have the latest updated data in 121.

---

## Delivery Mechanisms

The 121 platform enables multipurpose cash. The Platform focuses on **digital cash distribution**, mainly mobile money, prepaid cards and bank transfers. If your Financial Service Provider (FSP) supports digital vouchers and/or physical cash distribution, these payment methods can be activated in the 121 platform.

You will be able to process payments with one or multiple delivery mechanisms depending on your program settings and enabled payment by the FSP.

| Category | Description |
| ---------------- | ----------- |
| **FSP Portal** | For non-integrated FSP and universal cash distribution methods. Manual export of payment instructions to upload into the FSP portal and reconciliation of payment data into 121. |
| **Bank Wire** | Direct bank transfers issued with 121 platform to registrations (integrated FSP) |
| **VISA debit card** | Direct transfers and top-up to VISA debit card (integrated FSP). Allows conditional and unconditional modalities. |
| **Mobile money** | Direct transfers to mobile wallets. |
| **E-vouchers** | This is an electronic document with a specific amount and dates that support and authorize financial transactions at designated locations. These are sent via WhatsApp. |
| **Paper vouchers** | Vouchers that are printed and handed over to the registrations. |
| **Cash-out vouchers** | A voucher that the registration uses to collect the money in cash. |

*In cases physical cash payment may be a better approach, these options can be discussed on a case-by-case basis with our 121 Team.*


!!! Info "Integration with local FSP"
    The 121 platform has integrated with a certain number of local FSP and aggregators. Additional local FSP can be integrated upon evaluation. Please, share your request with our team.

    Not all FSP can be integrated with third tool software such as the 121 platform. This can be due to **lack of compatible technology** or for **security reasons**, in which case the bank refuses to integrate with any platform providers so to protect the financial data. Therefore, if you would like to consider integrating your Financial Service Provider with the 121 platform:

    - Check that your FSP or the bank allow integrating with third party tool or external service provider platform;
    - the FSP or the bank support API protocols. An application programming interface (API) is a way for two or more computer programs or components to communicate with each other;
    - Make sure to have an agreement signed regarding the use of their services and data protection.

---

## Financial Service Providers in 121

The table below lists the FSPs that the 121 platform supports, with their name in the portal. Which FSPs are available depends on your 121 instance. The Program Admin can see the FSPs set up for your program in **Settings** > **FSP integration**.

| FSP (name in the portal) | Delivery mechanism | Type |
| :---- | :---- | :---- |
| **Airtel** | Mobile money | Integrated FSP |
| **Al Fouad** | Money transfer, paid out to the registration by Al Fouad | Integrated FSP |
| **Albert Heijn voucher paper** | Paper vouchers | Integrated FSP |
| **Albert Heijn voucher WhatsApp** | E-vouchers sent via WhatsApp | Integrated FSP |
| **Commercial Bank of Ethiopia** | Bank transfer | Integrated FSP |
| **Cooperative Bank of Oromia** | Bank transfer | Integrated FSP |
| **Excel Payment Instructions** | Any FSP that is not integrated: you export the payment instructions and import the reconciliation file | FSP portal (manual) |
| **MTN** | Mobile money | Integrated FSP |
| **Nedbank** | Cash-out vouchers | Integrated FSP |
| **Onafriq** | Mobile money | Integrated FSP |
| **Safaricom** | Mobile money (M-Pesa) | Integrated FSP |
| **Visa debit card** | VISA debit card. See [Debit cards](./debit-cards.md). | Integrated FSP |

---

-8<- "docs/en/_snippets/contact-support.md"
