---
title: Registrations - Import Data Changes
hide:
  - toc
---

Import Data Changes function allows you to import or update registration information into the platform.

!!! Important "Who can perform actions on this page ?"
    CVA Manager can perform this action by default. The Data Changes permission can also be assigned in addition to your existing role.
    [Learn more about Users & Roles](../users/users-roles-page.md)

!!! warning "Phone numbers cannot be bulk updated"

    While it is possible to update phone numbers individually, it is not possible to bulk update phone numbers following the import data changes procedure. If you are looking to do that, we recommend to get in touch with us via [support@121.global](mailto:support@121.global).

### Format your import

Go to the **Registrations** page. You can optionally download a template including the columns you want to update.

- **Select the registrations** to update
- Click on **Import** and select **update selected registrations**
- **Select the column(s)** in the dropdownlist
- **Export the CSV**. The file will open on your device. You can now add the information into the matching columns.

![Export Data Changes button](../assets/img/MassUpdateButton.png)

![Export Data Changes Template](../assets/img/MassUpdateWindow.png)

!!! Important "Columns to always include"
    Your file must always include the referenceId to match the selected registrations. The data change function cannot match on names or other values.
    Column names must always match the 121 column names - as written in the csv template.
    Your file must be formatted as .csv


### How to import data changes

After you have formatted your file, you can now import the file. The system will automatically match the registration based on the referenceId.

!!! Warning "Only include registrations to update"
    Only import registrations for which you want to update the information. If you leave a blank cell in your imported file, this will delete the information. Make sure you exclude registrations you do not need to update.

- Click on **Choose file** and drop the csv file you created for the data changes,
- **Write a reason** for this update,
- Tick the box that you understand the impact of the data changes,
- Click on **Import file**.

![Data Changes Update file](../assets/img/MassUpdateImportFile.png)

![Data Changes Update Complete](../assets/img/MassUpdateDone.png)

---

