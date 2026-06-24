---
title: Enregistrements - Dédoublement V1
hide:
  - toc
---

Ci-dessous, vous trouverez les étapes pour vérifier les enregistrements dupliqués et dédoublonner si nécessaire. Notez que les doublons ne peuvent être vérifiés que dans un seul projet et qu'il n'y a aucun moyen de vérifier les doublons entre différents programmes dans 121.

!!! Important "Qui peut effectuer des actions sur cette page ?"
    L'administrateur du programme, l'agent d'assistance et le gestionnaire d'assistance peuvent effectuer des actions.
    Des utilisateurs supplémentaires peuvent uniquement avoir des permissions d'affichage sur cette page. [En savoir plus sur les utilisateurs et les rôles](../users/users-roles-page.md)

---

### Configuration de la vérification des doublons

**Les critères de détection des doublons ont été configurés dans votre formulaire Kobo.**

**Les doublons sont identifiés en fonction de critères uniques spécifiques** tels que le numéro de téléphone ou le numéro d'identification. Ce critère est flexible et peut être choisi par l'organisation et modifié en fonction des exigences du programme. Nous recommandons d'éviter les critères qui peuvent facilement correspondre entre les enregistrements (comme le nom).

Le critère peut être configuré directement dans votre Kobo, en marquant la question comme **+dedup** dans votre formulaire. La plateforme 121 reconnaîtra alors la valeur comme critère dupliqué. Demandez à notre équipe d'ajuster le critère en fonction de votre programme.

---

### Filtrez les enregistrements dupliqués

Sur la page **Enregistrement**, et suivant les procédures d'exploitation normalisées de votre organisation, tous les enregistrements dupliqués seront listés en fonction du critère unique sélectionné.

- Cliquez sur l'icône :material-cog: pour **gérer le tableau**;
- Sélectionnez **Doublons** et cliquez sur **Appliquer** pour afficher la colonne de doublons dans le tableau;
- Dans la colonne **Doublons**, sélectionnez l'icône de filtre et filtrez sur **Doublon**;
- La liste filtrée affichera uniquement les enregistrements marqués comme **Doublon**;
- Cliquez sur **Enreg. #** ou **Nom** pour ouvrir le profil d'enregistrement personnel. Une bannière rouge en haut de la page intitulée **Dupliqué avec** montrera avec qui cette personne est dupliquée et le **champ correspondant**;
- Pour résoudre ce doublon, vous pouvez décider d'ignorer, de refuser ou de mettre à jour. Voir la description ci-dessous.

![Gérer le tableau](../assets/img/ShowDuplicateColumn.png)

![Filtre doublon](../assets/img/FilterDuplicate.png)

!!! Note "Configuration de votre critère de doublons dans Kobo"
    **Les doublons sont identifiés en fonction de critères uniques spécifiques** tels que le numéro de téléphone ou le numéro d'identification. Ce critère est flexible et peut être choisi par l'organisation et modifié en fonction des exigences du programme. Nous recommandons des critères uniques pour faciliter la vérification des doublons.

    Le critère peut être configuré directement dans votre Kobo, en marquant la question comme **+dedup** dans votre formulaire. La plateforme 121 reconnaîtra alors la valeur comme critère dupliqué. Demandez à notre équipe d'ajuster le critère en fonction de votre programme.


## Mettre à jour la liste d'enregistrements

Une fois que vous avez identifié le doublon, vous pouvez décider de mettre à jour la liste d'enregistrements dans la plateforme 121 comme suit:
Vous pouvez effectuer 3 actions sur la page **Enregistrements**:

- **Modifiez la valeur directement dans le profil d'enregistrement;**
- **Refusez l'enregistrement**, en cas de double entrée pour le même enregistrement;
- **Ignorez le doublon**, en cas vos procédures d'exploitation normalisées permettent aux enregistrements de partager la même valeur - telle que le numéro de téléphone, qui peut être utilisé par plusieurs enregistrements dans la même communauté.

Ci-dessous, la solution basée sur l'une de ces 3 options:

---

### Modifiez la valeur dans le profil d'enregistrement

- Recherchez le numéro d'enregistrement en filtrant la colonne **Enreg. #**;
- Ouvrez le profil en cliquant sur **Enreg. #** sur le côté gauche. Vous verrez maintenant l'aperçu de l'enregistrement;
- Cliquez sur l'onglet **Informations personnelles**, puis sur le bouton **Modifier** et recherchez la valeur à modifier; ![Modifier la valeur](../assets/img/EditInformationDuplicate.png)
- **Modifiez** la valeur. Cliquez sur **Enregistrer** et donnez une raison;
- La nouvelle valeur est maintenant enregistrée;
- L'enregistrement sera automatiquement mis à jour et marqué comme **Unique**.

![Modifier les informations](../assets/img/EditInformationDuplicate.png)

---

## Refuser l'enregistrement

- Recherchez le numéro d'enregistrement en filtrant la colonne **Enreg. #**;
- Une fois que vous avez trouvé l'enregistrement, **entrez le profil d'enregistrement**;
- En haut à gauche de la page, cliquez sur **Action** puis sur le bouton **Refuser**;
- **Approuvez** l'action. *Confirmez uniquement si vous êtes sûr de refuser cet enregistrement, sinon annulez.*
- Vous devrez entrer une raison pour refuser le bénéficiaire.

![Refuser l'enregistrement](../assets/img/DeclineIgnoreDuplicate.png)

*Avez-vous accidentellement marqué un enregistrement comme refusé? Pas de problème, c'est une action réversible. Vous pouvez toujours modifier le statut en **Inclus(e)**.*

---

## Ignorer le doublon

- Une fois que vous avez trouvé l'enregistrement, **entrez le profil d'enregistrement**;
- En haut à gauche de la page, cliquez sur **Action** puis sur le bouton **Ignorer le doublon**;
- **Approuvez** l'action. *Confirmez uniquement si vous êtes sûr d'ignorer cet enregistrement, sinon annulez.*

![Ignorer le doublon](../assets/img/DeclineIgnoreDuplicate.png)

!!! Info "Pourquoi ignorer un doublon?"
    Dans certaines situations, le critère doublon peut être défini sur **numéros de téléphone**, ce qui signifie que si plusieurs enregistrements partagent les mêmes numéros de téléphone, la plateforme affichera les enregistrements comme doublon. Néanmoins, dans de nombreux cas, les communautés partagent le même numéro de téléphone avec plusieurs habitants. Par conséquent, en fonction de vos procédures d'exploitation normalisées, vous pouvez décider de considérer les enregistrements comme uniques si le même numéro de téléphone est partagé au sein de la communauté.

-8<- "docs/fr/_snippets/contact-support.md"
