---
title: Données d'enregistrement
hide:
  - toc
---

!!! Important "Qui peut effectuer des actions sur cette page ?"
    L'administrateur du programme peut consulter, configurer et mettre à jour l'intégration entre votre formulaire Kobo et la plateforme 121.

La plateforme 121 propose une intégration avec KoboToolbox. Si vous utilisez cet outil pour la collecte de données, vous pouvez l'intégrer à votre programme dans 121. Les enregistrements sont ensuite ajoutés automatiquement à 121 en temps réel. Notez que les Sociétés nationales du Mouvement RCRC peuvent créer leur formulaire Kobo via le serveur [IFRC](https://kobo.ifrc.org/) gratuitement. Si vous utilisez un autre outil de collecte de données, vous pouvez [importer vos enregistrements via Excel](../registration/registration-import-list.md).

Vous configurez et gérez l'intégration entre votre formulaire Kobo et 121 sur la page **Données d'enregistrement** sous **Paramètres**.

## Configurer l'intégration de votre formulaire Kobo

La configuration de votre intégration consiste en deux étapes :

- Vérifier la compatibilité entre votre formulaire, 121 et votre PSF ;
- Lier votre formulaire à 121.

## Vérifier la compatibilité entre votre formulaire, 121 et votre PSF

Avant de lier votre formulaire à la plateforme 121, vous devez vous assurer que la compatibilité est respectée. Cela signifie vérifier que les informations requises par la plateforme 121 et par votre(s) PSF(s) sont correctement présentes dans le formulaire. Vous pouvez trouver les champs requis sur la page **Données d'enregistrement**. Voici une liste de 5 vérifications obligatoires et 4 facultatives.

!!! Note
    En plus de la vérification de compatibilité, vous pouvez demander une revue de votre formulaire par notre équipe CVA-IM. Elle examinera la logique de votre formulaire et donnera des conseils pour réduire les erreurs et garantir la protection des données. Par exemple, des formats restreints pour certaines réponses (par exemple numéro de téléphone, identifiant), des listes déroulantes dépendantes, des règles de saut, la demande de consentement, et l'évitement de collecte de données inutiles. Si vous souhaitez ce support, veuillez contacter l'équipe 121.

Avant de suivre la liste de vérification, partagez votre compte avec l'équipe 121. Cela nous permettra de fournir un support rapide et efficace. **Notre nom de compte est `nlrc121platform` pour le Mouvement RCRC et `cva121_510` pour les autres organisations.**

### 1. Langue

Assurez-vous que la langue par défaut dans l'onglet **Formulaire** de Kobo correspond à la langue principale du programme. Vous pouvez ajouter plusieurs langues, mais **une langue doit être définie sur Anglais (EN)**.

- Ouvrez votre formulaire dans **KoboToolbox** et allez dans la section **Formulaire** ;
- Vérifiez les langues incluses ;
- Si l'anglais n'est pas ajouté, cliquez sur **Gérer**, puis sur **Ajouter une langue** ;
- Ajoutez le nom **English** et le code **en** ;
- Cliquez sur **Ajouter**.

