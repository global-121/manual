---
title: Protection des données
hide:
  - toc
---

??? "1. Comment les données sont-elles protégées ? Quelle est la politique de protection des données ?"

      510, l'unité numérique et des données, fait partie de la Croix-Rouge néerlandaise (NLRC). La NLRC a une **politique de protection des données** en vigueur depuis 2018. **La NLRC et la plateforme 121 adhèrent au Règlement général sur la protection des données (RGPD) européen**. Le RGPD a également spécifié la signalement de violation de données, qui doit être signalée à l'Autorité néerlandaise Persoonsgegevens. La NLRC emploie un agent juridique spécialisé dans la protection des données. La NLRC est un processeur de données pour le partenaire, et ceci est convenu dans l'accord de niveau de service (SLA). Pour plus d'informations sur le processeur de données : https://www.gdpreu.org/the-regulation/key-concepts/data-controllers-and-processors/ 

      Le partenaire reste le contrôleur de données et est donc responsable de toutes les données saisies dans la plateforme. Le partenaire doit donc être informé et en conformité avec sa législation sur la protection des données.

      Veuillez contacter notre équipe de gestionnaires de compte pour **discuter de toute exigence et question** concernant nos responsabilités RGPD à <info@121.global>.

??? "2. Quel est votre serveur cloud et votre fournisseur d'hébergement ?"

    La plateforme 121 s'exécute dans le cloud Microsoft Azure. Par défaut, l'emplacement de toutes les ressources est Europe occidentale. Éventuellement, et sur demande à notre équipe, il peut être possible d'héberger et de stocker les données dans une région différente. Veuillez contacter notre équipe pour plus d'informations <info@121.global>.

    Il peut être possible d'héberger la plateforme 121 dans le pays où le stockage et le traitement des données se produisent, mais cela dépend de la disponibilité des centres de données Azure.


??? "3. Pouvez-vous héberger les données dans le pays ?"

    En fonction de la disponibilité des centres de données Azure, le stockage et le traitement des données peuvent être possibles dans le pays. Des options alternatives peuvent être discutées avec notre équipe, telles que des fournisseurs IaaS ou PaaS alternatifs, ou une solution d'hébergement sur site. 
   
    Notez que l'hébergement des données sur des serveurs sur site, ou sur des serveurs tiers pour lesquels nous n'avons pas d'accord contractuel, peut affecter la maintenance de la plateforme 121. Il peut être nécessaire que votre équipe soutienne la maintenance de votre instance 121.
    
    Veuillez nous contacter pour discuter des meilleures alternatives et solutions à <info@121.global>.


??? "4. Dans quels emplacements géographiques stockez-vous ou traitez-vous les données ?"

    Les données de la plateforme 121 sont stockées, hébergées et traitées en Europe occidentale sur les serveurs Azure Cloud.
  
    Si vous utilisez KOBO toolbox pour l'enregistrement, les données resteront stockées sur le serveur KOBO, qui est situé en Europe. Veuillez noter que ceci est séparé du traitement des données de la plateforme 121 et en dehors de notre contrôle.

    Si vous utilisez les services de télécommunications de Twilio Inc., les données seront stockées sur un serveur situé aux États-Unis. Twilio Inc. participe au cadre de l'intimité des données entre l'UE et les États-Unis. Plus d'informations sur la façon dont Twilio traite les données personnelles peuvent être trouvées dans son [addendum sur la protection des données.](https://www.twilio.com/en-us/legal/data-protection-addendum)


