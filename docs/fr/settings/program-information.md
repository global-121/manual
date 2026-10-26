---
title: Informations sur le programme
hide:
  - toc
---

La **page Informations sur le programme** se trouve dans les **Paramètres**. La page se compose de deux sections :

- [Informations de base sur le programme](#informations-de-base-sur-le-programme)
- [Finances du programme](#finances-du-programme)

!!! Important "Qui peut effectuer des actions sur cette page ?"
    L'administrateur du programme et le responsable CVA peuvent effectuer des actions sur cette page. [En savoir plus sur les rôles et permissions.](../users/description-roles.md)

### Informations de base sur le programme

Dans le premier tableau **:octicons-info-24: Informations de base**, vous trouverez les détails liés à votre programme. Pendant le programme, vous pouvez modifier des informations telles que le nom du programme, la description, les dates, le lieu et le nombre de personnes ciblées. Ces paramètres peuvent être modifiés à tout moment. **Toutes les modifications effectuées sur la page Informations sur le programme prennent effet immédiatement**.

- Cliquez sur **:octicons-pencil-24: Modifier** en haut à droite du tableau Informations de base ;
- Modifiez les informations nécessaires ;
- **:material-check: Sauvegardez** vos modifications ;
- Tous les champs marqués d'une étoile (*) sont obligatoires.

![Informations de base sur le programme](../assets/img/settings-programinformation-updatebasicinformation.png)

![Informations de base sur le programme](../assets/img/settings-programinformation-updatebasicinformation2.png)

Dans le tableau **Informations de base**, vous pouvez activer soit **Utilisez la « validation » dans ce programme** (1), soit **Utilisez « scope » dans ce programme** (2). Après la sauvegarde, ces paramètres s'affichent sous les noms **Activer la validation** et **Activer le périmètre (scope)**.

#### 1. Utiliser la validation dans ce programme

L'activation de la validation ajoute un statut d'enregistrement supplémentaire, **Validé(e)**, et l'action **Valider** sur la page Enregistrements.

Un formulaire de validation hors ligne peut être lié à votre programme. Ce formulaire est développé en collaboration avec votre équipe IM et notre équipe de support. Il peut être utilisé après l'enregistrement, par exemple pour un échantillonnage aléatoire de validation ou dans les programmes où les enregistrements doivent être vérifiés avant certaines actions, comme la distribution de cartes SIM ou la confirmation d'identité lors de la distribution de QR code.

Le formulaire de validation comprend un ensemble de questions de vérification qui doivent être configurées selon les exigences de votre programme.

!!! warning "Mise en place du formulaire de validation"

    **L'activation de cette fonctionnalité ne crée pas automatiquement le formulaire de validation**. Pour le configurer, veuillez contacter notre équipe de support. Nous recommandons que le formulaire soit configuré au moins sept jours ouvrés avant le déploiement sur le terrain.

#### 2. Utiliser la portée dans le programme

La **Portée** définit le groupe spécifique auquel un utilisateur est associé. Par exemple, la Croix-Rouge néerlandaise peut avoir plusieurs antennes locales par région. Chacune de ces antennes a sa propre portée dans la plateforme 121. Cela garantit que les utilisateurs d'une antenne ne peuvent accéder qu'aux données ou enregistrements liés à leur propre branche.

Si vous souhaitez configurer des portées, notre équipe de support peut vous aider. Vous devrez fournir la liste de groupements que vous souhaitez utiliser. Ceux-ci seront intégrés à votre formulaire d'enregistrement afin de garantir que toutes les données sont correctement liées à la portée appropriée. Une fois configurées, vous pourrez attribuer des portées aux utilisateurs individuels sur la page [Équipe du programme](./programteam.md).

---

### Finances du programme

Dans le second tableau **:octicons-info-24: Finances**, vous définissez les fonds, la devise, les détails de transfert et les prestataires de services financiers de votre programme. <!-- VERIFY: French portal label of the "Finance" card --> Pendant le programme, vous pouvez ajuster les **Fonds disponibles**, la **Valeur de transfert fixe**, le **Nombre de transactions par enregistrement** ou la **Devise** du programme. Ces paramètres peuvent être modifiés à tout moment. **Toutes les modifications effectuées dans le tableau Finances prennent effet immédiatement et s'appliquent à l'ensemble de la liste d'enregistrements**.

- Cliquez sur **:octicons-pencil-24: Modifier** en haut à droite du tableau Finances ;
- Modifiez les informations nécessaires, telles que la devise, la valeur de transfert fixe et le PSF ;
- **:material-check: Sauvegardez** vos modifications ;
- Tous les champs marqués d'une étoile (*) sont obligatoires.

Les **Fonds disponibles** et le **Nombre d'enregistrements ciblés** (dans le tableau Informations de base) doivent être des nombres entiers. <!-- VERIFY: French portal label of "Target registrations" --> La **Valeur de transfert fixe** peut comporter jusqu'à deux décimales. Les montants s'affichent avec le symbole de la devise du programme.

!!! Note
    Seul l'administrateur du programme peut ajouter ou retirer des PSF dans le champ **Prestataires de services financiers**. Vous ne pouvez pas retirer un PSF encore utilisé par des enregistrements.

---

-8<- "docs/fr/_snippets/contact-support.md"
