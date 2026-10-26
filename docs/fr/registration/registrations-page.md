---
title: Enregistrements - Description de la page
hide:
  - toc
---

La page **Enregistrements** vous permet de vérifier et, si nécessaire, de mettre à jour la liste d'enregistrements et les détails avant de les inclure dans le programme pour commencer à recevoir une aide alimentaire et financière.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Tous les utilisateurs peuvent consulter la page Enregistrements. La validation, le fait de décliner, la mise en pause et la modification des enregistrements sont réservés au responsable CVA et au gestionnaire CVA. L'inclusion, l'exportation et la mise à jour en masse des enregistrements sont réservées au responsable CVA. Par défaut, aucun rôle standard ne peut supprimer des enregistrements — voir les pages correspondantes pour plus de détails. [En savoir plus sur les utilisateurs et les rôles](../users/description-roles.md)


### Aperçu des listes d'enregistrement

Superviser tous les nouveaux **enregistrements**. Le statut initial d'un enregistrement est affiché comme **Nouveau** et restera ainsi jusqu'à ce qu'un responsable CVA l'inclue (**Inclus(e)**) dans le programme, ou qu'un responsable CVA ou un gestionnaire CVA le décline (**Décliné(e)**) du programme.

![Page d'enregistrements](../assets/img/RegistrationsPage.png)

La colonne **Nom** affiche le nom complet de chaque enregistrement, tel que configuré sur la carte **Configuration du nom complet** de la page [Données d'enregistrement](../settings/registration-data.md#configurer-le-nom-complet). Si le nom complet n'est pas encore configuré, la colonne affiche **Configuration requise**. <!-- VERIFY: French portal labels of the "Name" column, "Full name setup" and "Set up needed" -->

La colonne **Valeur de transfert** affiche le montant qu'un enregistrement reçoit en un seul paiement. Il s'agit de la valeur de transfert fixe du programme multipliée par le multiplicateur de l'enregistrement, le cas échéant. Par exemple, si la valeur de transfert fixe est de 50 $ et que le multiplicateur dépend de la taille du ménage, un ménage de 3 personnes a une valeur de transfert de 150 $. La valeur de transfert s'affiche aussi sur la page de profil de chaque enregistrement. <!-- VERIFY: French portal label of the "Transfer value" column -->

- Si la colonne **Valeur de transfert** n'est pas visible, cliquez sur **Gérer le tableau** (:material-cog:), sélectionnez **Valeur de transfert** et cliquez sur **Appliquer**.

---

### Importer une liste d'enregistrement

Les listes d'enregistrements peuvent être importées de deux façons dans la plateforme 121:

- **Automatiquement**, en intégrant vos enregistrements avec votre formulaire KOBO, ou un formulaire de collecte de données équivalent, à la plateforme 121. En savoir plus sur la [page d'importation automatique d'enregistrement;](../settings/registration-data.md)
- **Manuellement**, en important une liste d'enregistrement à partir d'un fichier Excel (format .CSV). En savoir plus sur la [page de liste d'importation d'enregistrement.](../registration/registration-import-list.md)

---

### Vérifier et mettre à jour l'état d'enregistrement

Vos procédures d'exploitation normalisées peuvent inclure l'examen des détails collectés avant de valider et d'inclure les enregistrements dans le programme.
Suivez les instructions sur comment:

- [Vérifier, modifier et valider les détails d'enregistrement;](../registration/registration-validate-pa.md)
- [Dédoublonner votre liste d'enregistrement dans la plateforme 121;](../registration/registration-deduplication.md)
- [Inclure un enregistrement dans un programme;](../registration/inclusion-in-program.md)
- [Décliner un enregistrement d'un programme;](../registration/registration-reject-pa.md)
- [Mettre en pause un enregistrement dans un programme;](../payment/pause-payment-pa.md)
- [Mettre fin à la participation d'un enregistrement dans un programme.](../payment/end-payments.md)

---

### Dédoublonner l'enregistrement

Vérifiez les doublons dans la liste d'enregistrement avant d'inclure les enregistrements dans votre programme. Ce processus de validation prévient les doubles paiements et réduit les risques de fraude, nous recommandons fortement d'inclure le dédoublonnage dans votre processus de validation.

Suivez les instructions sur la [page de dédoublonnage](../registration/registration-deduplication.md)

---

### Supprimer des enregistrements

La suppression d'un enregistrement efface ses données personnelles de la plateforme 121. Ne supprimez des enregistrements que lorsque vos procédures d'exploitation normalisées ou vos règles de protection des données l'exigent.

!!! Important "Qui peut supprimer des enregistrements ?"
    La suppression d'enregistrements nécessite une permission spécifique. Par défaut, aucun rôle standard ne l'a. Contactez notre équipe d'assistance si vous devez supprimer des enregistrements.

- Sur la page **Enregistrements**, sélectionnez les enregistrements à supprimer et cliquez sur **Supprimer** en haut du tableau. Ou ouvrez un profil d'enregistrement, cliquez sur **Actions** puis, sous **Mise à jour du statut**, sur **Supprimer** ;
- La fenêtre contextuelle **Supprimer Enregistrements** apparaît. Indiquez une raison dans **Indiquer la raison de la mise à jour**. La raison est obligatoire ; ![Fenêtre Supprimer des enregistrements](../assets/img/DeleteRegistration.png)
- Cochez **Je comprends que cette action est irréversible.** ;
- Cliquez sur **Supprimer l'enregistrement** (ou **Supprimer les enregistrements**).

!!! Warning "Cette action est irréversible"
    Le statut de l'enregistrement devient **Supprimé(e)**. Ses données personnelles, ses notes et ses messages sont supprimés, et il n'apparaît plus dans le tableau Enregistrements. Vous ne pouvez pas restaurer un enregistrement supprimé.

---

-8<- "docs/fr/_snippets/contact-support.md"

