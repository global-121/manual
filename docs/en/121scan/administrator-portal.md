---
title: 121 Scan - Administrator Portal
hide:
  - toc
---

- [Link and configure your program in 121 Scan](#link-and-configure-your-program-in-121-scan)
- [Configure fields for verification](#configure-fields-for-verification)
- [Design and adjust the vouchers for your program](#design-and-adjust-the-vouchers-for-your-program)
- [Generate vouchers with(out) a QR code](#generate-vouchers-without-a-qr-code)
- [How to read the payment statuses in the 121 platform after using 121 Scan](#how-to-read-the-payment-statuses-in-the-121-platform-after-using-121-scan)

---

The 121 Scan Administrator Portal helps you configure 121 Scan and prepare your distribution. You will find four sections:

1. **Program configuration**: add and link a 121 program for the distribution.
2. **Verification field configuration**: select fields to display during the distribution so distribution staff can verify the beneficiary's identity when scanning the QR code.
3. **Design vouchers**: customize the vouchers to your program, such as adding the logo, program title, and description on the vouchers.
4. **Generate vouchers**: once a payment has been created in the 121 platform, you can automatically generate all vouchers and QR codes via this section.

---

## Link and configure your program in 121 Scan

In the Administrator Portal, go to **Program configuration**:

- Select the program in the dropdown list.
- Copy the Kobo form URL linked to your program.
- Save.

**How to find the Kobo form URL:**

- In your 121 program, go to **Settings > Registration data**, click on the Kobo configuration link, then copy and paste it.

---

## Configure fields for verification

During the distribution, distribution staff will see personal data to verify and confirm the beneficiary's identity. Your program may contain specific information to support the verification process. You can configure the display screen and the fields distribution staff will see in the **Verification field configuration** section.

On this page, you can also enable or disable the picture.

- Select the program at the top of the page.
- Click the left field and select the field to display from the dropdown list.
- You can edit the label in different languages in the fields on the right (2, 3, 4).
- You can select whether a field is read-only or editable. If you choose editable, distribution staff will be able to edit the field during distribution, and this field will be updated in the 121 platform.
- For each new field, click **+ Add a new field**.
- Finally, you can enable or disable the picture.

!!! Note "Display of picture: online vs offline"
    Pictures can only be displayed on the distribution staff screen when online; they cannot be displayed offline. If you expect the distribution to be held offline, we recommend not enabling the picture, but adding additional verification fields to help distribution staff identify beneficiaries.

    If you expect to use 121 Scan online and want to use the photo display, enable it. Supporting verification fields should still be added to complement the verification process alongside the picture and beneficiary personal information.

---

## Design and adjust the vouchers for your program

You can choose a different voucher design for each program distribution.

- Go to **Design vouchers**.
- Select the program at the top of the page.
- Follow the template and add the title.
- Add a description and 1 or 2 logos. These are optional.
- Enable or disable the display of a QR code.
- Check the preview and save.

The design can be updated at any time. If you have already printed the vouchers, you will need to print them again after the new design is saved.

---

## Generate vouchers with(out) a QR code

After a payment is created in the 121 platform, you can export your payment lists, adjust the Excel file, and automatically generate the QR code in the 121 Scan **Generate vouchers** section.

!!! Note "The voucher generator is a converter"
    The voucher generator converts your Excel file into a PDF. Therefore, all fields in your Excel file will be displayed on the vouchers. You can adjust, remove, or add columns in your Excel file accordingly. The payment Excel file can also be preformatted in the 121 platform, under **Program settings > FSP integration**. This information will be presented on the vouchers distributed to the beneficiary.

In the 121 platform:

- Go to **Program > Payment > Payment page**.
- Export the FSP payment list.
- Check your Excel file, and add or remove columns you want displayed on the vouchers. Note that the reference ID and amount are default columns and can be removed manually.

In the 121 Scan app:

- Go to **Administrator Portal > Generate vouchers**.
- Select the program at the top of your screen.
- Drag and drop your FSP payment list.
- Click **Import vouchers**.
- Click **Generate PDF**.
- A PDF file downloads. You can open the file and check the vouchers. This is ready to print.

---

## How to read the payment statuses in the 121 platform after using 121 Scan

121 Scan is mostly used for cash-in-hand distribution, and the logic for payment statuses is slightly different than for digital payments.

| Payment status | Description | Actions required |
| :--- | :--- | :--- |
| **Pending** | Beneficiaries need to receive their cash or cash out at the FSP agency. Payment statuses remain pending if no distribution has started, the beneficiaries have not picked up their cash yet, or sending the reconciliation via 121 Scan was not yet done. Pending statuses also remain if distribution staff scanned the QR code but selected "Decline payment" because the identity could not be verified — this means the beneficiary may have received the wrong QR code, and you may need to confirm the next steps with the distribution staff. | If the distribution has started, click **Send** to update the payment statuses. If the statuses remain pending after sending and the end of the distribution, beneficiaries have not picked up their cash yet. You may want to follow up with the distribution staff or beneficiaries directly. |
| **Successful** | Beneficiaries have picked up their cash; the QR code was scanned, and the distribution staff has sent the payment reconciliation via 121 Scan. | No further action needed. |
| **Failed** | This status is not used. Since physical distribution or cash-in-hand is used with 121 Scan, it is unlikely that a distribution has failed — it is either picked up or still pending. | No further action needed. |

---

-8<- "docs/en/_snippets/contact-support.md"
