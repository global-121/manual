---
title: Description of role-based permissions
hide:
  - toc
---

No single user can take all actions in the 121 platform. The 121 platform follows **role-based segregation of duties**, which improves task **accountability**. For example, users with a CVA profile will not be able to make payments but are able to make updates to beneficiary data. Users with a finance profile can make payments, but are not able to update beneficiaries' personal information. The following standard roles are configured in the 121 platform.

In the **Home page**, you can click on the **menu icon (:material-menu:)** on the top left, and select either **Users** or **User Roles**. Note that this access needs to be specifically requested to the 121 team as this allows you not only to view users and user roles, but also to add new users to the platform.

### Users page

On the **Users** page, you can:

- See the list of all registered users in your 121 instance,
- [Add new users into the 121 platform](../users/add-users.md) by sending them an invitation,
- [Reset user's password](../users/add-users.md).

### User Roles page

On the **User Roles** page, you can:

- View the list of available roles set in your instance. It is not possible to create new roles and permissions.
- To assign a role to a user, move to the Settings page of your program and [follow the instructions on this page.](../Settings/programteam.md#change-assigned-roles-and-permissions)

### Standard 121 user Roles

| Type | Description |
| :------------------ | :------------------------------------------------------------------- |
| **Program Admin** | Oversees program creation and management. |
| **CVA Manager** | Handles registrations with the permissions to mass update, deduplicate, include, and create payments. |
| **CVA Officer** | Handles registrations without the specific permissions mentioned for CVA manager. |
| **Finance Manager** | Creates, sends and reconciles payments, and exports payment instructions and reports. |
| **Finance Officer** | Exports payment instructions for the FSP and views payment data. Cannot create or process payments. |
| **View** | Allowed to view only and cannot perform actions. |

There might be additional roles available on your 121 platform. We advise you not to use these. If you have any questions about the set up of the roles and permissions in your 121 platform, reach out to the 121 support team. In your programs, you see also the 121 team added with the Admin role. This role allows us to provide the required support. We never make changes to your program without explicit permission.

### Permissions per role

| Permissions | **Program Admin** | **CVA Manager** | **CVA Officer** | **Finance Manager** | **Finance Officer** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Overview Users and Roles | :material-progress-question:{.req} | | | | |
| Add new 121 users | :material-progress-question:{.req} | | | | |
| Reset 121 users' password | :material-progress-question:{.req} | | | | |
| Create new programs | :octicons-check-circle-fill-24:{.yes} | | | | |
| Manage program team and assign roles | :octicons-check-circle-fill-24:{.yes} | | | | |
| Edit program information (basic details and budget) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Overview registration list | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Import registration list (via Excel) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Deduplicate registrations | | :octicons-check-circle-fill-24:{.yes} | | | |
| Edit registration details | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Include registrations | | :octicons-check-circle-fill-24:{.yes} | | | |
| Validate registrations | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Decline registrations | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Pause registrations (from receiving payments) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| (Mass) update registrations with Excel import | | :octicons-check-circle-fill-24:{.yes} | | | |
| Send SMS to registrations (if Twilio is activated) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| View activity logs in registrations' profile | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Create payments | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | |
| Send payments | | | | :octicons-check-circle-fill-24:{.yes} | |
| Export payment instructions (manual FSP export-import function) | | | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Import payment reconciliation (manual FSP export-import) | | | | :octicons-check-circle-fill-24:{.yes} | |
| Export reporting on registration (full list) | | :octicons-check-circle-fill-24:{.yes} | | | |
| Export reporting on data changes | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Export payment reports | | | | :octicons-check-circle-fill-24:{.yes} | |
| Upload files | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | |
| Rename or delete files | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| View Monitoring page | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View Power BI dashboard | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View Payments page | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

+:octicons-check-circle-fill-24:{.yes} Feature available.

+:material-progress-question:{.req} Feature upon request to 121 support team.

---

### Additional roles

Additional roles and permissions can be configured upon request. Contact our [support team via email](mailto:support@121.global).

---

!!! Note "Add users to a program"
    You can follow these instructions to [add team members to a program and assign a role](../Settings/programteam.md).

-8<- "docs/en/_snippets/contact-support.md"
