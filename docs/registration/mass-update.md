---
title: Registrations - Mass Update
hide:
  - toc
---

Mass update function allows you to import or update registration information into the platform.

!!! Important "Who can perform actions on this page ?"
    CVA Manager can perform this action by default. The Mass Update permission can also be assigned in addition to your existing role.
    [Learn more about Users & Roles](../users/users-roles-page.md)

### Format your import

Go to the **Registrations** page. You can optionally download a template including the columns you want to update.

- **Select the registrations** to update
- Click on **Import** and select **update selected registrations**
- **Select the column(s)** in the dropdownlist,
- **Export the CSV**. The file will open on your device. You can now add the information into the matching columns.

![Export Mass Update button](../assets/img/MassUpdateButton.png)

![Export Mass Update Template](../assets/img/MassUpdateWindow.png)

!!! Important "Columns to always include"
    Your file must always include the referenceId to match the selected registrations. The mass update function cannot match on names or other values.
    Column names must always match the 121 column names - as written in the csv template.
    Your file must be formatted as .csv


### How to do a mass update

After you have formatted your file, you can now import the file. The system will automatically match the registration based on the referenceId.

!!! Warning "Only include registrations to update"
    Only import registrations for which you want to update the information. If you leave a blank cell in your imported file, this will delete the information. Make sure you exclude registrations you do not need to update.

- Click on**Choose fil** and drop the csv file you created for the mass update,
- **Write a reason** for this update,
- Tick the box that you understand the impact of the mass update,
- Click on **Import file**.

![Mass Update file](../assets/img/MassUpdateImportFile.png)

![Mass Update Complete](../assets/img/MassUpdateDone.png)

---

