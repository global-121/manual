---
title: Enregistrements - Importer les modifications de données
hide:
  - toc
---

La fonction d'importation des modifications de données vous permet d'importer ou de mettre à jour les informations d'enregistrement dans la plateforme.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Le responsable CVA peut effectuer cette action par défaut. Les autres rôles ont besoin de la permission de mise à jour en masse des enregistrements : contactez notre équipe d'assistance.
    [En savoir plus sur les utilisateurs et les rôles](../users/description-roles.md)

!!! warning "Les numéros de téléphone ne peuvent pas être mis à jour en masse"

    Bien qu'il soit possible de mettre à jour les numéros de téléphone individuellement, il n'est pas possible de mettre à jour les numéros de téléphone en masse suivant la procédure d'importation des modifications de données. Si vous souhaitez le faire, nous vous recommandons de nous contacter via [support@121.global](mailto:support@121.global).

### Formatez votre importation

Allez à la page **Enregistrements**. Vous pouvez éventuellement télécharger un modèle incluant les colonnes que vous souhaitez mettre à jour.

- **Sélectionnez les enregistrements** à mettre à jour;
- Cliquez sur **Importer le fichier** et sélectionnez **Mise à jour des enregistrements sélectionnés**;
- **Sélectionnez la colonne(s)** dans la liste déroulante;
- **Exportez le CSV**. Le fichier s'ouvrira sur votre appareil. Vous pouvez maintenant ajouter les informations dans les colonnes correspondantes.

![Bouton Exporter les modifications de données](../assets/img/MassUpdateButton.png)

![Modèle Exporter les modifications de données](../assets/img/MassUpdateWindow.png)

!!! Important "Colonnes à toujours inclure"
    Votre fichier doit toujours inclure la colonne `referenceId` pour faire correspondre les enregistrements sélectionnés. Le CSV exporté ajoute automatiquement cette colonne. La fonction de modification des données ne peut pas correspondre sur les noms ou autres valeurs.
    Les noms de colonne doivent toujours correspondre aux noms de colonne 121 - tels qu'écrits dans le modèle CSV.
    Votre fichier doit être formaté en .csv


### Comment importer les modifications de données

Une fois que vous avez formaté votre fichier, vous pouvez maintenant importer le fichier. Le système fera automatiquement correspondre l'enregistrement en fonction de la colonne `referenceId`.

!!! Warning "Incluez uniquement les enregistrements à mettre à jour"
    Importez uniquement les enregistrements pour lesquels vous souhaitez mettre à jour les informations. Supprimez de votre fichier les lignes des enregistrements que vous n'avez pas besoin de mettre à jour. Si vous laissez une cellule vide dans votre fichier importé, cela supprimera les informations. Les champs obligatoires ne peuvent pas être vidés : l'importation affiche alors une erreur. Un fichier peut contenir au maximum 100 000 lignes.

- Cliquez sur **Choisir le fichier** et déposez le fichier CSV que vous avez créé pour les modifications de données;
- **Écrivez une raison** pour cette mise à jour;
- Cochez la case pour confirmer que vous comprenez l'impact des modifications de données;
- Cliquez sur **Importer le fichier**.

![Fichier de mise à jour des modifications de données](../assets/img/MassUpdateImportFile.png)

![Mise à jour des modifications de données complète](../assets/img/MassUpdateDone.png)

---
