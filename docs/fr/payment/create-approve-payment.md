---
title: Créer, approuver et démarrer les paiements
hide:
  - toc
---

Les paiements sont créés et lancés à partir de la **page Paiements**. Chaque paiement doit d'abord être approuvé par un approbateur avant de pouvoir être lancé. Voici les trois étapes principales pour créer, approuver et lancer un paiement dans votre programme, avant que les instructions de paiement ne soient partagées avec le PSF.

- [1. Créer une demande de paiement](#1-créer-une-demande-de-paiement)
- [2. Approuver les paiements](#2-approuver-les-paiements)
- [3. Lancer le paiement](#3-lancer-le-paiement)
- [4. Supprimer le paiement](#4-supprimer-le-paiement)
- [5. Instructions de paiement](#5-instructions-de-paiement)

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Les rôles de gestionnaire financier et agent financier peuvent créer et lancer des paiements. Les approbateurs doivent être sélectionnés et ajoutés à chaque programme.
    Les utilisateurs supplémentaires peuvent ne recevoir que la permission **Affichage** sur cette page. [En savoir plus sur Utilisateurs et rôles](../users/users-roles-page.md)

## 1. Créer une demande de paiement

Pour lancer une nouvelle demande de paiement :

- En haut à droite, cliquez sur **Créer un nouveau paiement** ![Bouton Créer un nouveau paiement](../assets/img/PaymentsPage.png)
- Une page s'affichera avec une liste d'enregistrements **inclus** dans le programme.
  *Seuls les enregistrements avec le statut **Inclus** qui n'ont pas encore reçu tous leurs versements apparaîtront dans la liste. Les enregistrements qui ont reçu et complété tous leurs paiements ne seront pas affichés.* ![Liste de sélection](../assets/img/CreateNewpaymentSelect.png)
- **Sélectionnez la liste des enregistrements à ajouter** au tour de paiement comme suit.
    - Faites une **sélection individuelle** en cliquant sur la :material-checkbox-outline: sur la ligne d'enregistrement individuelle ;
    - Ou faites une **sélection en masse** en cliquant sur la :material-checkbox-multiple-marked-outline: sur la ligne du tableau supérieur **Sélectionner**
- En bas à droite, cliquez sur **Ajouter au paiement** ; ![Ajouter au paiement](../assets/img/StartPayment.png)
- Confirmez les informations de paiement ;
- Cliquez sur **Créer un paiement**.

!!! Important "Aucun changement possible dans la liste de paiement"
    Une fois qu'un paiement est créé, ses détails ne peuvent pas être modifiés. Cela inclut la liste des personnes dans le paiement et la valeur du transfert.
    Avant de créer un paiement, assurez-vous d'examiner attentivement la valeur du transfert, le budget et les enregistrements sélectionnés. Si nécessaire, appliquez des filtres tels que l'emplacement ou le PSF et confirmez votre sélection avant de continuer.

    Pour modifier la valeur du transfert avant de créer un paiement, veuillez vous référer à [Paramètres du programme et budget](../Settings/payment-budget-settings.md)

## 2. Approuver les paiements

Une fois la demande de paiement créée, elle doit être approuvée par un approbateur.

- Allez à la **page Paiements**,
- Cliquez sur les cartes de paiement avec le message **XX de XX approuvés**
*Dans la transaction, vous pouvez examiner la liste des enregistrements inclus dans la liste de paiement, le montant total réservé et le nombre total d'enregistrements.*
- En fonction de cette information, vous pouvez soit approuver, soit laisser le paiement. ![Approuver ou Annuler](../assets/img/ApprovePaymentFinal.png)
- Si vous êtes d'accord, cliquez sur **Approuver le paiement**. **Le statut de la demande de paiement sera mis à jour.**
- Si vous n'êtes pas d'accord, cliquez sur **Annuler**. *Le paiement restera en attente. Selon votre SOP, informez vos collègues pertinents pour suivi.*
- Une fois approuvé par tous les approbateurs, le statut de la demande de paiement passera de **En attente d'approbation** à **Approuvé**

!!! Note "Flux d'approbateurs"
    Les approbations sont basées sur des seuils. C'est le montant minimum auquel cette approbation est requise. Au moins un approbateur avec seuil 0 est nécessaire pour assurer l'approbation de tous les paiements. Vous pouvez affecter plusieurs utilisateurs au même seuil et n'exiger que l'approbation de l'un d'eux (par exemple, le premier à se connecter). Les approbateurs doivent être affectés au programme sans portée. Les notifications par e-mail aux approbateur(s) et créateur de paiement sont automatiques et incluent un lien vers la page de paiement.

    Actuellement, les approbateurs et leurs seuils respectifs sont définis par programme par l'équipe 121. Si aucun utilisateur n'a été affecté jusqu'à présent ou si vous souhaitez modifier la configuration, veuillez partager les noms, l'ordre et les montants avec support@121.global.


## 3. Lancer le paiement

Une fois que le paiement a été approuvé par tous les approbateurs de la liste, le gestionnaire financier peut **lancer le paiement**.

- Entrez la carte de paiement **approuvée**,
- Cliquez sur **lancer le paiement** en haut à droite, ![Lancer le paiement](../assets/img/StartPaymentApproved.png)
- Le paiement commencera,
- Tous les statuts de paiement changeront de **Approuvé** à **En cours de traitement**.

---

## 4. Supprimer le paiement

- Vous pouvez supprimer les paiements qui sont en attente d'approbation. Cliquez sur :material-dots-horizontal: à côté du bouton d'export en haut à droite de la page.
- La suppression d'un paiement n'affecte pas le statut des enregistrements (inclus) ou le nombre de paiements reçus.
- Les utilisateurs qui peuvent créer des paiements ont également la permission de supprimer.

---

## 5. Instructions de paiement

Dans la plateforme 121, les paiements peuvent être traités de deux façons différentes : avec un **paiement manuel via un portail PSF** ou avec une **intégration PSF directe**.

- Pour les instructions de paiement avec une fonction d'export-import manuel, veuillez vous référer à la [page Instructions de paiement manuel](./issue-payment-fsp-portal.md). *Le statut de paiement restera sur **traitement** jusqu'à ce que la réconciliation ait été importée*,
- ou les instructions de paiement avec un prestataire de services financiers intégré, veuillez vous référer aux instructions sur la [page Paiement avec un PSF intégré](./payment-integrated-fsp.md)

---

Vous trouverez ci-dessous les différents statuts de paiement.

| Statut | Description | Actions requises |
| :------ | :----------- | :---------------- |
| **EN ATTENTE D'APPROBATION** | La demande de paiement a été créée mais attend toujours l'approbation de tous les approbateurs. | Les approbateurs doivent approuver le paiement pour continuer. |
| **APPROUVÉ** | La demande de paiement a été approuvée par tous les approbateurs. | Le paiement doit être lancé pour continuer. |
| **RÉUSSI** | Le paiement a été envoyé aux enregistrements et ils peuvent maintenant l'utiliser. | Aucun. |
| **EN COURS DE TRAITEMENT** | Le paiement attend la confirmation d'un ou plusieurs agents financiers. Le transfert n'a pas encore été envoyé aux enregistrements sélectionnés pour ce tour de paiement ou le fichier de réconciliation n'a pas encore été importé. | Importez le fichier de réconciliation dans la plateforme 121 pour mettre à jour le statut. |
| **ÉCHOUÉ** | La transaction a échoué. Les enregistrements n'ont pas reçu de paiements. | Veuillez vérifier le message d'erreur fourni par votre banque. L'échec du paiement peut être dû à des détails bancaires incorrects, un numéro de téléphone ou un numéro d'ID selon les méthodes de paiement choisies. Vous pouvez réessayer. Contactez notre équipe de soutien 121 si cela reste non résolu. |

-8<- "docs/fr/_snippets/contact-support.md"
