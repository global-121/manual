---
title: 121 Glossary
hide:
  - toc
---

A list of key terms used in the 121 platform.

- [General terms](#general-terms)
  - [Pages](#pages)
  - [Program Cards](#program-cards)
  - [Create new program](#create-new-program)
  - [Registration Status](#registration-status)
  - [Payments](#payments)
  - [Transfer statuses](#transfer-statuses)
  - [Debit cards (Visa Specific)](#debit-cards-visa-specific)

## General terms

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **121 Platform** | (“one to one”) is a platform that helps program managers by increasing efficiency in setting up and executing a cash program Information Management (IM) system. |
| **CVA** | Cash and Voucher Assistance, referring to Cash Transfer Programming (CTP). |
| **Program** | A program created by users in the platform. |
| **FSP** | Financial Service Provider - an entity that provides financial services, which may include digital payment services. |
| **Budget** | Amount of money in the project that will be disbursed to included people/households. |
| **Registrations** | People or households that registered, subscribed to a program. |
| **Import** | Adding or uploading data from Excel file or interview forms e.g. "import registrations". |
| **Export** | Downloading content from the 121 Platform. |
| **Actions** | Indicates something a user can do that affects one or multiple registrations, e.g. sending a message, adding a note, or updating the information. |
| **Filter by** | Users can use this to find a group of registrations or a single registration that they are looking to perform an action on e.g. filter registrations that received 2 payment and include in a new payment. |
| **Quick search** | A filter search that shows results of multiple columns instead of filtering in just one column. This is a fast way to find a single or small group of registrations. |
| **Type / Select value** | when a column is selected to filter by, users can then type or select the word/ numerical value they wish to filter the table by. |
| Payment or Payments | A collection of transfers to one or multiple registrations. |
| **Payment or payments** | A collection of transfers to one or multiple registrations. |
| **Transfer** | A single transfer of money to a registration. A registration will receive the number of transfers pre-decided in the program. Depending on the program, if registered late, the first transfer to the registration might be part of the third payment of a program. |
| **Log in** | How a user can access their account. |
| **Log out** | How a user can conclude their use of the platform. |

### Pages

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **All programs** | The home page of 121, contains all programs that the users are assigned to. |
| **Users** | All individuals who have access to, and work on the 121 platform e.g. CVA Officers, volunteers, Finance Officers etc. A user can have different roles in different programs. |
| **Roles** | Each user will be assigned a position for a specific program (e.g. CVA Officer, Finance Officer etc.). This is done on the **Program team** page in the program settings (**Settings** > **Users** > **Program team**). Each role has 1 or more permissions. |
| **Permissions** | Each role has different authorization to perform different actions. e.g. only a Finance Manager can start a payment. You can see which permissions are related to which role on the [Roles and permissions](users/description-roles.md) page. |
| **Settings** | The page of a program where users can review and update the program set-up: program information, FSP integration, registration data, program team and payment approval. |
| **Manual** | The place in which users can find instructions for how to use the platform. |
| **Monitoring** | The detailed information of a program and Power BI dashboard with information of the program's statistics. (if applicable). |
| **Program team** | 121 users that will be working on this program and their roles. |
| **Registrations** | The page within a program where all registrations who have registered are listed in a table. Each "Registration" represents the data submitted by individuals or households to enroll in the program. Users can perform various actions on these registrations, such as selecting them to include in the program. |
| **Payments** | The page where users can see the payments that have been made, create new payments and monitor ongoing payments. |


### Program Cards

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **Target registrations** | The amount of people/households that a program wishes to help. |
| **Included registrations** | The amount of registrations that are included in the program. |
| **Budget** | The amount of funds allocated for disbursement in a program. |
| **Cash disbursed** | The amount of funds transferred to the registrations in a program. |
| **Last payment** | The date in which the last payment was made. |

### Create new program

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **Program details** | In this page users can fill in the information of the program like it's name, amount of registrations the program wishes to reach etc. |
| **Program name** | The name of the program. Users can change it later on the **Program information** page. |

### Registration Status

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **New** | The registration was added to the program, through the Kobo form or an import. |
| **Validated** | Registration's identity was confirmed by a 121 user. Only used in programs where validation is enabled. |
| **Included** | The registration is included in the program and can receive payments. |
| **Declined** | The registration was found to be incorrectly registered (duplication, low inclusion score etc.) and will not be included in the program. |
| **Completed** | The registration received the full amount of transfers. |
| **Deleted** | The registration has been deleted, their personal details were deleted - only some details are still available for reporting. |
| **Paused** | The registration is currently not being included in the payments but is still part of the program. |

### Payments

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **Payment or transactions** | A collection of transfers to one or multiple registration(s). |
| **Transfer value** | The amount of money a registration is meant to receive in single a payment. |
| **Transfer** | A single transfer of transfers to a registration. A registration will receive the number of transfers pre-configured in the program. If registered late, the first transfer to a registration might be part of a later payment tranche. |
| **Total payment amount** | The sum value of adding up the transfer values of each included registration added to the payment. |
| **x of y approved** | A new payment has been created and it needs to be approved. The label shows how many of the required approvals were given. The approvers are set on the **Payment approval** page in the program settings. |
| **Approved** | All required approvals were given. The payment can now be started (or has already been started). |
| **In progress** | The payment is being sent to the included registrations. You cannot create a new payment while another payment is in progress. |


### Transfer statuses

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **Pending approval** | The transfer is part of a payment that still needs to be approved by all approvers. |
| **Approved** | The transfer is part of a payment approved by all approvers; it will be sent once the payment is started. |
| **Processing** | The transfer is being sent to the registration. The status might remain "processing" if the registration has not received the transfer yet, or may have received the transfer but the data in 121 is not yet reconciled. |
| **Successful** | The transfer arrived to the registration and they can now use it. |
| **Failed** | The transfer did not arrive to the registration. This could happen for a variety of reasons. |

In the reconciliation file, the status values always stay `success` or `error`.


### Debit cards (Visa Specific)

| Term | Definition |
| :------------------ | :------------------------------------------------------------------- |
| **Debit card(s)** | A rechargeable physical or digital card which is sent to the registration which they can use to purchase with. |
| **Current balance** | The amount of money currently in the wallet. |
| **Spent this month (max X)** | In some programs the amount of money a registration can spend in a single month is capped. This is a precaution measure to avoid misuse of the cards. |
| **Serial number** | The number that identifies the debit card of a registration. |

-8<- "docs/en/_snippets/contact-support.md"
