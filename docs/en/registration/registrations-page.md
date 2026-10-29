---
title: Registrations - Page Description
hide:
  - toc
---

The **Registrations** page lets you review and, if necessary, update the registrations list and details before including them in the program to start receiving cash assistance.

!!! Important "Who can perform actions on this page ?"
    All users can view the Registrations page. Validating, declining, pausing and editing registrations is limited to CVA Manager and CVA Officer. Including, exporting and bulk updating registrations is limited to CVA Manager. By default, no standard role can delete registrations — see the relevant pages for details. [Learn more about Roles & Permissions](../users/description-roles.md)


### Overview of registration lists

Oversee all new **registrations**. The initial status for a registration is shown as **New** and will remain as is until a CVA Manager **includes** (included) the registration in, or a CVA Manager or CVA Officer **declines** (declined) it from, the program.

![Registrations page](../assets/img/RegistrationsPage.png)

The **Name** column shows the full name of each registration, as set up on the **Full name setup** card of the [Registration data](../settings/registration-data.md#set-up-the-full-name) page. If the full name is not set up yet, the column shows **Set up needed**.

The **Transfer value** column shows the amount a registration receives in a single payment. It is the fixed transfer value of the program multiplied by the multiplier of the registration, if applicable. For example, if the fixed transfer value is $50 and the multiplier is based on household size, a 3-person household has a transfer value of $150. The transfer value is also shown on the profile page of each registration.

- If the **Transfer value** column is not visible, click **Manage table** (:material-cog:), select **Transfer value** and click **Apply**.

---

### Import a registration list

Registration lists can be imported in two ways into the 121 platform:

- **Automatically**, by integrating your registrations with your Kobo form, or equivalent data collection form, with the 121 platform. Learn more on the [automatic import of registration page;](../settings/registration-data.md)
- **Manually**, by importing a registration list from an Excel file (.CSV format). Learn more on the [registration import list page.](../registration/registration-import-list.md)

---

### Review and update the registration status

Your SOPs may include reviewing the collected details before validating and including the registrations in the program.
Follow the instructions on how to:

- [Review, edit and validate registrations details;](../registration/registration-validate-pa.md)
- [Deduplicate your registration list in 121 platform;](../registration/registration-deduplication.md)
- [Include a registration in a program;](../registration/inclusion-in-program.md)
- [Decline a registration from a program;](../registration/registration-reject-pa.md)
- [Pause a registration in a program;](../payment/pause-payment-pa.md)
- [End a registration participation in a program.](../payment/end-payments.md)

---

### Deduplicate registration

Check for duplicates in the registration list before including the registrations in your program. This validation process prevents double payments and reduces fraud risks, so we strongly recommend including deduplication in your validation process.

Follow the instructions on the [Deduplication page](../registration/registration-deduplication.md)

---

### Delete registrations

Deleting a registration removes its personal data from the 121 platform. Only delete registrations when your SOPs or data protection rules require it.

!!! Important "Who can delete registrations?"
    Deleting registrations needs a separate permission. By default, no standard role has it. Contact our support team if you need to delete registrations.

- On the **Registrations** page, select the registrations you want to delete and click **Delete** on the top of the table. Or open a registration profile, click **Actions** and, under **Status update**, click **Delete**;
- The **Delete registration(s)** pop-up appears. Enter a reason in **Write a reason for the update**. The reason is required; ![Delete registration(s) pop-up](../assets/img/DeleteRegistration.png)
- Tick **I understand this action can not be undone.**;
- Click **Delete registration** (or **Delete registrations**).

!!! Warning "This action cannot be undone"
    The status of the registration changes to **Deleted**. Its personal data, notes and messages are deleted, and it no longer appears in the Registrations table. You cannot restore a deleted registration.

---

-8<- "docs/en/_snippets/contact-support.md"

