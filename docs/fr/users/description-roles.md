---
title: Description des permissions basées sur les rôles
hide:
  - toc
---

Aucun utilisateur ne peut effectuer seul toutes les actions dans la plateforme 121. La plateforme 121 applique une **séparation des tâches basée sur les rôles**, ce qui améliore la **traçabilité des responsabilités**. Par exemple, les utilisateurs ayant un profil CVA ne peuvent pas effectuer de paiements, mais peuvent mettre à jour les données des bénéficiaires. Les utilisateurs ayant un profil financier peuvent effectuer des paiements, mais ne peuvent pas mettre à jour les informations personnelles des bénéficiaires. Les rôles standard suivants sont configurés dans la plateforme 121.

Sur la **page d'accueil**, vous pouvez cliquer sur l'**icône de menu (:material-menu:)** en haut à gauche et sélectionner **Utilisateurs** ou **Rôles des utilisateurs**. Vous ne voyez ces pages que si vous avez les **droits d'administrateur de l'organisation**. Ces droits ne sont pas un rôle : l'équipe d'assistance 121 les active pour un utilisateur, quel que soit son rôle dans les programmes. Les droits d'administrateur de l'organisation vous permettent de :

- Consulter les utilisateurs et les rôles des utilisateurs, et ajouter de nouveaux utilisateurs à la plateforme,
- Créer de nouveaux programmes et copier des programmes existants.

Si vous avez besoin de ces droits, contactez l'équipe d'assistance 121.

### Page Utilisateurs

Sur la page **Utilisateurs**, vous pouvez :

