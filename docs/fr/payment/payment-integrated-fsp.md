---
title: Paiements - Paiement instantané avec un PSF local intégré
hide:
  - toc
---

Dans la plateforme 121, les paiements peuvent être traités de deux façons différentes : avec un **paiement manuel via un portail PSF** ou avec une **intégration PSF directe**. Vous trouverez ci-dessous les instructions étape par étape pour **traiter un paiement instantané à la liste des enregistrements inclus avec une intégration PSF directe**.

*Pour les instructions de paiements manuels via un portail PSF, veuillez vous référer aux instructions sur la [page Instructions de paiement manuel (portail PSF).](./issue-payment-fsp-portal.md)*

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Les rôles de gestionnaire financier et agent financier peuvent effectuer des actions sur la page Paiements.  
    Les utilisateurs supplémentaires peuvent ne recevoir que la permission **Affichage**. [En savoir plus sur Utilisateurs et rôles](../users/users-roles-page.md)

## Aperçu des paiements

La page Paiements de votre programme affichera des informations sur tous les versements ou tours de paiement effectués. Si aucun paiement n'a été effectué, aucun détail n'apparaîtra. Cependant, si certains versements sont déjà en cours, vous verrez chaque versement individuel. **Tant que les paiements sont toujours en cours de traitement dans le programme actuel, vous pouvez ajouter des enregistrements aux nouveaux paiements.**

## Créer un nouveau paiement

- En haut à droite, cliquez sur **Créer un nouveau paiement**.

![Bouton Créer un nouveau paiement](../assets/img/PaymentsPage.png)

- Une page s'affichera avec une liste d'enregistrements inclus dans le programme.
  *Seuls les enregistrements avec le statut **Inclus(e)** qui n'ont pas encore reçu tous leurs versements apparaîtront dans la liste. Les enregistrements qui ont reçu et complété tous leurs paiements ne seront pas affichés.*

![Liste de sélection](../assets/img/CreateNewpaymentSelect.png)

- **Sélectionnez la liste des enregistrements à ajouter** au tour de paiement comme suit.
  - Faites une **sélection individuelle** en cliquant sur la :material-checkbox-outline: sur la ligne d'enregistrement individuelle ;
  - Ou faites une **sélection en masse** en cliquant sur la :material-checkbox-multiple-marked-outline: sur la ligne du tableau supérieur **Sélectionner** ;
- En bas à droite, cliquez sur **Ajouter au paiement** ;

![Ajouter au paiement](../assets/img/StartPayment.png)

- Une fenêtre s'affiche pour confirmer le nombre d'enregistrements inclus et le montant total à transférer ;
- Cliquez sur **Lancer le paiement**. **Cette action exécutera automatiquement et enverra la demande de paiement au PSF après le flux d'approbation.**

![Lancer le paiement](../assets/img/StartPayment.png)

- Une fois le paiement traité, un tableau affichera la liste des enregistrements inclus dans le tour de paiement avec leurs statuts de paiement respectifs.

![Tableau de bord de paiement](../assets/img/PaymentReportBoard.png)

!!! info "Calendrier du processus de paiement"
    Une fois que le paiement a été traité dans la plateforme 121, le statut de paiement avec PSF intégré est mis à jour instantanément. Dans certains cas, cela peut prendre quelques minutes pour que le statut soit mis à jour (jusqu'à 1 heure) car l'information doit être traitée du PSF revient à la plateforme 121. Les rapports de paiement mis à jour ne seront disponibles qu'ensuite.
    Parce que les données de paiement sont traitées sur le serveur, vous pouvez continuer à utiliser la plateforme 121 après avoir lancé un tour de paiement.

---

## Statut de paiement

Le statut sera mis à jour automatiquement pour les PSF intégrés.

| Type | Description | Actions requises |
| :---- | :----------- | :---------- |
| **RÉUSSI** | La transaction a été envoyée aux enregistrements sur la méthode de paiement préférée. La banque a approuvé la transaction. | Aucun. |
| **EN ATTENTE** | La transaction est en cours de traitement par la banque. En attente de réconciliation de paiement. Le statut sera mis à jour automatiquement par le PSF intégré (réussi ou échoué). | Cela peut parfois prendre quelques heures. Si cela reste inchangé après 24 heures, veuillez demander une mise à jour à votre PSF. Contactez notre équipe de soutien 121 si cela reste non résolu. |
| **ÉCHOUÉ** | La transaction a échoué. Les enregistrements n'ont pas reçu de paiements. | Veuillez vérifier le message d'erreur fourni par votre banque. L'échec du paiement peut être dû à des détails bancaires incorrects, un numéro de téléphone ou un numéro d'ID selon les méthodes de paiement choisies. Contactez notre équipe de soutien 121 si cela reste non résolu. |

---

## Exporter les rapports de paiement

Pour audit financier et exigences des donateurs, vous pouvez exporter les rapports de paiement une fois terminé. Suivez les instructions sur [cette page.](../payment/payment-reporting.md)

!!! info "Fréquence des paiements"
    Les décaissements peuvent être exécutés à une certaine fréquence (quotidienne, hebdomadaire, mensuelle ou paiement unique). Tous les paiements dans la plateforme 121 doivent être déclenchés manuellement.

    Les transferts ne sont pas envoyés automatiquement à une date spécifique. Cela permet au gestionnaire financier d'examiner la disponibilité des fonds avant qu'un paiement ne soit émis aux enregistrements.


-8<- "docs/fr/_snippets/contact-support.md"
