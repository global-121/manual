---
title: Enregistrements - Dédoublonnage V1
hide:
  - toc
---

Ci-dessous, vous trouverez les étapes pour vérifier les enregistrements dupliqués et dédoublonner si nécessaire. Notez que les doublons ne peuvent être vérifiés que dans un seul programme et qu'il n'y a aucun moyen de vérifier les doublons entre différents programmes dans 121.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    L'administrateur du programme peut configurer la vérification des doublons. Le responsable CVA peut effectuer les autres actions sur cette page. Le gestionnaire CVA peut aussi modifier et décliner des enregistrements, mais ne peut pas ignorer les doublons. [En savoir plus sur les utilisateurs et les rôles](../users/description-roles.md)

---

### Configuration de la vérification des doublons

**Les doublons sont identifiés en fonction de critères uniques spécifiques** tels que le numéro de téléphone ou le numéro d'identification. Ce critère est flexible et peut être choisi par l'organisation et modifié en fonction des exigences du programme. Nous recommandons d'éviter les critères qui peuvent facilement correspondre entre les enregistrements (comme le nom).

Vous définissez ces critères dans les paramètres du programme, sur la carte **Dédoublonnage** :

- Allez dans **Paramètres** et ouvrez la page **Données d'enregistrement** ;
- Sur la carte **Dédoublonnage**, cliquez sur **Modifier** ;
- Dans **Champs de dédoublonnage :**, sélectionnez un ou plusieurs champs ;
- Cliquez sur **Sauvegarder**.

Si l'un de ces champs a la même valeur pour deux enregistrements ou plus, ces enregistrements sont marqués comme **Doublon**. Les enregistrements déclinés ne sont pas pris en compte dans la vérification des doublons. Pour en savoir plus, consultez la [page Données d'enregistrement](../settings/registration-data.md#dedoublonnage).

!!! Note "Pas d'administrateur du programme dans votre équipe ?"
    Seul l'administrateur du programme peut modifier les champs de dédoublonnage. Si personne dans votre équipe n'a ce rôle, contactez notre équipe d'assistance pour configurer les champs de dédoublonnage de votre programme.

!!! Important "Les doublons bloquent l'inclusion et les paiements"
    Les enregistrements marqués comme **Doublon** ne peuvent pas être inclus. Si votre sélection contient un doublon, la plateforme affiche une erreur et aucun des enregistrements sélectionnés n'est inclus. Un paiement qui contient des doublons ne peut pas non plus être approuvé ni démarré. Traitez d'abord tous les doublons : modifiez la valeur, déclinez l'enregistrement ou ignorez le doublon, comme décrit ci-dessous.

---

### Filtrez les enregistrements dupliqués

Sur la page **Enregistrement**, et suivant les procédures d'exploitation normalisées de votre organisation, tous les enregistrements dupliqués seront listés en fonction du critère unique sélectionné.

- Si la colonne **Doublons** n'est pas visible, cliquez sur **Gérer le tableau** (:material-cog:), sélectionnez **Doublons** et cliquez sur **Appliquer** ;
- Dans la colonne **Doublons**, sélectionnez l'icône de filtre et filtrez sur **Doublon**;
- La liste filtrée affichera uniquement les enregistrements marqués comme **Doublon**;
- Cliquez sur **Enreg. #** ou **Nom** pour ouvrir le profil d'enregistrement personnel. Une bannière rouge en haut de la page intitulée **Dupliqué avec** montrera avec qui cette personne est dupliquée et le **champ correspondant**;
- Pour résoudre ce doublon, vous pouvez décider d'ignorer, de décliner ou de mettre à jour. Voir la description ci-dessous.

![Gérer le tableau](../assets/img/ShowDuplicateColumn.png)

![Filtre doublon](../assets/img/FilterDuplicate.png)

## Mettre à jour la liste d'enregistrements

Une fois que vous avez identifié le doublon, vous pouvez décider de mettre à jour la liste d'enregistrements dans la plateforme 121 comme suit:
Vous pouvez effectuer 3 actions sur la page **Enregistrements**:

- **Modifiez la valeur directement dans le profil d'enregistrement;**
- **Déclinez l'enregistrement**, en cas de double entrée pour le même enregistrement;
- **Ignorez le doublon**, en cas vos procédures d'exploitation normalisées permettent aux enregistrements de partager la même valeur - telle que le numéro de téléphone, qui peut être utilisé par plusieurs enregistrements dans la même communauté.

Ci-dessous, la solution basée sur l'une de ces 3 options:

---

### Modifiez la valeur dans le profil d'enregistrement

- Recherchez le numéro d'enregistrement en filtrant la colonne **Enreg. #**;
- Ouvrez le profil en cliquant sur **Enreg. #** sur le côté gauche. Vous verrez maintenant l'aperçu de l'enregistrement;
- Cliquez sur l'onglet **Informations personnelles**, puis sur le bouton **Modifier les informations** et recherchez la valeur à modifier; ![Modifier la valeur](../assets/img/EditInformationDuplicate.png)
- **Modifiez** la valeur. Cliquez sur **Sauvegarder** et donnez une raison;
- La nouvelle valeur est maintenant enregistrée;
- L'enregistrement sera automatiquement mis à jour et marqué comme **Unique**.

---

## Décliner l'enregistrement

- Recherchez le numéro d'enregistrement en filtrant la colonne **Enreg. #**;
- Une fois que vous avez trouvé l'enregistrement, **entrez le profil d'enregistrement**;
- En haut à droite de la page, cliquez sur **Actions** puis, sous **Mise à jour du statut**, sur **Décliner**;
- Dans la fenêtre pop-up **Décliner Enregistrements**, indiquez une raison pour décliner l'enregistrement et cliquez sur **Décliner l'enregistrement**. *Confirmez uniquement si vous êtes sûr de décliner cet enregistrement, sinon cliquez sur **Annuler**.*

![Décliner l'enregistrement](../assets/img/DeclineIgnoreDuplicate.png)

*Avez-vous accidentellement marqué un enregistrement comme décliné? Pas de problème, c'est une action réversible. Vous pouvez toujours modifier le statut en **Inclus(e)**.*

---

## Ignorer le doublon

- Une fois que vous avez trouvé l'enregistrement, **entrez le profil d'enregistrement**;
- En haut à droite de la page, cliquez sur **Actions** puis, sous **Doublons**, sur **Ignorer le doublon**;
- Dans la fenêtre pop-up **Ignorer le doublon**, indiquez une raison et cliquez sur **Approuver**. *Confirmez uniquement si vous êtes sûr d'ignorer cet enregistrement, sinon cliquez sur **Annuler**.*

![Ignorer le doublon](../assets/img/DeclineIgnoreDuplicate.png)

!!! Info "Pourquoi ignorer un doublon?"
    Dans certaines situations, le critère doublon peut être défini sur **numéros de téléphone**, ce qui signifie que si plusieurs enregistrements partagent les mêmes numéros de téléphone, la plateforme affichera les enregistrements comme doublon. Néanmoins, dans de nombreux cas, les communautés partagent le même numéro de téléphone avec plusieurs habitants. Par conséquent, en fonction de vos procédures d'exploitation normalisées, vous pouvez décider de considérer les enregistrements comme uniques si le même numéro de téléphone est partagé au sein de la communauté.

-8<- "docs/fr/_snippets/contact-support.md"