![Lien d'intégration](../assets/img/settings-registrationdata9.png)

![Lien d'intégration](../assets/img/settings-registrationdata8.png)

### 2. Nom complet

Le **Nom complet** est requis pour 121. Créez un champ **calculate** avec le nom de colonne de données **fullName**. Le calcul est une combinaison de tous les noms du bénéficiaire. Si tous les noms sont collectés dans une seule question, le champ calculate peut se référer directement à cette question.

### 3. Choix du ou des PSF

Le **PSF** est requis pour 121. Assurez-vous que le formulaire contient une référence au **PSF utilisé**. Le nom de colonne doit être **fsp**.

- **Utilisation d'un PSF** : créez un champ caché et ajoutez le nom de votre PSF sous « default ».
- **Utilisation de plusieurs PSF sans choix pour le bénéficiaire** : créez un champ calculate et ajoutez les noms des PSF dans le calcul déterminant le PSF. Les champs calculate sont toujours cachés.
- **Utilisation de plusieurs PSF avec choix pour le bénéficiaire** : créez une question de type select one ouverte et ajoutez les noms des PSF comme options.

Assurez-vous que le(s) PSF mentionné(s) dans votre formulaire Kobo correspondent aux noms des PSF configurés dans votre programme. Si vous utilisez l'option Excel manuelle, votre formulaire doit correspondre au « Nom d'affichage » indiqué dans la configuration PSF. Utilisez uniquement des lettres minuscules et des tirets « - » au lieu d'espaces.

### 4. Exigences des PSF

Assurez-vous que le formulaire collecte les **données requises par le PSF**. Vous pouvez trouver cet aperçu dans deux sections de 121 : dans Configuration PSF (cliquez sur :material-chevron-down: Exigences du formulaire par PSF) et dans Données d'enregistrement (cliquez sur :material-chevron-down: à côté de PSF intégrés). Chaque nom de colonne doit être correctement utilisé dans le formulaire. Si vous avez besoin d'aide, contactez l'équipe 121.

### 5. Numéro de téléphone

Le **Numéro de téléphone** est requis pour 121. Ce champ n'a pas besoin d'être obligatoire et peut être laissé vide dans les réponses. Le nom de colonne doit être **phoneNumber**. Si possible, définissez le format de réponse selon le standard téléphonique de votre pays pour éviter les erreurs.

### 6. Portée (facultatif)

Si vous souhaitez utiliser la **Portée** pour limiter l'accès des utilisateurs à des enregistrements spécifiques, incluez un champ calculate qui se réfère à la question correspondant à la portée (par exemple région, état, province).

### 7. Nombre maximum de paiements (facultatif)

Si vous souhaitez utiliser un **nombre maximum de paiements** après lequel les enregistrements passent automatiquement à **Terminé**, incluez un champ caché avec le nom de colonne **maxPayments** et indiquez ce nombre dans « default ».

Une fois fait, contactez l'équipe 121 pour qu'elle active cette fonctionnalité de son côté.

### 8. Score d'inclusion (facultatif)

Si vous souhaitez utiliser le **score d'inclusion** pour filtrer le score total et le mettre à jour automatiquement lorsqu'il est modifié, incluez un champ calculate qui se réfère aux réponses nécessaires pour le score total. Si vous attribuez des points à certaines réponses, l'équipe 121 vous aidera à configurer le calcul. Il n'y a pas de restriction sur le nom de colonne.

Une fois fait, contactez l'équipe 121 pour activer cela de leur côté.

### 9. Multiplicateur (facultatif)

Si vous souhaitez utiliser le **Multiplicateur** pour autoriser différentes valeurs de transfert dans un même programme, créez un champ calculate qui se réfère à la question déterminant la valeur du transfert (par exemple emplacement ou score total).

## Lier votre formulaire à 121

1. Assurez-vous que la version finale de votre formulaire est déployée dans Kobo (dans Formulaire, cliquez sur (Re)deploy) ;
2. Accédez à la page **Données d'enregistrement** sous **Paramètres** ;
3. Cliquez sur **KoboToolbox - Cliquer pour lier** ;

    ![Lien d'intégration](../assets/img/settings-registrationdata4.png)

4. Copiez l'URL complète du formulaire dans KoboToolbox. C'est le lien visible en haut du navigateur.

    ![Lien d'intégration](../assets/img/settings-registrationdata1.png)

5. Copiez la **clé API**. Dans KoboToolbox, cliquez sur l'icône de votre profil (en haut à droite) et sélectionnez **Paramètres du compte**, sous-section **Sécurité**. Cliquez sur **Afficher** à côté de la clé API avant de la copier.

    ![Lien d'intégration](../assets/img/settings-registrationdata2.png)
    ![Lien d'intégration](../assets/img/settings-registrationdata3.png)

6. Cliquez sur **Continuer**.

7. Si des problèmes sont détectés, un message d'erreur apparaît. Suivez les instructions, enregistrez le formulaire dans Kobo, redéployez dans Kobo, puis reprenez les étapes 4-5-6.

8. L'intégration doit maintenant fonctionner et vous pouvez commencer les enregistrements. Assurez-vous que les enquêteurs reçoivent le **lien Kobo correct**.

!!! Note
    Essayez d'attendre que votre formulaire Kobo soit finalisé et intégré à la plateforme 121 avant de lancer les enregistrements. Cela garantit que **tous les collecteurs utilisent le bon lien et évite les écarts dans les réponses**. Si vous devez modifier votre formulaire Kobo après l'intégration, cela peut être fait dans Kobo. Aucune action n'est requise dans la plateforme 121. Les colonnes sont automatiquement mises à jour dans 121 lorsqu'un nouvel enregistrement arrive. Notez que cette consigne s'applique uniquement aux modifications de la configuration du formulaire. Les modifications dans les réponses doivent être effectuées directement dans la plateforme 121.

## Importer des enregistrements existants

Si vous avez déjà effectué des enregistrements avec le formulaire Kobo avant son intégration à 121, vous pouvez les importer vous-même.

- Une fois votre formulaire lié, allez sur la page **Données d'enregistrement** sous **Paramètres** ;
- Cliquez sur les trois points :material-dots-vertical: ;
- Cliquez sur **Importer des enregistrements existants** ;
- Cliquez sur **Importer des enregistrements**. Notez qu'il y a un maximum de 1 000 enregistrements par importation. Si vous en avez plus, divisez-les en plusieurs fichiers.

![Lien d'intégration](../assets/img/settings-registrationdata7.png)

## Gérer votre intégration Kobo

!!! Info "Modification des données"
    Notez que la connexion entre Kobo et la plateforme 121 est un envoi unilatéral. Cela signifie que les données ne sont pas synchronisées entre les deux systèmes. Toute modification effectuée dans Kobo après le téléchargement dans 121 ne sera pas reflétée dans la plateforme. Vous devez effectuer les modifications directement dans 121.

    Par exemple, si l'enregistrement A est créé dans Kobo et que vous importez les données dans 121 à la fin de la journée, puis que vous constatez plus tard que la question 4 n'a pas été remplie pour l'enregistrement A, vous devrez trouver le profil de l'enregistrement A dans 121 et effectuer la correction. Les modifications effectuées dans Kobo après l'importation initiale ne seront pas mises à jour dans 121.

Vous pouvez consulter et gérer votre intégration Kobo sur la page **Données d'enregistrement** sous **Paramètres**. Les informations suivantes sont affichées :

- Le lien vers votre formulaire Kobo ;
- La dernière mise à jour de l'intégration Kobo ;
- Le(s) PSF intégré(s) et les champs requis dans le formulaire Kobo ;
- Les questions d'enregistrement telles qu'elles apparaissent dans le tableau des données et sur la page de profil.

Si vous souhaitez **remplacer votre formulaire**, cliquez sur **Reconfigurer** sous les trois points :material-dots-vertical: à côté du lien KoboToolbox. Vous devrez saisir l'URL du nouveau formulaire et la clé API. Notez qu'il n'est pas recommandé d'utiliser cette fonctionnalité lorsque des enregistrements ont déjà été effectués et synchronisés dans 121.

Si vous avez modifié la configuration du formulaire, elle se synchronise automatiquement lorsqu'un nouvel enregistrement est effectué. S'il n'y a pas de nouveaux enregistrements, vous pouvez utiliser **Actualiser le lien** sous les trois points :material-dots-vertical: à côté du lien KoboToolbox.

Si vous souhaitez simplifier les libellés affichés dans les profils 121 et dans le tableau des enregistrements, procédez comme suit :

- Cliquez sur **:octicons-pencil-24: Modifier** ;
- Allez sur le champ que vous souhaitez modifier ;
- Mettez à jour le texte de l'étiquette de la question ;

![Lien d'intégration](../assets/img/settings-registrationdata10.png)

## Voir vos enregistrements

- Ouvrez votre **programme** ;
- Allez à la page **Enregistrements** ;
- Vous verrez la liste des enregistrements mise à jour chaque fois qu'un nouvel enregistrement est complété et envoyé (lorsque la connexion internet est active).

Notez que KoboToolbox peut être utilisé hors ligne sur le terrain. Néanmoins, les enregistrements sont synchronisés avec 121 uniquement lorsqu'une connexion Internet est établie.

---

-8<- "docs/fr/_snippets/contact-support.md"
