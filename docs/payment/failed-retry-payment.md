---
title: Payment - Failed and retry payments
hide:
  - toc
---

When processing the payments, the statuses will be updated with **Successful**, **Pending** and **Failed**.
Below, you will find the step-by-step instructions to understand the reasons of **failed payments** and retry payments.

*For payment statuses description, please refer to this [page listing the statuses.](./list-status-payment-page.md)*

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can perform actions in the Payments page.  
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

### Reasons for failed payments

Failed payments occur due to an error in data. Depending on how the payment is processed in your instance, you may look at different errors. Your Financial Service Provider(s) should share the reasons for the payment to fail together with the reconciliation data.

To filter the beneficiaries with failed payments:

- Navigate to the specific payment;
- In the beneficiary list beneath the graph, click on **Transfer status** column filter and select **Failed**;
- The table will display all failed payments;
- You can view the reason in the column **Fail reason**

![Failed Payment](../assets/img/FailedPaymentstatus.png)


**1. Incorrect payment details**
    For both manual and automatic payments, The KYC required may be incorrect and cannot match the information required by the FSP to process the payment. The incorrect details can be as follows: Full name, Phone numbers, Bank account number, Id number and/or Location.

Once you have identified the incorrect data, you can **request your CVA manager or CVA officer to correct the information within the beneficiary's profile**. To further read on the instructions, visit [this page.](../registration/edit-pa-profile.md)


**2. Wrong format of the reconciliation file**
    For manual payment, the imported reconciliation file may not be formatted correctly. The data cannot match within the platform. Check the instructions on formatting your [manual reconciliation file.](./manual-payment-reconciliation.md)


**3. Beneficiary changed their payment details**
    If a failed payment occurs despite the beneficiary having successfully received payments in the past, it may be due to a change in their payment details or phone number. As a result, the Financial Service Provider (FSP) may be unable to match and process the payment.

Once you have identified the incorrect data, you can **request your CVA manager or CVA officer to correct the information within the beneficiary's profile**. To further read on the instructions, visit [this page.](../registration/edit-pa-profile.md)


**4. Updating payment between FSP-121 is failing**
    If your instance is integrated with an FSP, the integration may encounter issues. Please contact the 121 Support Team to verify if this can be due to an integration error.

---

### Retry failed transfers

Once you have identified the reason, you can proceed with retrying the payments:

- Go to the **Payments** page and enter the specific payment round;
- Click on the button :material-refresh: **Retry failed transfers** highlighted on the top right of your beneficiaries' list;

  ![Retry Payment button](../assets/img/RetryPaiementbutton.png)

- **Approve** the action.

![Approve the payment retry](../assets/img/RetryPaymentConfirm.png)

- The transaction will be automatically retried for beneficiaries identified with a **failed payment** status;
- The payment status will be updated.

!!! import "Retry based on your payment methods"
    If you are processing the payment with an integrated FSP, the payment request and reconciliation will be done automatically.

    However, **if you are processing the payments with a manual export-import**, please follow the same steps again. Further instructions can be read on [the manual payment page](../payment/issue-payment-fsp-portal.md)

---

**What if payments remain failing?**

We recommend getting in contact with our support team to verify the reasons of payment failing together with your finance team. We will provide guidance in the next steps.

-8<- "docs/_snippets/contact-support.md"
