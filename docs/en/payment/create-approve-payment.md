---
title: Payments - Create Approve and Start payments
hide:
  - toc
---

Payments are created and initiated from the **Payments** page. Each payment must first be approved by an approver before it can be started. Below are the main steps to create, approve, and start a payment in your program. This page also explains how to process a payment, interpret the payment statuses and how to delete a payment.

- [1. Create a payment request](#1-create-a-payment-request)
- [2. Approve payments](#2-approve-payments)
- [3. Start payment](#3-start-payment)
- [4. Delete payment](#4-delete-payment)
- [5. Rename payment](#5-rename-payment)
- [6. Payment Instructions](#6-payment-instructions)

!!! Important "Who can perform actions in this page?"
    CVA Manager and Finance Manager can create and delete payments. Approving does not depend on a role: only the team members set as approvers for the program can approve. Only the Finance Manager can start and rename payments. [Learn more about Roles & Permissions](../users/description-roles.md)

## 1. Create a payment request

To initiate a new payment request:

- On the top right, click **Create new payment** ![Create new payment button](../assets/img/PaymentsPage.png)
- Enter a name for the payment. A name is prefilled (*Payment dd/mm/yy, hh:mm*); you can change it if needed. Click **Continue to registration**.
- A page will open displaying a list of registrations **included** in the program.
  *Only registrations with **Included** status who have not yet received all their installments will appear in the list. Registrations who have received and completed all their payments will not be shown.* ![Select List](../assets/img/CreateNewpaymentSelect.png)
- **Select the list of registrations to be added** to the payment round as follows.
  - Make an **individual selection** by clicking on the :material-checkbox-outline: on the individual registration line;
  - Or do a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: on the upper table line **Select**
- On the bottom right, click **Add to payment**; ![Add to Payment](../assets/img/StartPayment.png)
- Review the summary (Financial Service Provider(s), Registrations and Total payment amount) and add a note if needed;
- Click on **Create payment**. You will land on the payment page.

!!! Important "No change possible in the payment list"
    Once a payment is created, its details cannot be changed. This includes the list of people in the payment and the transfer value.
    Before creating a payment, make sure to carefully review the transfer value, budget, and selected registrations. If needed, apply filters such as location or FSP and confirm your selection before proceeding.

!!! Important "Resolve duplicates before you create, approve or start a payment"
    Registrations marked as **Duplicate** block payments:

    - You cannot create a payment if your selection contains duplicate registrations. Remove them from the selection or resolve them first.
    - You cannot approve or start a payment that contains duplicate registrations. The portal shows an error with the number of duplicates.

    On the payment page, the **Transaction list** has a **Duplicates** column that shows which registrations are duplicates. To resolve duplicates, see [Deduplication](../registration/registration-deduplication.md).

## 2. Approve payments

Once the payment request has been created, it must be approved by an approver.

- Go to the **payment page**,
- Click on payment cards with the message **XX of XX approved**
*In the transaction, you can review the list of registrations included in the payment list, the total amount reserved and the total registrations.*
- Based on this information, you can either approve or leave the payment. ![Approve or Cancel](../assets/img/ApprovePaymentFinal.png)
- If you agree, click on **Approve payment** and confirm in the pop-up window. **The payment request status will be updated.** *Only users assigned as approver for this payment can approve it.*
- If you disagree, click on **Cancel**. *The payment will remain pending. Based on your SOP, inform your relevant colleagues for follow-up.*
- Once approved by all approvers, the payment request status will change from **Pending approval** to **Approved**

!!! Note "Approvers flow"
    Approvals are based on thresholds. This is the minimum amount at which this approval is required. At least one approver with threshold 0 is needed to ensure all payments are approved. You can assign multiple users to the same threshold and require only one of them to approve (e.g., the first to log in). Approvers must be assigned to the program without a scope. Email notifications to the approver(s) and payment creator are automated and include a link to the payment page.

    If no user has been assigned yet or you want to change the setup, please refer to the instructions on [Payment approval](../settings/payment-approval.md)


## 3. Start payment

Once the payment has been approved by all approvers in the list, the Finance Manager can **start the payment**.

- Enter the **approved** payment card,
- Click **Start payment** on the top right, ![Start Payment](../assets/img/StartPaymentApproved.png)
- The payment will start,
- All payments status will change from **Approved** to **Processing**.

---

## 4. Delete payment

The CVA Manager and the Finance Manager can delete payments. You can delete a payment as long as it has not been started (status **Pending approval** or **Approved**).

- Click the :material-dots-horizontal: next to the export button at the top right of the page,
- Click **Delete payment**,
- Deleting a payment does not affect the registrations’ status (included) or their received number of payments.

---

## 5. Rename payment

Only the Finance Manager can rename payments. You can rename the payment at any time.

- Navigate to the Payments page,
- Select the payment you wish to rename,
- Click the :material-dots-horizontal: next to the export button at the top right of the page,
- Click 'Rename payment'.

---

## 6. Payment Instructions

In the 121 platform, payments can be processed in two different methods: with a **manual payment via an FSP portal** or with an **FSP configuration**.

- For payment instructions with a manual export - import function, refer to the [Manual Payment instructions page](./issue-payment-fsp-portal.md). *Payment status will remain on **processing** until the reconciliation has been imported*,
- or payment instructions with an integrated Financial Service Provider, refer to the instructions on the [Payment with an integrated FSP page](./payment-integrated-fsp.md)

---

Below, the different payment statuses.

| Status | Description | Actions required |
| :------ | :----------- | :---------------- |
| **PENDING APPROVAL** | The payment request has been created but is still awaiting approval from all approvers. | Approvers must approve the payment to continue. |
| **APPROVED** | The payment request has been approved by all approvers. | The payment must be started to continue. |
| **SUCCESSFUL** | The payment has been sent to the Registrations and they can now use it. | None. |
| **PROCESSING** | The payment has been started and the transfer has been sent to the FSP. The 121 platform is waiting for the result from the FSP (integrated FSP) or for the reconciliation file to be imported (manual payment via an FSP portal). | For a manual payment, import the reconciliation file into the 121 platform to update the status. For an integrated FSP, the status is updated automatically. |
| **FAILED** | The transaction has failed. The registrations have not received any payments. | Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. You can try again. Contact our 121 Support Team if this remains unsolved. |

-8<- "docs/en/_snippets/contact-support.md"

