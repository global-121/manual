---
title: Enregistrements - Liste d'exportation d'enregistrement
hide:
  - toc
---

Vous pouvez exporter des fichiers sélectionnés à personnaliser à partir de la **page d'enregistrements**. Le fichier exporté **inclura uniquement les colonnes que vous avez ajoutées à votre vue de tableau**. Si une colonne n'est pas visible dans le tableau, elle ne sera pas incluse dans l'exportation.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Le responsable CVA peut effectuer des actions sur cette page. [En savoir plus sur les utilisateurs et les rôles.](../users/description-roles.md)

### Ajout de colonnes à votre vue de tableau

- Sur la page **Enregistrements**, cliquez sur **Gérer le tableau** (:material-cog:);
- Dans la fenêtre latérale, sélectionnez les colonnes que vous pouvez afficher;
- Cliquez sur **Appliquer**.

**Remarque**. Si vous souhaitez supprimer une colonne, répétez la même action:

- Ouvrez la gestion du tableau;
- Désélectionnez la ou les colonnes;
- Cliquez sur Appliquer.

### Exportation d'enregistrements

Une fois que votre tableau affiche les colonnes dont vous avez besoin, toutes seront disponibles pour l'exportation.

- **Sélectionnez les enregistrements** que vous souhaitez exporter de la liste;
- En haut à droite du tableau, cliquez sur **Exporter**;
- Choisissez **Enregistrements sélectionnés**;
- Sélectionnez le format de fichier souhaité (**XLSX** ou **CSV**);
- Cliquez sur **Continuer**;
- Le fichier sera généré et sauvegardé dans votre dossier Téléchargements.

---

### Rapports de vérification des comptes bancaires

Si votre programme utilise la Commercial Bank of Ethiopia (CBE) ou la Banque coopérative d'Oromia (Coopbank) comme PSF, le menu **Exporter** affiche aussi **Rapport de vérification CBE** ou **Rapport de vérification de Coopbank**. Ces rapports indiquent, pour chaque enregistrement, le dernier résultat de la vérification du compte bancaire effectuée auprès de la banque.

- En haut à droite du tableau, cliquez sur **Exporter**;
- Choisissez **Rapport de vérification CBE** ou **Rapport de vérification de Coopbank**;
- Cliquez sur **Continuer**.

!!! Note
    Les données de ces rapports sont importées de la banque chaque nuit. Si vous avez modifié des données aujourd'hui, la modification n'apparaît pas encore dans le rapport.

---

### Importer les modifications de données

Vous devrez peut-être importer des modifications pour un certain nombre d'enregistrements. Vous pouvez facilement importer des modifications en suivant les instructions sur la façon d'[importer la page des modifications de données.](./import-data-changes.md) Assurez-vous d'**inclure la colonne Numéro de référence** (UUID) dans votre exportation pour réconcilier facilement les données.

---

!!! Info "CONSEIL: ne pas sauvegarder les anciens fichiers Excel"
    Pour éviter les erreurs et garder les données personnelles sécurisées, les fichiers Excel doivent être supprimés de votre ordinateur une fois que votre base de données est nettoyée et mise à jour dans la plateforme 121. De cette façon, vous aurez toujours votre dernière liste d'enregistrements mise à jour dans 121.

-8<- "docs/fr/_snippets/contact-support.md"
