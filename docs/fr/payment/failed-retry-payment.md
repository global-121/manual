---
title: Paiement - Paiements échoués et retry
hide:
  - toc
---

Lors du traitement des paiements, les statuts seront mis à jour avec **Réussi**, **En attente** et **Échoué**.
Vous trouverez ci-dessous les instructions étape par étape pour comprendre les raisons des **paiements échoués** et retry les paiements.

*Pour la description des statuts de paiement, veuillez vous référer à cette [page listant les statuts.](./list-status-payment-page.md)*

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Les rôles de gestionnaire financier et agent financier peuvent effectuer des actions sur la page Paiements.  
    Les utilisateurs supplémentaires peuvent ne recevoir que la permission **Affichage**. [En savoir plus sur Utilisateurs et rôles](../users/users-roles-page.md)

## Raisons des paiements échoués

Les paiements échoués se produisent en raison d'une erreur dans les données. Selon la manière dont le paiement est traité dans votre instance, vous pouvez consulter différentes erreurs. Votre prestataire de services financier(s) doit partager les raisons de l'échec du paiement ainsi que les données de réconciliation.

Pour filtrer les enregistrements avec paiements échoués :

- Accédez au paiement spécifique ;
- Dans la liste d'enregistrement sous le graphique, cliquez sur le filtre de colonne **Statut de transaction** et sélectionnez **Échoué** ;
- Le tableau affichera tous les paiements échoués ;
- Vous pouvez voir la raison dans la colonne **Raison**.

![Paiement échoué](../assets/img/FailedPaymentstatus.png)


**1. Détails de paiement incorrects**.
    Pour les paiements manuels et automatiques, le KYC requis peut être incorrect et ne peut pas correspondre aux informations requises par le PSF pour traiter le paiement. Les détails incorrects peuvent être les suivants : Nom complet, Numéros de téléphone, Numéro de compte bancaire, Numéro d'ID et/ou Emplacement.

Une fois que vous avez identifié les données incorrectes, vous pouvez **demander à votre gestionnaire CVA ou agent CVA de corriger les informations dans le profil d'enregistrement**. Pour lire davantage sur les instructions, visitez [cette page.](../registration/edit-pa-profile.md)


**2. Format incorrect du fichier de réconciliation**.
    Pour le paiement manuel, le fichier de réconciliation importé peut ne pas être formaté correctement. Les données ne peuvent pas correspondre dans la plateforme. Consultez les instructions sur le formatage de votre [fichier de réconciliation manuel.](./manual-payment-reconciliation.md)


**3. L'enregistrement a modifié ses détails de paiement**.
    Si un paiement échoué se produit malgré l'enregistrement ayant reçu avec succès des paiements dans le passé, cela peut être dû à une modification de ses détails de paiement ou de numéro de téléphone. En conséquence, le prestataire de services financier (PSF) peut ne pas être en mesure de faire correspondre et traiter le paiement.

Une fois que vous avez identifié les données incorrectes, vous pouvez **demander à votre gestionnaire CVA ou agent CVA de corriger les informations dans le profil d'enregistrement**. Pour lire davantage sur les instructions, visitez [cette page.](../registration/edit-pa-profile.md)


**4. La mise à jour du paiement entre PSF-121 échoue**.
    Si votre instance est intégrée à un PSF, l'intégration peut rencontrer des problèmes. Veuillez contacter l'équipe d'assistance 121 pour vérifier si cela peut être dû à une erreur d'intégration.

---

## Retry des transactions échouées

Une fois que vous avez identifié la raison, vous pouvez procéder au retry des paiements :

- Allez à la **page Paiements** et entrez le tour de paiement spécifique ;
- Sélectionnez les enregistrements dans votre liste de transactions pour lesquels vous souhaitez retry le paiement ;
- Cliquez sur le bouton :material-refresh: **Retry les transaction(s) échouées** en haut à droite de votre liste de transactions ;

  ![Bouton Retry Paiement](../assets/img/RetryPaiementbutton.png)

- **Approuvez** l'action en cliquant sur **Retry transactions**.

![Approuver le retry du paiement](../assets/img/RetryPaymentConfirm.png)

- La transaction sera automatiquement réessayée pour les enregistrements sélectionnés identifiés avec un statut de **paiement échoué** ;
- Le statut de paiement sera mis à jour.

!!! import "Retry basé sur vos méthodes de paiement"
    Si vous traitez le paiement avec un PSF intégré, la demande de paiement et la réconciliation seront effectuées automatiquement.

    Cependant, **si vous traitez les paiements avec une export-import manuel**, veuillez suivre les mêmes étapes à nouveau. Les instructions supplémentaires peuvent être lues sur [la page de paiement manuel.](../payment/issue-payment-fsp-portal.md)

---

**Et si les paiements continuent d'échouer ?**

Nous vous recommandons de contacter notre équipe d'assistance pour vérifier les raisons de l'échec des paiements ainsi que votre équipe financière. Nous fournirons des conseils sur les prochaines étapes.

-8<- "docs/fr/_snippets/contact-support.md"
