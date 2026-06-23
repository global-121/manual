---
title: Paiement - Réconciliation manuelle des paiements
hide:
  - toc
---
Dans la plateforme 121, les paiements peuvent être traités de deux façons différentes : avec un **paiement manuel via un portail PSF** ou avec une **intégration PSF directe**. Vous trouverez ci-dessous les instructions étape par étape pour importer les **données de réconciliation manuelles** dans le programme, une fois que vous avez reçu les instructions de paiement de retour du PSF.

*Pour les instructions de paiement avec un prestataire de services financiers intégré, veuillez vous référer aux instructions sur la [page Paiement avec un PSF intégré.](../payment/payment-integrated-fsp.md)*

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Les rôles de gestionnaire financier et agent financier peuvent effectuer des actions sur la page Paiements.  
    Les utilisateurs supplémentaires peuvent ne recevoir que la permission **Affichage**. [En savoir plus sur Utilisateurs et rôles.](../users/users-roles-page.md)

Avant de télécharger le fichier de réconciliation dans la plateforme 121, il y a quelques étapes que vous devez suivre pour adapter le fichier à la plateforme 121.

---

## Télécharger le modèle de fichier de réconciliation

Allez à la page des paiements et entrez le tour de paiement spécifique que vous souhaiteriez mettre à jour.

- En haut à droite, cliquez sur **Importer les données de réconciliation**. ![Importer les données de réconciliation](../assets/img/IndividualExportReport.png)
- Dans la fenêtre pop-up, vous pouvez lire dans la première phrase *Importez le fichier envoyé par le PSF pour voir le statut de transfert des enregistrements inclus dans ce paiement. Téléchargez le modèle.*
- Cliquez sur **Télécharger le modèle**. ![Télécharger le modèle de réconciliation](../assets/img/ReconciliationImport.png)
- Vous pouvez maintenant commencer à éditer ce fichier avec la valeur demandée, comme suit.

## Vérifier le fichier de données de réconciliation

Quelques étiquettes doivent être ajustées selon la plateforme 121. Cela se rapporte aux statuts de paiement.
Le tableau ci-dessous indique les noms d'étiquettes corrects qui doivent être remplis dans le statut de paiement de vos données de réconciliation. Le PSF peut écrire les statuts différemment que la plateforme 121. Par conséquent, vous devez remplacer le statut par les données indiquées dans le tableau ci-dessous, colonne **Statut de données 121**, dans votre fichier de données de réconciliation (excel) :

| Statut des données 121 | Description |
| :---- | :---- |
| **succès** | Paiements réussis, terminés ou confirmés. |
| **attente** | Le paiement est en attente. Il n'est pas distribué ou ne peut pas être envoyé. |
| **erreur** | Paiements échoués, non reçus par les enregistrements en raison de données incorrectes partagées ou erreur au PSF. |


Si ces étiquettes ne correspondent pas correctement, trois erreurs peuvent se produire dans la plateforme 121 :

- Un *message d'erreur** s'affiche pour avertir que les données ne peuvent pas être téléchargées ;
- **Les statuts de paiement ne sont pas correctement mis à jour**, affichant plus de paiements échoués ou en attente car le système ne peut pas faire correspondre le statut au fichier importé ;
- Le **format n'est pas reconnu** dans la plateforme et affiche une page d'erreur.

*Certaines données peuvent être spécifiques à votre PSF, notre équipe vous conseillera lors de la mise en œuvre de votre instance 121.*

---

## Formater votre fichier en .csv

Une fois vos étiquettes mises à jour, vous pouvez enregistrer le fichier au format .csv :

- Cliquez sur **Enregistrer le fichier** dans votre fichier ;
- Ajoutez un nom de fichier, si nécessaire ;
- Sélectionnez le format **.csv** dans la liste déroulante ;
- **Enregistrez**

## Importer le fichier de réconciliation

Une fois que votre fichier mis à jour est prêt et enregistré au format .csv, vous pouvez importer le fichier de réconciliation des paiements :

- Allez à **Paiements** et sélectionnez le paiement spécifique à concilier.
- Cliquez sur **Importer les données de réconciliation** ![Importer les données de réconciliation](../assets/img/IndividualExportReport.png)
- **Déposez et déposez** ou **choisissez un fichier**
- Cliquez sur **Importer un fichier** ![Importer le fichier de réconciliation](../assets/img/ReconciliationImport.png)

!!! info "Statuts de paiement"
    Tous les statuts de paiement d'enregistrement seront mis à jour dans le tour de paiement spécifique. Vous pouvez ensuite afficher le nombre de paiements réussis, en attente et échoués au sein de la liste d'enregistrement. Lisez-en plus sur les statuts de paiement sur [cette page.](./list-status-payment-page.md)

-8<- "docs/fr/_snippets/contact-support.md"
