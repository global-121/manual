---
title: Payments - Instant payment with an integrated local FSP
hide:
  - toc
---

In the 121 Platform, payments can be processed in two different methods: with a **manual payment via an FSP portal** or with a **direct FSP integration**. Below, you will find the step-by-step instructions to **process an instant payment to the list of included registrations with a direct FSP integration**.

*For manual payments instructions via a FSP portal, please refer to the instructions on the [Manual Payment instructions (FSP portal) page.](./issue-payment-fsp-portal.md)*

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can perform actions in the Payments page.  
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

## Payments Overview

The Payments page in your program will display information about any completed installments or payment rounds. If no payments have been made yet, no details will appear. However, if some installments are already in progress, you will see each individual installment. **As long as payments are still being processed in the current program, you can add registrations to new payments.**

## Create new payment

- On the top right, click **Create new payment**.

![Create new payment button](../assets/img/PaymentsPage.png)

- A page will open displaying a list of registrations included in the program.
  *Only registrations with **Included** status who have not yet received all their installments will appear in the list. Registrations who have received and completed all their payments will not be shown.*

![Select List](../assets/img/CreateNewpaymentSelect.png)

- **Select the list of registrations to be added** to the payment round as follows.
    - Make an **individual selection** by clicking on the :material-checkbox-outline: on the individual registration line;
    - Or do a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: on the upper table line **Select**;
- On the bottom right, click **Add to payment**;

![Add to Payment](../assets/img/StartPayment.png)

- A window appears to confirm the number of registrations included and the total amount to be transferred;
- Click on **Start payment**. **This action will automatically process and send the payment request to the FSP after the approval flow.**

![Start Payment](../assets/img/StartPayment.png)

- Once the payment has been processed, a table will display the list of registrations included in the payment round with their respective payment statuses.

![Payment Board](../assets/img/PaymentReportBoard.png)

!!! info "Payment process timeframe"
    Once the payment has been processed in the 121 Platform, payment status with integrated FSP are updated instantly. In some cases, it can take a few minutes for the status to be updated (up to 1 hour) as the information needs to be processed from the FSP back to the 121 Platform. Updated payment reports will be available only then.
    Because the payment data is being processed on the server, you can keep using the 121 Platform after initiating a payment round.

---

## Payment status

The status will be updated automatically for integrated FSP.

| Type | Description | Actions required |
| :---- | :----------- | :---------- |
| **SUCCESSFUL** | The transaction has been sent to the registrations on the preferred payment method. The Bank approved the transaction. | None. |
| **PENDING** | The transaction is being processed by the bank. Pending payment reconciliation. The status will be updated automatically by the integrated FSP (successful or failed). | This can take sometimes a few hours. If this remains unchanged after 24 hours, please request an update to your FSP. Contact our 121 Support Team if this remains unsolved. |
| **FAILED** | The transaction has failed. The registrations have not received any payments. | Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. Contact our 121 Support Team if this remains unsolved. |

---

## Export payment reports

For financial audit and donor requirements, you can export the payment reports once this is completed. Follow the instructions on [this page.](../payment/payment-reporting.md)

!!! info "Payment Frequency"
    Disbursements can be executed at a certain frequency (daily, weekly, monthly or one-off payment). All payments in the 121 Platform must be triggered manually.

    Transfers are not sent automatically at a specific date. This allows the finance manager to review the availability of funds before a payment is issued to the registrations.


-8<- "docs/_snippets/contact-support.md"
