---
title: Guide étape par étape Préparer votre programme CVA
hide:
  - toc
---

Ce guide présente les étapes essentielles pour préparer et lancer votre programme d'assistance en espèces et bons d'achat (CVA) via la plateforme 121. Veuillez examiner attentivement chaque étape avant de commencer. Vous pouvez également imprimer ou enregistrer cette page afin de l'utiliser comme liste de contrôle tout au long du processus.

---

## 1. Définissez les informations de votre programme

Pour configurer votre programme, vous devez connaître les informations de base de votre programme.

Vous pouvez choisir d'ajouter une étape de validation dans votre flux de travail. Cette fonctionnalité dans la plateforme 121 vous permet d'utiliser le statut « Validation » pour les enregistrements avant de les inclure dans le paiement. Lors de l'utilisation du formulaire Kobo de validation hors ligne, l'envoi du formulaire fait automatiquement passer l'enregistrement du bénéficiaire au statut Validé.

Vous pouvez également choisir d'ajouter un scope à votre programme 121. Cette fonctionnalité vous permet de contrôler quels membres de l'équipe ont accès à certains enregistrements selon le scope qui leur est attribué.

Préparez votre formulaire d'enregistrement dans Kobo (ou un autre outil pris en charge). Le formulaire ne peut être intégré à 121 qu'une fois finalisé par votre équipe.

- [ ] Nom du programme
- [ ] Nombre d'enregistrements ciblés
- [ ] Montant du transfert
- [ ] Prestataire(s) de services financiers (PSF)
- [ ] Devise
- [ ] Calendrier pour l'enregistrement, le nettoyage des données et le paiement partagé avec l'équipe 121
- [ ] Décision de permettre ou non l'utilisation du scope dans 121 (permet un accès limité à certains membres de l'équipe)
- [ ] Décision de permettre ou non l'utilisation de la validation dans 121 (active le statut « Validation »)
- [ ] Champs à vérifier pour les doublons partagés avec l'équipe 121

Vous trouverez des instructions spécifiques pour configurer les informations de votre programme [**ici**](../Settings/program-information.md).

---

## 2a. Collaborez avec votre ou vos PSF

Concluez des accords avec votre PSF sur le programme à venir. Si vous travaillez avec un PSF intégré à votre instance, demandez les identifiants et configurez-les dans 121. Si vous travaillez avec un PSF qui n'est pas intégré à 121, assurez-vous de connaître les instructions de paiement requises. Cela est nécessaire pour exporter vos listes de paiement depuis 121.

- [ ] Contrat avec le PSF signé ou vérification que le contrat avec le ou les PSF est toujours valide
- [ ] PSF informé des spécificités du programme (par exemple, calendrier et modalité)
- [ ] Identifiants saisis dans 121 pour la configuration si le PSF est intégré
- [ ] Modèle d'instruction de paiement reçu du PSF si le PSF n'est pas intégré

Vous trouverez des instructions spécifiques pour configurer votre ou vos PSF [**ici**](../Settings/fsp-integration.md).

---

## 2b. Finalisez votre formulaire de collecte des données d'enregistrement

Préparez votre formulaire d'enregistrement dans Kobo (ou un autre outil pris en charge). Idéalement, utilisez un formulaire harmonisé au sein de votre organisation que vous adaptez au programme concerné. Notre équipe est disponible pour relire votre formulaire et vous conseiller. Nous vérifierons également sa compatibilité avec 121. Pour partager votre formulaire, veuillez l'envoyer à notre compte Kobo : `nlrc121platform` pour le Mouvement de la Croix-Rouge et du Croissant-Rouge | `cva121_510` pour les autres.

