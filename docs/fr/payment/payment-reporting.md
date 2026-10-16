---
title: Paiement - Rapports financiers et activité
hide:
  - toc
---

L'audit trail peut être effectué dans 121 pour les rapports financiers et l'aperçu des changements de données à un niveau général ou individuel. La page Paiements de votre programme affichera des informations sur tous les versements ou tours de paiement effectués. Si aucun paiement n'a été effectué, aucun détail n'apparaîtra. Cependant, si certains versements sont déjà en cours, vous verrez chaque versement individuel.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Seul le responsable financier peut télécharger le **Rapport de paiements** d'un paiement. Les utilisateurs qui peuvent voir la page Paiements peuvent aussi consulter le **Journal des paiements** de chaque paiement. Les exports de la page Paiements elle-même nécessitent des autorisations supplémentaires ; voir les remarques ci-dessous. [En savoir plus sur Utilisateurs et rôles](../users/description-roles.md)

## Télécharger le rapport financier général

Pour exporter un rapport financier général :

1. Allez à la **page Paiements**
2. En haut à droite, cliquez sur **Exporter**
3. Sélectionnez **Paiements** ![Rapport d'export de paiement](../assets/img/PaymentsPage.png)
4. Dans la fenêtre pop-up **Exporter les paiements**, sélectionnez si vous le souhaitez une **Date de début** et/ou une **Date de fin** pour filtrer les paiements
5. Cliquez sur **Continuer**. **Cela téléchargera un fichier Excel avec tous les enregistrements inclus dans les paiements** ![Confirmer l'export](../assets/img/ApprovePaymentExport.png)
  Le fichier sera exporté dans le dossier de téléchargement en tant que fichier Excel.

!!! Important "Qui voit le bouton Exporter sur la page Paiements ?"
    Le bouton **Exporter** de la page Paiements ne s'affiche que pour les utilisateurs qui ont à la fois l'autorisation d'exporter les données d'enregistrement avec des données personnelles et l'autorisation d'exporter les données de paiement. L'option **Paiements** nécessite aussi au moins un paiement dans le programme.

    Aucun des rôles standard n'a ces deux autorisations : le responsable CVA peut exporter les données d'enregistrement et le responsable financier peut exporter les données de paiement. Avec les rôles standard, vous ne verrez donc pas **Exporter** > **Paiements**. Un responsable financier peut télécharger les données de chaque paiement avec le **Rapport de paiements** (voir ci-dessous).

!!! Info "CONSEILS : Téléchargez uniquement les fichiers Excel si nécessaire et supprimez-les après exportation / utilisation"
    Les fichiers Excel ne doivent être téléchargés que si nécessaire pour assurer la sécurité des données personnelles. Après utilisation, les fichiers Excel doivent être supprimés de votre ordinateur pour maintenir les données personnelles sécurisées et prévenir les erreurs utilisant les anciens fichiers. De cette façon, vous aurez toujours les dernières données mises à jour dans 121.

---

## Télécharger des rapports financiers spécifiques

Pour exporter un rapport financier spécifique basé sur une date spécifique :

1. Allez à la **page Paiements** ;
2. Entrez le tour de paiement spécifique que vous recherchez ;
3. En haut à droite, cliquez sur **Exporter** ![Rapport d'export individuel](../assets/img/IndividualExportReport.png)
4. Sélectionnez **Rapport de paiements** ;
5. Une fenêtre pop-up demandera confirmation pour procéder.**Vous êtes sur le point de télécharger un fichier Excel avec tous les enregistrements inclus dans ce paiement.** ;
  Le fichier sera exporté dans le dossier de téléchargement en tant que fichier Excel.

---

## Autres exports sur la page Paiements

Selon les PSF de votre programme, le menu **Exporter** de la page Paiements propose d'autres options. Elles n'apparaissent que si le programme a au moins un paiement.

| Option | Quand elle apparaît | Ce que vous téléchargez |
| ---- | ---- | ---- |
| **Bons d’achat non utilisés** | Le programme utilise des bons Albert Heijn (papier ou WhatsApp). | Un fichier Excel avec tous les bons non utilisés. Les données ne sont pas en temps réel : le fichier indique la date et l'heure de la dernière mise à jour de chaque bon. |
| **Utilisation de la carte de débit** | Le programme utilise des cartes de débit Visa. | Un fichier Excel avec le solde de chaque carte. Les données ne sont pas en temps réel : le fichier indique la date et l'heure de la dernière mise à jour de chaque carte. |
| **Cartes de débit remboursées** | Le programme utilise des cartes de débit Visa. | Un fichier Excel avec toutes les cartes de débit remboursées, c'est-à-dire les cartes désactivées dont le solde a été reversé. |

Pour télécharger l'un de ces fichiers :

1. Allez à la **page Paiements**
2. En haut à droite, cliquez sur **Exporter**
3. Sélectionnez l'option
4. Cliquez sur **Continuer**

!!! Note "Autorisations pour ces exports"
    Chacune de ces options nécessite sa propre autorisation d'export, qu'aucun des rôles standard n'a. L'équipe de soutien 121 peut l'ajouter à un rôle. Comme ces options se trouvent dans le même menu **Exporter**, vous avez aussi besoin des autorisations du bouton **Exporter** décrites ci-dessus.

---

## Journal des paiements

Chaque page de paiement a deux onglets : **Liste des transactions** et **Journal des paiements**. Le **Journal des paiements** montre ce qui s'est passé pour le paiement : sa création, ses approbations, son lancement, ses relances, son changement de nom et les notes ajoutées.

1. Allez à la **page Paiements** ;
2. Cliquez sur le paiement que vous souhaitez consulter ;
3. Cliquez sur l'onglet **Journal des paiements**.
   Pour chaque événement, le tableau affiche l'**Activité**, une **Vue d'ensemble**, la personne qui l'a fait (**Fait par**) et la **Date et heure**. ![Onglet Journal des paiements d'un paiement](../assets/img/PaymentLog.png)

---

## Superviser le journal d'activité sur la page Paiements

Des informations de paiement détaillées peuvent être trouvées dans chaque versement séparé et pour chaque enregistrement. Pour accéder à l'aperçu individuel :

1. Allez à la **page Paiements** ;
2. Cliquez sur l'un des versements dont vous souhaiteriez lire les détails supplémentaires
   La liste incluse des enregistrements avec des informations détaillées sur la valeur de transfert, les statuts de paiement, le PSF et les dates s'affichera.
3. Pour plus de détails par individu, vous pouvez cliquer sur le lien hypertexte **Enreg. #** sur le profil d'enregistrement. Vous pouvez lire le journal d'activité à partir de différentes phases (enregistrement, inclusion, paiements).
4. Dans le journal d'activité, tous les changements ou activités seront automatiquement enregistrés, y compris les détails de paiement.

**Comment lire les journaux dans le journal d'activité ?**

| Catégorie | Description |
| ---- | ---- |
| **Modification des données** | Le journal affichera **Modifications des données** suivi du nom de la valeur ou du champ qui a été édité, le **ancien statut** et le **nouveau statut**, ainsi que le compte d'utilisateur 121 effectuant la modification. |
| **Transaction** | Le journal affichera la **date et l'heure du paiement**, le **statut du paiement** (réussi, approuvé, en attente d'approbation, échoué) et le compte d'utilisateur 121 exécutant le paiement. Dans la liste déroulante, la date de transaction, les détails de l'approbateur, la valeur de transfert et le nom du PSF seront indiqués. Pour les bons Albert Heijn, la liste déroulante affiche aussi le **Solde actuel** du bon, avec un bouton **Voir le bon d’achat**. Cliquez dessus pour voir le bon, puis cliquez sur **Télécharger** ou **Imprimer le bon d’achat**. |
| **Message** | Le journal affichera le **titre du modèle de message**, la date d'envoi, le statut d'envoi, le contenu du message et le compte d'utilisateur 121 effectuant l'action. |
| **Mise à jour du statut** | Le journal affichera la **mise à jour du statut**, la date et l'heure, le **ancien** et le **nouveau statut** et le compte d'utilisateur 121 effectuant la mise à jour du statut. |
| **Notes** | Le journal affichera l'historique des **notes**, la date et l'heure, le contenu et le compte d'utilisateur 121 ajoutant les notes au profil d'enregistrement. Une note peut être ajoutée manuellement en cliquant sur **Actions**, puis **Ajouter une note** (côté droit). |

---

-8<- "docs/fr/_snippets/contact-support.md"