??? "5. Combien de temps conservez-vous les données ?"

    Les données sont stockées pendant une période maximale de 7 ans sur notre serveur cloud Azure après la dernière mise à jour. Les données qui n'ont pas été mises à jour au cours des 7 dernières années seront supprimées du serveur cloud. Si vos programmes nécessitent une période de stockage plus courte, cela peut être demandé à notre équipe. 

    À la fermeture de votre instance, vos données seront supprimées et effacées de notre serveur cloud - y compris les utilisateurs, les programmes et les détails des bénéficiaires. Attention : cette action est irréversible et les données ne peuvent pas être récupérées par la suite. Si certaines données personnelles sont toujours pertinentes, nous vous demandons gentiment de sauvegarder tous les enregistrements nécessaires au préalable.

    **Les données collectées avec un outil tiers** intégré à la plateforme 121 ne sont pas hébergées sur nos serveurs. Le tiers gère le stockage des données. Par exemple, les données collectées avec l'outil KOBO seront stockées sur les serveurs KOBO et relèveront de leur politique de protection des données. Des conditions similaires s'appliquent à Twilio Inc. ou à tout autre tiers intégré à la plateforme 121. Veuillez noter que ceci est séparé du traitement des données de la plateforme 121 et en dehors de notre contrôle. Veuillez vous reporter à l'article 5 de notre FAQ, section Protection des données.

