---
title: Create Approve and Start payments
hide:
  - toc
---

Payments are created and initiated from the **Payments** page. Each payment must first be approved by an approver before it can be started. Below are the three main steps to create, approve, and start a payment in your progam, before payment instructions are shared to the FSP.

- [1. Create a payment request](#1-create-a-payment-request)
- [2. Approve payments](#2-approve-payments)
- [3. Start payment](#3-start-payment)
- [4. Delete payment](#4-delete-payment)
- [5. Payment Instructions](#5-payment-instructions)

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can create and start payments. Approvers must be selected and added to each programs.
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

## 1. Create a payment request

To initiate a new payment request:

- On the top right, click **Create new payment** ![Create new payment button](../assets/img/PaymentsPage.png)
- A page will open displaying a list of registrations **included** in the program.
  *Only registrations with **Included** status who have not yet received all their installments will appear in the list. Registrations who have received and completed all their payments will not be shown.* ![Select List](../assets/img/CreateNewpaymentSelect.png)
- **Select the list of registrations to be added** to the payment round as follows.
    - Make an **individual selection** by clicking on the :material-checkbox-outline: on the individual registration line;
    - Or do a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: on the upper table line **Select**
- On the bottom right, click **Add to payment**; ![Add to Payment](../assets/img/StartPayment.png)
- Confirm the payment information;
- Click on **Create payment**.

!!! Important "No change possible in the payment list"
    Once a payment is created, its details cannot be changed. This includes the list of people in the payment and the transfer value.
    Before creating a payment, make sure to carefully review the transfer value, budget, and selected registrations. If needed, apply filters such as location or FSP and confirm your selection before proceeding.

    To change the transfer value before creating a payment, please refer to [Program settings & Budget](../Settings\payment-budget-settings.md)

## 2. Approve payments

Once the payment request has been created, it must be approved by an approver.

- Go to the **payment page**,
- Click on payment cards with the message **XX of XX approved**
*In the transaction, you can review the list of registrations included in the payment list, the total amount reserved and the total registrations.*
- Based on this information, you can either approve or leave the payment. ![Approve or Cancel](../assets/img/ApprovePaymentFinal.png)
- If you agree, click on **Approve payment**. **The payment request status will be updated.**
- If you disagree, click on **Cancel**. *The payment will remain pending. Based on your SOP, inform your relevant colleagues for follow-up.*
- Once approved by all approvers, the payment request status will change from **Pending approval** to **Approved**

!!! Note "Approvers flow"
    Approvals are based on thresholds. This is the minimum amount at which this approval is required. At least one approver with threshold 0 is needed to ensure all payments are approved. You can assign multiple users to the same threshold and require only one of them to approve (e.g., the first to log in). Approvers must be assigned to the program without a scope. Email notifications to the approver(s) and payment creator are automated and include a link to the payment page.

    Currently, approvers and their respective thresholds are set per program by the 121 team. If no user has been assigned yet or you want to change the setup, please share the names, order, and amounts with the support@121.global.


## 3. Start payment

Once the payment has been approved by all approvers in the list, the finance manager can **start the payment**.

- Enter the **approved** payment card,
- Click the **start payment** on the top right, ![Start Payment](../assets/img/StartPaymentApproved.png)
- The payment will start,
- All payments status will change from **Approved** to **Processing**.

---

## 4. Delete payment

-	You can delete payments that are pending approval. Click the :material-dots-horizontal: next to the export button at the top right of the page.
-	Deleting a payment does not affect the registrations’ status (included) or their received number of payments.
-	Users who can create payments also have permission to delete.
---

## 5. Payment Instructions

In the 121 Platform, payments can be processed in two different methods: with a **manual payment via a FSP portal** or with a **direct FSP integration**.

- For payment instructions with a manual export - import function, refer to the [Manual Payment instructions page](./issue-payment-fsp-portal.md). *Payment status will remain on **processing** until the reconciliation has been imported*,
- or payment instructions with an integrated Financial Service Provider, refer to the instructions on the [Payment with an integrated FSP page](./payment-integrated-fsp.md)

---

Below, the different payment statuses.

| Status | Description | Actions required |
| :------ | :----------- | :---------------- |
| **PENDING APPROVAL** | The payment request has been created but is still awaiting approval from all approvers. | Approvers must approve the payment to continue. |
| **APPROVED** | The payment request has been approved by all approvers. | The payment must be started to continue. |
| **SUCCESSFUL** | The payment has been sent to the Registrations and they can now use it. | None. |
| **PROCESSING** | The payment is waiting for confirmation of one or more financial officers. The transfer is not yet sent to the Registrations selected for this payment round or the reconciliation file has not been imported yet. | Import the reconciliation file into 121 Platform to update the status. |
| **FAILED** | The transaction has failed. The registrations have not received any payments. | Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. You can try again. Contact our 121 Support Team if this remains unsolved. |

-8<- "docs/_snippets/contact-support.md"
