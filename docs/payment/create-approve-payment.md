---
title: Create Approve and Start payments
hide:
  - toc
---

Payments are created and initiated from the **Payments** page. Each payment must first be approved by an approver before it can be started. Below are the three main steps to create, approve, and start a payment in your progam, before payment instructions are shared to the FSP.

- [1. Create a payment request](#1-create-a-payment-request)
- [2. Approve payments](#2-approve-payments)
- [3. Start payment](#3-start-payment)
- [4. Payment Instructions](#4-payment-instructions)

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can create and start payments.
    Approvers must be selected and added to each projects.
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

## 1. Create a payment request

To initiate a new payment request:

- On the top right, click **Create new payment** ![Create new payment button](../assets/img/PaymentsPage.png)
- A page will open displaying a list of beneficiaries **included** in the program.
  *Only beneficiaries with **Included** status who have not yet received all their installments will appear in the list. Beneficiaries who have received and completed all their payments will not be shown.* ![Select List](../assets/img/CreateNewpaymentSelect.png)
- **Select the list of beneficiaries to be added** to the payment round as follows.
    - Make an **individual selection** by clicking on the :material-checkbox-outline: on the individual beneficiary line;
    - Or do a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: on the upper table line **Select**
- On the bottom right, click **Add to payment**; ![Add to Payment](../assets/img/StartPayment.png)
- Confirm the payment information;
- Click on **Start payment**.

!!! Important "No change possible in the payment list"
    Once a payment is created, its details cannot be changed. This includes the list of people in the payment and the transfer value.
    Before creating a payment, make sure to carefully review the transfer value, budget, and selected beneficiaires. If needed, apply filters such as location or FSP and confirm your selection before proceeding.

    To change the transfer value before creating a payment, please refer to [Program settings & Budget](./settings/payment-budget-settings.md)

## 2. Approve payments

Once the payment request has been created, it must be approved by an approver.

!!! Important "All payment requests must be approved"
    One or multiple approvers must be added to the project in order to approve a payment. If no user has been assigned yet, please contact the 121 Support team.


- Go to the **payment page**,
- Click on payment cards with the message **XX of XX approved**
*In the transaction, you can review the list of beneficiaries included into the payment list, the total amount reserved and the total beneficiaires.*
- Based on this information, you can either approve or leave the payment. ![Approve or Cancel](../assets/img/ApprovePaymentFinal.png)
- If you agree, click on **Approve payment** button on the top right of the page. **The payment request status will be updated.**
- If you disagree, click on **Cancel**. *the payment will remain pending. We recommend getting in touch with the finance users*
- Once approved by all approvers, the payment request status will change from **Pending approval** to **Approved**

!!! Note "Approvers flow"
    Approvals happen in order, so each approver must approve the payment before the next one can. Once all approvals are completed, the payment request is valid and the payment can be started.

## 3. Start payment

Once the payment has been approved by all approvers in the list, the finance manager can **start the payment**.

- Enter the **approved** payment card,
- Click the **start payment** on the top right, ![Start Payment](./img/StartPaymentApproved.png)
- The payment will start,
- All payments status will change from **Approved** to **Processing**.

---

## 4. Payment Instructions

In the 121 Platform, payments can be processed in two different methods: with a **manual payment via a FSP portal** or with a **direct FSP integration**.

- For payment instructions with a manual export - import function, refer to the [Manual Payment instructions page](./issue-payment-fsp-portal.md). *Payment status will remain on **processing** until the reconciliation has been imported*,
- or payment instructions with an integrated Financial Service Provider, refer to the instructions on the [Payment with an integrated FSP page](./payment-integrated-fsp.md)

---

Below, the different payment statuses.

| Status | Description | Actions required |
| :------ | :----------- | :---------------- |
| **PENDING APPROVAL** | The payment request has been created but is still awaiting approval from all approvers. | Approvers must approve the payment to continue. |
| **APPROVED** | The payment request has been approved by all approvers. | The payment must be started to continue. |
| **SUCCESSFUL** | The payment have been sent to the Beneficiaries and they can now use it. | None. |
| **PROCESSING** | The payment is waiting for confirmation of one or more financial officers. The transfer is not yet sent to the Beneficiaries selected for this payment round or the reconciliation file has not been imported yet. | Import the reconciliation file into 121 Platform to update the status. |
| **FAILED** | The transaction has failed. The beneficiaries have not received any payments. | Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. You can try again. Contact our 121 Support Team if this remains unsolved. |

-8<- "docs/_snippets/contact-support.md"
