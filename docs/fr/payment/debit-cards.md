---
title: Paiements - Cartes de débit
hide:
  - toc
---

Cette page explique comment gérer la carte de débit Visa d'un enregistrement (mettre en pause, réactiver, remplacer, associer ou désactiver une carte) et comment commander de nouvelles cartes de débit pour votre programme.

!!! Important "Uniquement pour les programmes avec des cartes de débit Visa"
    Cette page ne concerne que les programmes qui paient via le PSF **Visa debit card** (Intersolve Visa).

    - L'onglet **Cartes de débit** d'un enregistrement n'apparaît que si l'enregistrement reçoit ses paiements via le PSF **Visa debit card**.
    - L'onglet **Cartes de débit** du **Suivi** n'apparaît que si le programme a le PSF **Visa debit card** et que votre rôle a l'autorisation de voir les commandes de cartes.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    - Consulter l'onglet **Cartes de débit** d'un enregistrement : responsable CVA, gestionnaire CVA, responsable financier, gestionnaire financier, lecteur et lecteur sans données personnelles.
    - Mettre en pause une carte : responsable CVA, gestionnaire CVA, responsable financier et gestionnaire financier.
    - Réactiver une carte : responsable CVA, responsable financier et gestionnaire financier.
    - Associer, remplacer ou désactiver une carte, et voir ou commander des cartes dans le **Suivi** : aucun des rôles standard. Ces actions nécessitent des autorisations spécifiques que l'équipe de soutien 121 peut ajouter à un rôle lorsque votre programme en a besoin.

    [En savoir plus sur Utilisateurs et rôles](../users/description-roles.md)

## Ouvrir la carte de débit d'un enregistrement

- Allez à la page **Enregistrements**.
- Cliquez sur l'enregistrement.
- Cliquez sur l'onglet **Cartes de débit**.

L'onglet affiche la carte actuelle de l'enregistrement : **Numéro de carte**, **Statut de la carte**, **Solde actuel**, le montant dépensé ce mois-ci, **Délivrée le** et **Dernière utilisation**. S'il y a plus d'informations sur le statut de la carte, elles s'affichent sous **Explication**. Les cartes précédentes de l'enregistrement sont listées sous la carte actuelle, chacune sous **Ancienne carte :**.

!!! Note "Les boutons dépendent du statut de la carte"
    Le portail n'affiche que les actions possibles pour la carte actuelle. Par exemple, **Annuler la pause de la carte** n'apparaît que si la carte est mise en pause, et **Désactiver la carte** n'apparaît pas pour une carte déjà désactivée ou expirée. **Suspendre la carte**, **Annuler la pause de la carte**, **Remplacer la carte** et **Désactiver la carte** n'apparaissent aussi que si votre rôle autorise l'action.

---

## Mettre en pause ou réactiver une carte

Pour mettre en pause une carte :

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Suspendre la carte**.
- Vérifiez le numéro de carte dans la fenêtre pop-up et cliquez sur **Suspendre la carte**.
- Un message est envoyé à l'enregistrement à propos de cette mise à jour.

Pour réactiver une carte mise en pause :

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Annuler la pause de la carte**.
- Vérifiez le numéro de carte dans la fenêtre pop-up et cliquez sur **Annuler la pause de la carte**.
- Un message est envoyé à l'enregistrement à propos de cette mise à jour.

---

## Remplacer une carte

La façon de remplacer une carte dépend du paramètre **Distribution de cartes par courrier** du PSF **Visa debit card** de votre programme.

Si les cartes sont envoyées par courrier :

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Remplacer la carte**.
- Lisez la fenêtre pop-up : la carte actuelle sera bloquée et une nouvelle carte sera émise.
- Cliquez sur **Demander une nouvelle carte**.
- Un message est envoyé à l'enregistrement à propos de cette mise à jour.

Si les cartes sont remises sur place :

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Remplacer la carte**. La fenêtre pop-up **Remplacer la carte Visa** s'ouvre.
- Scannez le code-barres au dos de la nouvelle carte que vous remettez à l'enregistrement, ou saisissez le **Numéro de série** à 19 chiffres qui se trouve sous le code-barres.
- Cliquez sur **Remplacer la carte**.

---

## Associer une carte à un enregistrement

Vous ne pouvez associer une carte que si les cartes sont remises sur place (le paramètre **Distribution de cartes par courrier** est désactivé) et que l'enregistrement n'a pas encore de carte de débit. L'onglet affiche alors **Aucune carte de débit trouvée**.

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Associer la carte Visa**.
- Scannez le code-barres au dos de la carte que vous remettez à l'enregistrement, ou saisissez le **Numéro de série** à 19 chiffres qui se trouve sous le code-barres.
- Cliquez sur **Associer la carte**.

!!! Note "Numéro de carte refusé"
    Si le numéro de carte est introuvable ou déjà associé à un autre enregistrement, le portail affiche une erreur. Vérifiez le numéro, ou utilisez une autre carte et informez votre superviseur.

---

## Désactiver une carte

La désactivation d'une carte est définitive. Les fonds de la carte sont reversés et la carte n'est pas remplacée.

- Ouvrez l'onglet **Cartes de débit** de l'enregistrement.
- Cliquez sur **Désactiver la carte**.
- Lisez l'avertissement dans la fenêtre pop-up. Cette action ne peut pas être annulée.
- Cliquez sur **Désactiver la carte**.

Les cartes désactivées figurent dans l'export **Cartes de débit remboursées** de la page Paiements. Consultez [Rapports de paiement](./payment-reporting.md).

---

## Commander des cartes de débit

Vous pouvez commander de nouvelles cartes de débit pour votre programme depuis la page **Suivi**. Les cartes sont envoyées à l'adresse que vous indiquez, par exemple celle de votre antenne.

- Allez à **Suivi**.
- Cliquez sur l'onglet **Cartes de débit**.
  *Le tableau sous **Cartes commandées** affiche les commandes envoyées avec succès à Intersolve. Il n'indique pas si les cartes ont été livrées.*
- Cliquez sur **Cartes de commande**.
- Remplissez le formulaire :
  - **Nombre de cartes** (de 1 à 700)
  - **Destinataire (nom du destinataire du colis)**
  - **Adresse e-mail du destinataire**
  - **numéro de téléphone du destinataire**
  - **Ville**, **Code Postal**, **Rue** et **Numéro de maison**
  - **Ajout** (facultatif)
- Cliquez sur **Order debit cards**.
- La commande est ajoutée au tableau. Consultez la colonne **Statut de la commande** pour suivre son avancement.

---

-8<- "docs/fr/_snippets/contact-support.md"
