---
title: FSP integration
hide:
  - toc
---

!!! Important "Who can perform actions on this page ?"
    Program Admin can view, set up and update the FSP integration.

Every time a new program starts, the Program Admin configures the Financial Service Provider (FSP). You can add multiple FSPs to the same program. You can also select the manual option using Excel, which allows exporting the instructions from the FSP and later importing the reconciliation file.

**Step 3 of program creation** asks to select the FSP(s). This can also be done in the Budget table of the **Program information** page. If this is done, the FSP(s) will automatically show on the **FSP integration** page under **Settings**.

### Review required fields registration form

To ensure your registration form contains the required fields for the FSP(s), you can click **:material-chevron-down: Form requirements** on the FSP card.
![Required Fields](../assets/img/settings-fspintegration-requiredfields.png)

Your form has to match exactly the data column name as shown. If you need support, you can reach out to the 121 team.
![Required Fields](../assets/img/settings-fspintegration-requiredfields2.png)

### Complete FSP configuration

In order to use the integration, you must **complete the configuration** by entering the credentials. You will receive this from the FSP. If this is not yet done, the 121 platform shows the following notification, and the FSP card shows **Integration required**:
![Integration Required](../assets/img/settings-fspintegration-required.png)

- On the FSP card, click **Integrate**;
- Enter the credentials;
- Click **Integrate FSP**.

### Update FSP configuration

You can update the FSPs at any time during your program.

- If you wish to reconfigure an FSP, click on the 3 dots :material-dots-vertical: and select **Reconfigure**.
- If you wish to delete an FSP, remove the FSP under Program information. Note that you cannot delete an FSP that is already linked to registrations.
- If you wish to add an FSP, add the FSP under Program information and configure under FSP integration

![Reconfigure](../assets/img/settings-fspintegration-reconfigure2.png)

### Excel FSPs

If you use the manual option with Excel, you can set up more than one Excel FSP in the same program.

To add another Excel FSP:

- On the card of an Excel FSP, click on the 3 dots :material-dots-vertical:;
- Select **Create another Excel FSP**; ![Excel FSP menu with Create another Excel FSP](../assets/img/settings-fspintegration-excelfsp.png)
- Fill in the **Display name**;
- Select the **Unique identifier field**. This field is used during reconciliation to update the transaction status of each registration, for example the phone number or ID number;
- Optionally, select the **FSP export fields (optional)**. These are the fields included in the payment report you send to your FSP;
- Click **Integrate FSP**.

To remove an Excel FSP:

- On the card of the Excel FSP, click on the 3 dots :material-dots-vertical:;
- Select **Remove integration**;
- Click **Remove FSP** to confirm.

!!! Note
    **Remove integration** is only available when your program has more than one Excel FSP. You cannot remove an FSP that is still used by registrations.

---

-8<- "docs/en/_snippets/contact-support.md"
