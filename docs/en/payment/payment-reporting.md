---
title: Payments - Financial reporting and activity
hide:
  - toc
---

Audit trail can be performed in 121 for financial reporting and data changes overview at a general or individual level. The Payments page in your program will display information about any completed installments or payment rounds. If no payments have been made yet, no details will appear. However, if some installments are already in progress, you will see each individual installment.

!!! Important "Who can perform actions in this page?"
    Only the Finance Manager can download the **Payment report** of a payment. Users who can see the Payments page can also view the **Payment log** of each payment. The exports on the Payments page itself need extra permissions; see the notes below. [Learn more about Roles & Permissions](../users/description-roles.md)

## Download the General financial reporting

To export a general financial report:

1. Go to **Payments page**
2. On the top right, click on **Export**
3. Select **Payments** ![Payment Export Report](../assets/img/PaymentsPage.png)
4. In the **Export payments** pop-up window, optionally select a **Start Date** and/or an **End Date** to filter the payments
5. Click on **Proceed**. **This will download an Excel file with all of the registrations included in payments** ![Confirm Export](../assets/img/ApprovePaymentExport.png)
  The file will be exported into the download folder as an Excel file.

!!! Important "Who sees the Export button on the Payments page?"
    The **Export** button on the Payments page is only shown to users who have both the permission to export registration data with personal information and the permission to export payment data. The **Payments** option also needs at least one payment in the program.

    None of the standard roles has both permissions: the CVA Manager can export registration data, and the Finance Manager can export payment data. With the standard roles, you will therefore not see **Export** > **Payments**. A Finance Manager can download the data of each payment with the **Payment report** (see below).

!!! Info "TIPS: Only download Excel files when required and delete after exporting / using"
    Excel files should only be downloaded when required to ensure personal data is kept secure. After use, Excel files should be deleted from your computer to keep personal data secure and prevent mistakes using old files. This way, you will always have the latest updated data in 121.

---

## Download specific financial reporting

To export a specific financial report based on a specific date:

1. Go to **Payments page**;
2. Enter the specific payment round you are looking for;
3. On the top right, click on **Export** ![Individual Export Report](../assets/img/IndividualExportReport.png)
4. Select **Payment report**;
5. A pop-up window will request confirmation to proceed.**You're about to download an Excel file with all of the registrations included in this payment.**;
  The file will be exported into the download folder as an Excel file.

---

## Other exports on the Payments page

Depending on the FSPs of your program, the **Export** menu on the Payments page has more options. They only appear when the program has at least one payment.

| Option | When it appears | What you download |
| ---- | ---- | ---- |
| **Unused vouchers** | The program uses Albert Heijn vouchers (paper or WhatsApp). | An Excel file with all unused vouchers. The data is not real-time: the file shows the date and time of each voucher's last update. |
| **Debit card usage** | The program uses Visa debit cards. | An Excel file with the balance of every card. The data is not real-time: the file shows the date and time of each card's last update. |
| **Refunded debit cards** | The program uses Visa debit cards. | An Excel file with all refunded debit cards, that is cards that were closed and whose balance was booked back. |

To download one of these files:

1. Go to **Payments page**
2. On the top right, click on **Export**
3. Select the option
4. Click on **Proceed**

!!! Note "Permissions for these exports"
    Each of these options needs its own export permission, which none of the standard roles has. The 121 support team can add it to a role. Because the options are in the same **Export** menu, you also need the permissions for the **Export** button described above.

---

## Payment log

Each payment page has two tabs: **Transaction list** and **Payment log**. The **Payment log** shows what happened to the payment: when it was created, approved, started, retried or renamed, and the notes added to it.

1. Go to **Payments** page;
2. Click on the payment you want to check;
3. Click on the **Payment log** tab.
   For each event, the table shows the **Activity**, an **Overview**, who did it (**Done by**) and the **Date and time**. ![Payment log tab of a payment](../assets/img/PaymentLog.png)

---

## Oversee the Activity Log in Payments Page

Detailed payment information can be found in each separate installment and for each registration. To access the Individual overview:

1. Go to **Payments** page;
2. Click on one of the installments you would like to read further details.
   The included list of registrations with detailed information about the transfer value, the payment statuses, FSP and dates will be shown.
3. For further details per individual, you can click on the hyperlink **reg. #** on the registration profile. You can read the activity log from different phases (registration, inclusion, payments).
4. In the Activity Log, any changes or activities will be automatically logged, including payment details.

**How to read the logs in the Activity Log?**

| Category | Description |
| ---- | ---- |
| **Data change** | The log will show **Data Changes** followed by the value or field name that was edited, the **old status** and the **new status**, as well as the 121 user account performing the change. |
| **Transaction** | The log will show the **payment date and time**, the **payment status** (successful, approved, pending approval, failed) and the 121 user account executing the payment. In the dropdown, the transaction date, approver details, transfer value, and FSP name will be indicated. For Albert Heijn vouchers, the dropdown also shows the **Current balance** of the voucher, with a **View voucher** button. Click it to see the voucher, then click **Download** or **Print voucher**. |
| **Message** | The log will show the **message template title**, the sending date, the sending status, the message content and the 121 user account performing the action. |
| **Status Update** | The log will show the **Status update**, the date and time, the **old** and **new status** and the 121 user account performing the status update. |
| **Notes** | The log will show the **notes** history, the date and time, the content and the 121 user account adding the notes into the Registration profile. A note can be added manually by clicking on **Actions** and then **Add note** (right side). |

---

-8<- "docs/en/_snippets/contact-support.md"
