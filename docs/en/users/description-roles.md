---
title: Description of role-based permissions
hide:
  - toc
---

No single user can take all actions in the 121 platform. The 121 platform follows **role-based segregation of duties**, which improves task **accountability**. For example, users with a CVA profile will not be able to make payments but are able to make updates to beneficiary data. Users with a finance profile can make payments, but are not able to update beneficiaries' personal information. The following standard roles are configured in the 121 platform.

In the **Home page**, you can click on the **menu icon (:material-menu:)** on the top left, and select either **Users** or **User roles**. You only see these pages if you have **Organisational Admin rights**. These rights are not a role: the 121 support team turns them on for a user, whatever role that user has in programs. Organisational Admin rights let you:

- View users and user roles, and add new users to the platform,
- Create new programs and duplicate existing programs.

If you need these rights, contact the 121 support team.

### Users page

On the **Users** page, you can:

- See the list of all registered users in your 121 instance,
- [Add new users into the 121 platform](../users/add-users.md) by sending them an invitation,
- [Edit a user's name](../users/add-users.md#edit-a-user),
- [Reset user's password](../users/add-users.md#reset-user-password).

### User Roles page

On the **User roles** page, you can:

- View the list of available roles set in your instance. It is not possible to create new roles and permissions.
- To assign a role to a user, move to the Settings page of your program and [follow the instructions on this page.](../settings/programteam.md#change-assigned-roles-and-permissions)

### Standard 121 user Roles

When you add a user to your program team, you choose their role(s) in the **Select role(s)** list. The second column shows the name of each role in that list.

| Type | Name in the **Select role(s)** list | Description |
| :------------------ | :------------------ | :------------------------------------------------------------------- |
| **Program Admin** | Program Admin | Sets up and manages the program: program information, FSP integration, registration data, program team and payment approval. Cannot see the personal data of registrations. |
| **CVA Manager** | Cash Assistance Program Manager | Handles registrations with the permissions to mass update, deduplicate, include, export and create payments. |
| **CVA Officer** | Cash Assistance Program Officer | Handles registrations without the specific permissions mentioned for CVA manager. |
| **Finance Manager** | Finance Manager | Creates, starts, retries and reconciles payments, and exports payment instructions and reports. |
| **Finance Officer** | Finance Officer | Exports payment instructions for the FSP and views payment data. Cannot create or process payments. |
| **View** | Only view data, including Personally Identifiable Information | Allowed to view only (including personal data) and cannot perform actions. |
| **View without PII** | Only view data, not including Personally Identifiable Information | Allowed to view only, without personal data, and cannot perform actions. |
| **Approver** | Approve payments | Views registrations and payments and exports payment instructions. Meant for users who approve payments. |
| **Program Team Manager** | Program Team Manager | Manages the program team and assigns roles. Views registrations (without personal data) and payments. |

Your 121 platform also has two technical roles for the Kobo integration: **Only CREATE registrations** and **Only UPDATE registrations**. They are used by the accounts that connect Kobo to 121. Do not assign them to people in your team. Your organisation may also have other roles, or roles with different permissions, set up on request. If you have any questions about the set up of the roles and permissions in your 121 platform, reach out to the 121 support team. In your programs, you see also the 121 team added with the Admin role. This role allows us to provide the required support. We never make changes to your program without explicit permission.

### Permissions per role

| Permissions | **Program Admin** | **CVA Manager** | **CVA Officer** | **Finance Manager** | **Finance Officer** | **View** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Edit program information (basic details and finance) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Add or remove FSPs in the program | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Set up the FSP integration | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Link the Kobo form, edit registration questions and de-duplication fields | :octicons-check-circle-fill-24:{.yes} | | | | | |
| View program team | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Manage program team and assign roles | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Set up payment approval | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Overview registration list | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Import registration list (via Excel) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Ignore duplicates (**Ignore duplication**) | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Edit registration details | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Edit **Max. payments** and **Transfer value multiplier** of a registration | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Change the FSP of a registration² | | | | | | |
| Include registrations | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Validate registrations (if validation is enabled) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Decline registrations | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Pause registrations (from receiving payments) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Delete registrations² | | | | | | |
| (Mass) update registrations with Excel import | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Send SMS to registrations (if Twilio is activated) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| View activity logs in registrations' profile¹ | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Create payments | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Delete payments that have not been started | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Rename payments | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Approve payments³ | | | | | | |
| Start payments | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Retry failed transactions | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Export the FSP payment list (manual FSP export-import function) | | | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Import payment reconciliation (manual FSP export-import) | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Export reporting on registration (full list) | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Export reporting on status and data changes | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Export the payment report of a payment⁴ | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Pause debit cards (Intersolve Visa programs) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Link, replace, close or order debit cards (Intersolve Visa programs)² | | | | | | |
| Unpause debit cards (Intersolve Visa programs) | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Export debit card usage, refunded debit cards or unused vouchers² | | | | | | |
| Upload files | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Rename or delete files | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| View Monitoring page | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View Power BI dashboard | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View Payments page | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

+:octicons-check-circle-fill-24:{.yes} Feature available.

¹ The activity log only shows what the role is allowed to see. Finance Manager and Finance Officer do not see messages. Program Admin does not see any activities.

² No standard role has this permission. Contact the 121 support team if you need it.

³ Approving payments does not depend on the role. Only the team members set as approvers on the [Payment approval](../settings/payment-approval.md) page can approve a payment.

⁴ The payment report is exported from the page of a single payment. Exporting all payments at once from the Payments page (**Export** > **Payments**) needs two export permissions that no standard role has together. Contact the 121 support team if you need this export.

The **View without PII**, **Approver** and **Program Team Manager** roles are not in the table above. They have fewer permissions:

- All three can view the registration list, the Payments page and the Monitoring page.
- **View without PII** cannot see personal data. In the activity log, it only sees transactions and messages.
- **Approver** can see personal data and export the FSP payment list (manual FSP export-import function). To approve payments, the user must also be set as an approver on the [Payment approval](../settings/payment-approval.md) page.
- **Program Team Manager** can view and manage the program team and assign roles. It cannot see personal data.

---

### Additional roles

Additional roles and permissions can be configured upon request. Contact our [support team via email](mailto:support@121.global).

---

!!! Note "Add users to a program"
    You can follow these instructions to [add team members to a program and assign a role](../settings/programteam.md).

-8<- "docs/en/_snippets/contact-support.md"
