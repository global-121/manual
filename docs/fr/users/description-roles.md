---
title: Description des permissions basées sur les rôles
hide:
  - toc
---

Aucun utilisateur ne peut effectuer seul toutes les actions dans la plateforme 121. La plateforme 121 applique une **séparation des tâches basée sur les rôles**, ce qui améliore la **traçabilité des responsabilités**. Par exemple, les utilisateurs ayant un profil CVA ne peuvent pas effectuer de paiements, mais peuvent mettre à jour les données des bénéficiaires. Les utilisateurs ayant un profil financier peuvent effectuer des paiements, mais ne peuvent pas mettre à jour les informations personnelles des bénéficiaires. Les rôles standard suivants sont configurés dans la plateforme 121.

Sur la **page d'accueil**, vous pouvez cliquer sur l'**icône de menu (:material-menu:)** en haut à gauche et sélectionner **Utilisateurs** ou **Rôles utilisateur**. Veuillez noter que cet accès doit être demandé spécifiquement à l'équipe 121, car il permet non seulement de consulter les utilisateurs et les rôles utilisateur, mais aussi d'ajouter de nouveaux utilisateurs à la plateforme.

### Page Utilisateurs

Sur la page **Utilisateurs**, vous pouvez :

- Voir la liste de tous les utilisateurs enregistrés dans votre instance 121,
- [Ajouter de nouveaux utilisateurs à la plateforme 121](../users/add-users.md) en leur envoyant une invitation,
- [Réinitialiser le mot de passe d'un utilisateur](../users/add-users.md).

### Page Rôles utilisateur

Sur la page **Rôles utilisateur**, vous pouvez :

- Voir la liste des rôles disponibles dans votre instance. Il n'est pas possible de créer de nouveaux rôles ni de nouvelles permissions.
- Pour attribuer un rôle à un utilisateur, allez dans la page Paramètres de votre programme et [suivez les instructions sur cette page](../Settings/programteam.md#modifier-les-roles-et-permissions-assignes).

### Rôles utilisateur standard 121

| Type | Description |
| :------------------ | :------------------------------------------------------------------- |
| **Administrateur du programme** | Supervise la création et la gestion du programme. |
| **Responsable CVA** | Gère les enregistrements avec les permissions de mise à jour en masse, de dédoublonnage, d'inclusion et de création des paiements. |
| **Gestionnaire CVA** | Gère les enregistrements sans les permissions spécifiques réservées au responsable CVA. |
| **Responsable financier** | Crée, envoie et réconcilie les paiements, et exporte les instructions de paiement ainsi que les rapports. |
| **Gestionnaire financier** | Exporte les instructions de paiement pour le PSF et consulte les données de paiement. Il ne peut pas créer ni traiter les paiements. |
| **Lecteur** | Peut uniquement consulter et ne peut effectuer aucune action. |

Il peut y avoir des rôles supplémentaires disponibles sur votre plateforme 121. Nous vous conseillons de ne pas les utiliser. Si vous avez des questions sur la configuration des rôles et des permissions dans votre plateforme 121, contactez l'équipe d'assistance 121. Dans vos programmes, vous verrez également l'équipe 121 ajoutée avec le rôle Admin. Ce rôle nous permet de fournir l'assistance nécessaire. Nous n'apportons jamais de modifications à votre programme sans votre autorisation explicite.

### Permissions par rôle

| Permissions | **Administrateur du programme** | **Responsable CVA** | **Gestionnaire CVA** | **Responsable financier** | **Gestionnaire financier** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Aperçu des utilisateurs et des rôles | :material-progress-question:{.req} | | | | |
| Ajouter de nouveaux utilisateurs 121 | :material-progress-question:{.req} | | | | |
| Réinitialiser le mot de passe des utilisateurs 121 | :material-progress-question:{.req} | | | | |
| Créer de nouveaux programmes* | :octicons-check-circle-fill-24:{.yes} | | | | |
| Gérer l'équipe du programme et attribuer les rôles | :octicons-check-circle-fill-24:{.yes} | | | | |
| Modifier les informations du programme (détails de base et budget) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Aperçu de la liste d'enregistrement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Importer une liste d'enregistrement (via Excel) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Dédoublonner les enregistrements | | :octicons-check-circle-fill-24:{.yes} | | | |
| Modifier les détails d'enregistrement | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Inclure les enregistrements | | :octicons-check-circle-fill-24:{.yes} | | | |
| Valider les enregistrements | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Décliner les enregistrements | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Suspendre les enregistrements (réception des paiements) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Mettre à jour les enregistrements en masse via un import Excel | | :octicons-check-circle-fill-24:{.yes} | | | |
| Envoyer des SMS aux enregistrements (si Twilio est activé) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Afficher les journaux d'activité dans le profil des enregistrements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Créer des paiements | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | |
| Envoyer des paiements | | | | :octicons-check-circle-fill-24:{.yes} | |
| Exporter les instructions de paiement (fonction d'export-import manuel du PSF) | | | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Importer la réconciliation des paiements (fonction d'export-import manuel du PSF) | | | | :octicons-check-circle-fill-24:{.yes} | |
| Exporter les rapports sur les enregistrements (liste complète) | | :octicons-check-circle-fill-24:{.yes} | | | |
| Exporter les rapports sur les modifications de données | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Exporter les rapports de paiement | | | | :octicons-check-circle-fill-24:{.yes} | |
| Télécharger des fichiers | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | |
| Renommer ou supprimer des fichiers | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Afficher la page de surveillance | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher le tableau de bord Power BI | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher la page Paiements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

+:octicons-check-circle-fill-24:{.yes} Fonction disponible.

+:material-progress-question:{.req} Fonction disponible sur demande auprès de l'équipe d'assistance 121.

\* Cette action nécessite les droits d'administrateur de l'organisation, activés par l'équipe d'assistance 121. Si vous êtes administrateur de programme et que vous ne pouvez pas créer de programmes, veuillez contacter l'équipe d'assistance 121 pour mettre cela en place.

---

### Rôles supplémentaires

Des rôles et permissions supplémentaires peuvent être configurés sur demande. Contactez notre [équipe d'assistance par e-mail](mailto:support@121.global).

---

!!! Note "Ajouter des utilisateurs à un programme"
    Vous pouvez suivre ces instructions pour [ajouter des membres de l'équipe à un programme et attribuer un rôle](../Settings/programteam.md).

-8<- "docs/fr/_snippets/contact-support.md"