- [ ] Question de consentement incluse dans le formulaire
- [ ] Localités ciblées incluses dans le formulaire
- [ ] Informations requises sur les bénéficiaires par le PSF incluses dans le formulaire
- [ ] Si un choix de PSF est proposé (y compris via Onafriq), question sur la préférence de PSF incluse dans le formulaire
- [ ] Restrictions pour limiter les erreurs incluses dans le formulaire (par exemple, format spécifique pour le numéro d'identité, le numéro de téléphone ou le nom complet)
- [ ] Vérification que la collecte de données est limitée à ce qui est nécessaire
- [ ] Formulaire relu par l'équipe d'assistance 121 (contrôle obligatoire de compatibilité 121, relecture générale facultative)
- [ ] Formulaire lié au programme 121

Vous trouverez des instructions spécifiques pour configurer votre formulaire d'enregistrement [**ici**](../Settings/registration-data.md).

---

## 3. Créez votre équipe

Identifiez les membres de l'équipe de votre programme. Une fois leurs comptes utilisateurs créés (à faire une seule fois), vous pouvez les ajouter à l'équipe du programme et leur attribuer un rôle. Les rôles dans 121 ne doivent pas nécessairement correspondre aux fonctions réelles des membres de l'équipe. Ce sont plutôt les autorisations associées qui doivent correspondre aux actions que l'utilisateur effectuera dans la plateforme. Vous pouvez attribuer un ou plusieurs rôles à une même personne.

- [ ] Comptes utilisateurs créés pour les nouveaux membres de l'équipe
- [ ] Utilisateurs ajoutés au programme avec un rôle attribué
- [ ] Scope défini pour les utilisateurs (facultatif)

Vous trouverez des instructions spécifiques pour configurer l'équipe de votre programme [**ici**](../Settings/programteam.md).

L'utilisateur n'a pas encore été créé ? Reportez-vous au [guide de création d'utilisateur](../users/add-users.md).

---

## 4. Configurez les services de messagerie (facultatif)

La plateforme 121 propose une intégration technique avec Twilio pour l'envoi de messages. Si vous prévoyez d'envoyer des messages WhatsApp et/ou des SMS à vos bénéficiaires, il peut être utile d'ouvrir un compte Twilio. Vous pouvez consulter leurs tarifs sur leur site web. **Remarque :** si vous utilisez Twilio pour votre programme, assurez-vous que votre compte dispose de fonds suffisants, sinon les messages échoueront. Si vous prévoyez d'envoyer des messages à différentes étapes du programme, des modèles peuvent être ajoutés à votre instance.

!!! Important "Nombre de caractères par SMS"
    Un SMS est limité à 160 caractères. Les messages plus longs seront divisés en plusieurs SMS et facturés en conséquence. Par exemple, un message compris entre 161 et 320 caractères sera compté et facturé comme deux SMS.

- [ ] Décision prise quant à l'utilisation de Twilio
- [ ] Compte Twilio créé
- [ ] Équipe 121 informée
- [ ] Demande d'appui à l'équipe 121 pour créer des modèles de messages (facultatif)
- [ ] Fonds ajoutés à votre compte

---

## 5. Configurez le formulaire de validation hors ligne (facultatif)

Si vous validez les bénéficiaires sur le terrain, nous pouvons vous aider à mettre en place un formulaire de validation dans Kobo. Celui-ci peut être préparé une fois l'enregistrement et le nettoyage des données terminés. En saisissant un identifiant unique (par exemple, un numéro d'identité), le formulaire récupère les informations personnelles du bénéficiaire. Cela permet de vérifier l'identité de la personne. Une fois le formulaire envoyé et l'appareil synchronisé à Internet, le statut du bénéficiaire passe automatiquement à Validé.

Le formulaire peut également être utilisé pour mettre à jour les informations du bénéficiaire lorsqu'il se trouve sur le terrain. Par exemple, son numéro de téléphone. Une fois le formulaire envoyé et l'appareil synchronisé à Internet, le profil 121 du bénéficiaire est automatiquement mis à jour.

Contactez notre équipe pour organiser ce processus et indiquez-nous les critères de vérification et les champs que vous souhaitez utiliser.

- [ ] Décision prise sur l'utilisation du formulaire pour la validation sur le terrain
- [ ] Formulaire de validation demandé et co-conçu avec l'équipe 121
- [ ] Formation à l'utilisation du formulaire assurée

Vous trouverez des instructions spécifiques pour configurer votre formulaire de validation hors ligne [**ici**](../registration/offline-verification.md).

---

## 6. Configurez un formulaire hors ligne pour la distribution de cartes SIM ou une mise à jour en masse (facultatif)

Si vous prévoyez de distribuer des cartes SIM, nous pouvons vous aider à mettre à jour votre base de données dans 121 en conséquence. Deux options sont possibles :

- [ ] Créer un formulaire Kobo à utiliser pendant la distribution afin d'ajouter le numéro de téléphone de la carte SIM au profil du bénéficiaire dans 121
- [ ] Mettre à jour en masse les profils des bénéficiaires dans 121 avec la liste des numéros de téléphone

- [ ] Décision prise sur la distribution des cartes SIM et processus discuté avec l'équipe 121
- [ ] Champs clés pour faire correspondre la carte SIM à la personne (par exemple, nom, numéro d'identité, numéro d'enregistrement) identifiés et vérifiés
- [ ] Vérification que les données entre 121 et le fournisseur chargé de la distribution des cartes SIM sont alignées
- [ ] Formulaire de mise à jour des cartes SIM co-conçu avec l'équipe 121

---

Vous êtes maintenant entièrement prêt à lancer votre programme et à distribuer avec succès une assistance en espèces à celles et ceux qui en ont besoin.

## Besoin d'aide ?

Veuillez contacter notre [équipe d'assistance par e-mail](mailto:support@121.global) si vous avez besoin d'aide ou de précisions supplémentaires.

---

-8<- "docs/fr/_snippets/contact-support.md"
