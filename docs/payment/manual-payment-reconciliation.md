---
title: Payment - Manual payment reconciliation
hide:
  - toc
---
In the 121 Platform, payments can be processed in two different methods: with a **manual payment via a FSP portal** or with **a direct FSP integration**. Below, you will find the step-by-step instructions to import the **manual reconciliation data** into the program, once you have received the payment instructions back from the FSP.

*For payments instructions with an integrated Financial Service Provider, please refer to the instructions on the [Payment with an integrated FSP page](../payment-integrated-fsp.md)*

!!! Important "Who can perform actions in this page?"
    Finance Manager and Finance Officer roles can perform actions in the Payments page.  
    Additional users may be granted only **View** permission on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

Before dowloading the reconciliation file into the 121 platform, there are a few steps you should follow so to adjust the file to the 121 platform.

### Download the reconciliation file template

Go to the Payments page, and enter the specific payment round you would like to update.

- On the top right, click on **Import Reconciliation data** ![Import Reconciliation data](../assets/img/IndividualExportReport.png)
- In the pop-up window, you can read in the first sentence *Import the file sent by the FSP to see the transfer status of the registrations included in this payment. Download the template .*
- Click on the **Donwload the template** ![Download Reconciliation template](../assets/img/ReconciliationImport.png)
- You can now start editing this file with the requested value, as follows.

### Check the reconciliation data file

A few labels that must be adjusted according to the 121 platform. This relates to the payment statuses.
The below table indicate the correct label names that must be filled in the payment status of your reconciliation data. The FSP may write the statuses differently than the 121 Platform. Therefore, you should overwrite the status with the data indicated in the below table, column **121 Data status**, in your reconciliation data file (excel):

| 121 Data Status | Description |
| :---- | :---- |
| **success** | Successful, completed or confirmed payments |
| **waiting** | Payments is pending. It is not distributed yet or cannot be sent yet. |
| **error** | Failed payments, not received by beneficiaries due to wrong data shared or error at the FSP. |


If these labels are not correctly matching, three errors can occur in the 121 Platform:

- An *error message** appear to warn the data cannot be uploaded;
- **Payment statuses are not correctly updated**, showing more failed or waiting payments as the system cannot match the status with the imported file;
- The **format is not recognized** in the platform and shows an error page.

*Some data may be specific to your FSP, our team will advice you when implementing your 121 instance.*

---

### Format your file in .csv

Once your labels are updated, you can save the file as a .csv format:

- Click on **Save File** in your file;
- Add a file name, if required;
- Select **.csv** format in the dropdown list;
- **Save**

### Import the reconciliation file

Once your updated file is ready and saved as a .csv format, you can import the payment reconciliation file:

- Go to **Payments** and select the specific payment to be reconciled.
- Click **Import reconciliation data** ![Import Reconciliation data](../assets/img/IndividualExportReport.png)
- **Drag and drop** or **choose a file**
- Click on **Import file** ![Import reconciliation file](../assets/img/ReconciliationImport.png)

!!! info "Payment statuses"
    All beneficiaries payment statuses will be updated in the specific payment round. You can then overview the number of successful, waiting and failed payments within the beneficiaries list. Read more about the payment statuses in [this page](./list-status-payment-page.md)

-8<- "docs/_snippets/contact-support.md"
