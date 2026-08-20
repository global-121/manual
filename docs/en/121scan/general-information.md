---
title: 121 Scan - General Information
hide:
  - toc
---

- [What can you use 121 Scan for?](#what-can-you-use-121-scan-for)
- [How does 121 Scan work with the 121 platform?](#how-does-121-scan-work-with-the-121-platform)
- [Data security](#data-security)
- [Prerequisites for using 121 Scan](#prerequisites-for-using-121-scan)
- [Using 121 Scan for personal verification](#using-121-scan-for-personal-verification)
- [Using 121 Scan to update information in 121](#using-121-scan-to-update-information-in-121)

---

121 Scan is an offline app built by the 510 (The Netherlands Red Cross). It can automatically create beneficiary cards with QR codes for each person in a program. Staff then open 121 Scan on a phone, tablet, or laptop, scan that QR code (or type in the person's unique code), and it shows information about the person the code belongs to. For example, their name, photo, and any other details the program has chosen to display. Staff can then confirm whether the person is who they say they are, add or edit information in their 121 registration, and record that a transaction was done.

121 Scan does **not** replace the 121 platform; it works alongside 121. Think of it as a field tool that talks to 121 in the background, so that staff working at a distribution site, who may not have their own 121 account or a reliable internet connection, can still perform verification and payment actions. The 121 Scan application later synchronizes with the 121 platform, using an internet connection.

!!! Info "121 Scan is a tool that keeps evolving"
    It was built to solve specific problems in the field while a permanent solution is developed inside 121 itself. It is currently only used in a small number of pilot contexts. If you want to know more, talk to your Account Manager and see [**Onboarding and Support**](./distribution-staff-portal.md#onboarding-and-support) on the Distribution Staff Portal page.

---

## What can you use 121 Scan for?

121 Scan is useful in situations where distributions on site are organized, such as for cash in hand or pre-paid cards, and the standard 121 payment workflow may not suit all needs. For example, because there is no internet connection, or because the Financial Service Provider (FSP) handling the cash does not have direct access to 121. It can help with:

- **Verifying who someone is**, by scanning a QR code / entering a unique code and showing their photo and details, instead of relying only on paper lists or asking people to prove their identity another way.
- **Letting an FSP take part in the payment process** without giving them access to the 121 platform or sharing additional Excel files: they only see the information they need to do their job.
- **Recording missing details on the spot**, such as a card or SIM number that a person only receives at the moment of distribution, so it doesn't have to be written down on paper and entered into 121 later.
- **Updating transaction statuses automatically with a synchronization to the 121 platform payment**, so staff don't have to reconcile a paper list or spreadsheet manually against 121 afterwards.

---

## How does 121 Scan work with the 121 platform?

121 Scan sits between 121 and the field. It does not store or own any data permanently on your device: it borrows information from 121 (and sometimes Kobo) for as long as it's needed in the field and sends the results back to 121 as soon as the user clicks **Send** when they have an internet connection.

Two groups of people use it, with access to 2 different portals:

- **Red Cross staff** log in as "Administrator" to connect 121 Scan to the right 121 program, choose which details the FSP is allowed to see (if involved in 121 Scan), and generate the QR codes or vouchers that will be scanned.
- **The FSP or Red Cross staff** log in as "Distribution Staff" to scan people's codes at the distribution site and record what happens.

### The cash journey, and where 121 Scan fits in

The diagram below shows a typical cash journey through 121, and the points where 121 Scan comes in. The exact steps can look slightly different between programs, for example whether people receive a printed voucher, a prepaid card, or a SIM card, but the overall flow is the same.

![The standard cash journey through 121, and where 121 Scan is used.](../assets/img/121Scan-CashJourney.png)

**1. Set up in 121.** As with any cash program, people are registered, checked, and included in the program. A payment is created and approved in 121.

**2. Get 121 Scan ready.** A staff member exports the payment list from 121 into 121 Scan in the Administrator Portal, configures what information the FSP will be shown, and generates a QR code or printed voucher for each person in PDF format.

**3. At the distribution site.** Before the distribution on site, and while an internet connection is available, the FSP or RC staff has to log in via the Distribution Staff Portal, select the correct program they are working on, and sync their device, so that it will work offline. Once the data is synchronized, they then scan each person's code with 121 Scan. This works even without an internet connection. They check the person's identity and, depending on the program, may also add details to their registration information and record the transaction status (successful/failed). (See [**Using 121 Scan for personal verification**](#using-121-scan-for-personal-verification) below for the exact steps.)

**4. Back to 121.** As soon as the device is online again, the FSP sends all the information it collected to 121, including the transaction statuses and updated registration information. This closes the loop and supports reconciliation, without extra manual work. The payment statuses in the selected program are updated in the 121 platform.

---

## Data security

121 Scan is used on ordinary phones, tablets, and laptops in the field, so it's built to keep information safe even if a device is lost or stolen:

- **Nothing is stored permanently.** 121 Scan only holds a working copy of that day's list and clears it once results are sent back to 121.
- **That working copy is fully encrypted** and can only be unscrambled by 121 Scan itself, so a lost or stolen device exposes no personal information.
- **Access is scoped.** FSPs only see the details they need (set by an administrator), and voucher/export access is limited to each staff member's own program and area.

121 Scan doesn't keep a separate permanent record; 121 remains the one source of truth. Report a lost or stolen device to your IM focal point right away, so any unsent data can be accounted for.

!!! Important "Data loss if a device is damaged or stolen before sending"
    Although this case remains limited, because the app works offline and on local devices, it is important to know that if the device is damaged or stolen, all data that has not been sent yet — via the **SEND** button — will be lost. Therefore, we recommend discussing with our CVA IM Team so we can share a few best practices to adopt for your distribution with 121 Scan.

---

## Prerequisites for using 121 Scan

Before using 121 Scan in a program, make sure you have:

- A smartphone, tablet, or laptop with a camera and a reasonably up-to-date browser (Chrome, Safari, Firefox, or Edge). It runs inside the browser, nothing to install; very old devices may run it slowly.
- An internet connection (Wi-Fi, mobile data, or satellite such as Starlink) to **Sync** before you start and **Send** once you're done. This is, however, not needed while actually scanning the QR code.
- A 121 user account with the correct program selected.
- Enough free storage for that day's list and photos; a long, photo-heavy list takes longer to sync, so do this on a decent connection.
- Current pilots are typically set up for one FSP at a time.

!!! Important "Testing your devices before a live distribution"
    It is good practice to do some tests before a live distribution. We recommend testing the 121 Scan app (Android) or browser on the device that you will be using during the distribution. For a successful test, request the 121 support team to plan a test session with you. We will 1) advise on the program to test, 2) add as many registrations as planned for your distribution, 3) log in to the 121 Scan web app via the link on your device, and 4) synchronize and troubleshoot any connection issues. This step is crucial: if it is not tested properly before a live distribution, this may impact your experience in the field. **Do not skip this step!**

---

## Using 121 Scan for personal verification

The most common use of 121 Scan is confirming that the person standing in front of an FSP is really the person entitled to the payment. Both the RC Staff and FSP agents can use the Distribution Staff Portal.

- Before the day starts, while still online, the FSP logs in as "Distribution Staff", selects the correct program, and taps **Sync**.
- The distribution staff opens 121 Scan and taps **Scan**.
- They point the camera at the person's QR code, printed on a voucher or card. If the code is damaged or can't be read, its reference number can be typed in the reserved field instead (see [**Allowing camera access on your device**](./distribution-staff-portal.md#allowing-camera-access-on-your-device) if the camera won't open).
- 121 Scan shows the person's details: usually a photo, name, and any other information the program has chosen to display, for example the answer to a security question.
- The FSP compares this to the person in front of them and taps **Payment Approved** or **Payment Rejected**.
- Keep the physical voucher; hand in all used QR vouchers to your focal point at day's end alongside the digital reconciliation.

---

## Using 121 Scan to update information in 121

Sometimes a person only receives certain information at the moment of distribution, for example a new prepaid card number, or a SIM card number for mobile money. Instead of noting this on paper and entering it into 121 later, it can be recorded directly in 121 Scan.

- When the person's QR code is scanned, staff can add missing details (for example, the number of the card just handed to them) on the same screen used for verification.
- This is saved on the device, even without an internet connection (see [**Data security**](#data-security) above).
- Once the device reconnects to the internet, the FSP can send the update to 121, where it is added to that person's record. This goes out together with the day's payment outcomes via the same **Send** step.

This avoids double data entry and reduces the risk of a card or SIM number never making it back into 121.

**Role of the FSP:** the FSP is usually the one handing over the card or SIM, so it is practical for them (or the Red Cross staff present) to record the number at that moment, rather than passing it on separately afterwards.

---

-8<- "docs/en/_snippets/contact-support.md"
