---
title: Registrations - Deduplication
hide:
  - toc
---

Below you will find the steps to check duplicated registrations and deduplicate as needed. Note that duplicates can only be checked within a single project and there is no way to check duplicates across different projects in 121.

!!! Important "Who can perform actions on this page ?"
    Program Admin, CVA Officer and CVA Manager can perform actions.  
    Additional users may only have View permissions on this page. [Learn more about Users & Roles](../users/users-roles-page.md)

---

### Setting up the Duplicate Check

**The criteria for detecting duplicates have been configured in your Kobo form.**

**Duplicates are identified based on specific unique criteria** such as phone number or ID number. This criteria is flexible and can be chosen by the organisation and changed depending on the program requirements. We recommend using unique identification criteria (e.g., ID Number, phone number) to reduce the duplicate check, instead of criteria that can easily match across registrations (like name).

The criteria can be set up directly in your Kobo, marking the question as **+dedup** in your form. The 121 Platform will then recognize the value as the duplicate criteria. Request our team to adjust the criteria based on your project.

---

### Filter the duplicated Registrations

In the **Registration** page, all duplicated entries will be marked based on the unique criteria selected by your organization (e.g., ID number, phone number, etc.).

- Click on :material-cog: icon to **manage the table**,
- Select **Duplicates** and click **Apply** to show duplicate column in the table,
- In the **Duplicates** column, select the filter icon and filter on **Duplicate**,
- The filtered list will only show the registrations marked as **Duplicate**,
- Click on **Reg #** or **Name** to open the personal registration profile. A red banner at the top of the page labelled **Duplicated with** will show who this person is duplicated with and the **matching field**.
- To resolve this duplicate you can decide to ignore, decline or update. See the description below.

![Manage Table](../assets/img/ShowDuplicateColumn.png)

![Filter Duplicate](../assets/img/FilterDuplicate.png)

## Update the list of registrations

Once you have identified the duplicate, you can update the registration and remove the duplicate label in 3 ways:

- **Edit the duplicated value directly in the registration profile** after validating the information.
- **Decline the registration**, if the same person is registered twice.
- **Ignore the duplicate**, if your SOPs allow registrations to share the value - such as phone number, which may be used by multiple people in the same community.

---

## Edit the duplicated value in the registration profile

- Open the profile clicking on **Reg. #** on the left side. You will now see the registration overview,
- Click the tab **Personal Information** and search for the value to be edited,
- **Edit** the value. Click on **Save** and give a reason,
- The new value is now saved,
- The registration will automatically be updated and marked as **Unique**.

![Edit Information](../assets/img/EditInformationDuplicate.png)

---

## Decline the registration

- In the personal registration profile, on the top left of the page, click on **Action**
- Click on the **Decline** button,
- **Approve** the action. *Confirm only if you are sure to decline this registration, otherwise cancel.*
- You will have to enter a reason for declining the beneficiary.
- When a registration is declined they are no longer included in the duplicate check so the registration they were duplicated with will change to **Unique**.

![Decline Registration](../assets/img/DeclineIgnoreDuplicate.png)

Did you accidentally mark a registration as declined? No worries, this is a reversible action. You can always change the status back to **Included**.

---

## Ignore the duplicate

- In the personal registration profile, on the top left of the page, click on **Action**,
- Click on the **Ignore the duplicate** button,
- **Approve** the action. *Confirm only if you are sure to ignore this registration, otherwise cancel.*
- The registration will automatically be updated and marked as **Unique**.

![Ignore Duplicate](../assets/img/DeclineIgnoreDuplicate.png)

!!! Info "Why ignoring a duplicate?"
    In some situations, the duplicate criteria may be set on **phone number**, meaning that if multiple registrations share the same phone number, the platform will show the registrations as duplicates. 
    
    However, in some cases, phone numbers are shared by multiple people in a community (for example, if one person doesn't have a phone they might use the phone number from their neighbour). Therefore, if it aligns with your SOPs, you may decide to consider the registrations as Unique if you've validated that the same phone number is being used by different people.

-8<- "docs/_snippets/contact-support.md"
