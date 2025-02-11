---
title: Payments - Manual payment via the FSP portal (excel export)
hide:
  - toc
---

In the 121 Platform, payments can be processed in two different methods: with a **manual payment via a FSP portal** or with a **direct FSP integration**. Below, you will find the step-by-step instructions to **process the manual payment via a FSP portal**, to export the payment instructions and reconcile payments into your program.

*For payments instructions with an integrated Financial Service Provider, please refer to the instructions on the [Payment with an integrated FSP page](./payment-integrated-fsp.md)*

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can perform actions in the Payments page.  
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

### Payments Overview

The Payments page in your program will display information about any completed installments or payment rounds. If no payments have been made yet, no details will appear. However, if some installments are already in progress, you will see each individual installment. **As long as payments are still being processed in the current program, you can add beneficiaries to new payments.**

### Create a new payment

To initiate a new payment:

- On the top right, click **Create new payment**

![Create new payment button](../assets/img/PaymentsPage.png)

- A page will open displaying a list of beneficiaries included in the program.
  *Only beneficiaries with **Included** status who have not yet received all their installments will appear in the list. Beneficiaries who have received and completed all their payments will not be shown.*

![Select List](../assets/img/CreateNewpaymentSelect.png)

- **Select the list of beneficiaries to be added** to the payment round as follows.
    - Make an **individual selection** by clicking on the :material-checkbox-outline: on the individual beneficiary line;
    - Or do a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: on the upper table line **Select**
- On the bottom right, click **Add to payment**;

![Add to Payment](../assets/img/StartPayment.png)

- A window appears to confirm the number of beneficiaries included and the total amount to be transferred;
- The portal will display guidelines on the left side of your screen for exporting the FSP payment instructions (as shown below).
- Click on **Start payment**. **This action will NOT automatically process or send the payment request to the FSP. However, it will prepare the payment instructions, including the list of beneficiaries set to receive payments.**

Once the payment has been processed, **remain on the payment page you just worked on**. From there, you can download the payment instructions. You will see all pending payments for registrations that have opted to receive cash aid through the FSP via manual import-export (Excel).

### Export the payment instructions

![Pending Statuses Excel](../assets/img/PendingStatusExcel.png)
The file will provide the necessary instructions for the FSP to issue the payments.

- On the top right of your **page**, go into the **Payment data** dropdown list;
- Click on **Export** and select the **Export FSP payment list**;
- The file will be available in your downloaded folder;
- Review the file if required. *Based on your agreement with the FSP, share the file to your FSP or import it into the FSP portal (if available).*

The payment status displayed in the payment page will be updated depending on the payment phase. For Manual Payment, the default message will be **PENDING** until the payment reconciliation has been processed.
![Export FSP payment list](../assets/img/IndividualExportReport.png)
!!! info "Payment instructions excel template"
    Each program may require a different template depending on the FSP you work with in the region of your operations. Our Team will create a template specifically adapted to upload into each FSP portal.

    The payment instructions excel file should only contain the criteria needed for the FSP to confirm the beneficiaries' identity and issue the payments, such as names, phone number and ID number or any other criteria based on your program SOPs. For data privacy, we recommend to only export the minimum criteria to verify the beneficiary identity. All other irrelevant data for the payment process should be excluded from the payment instructions file. After usage the exported data should be deleted to ensure personal data is kept secure.

---

### Reconcile payments in 121 platform

Once the FSP shared the reconciliation data file to you, you can reconcile payments in the 121 Platform. This will update the payment status by uploading the file in the **specific payment page**.

!!! important "Format the reconciliation file"
    Before importing the reconciliation file, ensure it meets the required format. You can download the template by clicking Import reconciliation data and selecting the template. Make sure all required columns are included, and adjust the statuses as follows:

      - **Completed** → success
      - **Failed** → error
      - **Pending** → waiting

    The file must be in .csv format. Follow the instructions [in this page](./manual-payment-reconciliation.md)

To update the payment statuses:

- Go to the payments page for the selected date and payment that match the file;
- On the top right of your page, click on **Import reconciliation data**.
  
![Export FSP payment list](..\assets\img\IndividualExportReport.png)

- Click on the import button to upload the FSP file, *the file must be in .csv format*;
- **Drag and drop** the file; or use the **Choose file** function;
- Click on **Proceed**. The beneficiaries status will be updated according to whether the transfer was marked as Successful, Pending or Failed by the FSP.
![Export FSP payment list](../assets/img/IndividualExportReport.png)

---

### Payment status

![Reconciliation Data Import](../assets/img/ReconciliationImport.png)
The payment status displayed in the payment page will be updated depending on the payment phase. For Manual Payment, the default message will be **PENDING** until the payment reconciliation has been processed.

Below, the different payment statuses.

| Status | Description | Actions required |
| :------| :-----------| :----------------|
| **SUCCESSFUL** | The transfer have been sent to the Beneficiaries or Household and they can now use it. | None.|
| **PENDING** | The payment is waiting for approval of one or more financial officers. The transfer is not yet sent to the Beneficiaries or Household selected for this payment round. | Import the reconciliation file into 121 Platform to update the status |
| **FAILED** | The transaction has failed. The beneficiaries have not received any payments.| Please check the error message provided by your bank. Failed payment can be due to wrong bank details, phone number or ID number depending on the chosen payment methods. You can try again. Contact our 121 Support Team if this remains unsolved.|

!!! info "Manual payment reconciliation"
    Once the FSP share back the payment data, you can process the manual payment reconciliation in the 121 platform.
    Follow the instructions on [this page](./manual-payment-reconciliation.md)

-8<- "docs/_snippets/contact-support.md"