- Voir la liste de tous les utilisateurs enregistrés dans votre instance 121,
- [Ajouter de nouveaux utilisateurs à la plateforme 121](../users/add-users.md) en leur envoyant une invitation,
- [Modifier le nom d'un utilisateur](../users/add-users.md#modifier-un-utilisateur),
- [Réinitialiser le mot de passe d'un utilisateur](../users/add-users.md#reinitialiser-le-mot-de-passe-dun-utilisateur).

### Page Rôles utilisateur

Sur la page **Rôles des utilisateurs**, vous pouvez :

- Voir la liste des rôles disponibles dans votre instance. Il n'est pas possible de créer de nouveaux rôles ni de nouvelles permissions.
- Pour attribuer un rôle à un utilisateur, allez dans la page Paramètres de votre programme et [suivez les instructions sur cette page](../settings/programteam.md#modifier-les-roles-et-permissions-assignes).

### Rôles utilisateur standard 121

Lorsque vous ajoutez un utilisateur à l'équipe de votre programme, vous choisissez son ou ses rôles dans la liste **Sélectionner le(s) rôle(s)**. Les noms des rôles ne sont pas traduits dans le portail : la deuxième colonne indique le nom de chaque rôle dans cette liste.

| Type | Nom dans la liste **Sélectionner le(s) rôle(s)** | Description |
| :------------------ | :------------------ | :------------------------------------------------------------------- |
| **Administrateur du programme** | Program Admin | Configure et gère le programme : informations sur le programme, intégration PSF, données d'enregistrement, équipe du programme et approbation des paiements. Ne peut pas voir les données personnelles des enregistrements. |
| **Responsable CVA** | Cash Assistance Program Manager | Gère les enregistrements avec les permissions de mise à jour en masse, de dédoublonnage, d'inclusion, d'export et de création des paiements. |
| **Gestionnaire CVA** | Cash Assistance Program Officer | Gère les enregistrements sans les permissions spécifiques réservées au responsable CVA. |
| **Responsable financier** | Finance Manager | Crée, lance, relance et réconcilie les paiements, et exporte les instructions de paiement ainsi que les rapports. |
| **Gestionnaire financier** | Finance Officer | Exporte les instructions de paiement pour le PSF et consulte les données de paiement. Il ne peut pas créer ni traiter les paiements. |
| **Lecteur** | Only view data, including Personally Identifiable Information | Peut uniquement consulter (y compris les données personnelles) et ne peut effectuer aucune action. |
| **Lecteur sans données personnelles** | Only view data, not including Personally Identifiable Information | Peut uniquement consulter, sans les données personnelles, et ne peut effectuer aucune action. |
| **Approbateur** | Approve payments | Consulte les enregistrements et les paiements et exporte les instructions de paiement. Destiné aux utilisateurs qui approuvent les paiements. |
| **Responsable de l'équipe du programme** | Program Team Manager | Gère l'équipe du programme et attribue les rôles. Consulte les enregistrements (sans données personnelles) et les paiements. |

Votre plateforme 121 dispose aussi de deux rôles techniques pour l'intégration Kobo : **Only CREATE registrations** et **Only UPDATE registrations**. Ils sont utilisés par les comptes qui connectent Kobo à 121. Ne les attribuez pas aux personnes de votre équipe. Votre organisation peut aussi avoir d'autres rôles, ou des rôles avec des permissions différentes, configurés sur demande. Si vous avez des questions sur la configuration des rôles et des permissions dans votre plateforme 121, contactez l'équipe d'assistance 121. Dans vos programmes, vous verrez également l'équipe 121 ajoutée avec le rôle Admin. Ce rôle nous permet de fournir l'assistance nécessaire. Nous n'apportons jamais de modifications à votre programme sans votre autorisation explicite.

### Permissions par rôle

| Permissions | **Administrateur du programme** | **Responsable CVA** | **Gestionnaire CVA** | **Responsable financier** | **Gestionnaire financier** | **Lecteur** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Modifier les informations du programme (détails de base et finances) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Ajouter ou retirer des PSF dans le programme | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Configurer l'intégration PSF | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Lier le formulaire Kobo, modifier les questions d'enregistrement et les champs de dédoublonnage | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Configurer le nom complet des enregistrements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Consulter l'équipe du programme | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Gérer l'équipe du programme et attribuer les rôles | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Configurer l'approbation des paiements | :octicons-check-circle-fill-24:{.yes} | | | | | |
| Aperçu de la liste d'enregistrement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Importer une liste d'enregistrement (via Excel) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Ignorer les doublons (**Ignorer le doublon**) | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Modifier les détails d'enregistrement | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Modifier **Paiements max.** et **Multiplicateur de valeur de transfert** d'un enregistrement | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Changer le PSF d'un enregistrement² | | | | | | |
| Inclure les enregistrements | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Valider les enregistrements (si la validation est activée) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Décliner les enregistrements | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Mettre en pause les enregistrements (réception des paiements) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Supprimer des enregistrements² | | | | | | |
| Mettre à jour les enregistrements en masse via un import Excel | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Envoyer des SMS aux enregistrements (si Twilio est activé) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Afficher les journaux d'activité dans le profil des enregistrements¹ | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Créer des paiements | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Supprimer des paiements qui n'ont pas été lancés | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Renommer des paiements | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Approuver des paiements³ | | | | | | |
| Lancer des paiements | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Relancer les transactions échouées | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Exporter la liste des instructions de paiement (fonction d'export-import manuel du PSF) | | | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Importer la réconciliation des paiements (fonction d'export-import manuel du PSF) | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Exporter les rapports sur les enregistrements (liste complète) | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Exporter les rapports sur les modifications de statut et de données | | :octicons-check-circle-fill-24:{.yes} | | | | |
| Exporter le rapport de paiement d'un paiement⁴ | | | | :octicons-check-circle-fill-24:{.yes} | | |
| Mettre en pause des cartes de débit (programmes Intersolve Visa) | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Lier, remplacer, fermer ou commander des cartes de débit (programmes Intersolve Visa)² | | | | | | |
| Réactiver des cartes de débit (programmes Intersolve Visa) | | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | |
| Exporter l'utilisation des cartes de débit, les cartes de débit remboursées ou les bons d'achat non utilisés² | | | | | | |
| Télécharger des fichiers | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | :octicons-check-circle-fill-24:{.yes} | | |
| Renommer ou supprimer des fichiers | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | | |
| Afficher la page de surveillance | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher le tableau de bord Power BI | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher la page Paiements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

+:octicons-check-circle-fill-24:{.yes} Fonction disponible.

¹ Le journal d'activité n'affiche que ce que le rôle est autorisé à voir. Le responsable financier et le gestionnaire financier ne voient pas les messages. L'administrateur du programme ne voit aucune activité.

² Aucun rôle standard n'a cette permission. Contactez l'équipe d'assistance 121 si vous en avez besoin.

³ L'approbation des paiements ne dépend pas du rôle. Seuls les membres de l'équipe définis comme approbateurs sur la page [Approbation des paiements](../settings/payment-approval.md) peuvent approuver un paiement.

⁴ Le rapport de paiement s'exporte depuis la page d'un paiement. L'export de tous les paiements en une fois depuis la page Paiements (**Exporter** > **Paiements**) nécessite deux permissions d'export qu'aucun rôle standard ne possède ensemble. Contactez l'équipe d'assistance 121 si vous avez besoin de cet export.

Les rôles **Lecteur sans données personnelles**, **Approbateur** et **Responsable de l'équipe du programme** ne figurent pas dans le tableau ci-dessus. Ils ont moins de permissions :

- Les trois peuvent consulter la liste d'enregistrement, la page Paiements et la page de surveillance.
- Le **Lecteur sans données personnelles** ne peut pas voir les données personnelles. Dans le journal d'activité, il ne voit que les transactions et les messages.
- L'**Approbateur** peut voir les données personnelles et exporter la liste des instructions de paiement (fonction d'export-import manuel du PSF). Pour approuver des paiements, l'utilisateur doit aussi être défini comme approbateur sur la page [Approbation des paiements](../settings/payment-approval.md).
- Le **Responsable de l'équipe du programme** peut consulter et gérer l'équipe du programme et attribuer les rôles. Il ne peut pas voir les données personnelles.

---

### Rôles supplémentaires

Des rôles et permissions supplémentaires peuvent être configurés sur demande. Contactez notre [équipe d'assistance par e-mail](mailto:support@121.global).

---

!!! Note "Ajouter des utilisateurs à un programme"
    Vous pouvez suivre ces instructions pour [ajouter des membres de l'équipe à un programme et attribuer un rôle](../settings/programteam.md).

-8<- "docs/fr/_snippets/contact-support.md"
