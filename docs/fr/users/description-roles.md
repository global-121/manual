---
title: Description des permissions basées sur les rôles
hide:
  - toc
---

Aucun utilisateur unique ne peut effectuer toutes les actions dans la plateforme 121. La plateforme 121 suit **une séparation des tâches basée sur les rôles**, ce qui améliore la **responsabilité** des tâches. Par exemple, les utilisateurs ayant un profil d'assistance alimentaire et financière ne pourront pas effectuer de paiements mais seront en mesure de mettre à jour les données d'enregistrement. Les utilisateurs ayant un profil financier peuvent effectuer des paiements, mais ne peuvent pas mettre à jour les informations personnelles des bénéficiaires. Les rôles standard suivants sont configurés dans la plateforme 121.

### Rôles utilisateur standard 121

| Type | Description |
| :------------------ | :------------------------------------------------------------------- |
| **Administrateur du programme** | Administrateur système, supervisant l'accès des utilisateurs sur la plateforme et gérant le projet avec une vue d'ensemble de la progression du projet. |
| **Agent d'assistance** | Agent pour l'assistance alimentaire et financière. |
| **Gestionnaire d'assistance** | Gestionnaire de l'assistance alimentaire et financière. |
| **Agent financier** | Agent pour les opérations financières et l'audit. |
| **Gestionnaire financier** | Gestionnaire des opérations financières, instructions de paiement. |
| **Affichage** | Utilisateurs du portail autorisés à afficher uniquement et ne peuvent pas effectuer d'actions. |
| **Gestionnaire d'utilisateurs** | Le gestionnaire d'utilisateurs peut créer des comptes utilisateurs, réinitialiser les mots de passe et ajouter des utilisateurs aux équipes du programme. |

### Permissions par rôle


| Permissions | **Administrateur du programme** | **Gestionnaire d'assistance** | **Agent d'assistance** | **Agent financier** | **Gestionnaire financier** |
| :-------------------------------------------------------------- | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: | :-----------------------------------: |
| Aperçu des utilisateurs et des rôles | :material-progress-question:{.req} | | | | |
| Ajouter de nouveaux utilisateurs 121 | :material-progress-question:{.req} | | | | |
| Réinitialiser le mot de passe des utilisateurs 121 | :material-progress-question:{.req} | | | | |
| Modifier et mettre à jour les paramètres des programmes (informations et budget) | :octicons-check-circle-fill-24:{.yes} | | | | |
| Aperçu de tous les programmes actifs | :octicons-check-circle-fill-24:{.yes} | | | | |  
| Afficher uniquement les programmes actifs assignés à l'utilisateur | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Créer de nouveaux projets dans 121 | :octicons-check-circle-fill-24:{.yes} | | | | |
| Gérer les membres de l'équipe et assigner les rôles dans les projets | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Aperçu de la liste d'enregistrement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Importer une liste d'enregistrement (via Excel) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Modifier les détails d'enregistrement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Inclure les enregistrements dans les projets | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Valider la liste d'enregistrement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Refuser les enregistrements d'un projet | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Enregistrements en double (et exporter un rapport de doublon) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Suspendre les enregistrements pour recevoir des paiements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Supprimer les enregistrements du projet | | | | | |
| Importer (en masse) les modifications de données dans les enregistrements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | | |
| Envoyer des SMS aux enregistrements (SMS unidirectionnel) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | | |
| Afficher les journaux d'activité dans le profil des enregistrements | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Créer de nouveaux paiements aux enregistrements | | | | | :octicons-check-circle-fill-24:{.yes} |
| Envoyer des paiements aux enregistrements | | | | | :octicons-check-circle-fill-24:{.yes} |
| Exporter les instructions de paiement (fonction d'exportation-importation manuelle FSP) | | | | | :octicons-check-circle-fill-24:{.yes} |
| Réconcilier les paiements (fonction d'exportation-importation manuelle FSP) | | | | | :octicons-check-circle-fill-24:{.yes} |
| Exporter les rapports sur l'enregistrement (liste complète) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Exporter les rapports sur les modifications de données | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Exporter les rapports de paiement | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Exporter le rapport de vérification des numéros de compte | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher la page de surveillance | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher le tableau de bord PowerBi | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |
| Afficher les tableaux de bord de paiement (page de paiement) | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} | :octicons-check-circle-fill-24:{.yes} |

:octicons-check-circle-fill-24:{.yes} Fonction disponible.:material-progress-question:{.req}  Fonction non disponible, à la demande de l'équipe d'assistance 121.

---

### Rôles supplémentaires

Des rôles et permissions supplémentaires peuvent être configurés sur demande. Contactez notre [équipe d'assistance par e-mail](mailto:support@121.global).

---

!!! note "Ajouter des utilisateurs à un programme"
    Vous pouvez suivre ces instructions pour [ajouter des membres de l'équipe à un programme et assigner un rôle](../team/add-team-members.md).

-8<- "docs/fr/_snippets/contact-support.md"
