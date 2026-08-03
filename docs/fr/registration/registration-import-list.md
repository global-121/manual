---
title: Enregistrements - Importer une liste d'enregistrement à partir d'Excel
hide:
  - toc
---

Suivez les instructions sur cette page si vous souhaitez importer dans 121 des enregistrements collectés avec un autre outil de collecte de données que KoboToolbox. Si vous utilisez KoboToolbox, veuillez vous référer à cette [page](../Settings/registration-data.md).

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Le responsable CVA et le gestionnaire CVA peuvent effectuer des actions sur cette page. [En savoir plus sur les utilisateurs et les rôles](../users/description-roles.md)

Le format utilisé pour importer des enregistrements dans 121 est **Excel CSV**. Vous téléchargez d'abord le fichier modèle .csv depuis la plateforme 121, vous le remplissez avec vos données d'enregistrement, puis vous téléchargez ce fichier vers 121.

### Téléchargez le fichier modèle d'enregistrement

Le modèle est **automatiquement généré dans la plateforme 121**, basé sur le formulaire d'enregistrement du programme.
Par exemple, le formulaire d'enregistrement du programme peut inclure des critères de sélection tels que le nom, le numéro de téléphone, le nombre de membres du ménage, la province et le numéro IBAN. Le modèle inclura automatiquement ces étiquettes, correspondant aux questions du formulaire d'enregistrement. Ci-dessous, vous pouvez trouver un exemple d'un modèle basé sur un formulaire d'enregistrement KOBO.

- **Sélectionnez le programme** pour lequel vous téléchargez les enregistrements;
- Allez à la page **Enregistrements**; ![Page d'enregistrement](../assets/img/RegistrationsPageImport.png)
- Cliquez sur le bouton **Importer de nouveaux enregistrements** sur le côté droit de l'écran; ![Pop-up d'importation d'enregistrement](../assets/img/ImportRegistrationTemplate.png)
- Sélectionnez **Télécharger le fichier modèle CSV**;
- Ouvrez le modèle CSV téléchargé dans Excel;
- Copiez les données d'enregistrement que vous avez dans Excel dans le fichier .csv pour correspondre à ce format, en vous assurant que chaque information va dans la colonne correcte avec les étiquettes appropriées.

### Importer une liste d'enregistrement

- Retournez à la page **d'enregistrements** de votre **programme sélectionné**, pour lequel vous téléchargez les enregistrements;
- Cliquez sur le bouton **Importer de nouveaux enregistrements** sur le côté droit de l'écran;
- Cliquez pour choisir le fichier CSV de votre ordinateur que vous avez **déjà fait correspondre au format requis par 121**; ![Pop-up d'importation d'enregistrement](../assets/img/ImportRegistrationTemplate.png)
- Après avoir téléchargé le fichier, cliquez sur **Importer le fichier** pour appliquer l'action;
- Une autre fenêtre contextuelle apparaîtra avec la confirmation que l'importation a réussi. *Veuillez noter que cela peut prendre du temps selon le nombre d'enregistrements en cours de téléchargement.*

!!! warning "Importation infructueuse"
    Si l'importation est infructueuse ou affiche un message d'erreur, vérifiez que votre fichier Excel est correctement formaté et enregistré en tant que fichier .CSV.
Si vous avez besoin d'aide supplémentaire, veuillez ne pas hésiter à contacter notre [équipe d'assistance](mailto:support@121.global).

---

### Dédoublonnage

Les entrées en double peuvent se produire lors de l'enregistrement sur le terrain. Les enregistrements en double peuvent être vérifiés dans la plateforme 121. Vous pouvez suivre les étapes sur [cette page.](./registration-deduplication.md)

Si vous avez besoin d'explications supplémentaires, contactez notre [équipe d'assistance par e-mail](mailto:support@121.global).

---

!!! Info "CONSEIL: ne pas sauvegarder les anciens fichiers Excel"
    Pour éviter les erreurs et garder les données personnelles sécurisées, les fichiers Excel doivent être supprimés de votre ordinateur une fois que votre base de données est nettoyée et mise à jour dans la plateforme 121. De cette façon, vous aurez toujours votre dernière liste à jour des bénéficiaires enregistrés dans 121.

-8<- "docs/fr/_snippets/contact-support.md"
