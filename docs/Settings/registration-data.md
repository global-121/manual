---
title: Registration data integration
hide:
  - toc
---

!!! Important "Who can perform actions on this page ?"
    Program Admin can view, set up and update the integration between your Kobo form and the 121 platform.

The 121 platform has an integration with KoboToolbox. If you use this tool for data collection, you can proceed with integrating your form to the program in 121. Registrations are then automatically added to 121 in real-time. Note that Red Cross Red Crescent National Societies can create their Kobo form via [IFRC server](https://kobo.ifrc.org/) for free. If you use another data collection tool, you can [import your registrations via Excel](../registration/registration-import-list.md).

You set up and manage the integration between your Kobo form and 121 on the **Registration data** page under **Settings**.

## Set up your Kobo form integration

Setting up your integration consists of two steps:

- Check compatibility between your form, 121 and FSP
- Link your form to 121

## Check compatibility between your form, 121 and FSP

Before you link your form to the 121 platform, you must ensure compatibility between your form, 121 and FSP. This means that you verify if the information required by the 121 platform and your FSP(s) are correctly reflected in the form. You can find the required fields in the **Registrations data** page. Find below a checklist of the 5 mandatory checks and 4 optional ones.

!!! Note
    In addition to the compatibility check, you can request a review of your form by our CVA-IM team. They will review the logic of your form and provide advice to minimize errors and ensure data protection. For instance, restricted formats for certain responses (e.g., phone number, ID), cascading select (next question depends on the answer to the previous question), skip logic (skip question depending on the answer to the previous question), asking consent, and avoidance of collecting unnecessary data. If you are interested in this support, please reach out to the 121 support team.

Before you follow the checklist, share your account with the 121 support team. This will enable us provide timely and efficient support when needed. **Our account name is `nlrc121platform` for the RCRC Movement and `cva121_510` for all other organizations.**

### 1. Language

Make sure the default language in the 'Form' tab of Kobo matches the main language of the program. You can choose as many languages as you like, but **one language must be set to English (EN)**.

- Open your form in **KoboToolbox** and navigate to the **Form** section
- Review which languages are included
- If English is not added, click **Manage**, then **Add language**
- Add as language name **English** and as language code **en**
- Click **Add**

![Registration data link](../assets/img/settings-registrationdata9.png)

![Registration data link](../assets/img/settings-registrationdata8.png)

### 2. Full Name

The **Full Name** is required for 121. Create a **calculate** field with the data column name **fullName**. The calculation is a combination of all names of the beneficiary. If all names are collected in 1 question, the calculate field can directly refer to this.

### 3. Choice of FSP(s)

The **FSP** is required for 121. Make sure the form includes a reference to **which FSP** is used. The data column name must be **fsp**.

- **Using 1 FSP**: create a hidden field and add the name of your FSP under 'default'.
- **Using multiple FSPs with no choice for beneficiary**: create a calculate field and add the names of your FSPs in the calculation that determines the FSP. Calculate fields are always hidden.
- **Using multiple FSPs with choice for beneficiary**: create an open select one question and add the names of your FSPs as responses.

Make sure that the FSP(s) mentioned in your Kobo form match the names of the FSP(s) configured in your program. If you use the Excel manual option, your form should match the 'Display Name' mentioned under FSP configuration. This is a name you provided yourself when you configured the Excel. Use only small letters and - instead of spaces.

### 4. FSP requirements

Make sure the form collects the **data required by the FSP**. You can find this overview in two sections on 121: under FSP configuration (click :material-chevron-down: Form requirements per FSP) and under Registration data (click :material-chevron-down: next to Integrated FSPs). Each data column name should be correctly used in the form. If you require support, please reach out to the 121 team.

### 5. Phone Number

The **Phone Number** is required for 121. This does not have to be a mandatory field and can be left empty in the responses. The data column name must be **phoneNumber**. If possible, set the format of the response to the standard phone number format of your country to prevent errors.

### 6. Scope (optional)

If you wish to use **scope** to limit the access of users to specific registrations, include a calculate field which refers to the question that matches the scope (e.g., region, state, province).

### 7. Max Payments (optional)

If you wish to use a **maximum number of payments** after which your registrations automatically move to **Completed**, include a hidden field with the data column name **maxPayments** and add the number under 'default'.

Once done, reach out to the 121 support team so we can activate this also from our side.

### 8. Inclusion score (optional)

If you wish to use the **Inclusion score** to filter on the total score and automatically update this when a score is edited for a registration, include a calculate field which refers to the responses required for the total score. If you give points to certain answers, the 121 support team will help you set this up in the calculation. There are no restrictions on the data column name.

Once done, reach out to the 121 support team so we can activate this also from our side.

### 9. Multiplier (optional)

If you wish to use the **Multiplier** to allow different transfer values in one program, create a calculate field which refers to the question that determines the transfer value (e.g., location or total score).

## Link your form to 121

1. Make sure the final version of your form is deployed in Kobo (under Form, click (Re)deploy)
2. Navigate to the page **Registration data** under **Settings**
3. Click **KoboToolbox- Click to link**

    ![Registration data link](../assets/img/settings-registrationdata4.png)

4. Copy the **full URL** from the form's page in KoboToolbox. This is the link that you see at the top of your browser.

    ![Registration data link](../assets/img/settings-registrationdata1.png)

5. Copy the **API key**. In KoboToolbox, click on your profile icon (top-right) and select **Account Settings**, sub-page **Security**. Make sure to click **Display** next to the API Key before copying.

    ![Registration data link](../assets/img/settings-registrationdata2.png)
    ![Registration data link](../assets/img/settings-registrationdata3.png)

6. Click **Continue**

    ![Registration data link](../assets/img/settings-registrationdata5.png)

7. If any issues are detected, you will get an automated **error message**. Follow the instructions, save the form in Kobo, redeploy in Kobo, and try again steps 4-5-6.

8. The **integration should now work** and you can start registrations. Make sure the enumerators receive the **correct Kobo link**.

    If you cannot solve the issues yourself, please **contact the 121 team**.

    ![Registration data link](../assets/img/settings-registrationdata6.png)

!!! Note
    Aim to wait with registrations until your Kobo form is final and integrated with the 121 platform. This ensures that **all collectors use the correct link and prevents differences in responses**. If you must make changes to your Kobo form after its integration, this can be done in Kobo. There is no action required on the 121 platform. The columns are automatically updated in 121 once a new registration comes in. Note that this guidance only applies to changes in the **form set up**. Changes in the responses must be made only in the 121 platform.

## Import existing registrations

If you have done registrations with the Kobo form **before** its integration with 121, you can easily import these yourself.

- Once your form is linked, navigate to the **Registration data** page under **Settings**
- Click the **three dots** :material-dots-vertical:
- Click **Import existing reg.**
- Click **Import registrations**. Note that there is a maximum of 1,000 registrations per import. If you have more, split them into multiple files.

![Registration data link](../assets/img/settings-registrationdata7.png)

## Manage your Kobo form integration

!!! Info "Editing the data"
    Please note that the connection between Kobo and the 121 platform is a one-way upload. This means that data is not synchronized between the two systems. Any changes made in Kobo after the data has been uploaded to 121 will not be reflected in the platform. You must make edits directly in the 121 platform.

    For example, if Registration A is registered in Kobo and you upload the data to the 121 platform at the end of the day, you might later notice that question 4 was not answered by Registration A. In this case, you will need to find Registration A's profile in the 121 platform to make the necessary edits. Changes made instead in Kobo Registration A's form after the initial upload will not be updated in the 121 platform.

You can view and manage your Kobo form integration on the page **Registration data** under **Settings**. The following information is displayed:

- The link to your Kobo form
- Last time the Kobo form integration was updated
- The integrated FSP(s) and required fields in the Kobo form
- The registration questions as displayed in the data table and on the profile page.

If you wish to **replace your form** you can click **Reconfigure** under the three dots **:material-dots-vertical:** next to the KoboToolbox link. You will have to enter the URL of the new form and the API key. Note that it is not recommended to use this feature when there are already registrations made through the former form and synced to 121.

If you edited the form set up, it automatically syncs when a new registration is made. If there will be no new registrations, you can use the **Refresh link** under the three dots **:material-dots-vertical:** next to the KoboToolbox link.

If you wish to simplify the questions as displayed in the 121 profiles and registration table, follow these steps:

- Click **:octicons-pencil-24: Edit**;
- Go to the field you wish to change;
- Update the text for the question label;

![Registration data link](../assets/img/settings-registrationdata10.png)

## View your registrations

- Go to your **Program;**
- Enter the **Registrations** page;
- You will see the updated list of registrations any time a new registration is completed and sent (when connected to the internet).

Note that KoboToolbox can be used offline, while on-site. Nevertheless, the registrations are synced to 121 only when an internet connection is established.

---

-8<- "docs/_snippets/contact-support.md"
