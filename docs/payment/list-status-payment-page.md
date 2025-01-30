---
title: Payment - Payment Messages and Status in 121
hide:
  - toc
---

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can perform actions in the Payment page.  
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

When performing a payment, 121 platform will notify the users on their actions through a certain number of updated status and messages. Here is the list and related explanations.

### Payment statuses in Payment page

The status will be updated automatically for integrated FSP when successful, or after manual reconciliation when the FSP has shared the payment reconciliation file back to your finance team and they have uploaded it to the 121 Platform.


| Type | Description | Actions required |
| :---- | :----------- | :----------  |
| **SUCCESSFUL** | The transaction has be sent to the PAs on the preferred payment method. The Bank approved the transaction.| None|
| **PENDING** | The transaction is being processed by the bank. Pending payment reconciliation. The status will be updated automatically for integrated FSP or by uploading the reconciliation data file (manual payment) | Check with the FSP, if integrated. For manual reconciliation, reconcile the data when the FSP shared the payment reconciliation file back to your finance team |
| **FAILED** | The transaction has failed. The beneficiaries have not received any cash payment. | Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. Contact our 121 Support Team if this remains unsolved. |


### People Affected statuses

| Type | Description | Actions required |
| :---- | :----------- | :----------  |
| **Registered** | beneficiaries have been registered into the program and is not yet included. | a CVA Manager or Officer needs to validate and include them in the program. |
| **Validated** | The beneficiaries details have been verified. Registration was validated by a CVA Manager or Officer. They are not yet included in the program and cannot receive payments.| a CVA Manager or Officer can include or decline the beneficiaries in the program. |
| **Included** | The beneficiaries were included in the program and can start receiving payment transfers via the 121 portal | A Finance Manager or Officer can select the beneficiaries in the next payment rounds.|
| **Declined** | The beneficiaries was found to be incorrectly registered or did not meet the criteria for inclusion in the program. The beneficiaries will not receive any payments.| No action required, unless the beneficiaries was wrongly declined. The beneficiaries can be re-included if necessary.|
| **Paused** | The beneficiaries are currently not being included in the distribution (payments are paused) but still part of the program. | The beneficiaries can be included or declined in the program depending on the SOPs. A Finance Manager can decide on the status update.|
| **Completed** | The beneficiaries have received the full amount of transfers. No other payments can be sent.|None. Unless additional payment rounds have been added to the program.|


-8<- "docs/_snippets/contact-support.md"
