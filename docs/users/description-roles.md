---
title: Description of role-based permissions
hide:
  - toc
---

No single user can take all actions in the 121 platform. The 121 platform follows **role-based segregation of duties**, which improves task **accountability**. For example, users with a CVA profile will not be able to make payments but are able to make updates to registration data. Users with a finance profile can make payments, but are not able to update registrations' personal information. The following standard roles are configured in the 121 platform.

### Standard 121 user Roles

| Type | Description |
| :------------------ | :------------------------------------------------------------------- |
| **Program Admin** | System Administrator, overseeing user access on the platform and managing project with an overall view of project progress. |
| **CVA Officer** | Officer for Cash and Voucher Assistance. |
| **CVA Manager** | Manager for Cash and Voucher Assistance. |
| **Finance Officer** | Officer for Finance operations and audit. |
| **Finance Manager** | Manager for Finance operations, payment instructions. |
| **View** | Portal Users who are allowed to view only and cannot perform actions. |

### Permissions per role


| Permissions | **Program Admin** | **CVA Manager** | **CVA Officer** | **Finance Officer** | **Finance Manager** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Overview Users and Roles | :material-progress-question:{.req} | | | | |
| Add new 121 users | :material-progress-question:{.req} | | | | |
| Reset 121 users ' password | :material-progress-question:{.req} | | | | |
| Edit and update programs settings (information & budget) | :octicons-check-circle-fill-24:{.yes} | | | | |
| Overview of all active programs | :octicons-check-circle-fill-24:{.yes} | | | | |  
| View only active programs assigned to the user | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Create new projects in 121 | :octicons-check-circle-fill-24:{.yes} | | | | |
| Manage Team members and assign roles in projects | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Overview registration list | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Import registration list (via excel) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Edit registrations details | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Include registrations in projects | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Validate registrations list | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Decline registrations from a project | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Duplicate registrations (and export duplicate report) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Pause registrations from receiving payments | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Delete registrations from project | | | | | |
| Import (mass) Data changes into registrations | :octicons-check-circle-fill-24:{.yes} | c:octicons-check-circle-fill-24:{.yes} | | | |
| Send SMS to registrations (1-way SMS) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| View activity logs in registrations' profile | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Create new payments to registrations | | | | | :octicons-check-circle-fill-24:{.yes} |
| Send payments to registrations | | | | | :octicons-check-circle-fill-24:{.yes} |
| Export Payment Instructions (manual FSP export-import function) | | | | | :octicons-check-circle-fill-24:{.yes} |
| Reconcile payments (manual FSP export-import function) | | | | | :octicons-check-circle-fill-24:{.yes} |
| Export reporting on registration (full list) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Export reporting on data changes | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Export payment reports | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Export account number verification report | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View Monitoring page | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View PowerBi dashboard | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| View payment dashboards (payment page) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

:octicons-check-circle-fill-24:{.yes} Feature available.:material-progress-question:{.req}  Feature not available, upon request to 121 support team.

---

### Additional roles

Additional roles and permissions can be configured upon request. Contact your dedicated Account Manager or reach out to our [support team via email](mailto:support@121.global).

---

!!! note "Add users to a program"
    You can follow these instructions to [add team members to a program and assign a role](../team/add-team-members.md).

-8<- "docs/_snippets/contact-support.md"
