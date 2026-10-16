---
title: Intégration FSP
hide:
  - toc
---

!!! Important "Qui peut effectuer des actions sur cette page ?"
    L'administrateur du programme peut consulter, configurer et mettre à jour l'intégration PSF.

Chaque fois qu'un nouveau programme commence, l'administrateur du programme configure le Prestataire de Services Financiers (PSF). Vous pouvez ajouter plusieurs PSF au même programme. Vous pouvez également sélectionner l'option manuelle via Excel, ce qui permet d'exporter les instructions du PSF puis d'importer le fichier de réconciliation.

La **Étape 3 de la création du programme** demande de sélectionner le(s) PSF. Cela peut également être fait dans le tableau Budget de la page **Informations sur le programme**. Si cela est fait, le(s) PSF apparaîtront automatiquement sur la page **Intégration FSP** sous **Paramètres**.

### Vérifier les champs requis du formulaire d'enregistrement

Pour vous assurer que votre formulaire d'enregistrement contient les champs requis pour le(s) PSF, vous pouvez cliquer sur **:material-chevron-down: Exigences relatives au formulaire** sur la carte du PSF.
![Champs requis](../assets/img/settings-fspintegration-requiredfields.png)

Votre formulaire doit correspondre exactement aux noms de colonnes indiqués. Si vous avez besoin d'aide, vous pouvez contacter l'équipe 121.
![Champs requis](../assets/img/settings-fspintegration-requiredfields2.png)

### Compléter la configuration du PSF

Pour utiliser l'intégration, vous devez **compléter la configuration** en saisissant les identifiants fournis par le PSF. Si cela n'est pas encore fait, la plateforme 121 affiche la notification suivante, et la carte du PSF indique **Intégration requise** :
![Intégration requise](../assets/img/settings-fspintegration-required.png)

- Sur la carte du PSF, cliquez sur **Intégrer** ;
- Saisissez les identifiants ;
- Cliquez sur **Intégrer le PSF**.

### Mettre à jour la configuration PSF

Vous pouvez mettre à jour les PSF à tout moment pendant votre programme.

- Si vous souhaitez reconfigurer un PSF, cliquez sur les 3 points :material-dots-vertical: et sélectionnez **Reconfigurer** ;
- Si vous souhaitez supprimer un PSF, retirez le PSF dans Informations sur le programme. Notez que vous ne pouvez pas supprimer un PSF déjà lié à des enregistrements.
- Si vous souhaitez ajouter un PSF, ajoutez le PSF dans Informations sur le programme puis configurez-le dans Intégration FSP.

![Reconfigurer](../assets/img/settings-fspintegration-reconfigure2.png)

### PSF Excel

Si vous utilisez l'option manuelle via Excel, vous pouvez configurer plusieurs PSF Excel dans le même programme.

Pour ajouter un autre PSF Excel :

- Sur la carte d'un PSF Excel, cliquez sur les 3 points :material-dots-vertical: ;
- Sélectionnez **Créez un autre PSF Excel** ; ![Menu du PSF Excel avec Créez un autre PSF Excel](../assets/img/settings-fspintegration-excelfsp.png)
- Remplissez le champ **Nom d'affichage** ;
- Sélectionnez le champ **Unique identifier field**. Ce champ est utilisé lors de la réconciliation pour mettre à jour le statut de la transaction de chaque enregistrement, par exemple le numéro de téléphone ou le numéro d'identification ;
- Si vous le souhaitez, sélectionnez les **FSP export fields (optional)**. Ce sont les champs inclus dans le rapport de paiement que vous envoyez à votre PSF ;
- Cliquez sur **Intégrer le PSF**.

Pour retirer un PSF Excel :

- Sur la carte du PSF Excel, cliquez sur les 3 points :material-dots-vertical: ;
- Sélectionnez **Supprimer l'intégration** ;
- Cliquez sur **Supprimer le PSF** pour confirmer.

!!! Note
    **Supprimer l'intégration** n'est disponible que si votre programme a plus d'un PSF Excel. Vous ne pouvez pas retirer un PSF encore utilisé par des enregistrements.

---

-8<- "docs/fr/_snippets/contact-support.md"
