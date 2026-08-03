---
title: Step-by-Step Guide Prepare your CVA program
hide:
  - toc
---

This guide provides the essential steps to prepare and launch your Cash and Voucher Assistance (CVA) program through the 121 platform. Please review each step carefully before getting started. You can also print or save this page to use as a checklist throughout the process.

---

## 1. Define Your Program Details

To set up your program, you need to know your basic program information.

You may want to add a validation step in your cash flow. This functionality in the 121 platform allows you to use the ‘Validation’ status for registrations before including them in the payment. When making use of the Kobo Offline Validation Form, submitting the form automatically moves the beneficiary registration to Validated.

You may want to add scope to your 121 program. This functionality allows you to control which team members have access to specific registrations based on the scope they are assigned to.

Prepare your registration form in Kobo (or another supported tool). The form can only be integrated into 121 once finalized by your team.

- [ ] Program name
- [ ] Target registrations
- [ ] Transfer value
- [ ] Financial Service Provider(s) (FSP)
- [ ] Currency
- [ ] Timeline for registration, data cleaning and payment shared with 121 team
- [ ] Decision whether to enable scope in 121 (enables limited access to team members)
- [ ] Decision whether to enable validation in 121 (enables the status 'Validate')
- [ ] Fields to be checked for duplicates shared with 121 team

Find specific instructions to set up your program information on the [**Program information page**](../Settings/program-information.md).

---

## 2a. Collaborate with your FSP(s)

Make agreements with your FSP on the upcoming program. If you work with an FSP integrated to your instance, request the credentials and configure this in 121. If you work with an FSP that is not integrated with 121, ensure you know which payment instructions are required. This is required to export your payment lists from 121.

- [ ] Contract FSP / verify if contract with the FSP(s) is still valid
- [ ] Inform FSP on program specifics (e.g., timeline and modality)
- [ ] Credentials entered in 121 for configuration – if FSP is integrated
- [ ] Payment instruction template received from FSP – if FSP is not integrated

Find specific instructions to set up your FSP on the [**FSP configuration page**](../Settings/fsp-integration.md).

---

## 2b. Finalize Your Registration Data Collection Form

Prepare your registration form in Kobo (or another supported tool). Ideally use one harmonized form in your organization that you adapt to the specific program. Our team is available to review and advise on your form. We will also ensure its compatibility with 121. To share your form, please send it to our Kobo account: `nlrc121platform` for the RCRC Movement | `cva121_510` for others.

- [ ] Consent question included in the form
- [ ] Targeted localities included in the form
- [ ] Required beneficiary information by FSP included in the form
- [ ] If choice of FSP is offered (also through Onafriq), question about FSP preference included in the form
- [ ] Restrictions to limit errors included in the form (e.g., specific format for ID number, phone number, Full Name)
- [ ] Check if data collection is minimized to what is necessary
- [ ] Form reviewed by the 121 support team (mandatory 121 compatibility check, optional general review)
- [ ] Form linked to 121 program

Find specific instructions to set up your registration data collection form on the [**registration data collection form page**](../Settings/registration-data.md).

---

## 3. Create Your Team

Identify the members of your program team. Once their user accounts are created (only to be done once) you can add them to the program team and assign them a role. The roles in 121 do not have to match with the actual positions of the team members. Rather, the respective permissions should match the actions that the user will perform in the platform. You can give someone one or more roles.

- [ ] User accounts created for new team members
- [ ] Users added to the program with an assigned role
- [ ] Scope defined for users (optional)

Find specific instructions to set up your program team on the [**program team page**](../Settings/programteam.md).

The user has not been created yet? Refer to the [user creation guide](../users/add-users.md).

---

## 4. Set Up Messaging Services (Optional)

The 121 platform offers a technical integration to use Twilio for messaging. If you plan to send WhatsApp and/or SMS to your beneficiaries, it might be interesting to open a Twilio account. You can check the fees on their website. **Note:** When using Twilio for your program, ensure you have sufficient funds in your account, otherwise the messages will fail. If you plan to send messages at different stages of the program, templates can be added to your instance.

!!! Important "Number of characters per SMS"
    One SMS is limited to 160 characters — messages longer than this will be split into multiple SMS and charged accordingly. For example, a message between 161 and 320 characters will be counted and billed as two SMS.

- [ ] Decision on whether to use Twilio
- [ ] Create a Twilio account
- [ ] Inform 121 team
- [ ] Request support from the 121 team to create messaging templates (optional)
- [ ] Top up funding in your account

---

## 5. Set Up Offline Validation Form (Optional)

If you validate beneficiaries in the field, we can support you in setting up a validation form in Kobo. This can be prepared once registration and data cleaning are completed. By entering a unique identifier (e.g., ID number), the form pulls the personal information of the beneficiary. This can be used to verify the person. Once the form is submitted and the device is synced to the internet, the status of the beneficiary automatically moves to Validated.

The form can also be used to update beneficiary information when in the field. For instance, a phone number. Once the form is submitted and the device is synced to the internet, the 121 profile of the beneficiary automatically updates.

Contact our team to organize this process and let us know the verification criteria and fields you want to use.

- [ ] Decision on use of form for field validation
- [ ] Validation form requested and co-designed with the 121 team
- [ ] Training on how to use the form provided

Find specific instructions to set up your offline validation form on the [**offline validation form page**](../registration/offline-verification.md).

---

## 6. Set Up Offline Form for SIM Card distribution or Mass Update (Optional)

If you are planning to distribute SIM cards, we can support you in updating your database in 121 accordingly. There are two options:

- [ ] Create a Kobo form to use during the distribution in which the phone number of the SIM card is added to the 121 beneficiary profile
- [ ] Mass update the 121 beneficiary profiles with the list of phone numbers

- [ ] Decision made on SIM card distribution and process discussed with 121 team
- [ ] Key fields for matching SIM to person (e.g., name, ID number, registration number) identified and verified
- [ ] Ensure data between 121 and the provider managing the SIM card distribution aligns
- [ ] Form for SIM card update co-designed with the 121 team

---

You are now fully prepared to launch your program and successfully distribute cash assistance to those in need!

## Need Support?

Please reach out to our [support team via email](mailto:support@121.global) if you need assistance or further clarification.

---

-8<- "docs/en/_snippets/contact-support.md"
