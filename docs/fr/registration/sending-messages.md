---
title: Enregistrements - Envoi de messages
hide:
  - toc
---

Il existe une option pour envoyer des **messages sortants** via SMS ou WhatsApp aux enregistrements pour chaque action que vous effectuez dans l'instance, telle que l'inclusion, le refus ou l'envoi de paiements. Si vous souhaitez communiquer la progression du programme aux individus enregistrés, vous pouvez cliquer sur le bouton **Envoyer un message aux enregistrements** et activer la messagerie via la plateforme 121. Pour activer les services de messagerie, vous devez créer un compte Twilio et vous assurer qu'il y a suffisamment de crédits de messagerie. Contactez notre équipe pour configurer cela. Voici les étapes à suivre:

- [Créer un compte Twilio](#cr%C3%A9er-un-compte-twilio)
- [Recharger avant d'envoyer des messages](#recharger-avant-denvoyer-des-messages)
- [Formatage des numéros de téléphone dans Kobo](#formatage-des-num%C3%A9ros-de-t%C3%A9l%C3%A9phone-dans-kobo)
- [Envoyer un message aux individus enregistrés](#envoyer-un-message-aux-individus-enregistr%C3%A9s)
- [Message personnalisé](#message-personnalis%C3%A9)
- [Messages modèles prédéfinis](#messages-mod%C3%A8les-pr%C3%A9d%C3%A9finis)


!!! Important "Qui peut effectuer des actions sur cette page?"
    Les rôles de gestionnaire d'assistance et d'agent d'assistance peuvent effectuer des actions sur la page Enregistrements.
    Des utilisateurs supplémentaires peuvent se voir accorder uniquement la permission d'affichage sur cette page. [En savoir plus sur les utilisateurs et les rôles](../users/users-roles-page.md)

---

<a id="cr%C3%A9er-un-compte-twilio"></a>
### Créer un compte Twilio

L'équipe 121 vous aidera à créer votre compte. Si vous n'avez pas de compte, veuillez contacter notre équipe pour obtenir du soutien. Twilio vous demandera d'ajouter une méthode de paiement afin que les fonds puissent être automatiquement rechargés ou ajoutés selon les besoins.

Une fois que votre compte Twilio est actif, l'équipe d'assistance 121 le liera à votre plateforme 121, activant la fonctionnalité de messagerie.

*Veuillez noter que ni 121 ni la Croix-Rouge néerlandaise ne facturent de frais au nom de Twilio. Notre équipe est seule responsable de l'intégration technique entre les deux systèmes pour faciliter l'envoi de messages.*

---

<a id="recharger-avant-d%27envoyer-des-messages"></a>
### Recharger avant d'envoyer des messages

Vous pouvez vous connecter à votre compte Twilio chaque fois que vous avez besoin de recharger votre compte.

**Envoi de SMS**
Les frais par SMS varient selon la destination et le nombre de caractères envoyés par message. Vérifiez le site Web de Twilio pour les frais appliqués à votre destination sur ce site Web pour [SMS.](https://www.twilio.com/en-us/sms/pricing/ma)

Notez qu'un **SMS est limité à 160 caractères** — les messages plus longs que cela seront divisés en plusieurs SMS et facturés en conséquence. Par exemple, un message entre 161 et 320 caractères sera compté et facturé comme deux SMS. Un message entre 321 et 481 comme trois messages, etc. Vous pouvez utiliser cette base pour calculer combien votre compte Twilio devrait être rechargé. Le calcul comprendra: nombre de SMS envoyés x nombre d'enregistrements x prix par SMS pour la destination.

**Messages WhatsApp**
Les messages WhatsApp suivent un schéma différent. Vous pouvez trouver la description des frais sur [le site Web de Twilio.](https://www.twilio.com/en-us/whatsapp/pricing)

Une fois que vous avez calculé les coûts totaux, vous pouvez recharger votre compte via le portail Twilio et ajouter les fonds nécessaires.

!!! Important "Ajouter des fonds suffisants à votre compte Twilio"
    Sans fonds disponibles sur votre compte Twilio, les messages SMS ou WhatsApp échoueront. Contactez notre équipe si vous avez besoin d'aide pour configurer votre compte Twilio.

---

<a id="formatage-des-num%C3%A9ros-de-t%C3%A9l%C3%A9phone-dans-kobo"></a>
### Formatage des numéros de téléphone dans Kobo

Les numéros de téléphone doivent être entrés au format international. Cela signifie commencer par l'indicatif régional, suivi du reste du numéro sans le zéro initial. Par exemple, un numéro de téléphone en République démocratique du Congo (RDC) comme 0900887766 devrait être écrit comme 243900887766 — où 243 est l'indicatif régional et le 0 initial est supprimé.

**Lors de la création de votre formulaire Kobo, vous pouvez appliquer le format de numéro de téléphone international à l'aide d'une contrainte ou d'un calcul. Ni Kobo ni la plateforme 121 ne reformateront automatiquement les numéros, il est donc important de configurer cette logique dans votre formulaire pour assurer la cohérence.**

| type | name label | constraint | constraint_message |
| :------- | :------- | :--------- | :------ |
| text_phone | Entrer le numéro de téléphone | regex(., '^243[0-9]{9}$') | Le téléphone doit commencer par 243 et avoir 12 chiffres. |


---

<a id="envoyer-un-message-aux-individus-enregistr%C3%A9s"></a>
### Envoyer un message aux individus enregistrés

Vous pouvez choisir d'envoyer un message à un seul ou plusieurs enregistrements sélectionnés. Vous pouvez utiliser soit un message personnalisé, soit un modèle prédéfini. Voir ci-dessous pour les différences et les directives d'utilisation recommandées.

<a id="message-personnalis%C3%A9"></a>
### Message personnalisé

Sur la **page d'enregistrement**:

- Sélectionnez la liste d'enregistrements auxquels vous souhaitez envoyer un message;
- Cliquez sur l'icône **Message** en haut de la page;
- Sélectionnez **Message personnalisé** et ajoutez le message que vous souhaitez envoyer;
- Vous pouvez utiliser variable en utilisant **@** et **sélectionner le champ** que vous souhaitez insérer. Les variables vous permettent de récupérer des informations directement du formulaire d'enregistrement et de l'insérer automatiquement, sans avoir à la remplir manuellement pour chaque personne. Le contenu s'ajustera automatiquement en fonction des données fournies par chaque individu lors de l'enregistrement.

!!! Note "Qu'est-ce qu'une variable et comment fonctionne-t-elle?"
    Une variable est un espace réservé qui récupère et insère automatiquement des informations spécifiques de votre formulaire d'enregistrement — comme un nom, une adresse e-mail, un numéro de téléphone ou tout autre champ collecté lors de l'inscription.

    Vous pouvez utiliser une variable en tapant @ et en sélectionnant le champ que vous souhaitez insérer. Par exemple, taper @name insérera automatiquement le nom de chaque personne dans le message. Cela signifie que vous n'avez pas besoin de personnaliser manuellement le message pour chaque individu. La variable s'ajustera dynamiquement pour chaque enregistrement, en fonction des informations soumises par cette personne.

    Par exemple: Cher **@name**, vous recevrez le montant de **@amount** demain. Cordialement, **@Organization**. serait lu comme Cher **Paulina Baker**, vous recevrez le montant de **150 USD** demain. Cordialement, **HelpOrg**.

    *Les variables correspondent à vos champs kobo et peuvent différer par programme.*

<a id="messages-mod%C3%A8les-pr%C3%A9d%C3%A9finis"></a>
### Messages modèles prédéfinis

Si vous avez l'intention d'envoyer des messages à différents stades du programme, vous pouvez ajouter des modèles de messages à votre instance. Pour ce faire, fournissez le contenu du message avec un titre et spécifiez quand le message doit être déclenché. Notre équipe d'assistance les configurera. Il y a 2 options pour envoyer des messages modèles:

  1. Les modèles peuvent être liés à des étapes clés telles que l'enregistrement, la validation, l'inclusion, le refus et le paiement. Cela signifie que le message sera automatiquement envoyé lorsque l'action correspondante est effectuée — par exemple, en cliquant sur un bouton spécifique.

  2. Les messages modèles seront disponibles dans le menu déroulant lorsque vous cliquez sur le bouton **Message**. Vous pouvez choisir de les envoyer quand vous le souhaitez, indépendamment d'une action ou d'une étape spécifique du programme — contrairement à la première option, où les messages sont déclenchés automatiquement par des actions telles que l'enregistrement ou la validation.

---

-8<- "docs/fr/_snippets/contact-support.md"