??? "6. Comment garantissez-vous la confidentialité, l'intégrité et la disponibilité des données ?"

    **La confidentialité** est protégée en ne permettant qu'à un ensemble limité et contrôlé d'administrateurs d'accéder aux ressources liées à la production dans Azure. De plus, la confidentialité est protégée en ayant des instances 121 séparées avec des bases de données séparées et des identifiants pour chaque partenaire, et pour chaque partenaire ayant des comptes d'utilisateur individuels avec un accès basé sur les rôles aux données, y compris l'administrateur technique.

    **La disponibilité** est protégée en utilisant une configuration optimisée des ressources dans Microsoft Azure, y compris les sauvegardes automatisées et les contrôles de santé. De plus, des rapports d'exception automatisés sont mis en place, de sorte qu'en cas d'indisponibilité du service, l'équipe DevOps de la NLRC 510 peut réagir rapidement. De plus, tout nouveau code est minutieusement testé en utilisant à la fois des tests automatisés et des tests manuels avant d'être mis en production.

    **L'intégrité** est protégée par des tests approfondis du logiciel en utilisant divers types de tests automatisés et manuels, et en utilisant la fonctionnalité d'intégrité fournie par le SGBD avec un ERD en 3e forme normale (relations clé primaire-étrangère, contraintes d'unicité, colonnes non nulles, etc.). Les tentatives malveillantes d'accès aux données sont atténuées par la surveillance quotidienne des journaux et des ressources et par des tests de pénétration réguliers menés par une entreprise externe. La Croix-Rouge néerlandaise (NLRC) a signé le Code de conduite de la FICR et les entrepreneurs externes le font également.

??? "7. Qui traite les données ?"

    Le principal processeur est la NLRC, qui est soumise au Règlement général sur la protection des données (RGPD) de l'UE. Elle maintient la plateforme 121 mais n'accédera aux données personnelles que si nécessaire pour fournir un support ou des améliorations de produit.

    Cependant, pour faire fonctionner la plateforme 121, plusieurs processeurs de données (parties de confiance qui aident au fonctionnement réel de la plateforme) sont nécessaires.

    L'utilisateur peut trouver plus d'informations sur les tiers (sous-traitants) impliqués dans 121 et examiner leurs addendums de protection des données via les liens fournis ci-dessous :

      - **Informations légales Microsoft Azure** [https://azure.microsoft.com/en-us/support/legal/](https://azure.microsoft.com/en-us/support/legal/)

        Et le cas échéant :

    - **Twilio Flex** [https://www.twilio.com/en-us/legal/online-terms-updates](https://www.twilio.com/en-us/legal/online-terms-updates)

      - **KoboToolbox** [https://www.ifrc.org/ifrc-kobo](https://www.ifrc.org/ifrc-kobo)

    121 peut également utiliser EspoCRM, un logiciel open-source auto-hébergé par le partenaire sur un serveur à un emplacement choisi par le partenaire  [https://www.espocrm.com/tos/](https://www.espocrm.com/tos/)

??? "8. Quelles sont mes responsabilités en tant qu'utilisateur de 121 ?"

    Ci-dessous, vous pouvez trouver une liste non exhaustive des responsabilités des utilisateurs concernant la protection des données personnelles traitées par la plateforme 121. Veuillez noter qu'il peut y avoir d'autres obligations imposées par la législation nationale ou internationale applicable à votre organisation.
    
    **Liste non exhaustive des responsabilités des utilisateurs :**

    - Assurer le respect de la législation applicable.
    - S'assurer que toute personne ayant accès à 121 sous la Société nationale ou l'organisation doit maintenir la confidentialité de son compte et de son mot de passe.
    - S'assurer que tout le personnel impliqué, y compris le nouveau personnel, est adéquatement formé à leurs rôles et comprend leurs responsabilités et l'importance de la protection des données.
    - Évaluer si une évaluation d'impact sur la protection des données (DPIA) est requise pour le cas d'usage et le contexte spécifiques. Une DPIA évalue les risques de confidentialité associés au traitement des données personnelles et détermine les mesures nécessaires pour atténuer efficacement les risques identifiés.
    - Établir et adhérer à une politique de conservation des données qui reflète exactement la nature et la sensibilité des données personnelles traitées.
    - Fournir des informations adéquates et compréhensibles sur le traitement des données personnelles et tous les droits associés aux sujets des données en langue(s) locale(s), conformément aux exigences de la législation applicable.  
    - S'assurer que les sujets des données peuvent exercer efficacement leurs droits, tels que leurs droits d'accès, de rectification, d'effacement et d'objection, ou tous les droits supplémentaires accordés en vertu de la législation applicable.  
    - Avoir en place un protocole de violation de données.

    Considérez toute autre exigence qui peut être imposée par la législation applicable.

??? "9. Quelles sont les bonnes pratiques supplémentaires en matière de confidentialité pour les utilisateurs finaux ?"

    Lectures recommandées pour les utilisateurs du Mouvement de la Croix-Rouge et du Croissant-Rouge :

    - Guidance pratique de la FICR pour la protection des données dans l'aide au transfert d'argent et aux bons d'achat
    - Aperçu et meilleures pratiques en matière de protection des données de la FICR

    Lectures recommandées pour toutes les organisations :

    - Règlement général sur la protection des données (RGPD)

    - Module 3 (Responsabilité des données et des données numériques) du cours d'introduction à la littératie des données et des données numériques

    Recommandations supplémentaires :

    - Ne collectez pas plus de données que nécessaire pour l'objectif du programme spécifique.
    - Ne gardez pas les données plus longtemps que nécessaire.
    - Effectuez un examen d'accès mensuel/bimensuel.
    - Gérez de manière responsable tous les fichiers excel exportés de 121.
    - Suivez une formation sur la protection des données.
    - Utilisez un gestionnaire de mots de passe numérique (par exemple, Bitwarden).
    
    En général, il est fortement conseillé de supprimer les fichiers après avoir effectué le contrôle de duplication afin qu'ils ne puissent pas être facilement récupérés. L'utilisateur peut appliquer des mesures supplémentaires telles que la protection du classeur avec un mot de passe. Dans Microsoft Excel, cela peut être fait en suivant ces étapes :

      - Sélectionnez Fichier > Infos.
      - Sélectionnez la zone Protéger le classeur et choisissez Chiffrer avec un mot de passe.
      - Entrez un mot de passe dans la boîte Mot de passe, puis sélectionnez OK.
      - Confirmez le mot de passe dans la zone Entrez à nouveau le mot de passe, puis sélectionnez OK.
      - Mettez à jour le mot de passe initial qui vous a été partagé pour accéder à la plateforme 121 et choisissez un nouveau mot de passe robuste (par exemple, utilisez des phrases de passe contenant des lettres majuscules, des chiffres et des symboles).


-8<- "docs/fr/_snippets/contact-support.md"
