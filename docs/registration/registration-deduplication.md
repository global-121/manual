---
title: Registrations - Deduplication V1
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

In the **Registration** page, and following your organization's SOPs, all duplicated entries will be listed based on the unique criteria (ID number, phone number or required criteria).

- Click on :material-cog: icon to **manage the table**,
- Select **Duplicates** and click **Apply** to show duplicate column in the table,
- In the **Duplicates** column, select the filter icon and filter on **Duplicate**,
- The filtered list will only show the registrations marked as **Duplicate**,
- Click on **Reg #** or **Name** to open the personal registration profile. A red banner at the top of the page labelled **Duplicated with** will show who this person is duplicated with and the **matching field**.
- To resolve this duplicate you can decide to ignore, decline or update. See the description below.

![Manage Table](../assets/img/ShowDuplicateColumn.png)

![Filter Duplicate](../assets/img/FilterDuplicate.png)

!!! Note "Setting up your duplicates criteria in Kobo"
    **Duplicates are identified based on specific unique criteria** such as phone number or ID number. This criteria is flexible and can be chosen by the organisation and changed depending on the program requirements. We recommand unique criteria so to ease the duplicate check, such as ID number when possible or similar alternative which makes the criteria unique to the registration.

    The criteria can be set up directly in your Kobo, marking the question as **+dedup** in your form. The 121 Platform will then recognize the value as the duplicate criteria. Request our team to adjust the criteria based on your project.


## Update the list of registrations

Once you have identified the duplicate, you can either decide to update the registration list in the 121 platform as follows:
You can perform 3 actions in the **Registrations** page:

- **Edit the value directly in the registration profile**
- **Decline the registration**, in case this is a double entry for the same beneficiary.
- **Ignore the duplicate**, in case your SOPs allow registrations to share a same value - such as phone number, which can be used by multiple beneficiaires in the same community.

Below, the solution based on either of these 3 options:

---

### Edit the value in the registration profile

- Search for the registration number by filtering the **Reg. # column**
- Open the profile clicking on **Reg. #** on the left side. You will now see the registration overview,
- Click the tab **Personal Information**, then **Edit** button and search for the value to be edited, ![Edit Value](../assets/img/EditInformationDuplicate.png)
- **Edit** the value. Click on **Save** and give a reason,
- The new value is now saved,
- The duplicate will automatically be updated and marked as **Unique**.

![Edit Information](../assets/img/EditInformationDuplicate.png)

---

## Decline the registration

- Search for the registration number by filtering the **Reg. # column**
- Once you have found the registration, **enter the beneficiary registration**,
- On the top left of the page, click on **Action** and then on the **Decline** button,
- **Approve** the action. *Confirm only if you are sure to decline this registration, otherwise cancel.*
- You will have to enter a reason for declining the beneficiary.

![Decline Registration](../assets/img/DeclineIgnoreDuplicate.png)

If you need to decline multiple registrations, this action will have to be done for each invididual registration.

*Did you accidentally mark a registration as declined? No worries, this is a reversible action. You can always change the status back to **Included**.

---

## Ignore the duplicate

- Once you have found the registration, **enter the beneficiary registration**,
- On the top left of the page, click on **Action** and then on the **Ignore the duplicate** button,
- **Approve** the action. *Confirm only if you are sure to ignore this registration, otherwise cancel.*

![Ignore Duplicate](../assets/img/DeclineIgnoreDuplicate.png)

!!! Info "Why ignoring a duplicate?"
    In some situations, the duplicate criteria may be set on **phone numbers**, meaning that if multiple registrations share the same phone numbers, the platform will show the registrations as duplicate. Nevertheless, in many cases, communities share the same phone number with multiple inhabitants. Therefore, based on your SOPs, you may decide to consider the registrations as Unique if a same phone number is shared within the community.

-8<- "docs/_snippets/contact-support.md"
