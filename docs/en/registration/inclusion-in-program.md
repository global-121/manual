---
title: Registrations - Inclusion in program
hide:
  - toc
---
The Inclusion stage is a necessary step to move a list of beneficiaries from the registration phase to the payment phase.

Based on the SOPs you follow for your CVA program, **Validation** can be used to identify registrations whose information has been verified, either prior to including them in the program or for sharing the verified list with a committee for approval. Validation is only available if **Enable validation** is turned on in the program settings. You can follow the steps to validate the PA details on the [Validation page](./registration-validate-pa.md)

!!! Important "Who can perform actions in this page?"
    CVA Manager can perform actions in this page. [Learn more about Roles & Permissions](../users/description-roles.md)

### Inclusion of registrations into the program

The **Registrations table** shows all of the registered households or individuals for your program. Their initial status should be **New**. Or, if your SOPs include a validation step, the status may show **Validated**.

To mark the registrations as **included**:

- go to the **Registrations page**;
- Filter the list of registrations on **Registration Status**, select **New** (or **Validated**, if your program uses validation) and **Apply**. *This action is to make sure you select only the registrations you want to include;* ![Filter Status Register](../assets/img/RegisteredStatusFilter.png)
- You can:
  - Make an **individual selection** by clicking on the :material-checkbox-outline: on the PA line;
  - Make a **bulk selection** by clicking on the :material-checkbox-multiple-marked-outline: checkbox in the table header;
- On the top of the table, click **:octicons-check-16: Include** button;
- The **Include registration(s)** pop-up appears to confirm your action **You're about to include X registrations. This means that they can be included in payments.** *Optionally, turn on **Send a message to registration(s)**;*
- Click on **Include registration**. A message indicates the completion of the action;
- The status is now updated to **Included**.

!!! Important "Duplicates cannot be included"
    Registrations marked as **Duplicate** cannot be included. If your selection contains a duplicate, an error message appears and none of the selected registrations is included. Resolve the duplicates first (edit, decline or ignore them), then try again. Follow the instructions on the [Deduplication page](./registration-deduplication.md).

!!! Note "Which registrations can be included?"
    **Include** works for registrations with any status except **Included**, unless they have already received their maximum number of payments. For example, you can also include registrations that are **Declined** or **Paused**.

!!! Info "Deduplication process"
    The SOPs may include a deduplication process before initiating the inclusion phase. Follow the instructions to [check your registration list and deduplicate registrations before moving the list to the inclusion phase](./registration-deduplication.md).

### Decline registrations from the program

You may have to **decline** a certain number of **registrations** from your program.
You can follow the instructions on this [page](./registration-reject-pa.md)

---

### Send a message to the registrations

There is an option to send a message to registered households or individuals for each action you perform in the instance, such as Including, Declining, or Sending payments. If you would like to communicate program progress to the registrations, you can turn on **Send a message to registration(s)** and enable messaging through the 121 platform.

To enable messaging services, you must create a Twilio account and ensure there are sufficient messaging credits. Contact our support team to set this up.

---

-8<- "docs/en/_snippets/contact-support.md"
