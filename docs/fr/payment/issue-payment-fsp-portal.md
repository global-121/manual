---
title: Paiements - Paiement manuel via le portail PSF (export Excel)
hide:
  - toc
---

Dans la plateforme 121, les paiements peuvent être traités de deux façons différentes : avec un **paiement manuel via un portail PSF** ou avec une **intégration PSF directe**. Vous trouverez ci-dessous les instructions étape par étape pour **traiter le paiement manuel via un portail PSF**, exporter les instructions de paiement et concilier les paiements dans votre programme.

*Pour les instructions de paiement avec un prestataire de services financiers intégré, veuillez vous référer aux instructions sur la [page Paiement avec un PSF intégré.](./payment-integrated-fsp.md)*

!!! Important "Qui peut effectuer des actions sur cette page ?"
    Le responsable CVA et le responsable financier peuvent créer des paiements. Seuls les membres de l'équipe désignés comme approbateurs du programme peuvent les approuver. Seul le responsable financier peut lancer les paiements et importer les données de réconciliation. Le responsable financier, le gestionnaire financier et l'approbateur peuvent exporter la liste des instructions de paiements (PSF). [En savoir plus sur Utilisateurs et rôles.](../users/description-roles.md)

## Aperçu des paiements

La page Paiements de votre programme affichera des informations sur tous les versements ou tours de paiement effectués. Si aucun paiement n'a été effectué, aucun détail n'apparaîtra. Cependant, si certains versements sont déjà en cours, vous verrez chaque versement individuel. **Vous pouvez créer de nouveaux paiements même si des transactions de paiements précédents ont encore le statut En cours.** Tant que la plateforme 121 traite encore un paiement (par exemple juste après la création, le lancement ou la relance d'un paiement), la page Paiements affiche **Paiement en cours** et vous ne pouvez pas créer de nouveau paiement avant la fin du traitement.

### Créer un nouveau paiement

Pour lancer un nouveau paiement :

- En haut à droite, cliquez sur **Créer un nouveau paiement**.

![Bouton Créer un nouveau paiement](../assets/img/PaymentsPage.png)

- Saisissez un nom pour le paiement. Un nom est prérempli (*Payment jj/mm/aa, hh:mm*) ; vous pouvez le modifier si nécessaire. Cliquez sur **Poursuivre l'enregistrement**.
- Une page s'affichera avec une liste d'enregistrements inclus dans le programme.
  *Seuls les enregistrements avec le statut **Inclus(e)** qui n'ont pas encore reçu tous leurs versements apparaîtront dans la liste. Les enregistrements qui ont reçu et complété tous leurs paiements ne seront pas affichés.*

![Liste de sélection](../assets/img/CreateNewpaymentSelect.png)

- **Sélectionnez la liste des enregistrements à ajouter** au tour de paiement comme suit.
  - Faites une **sélection individuelle** en cliquant sur la :material-checkbox-outline: sur la ligne d'enregistrement individuelle ;
  - Ou faites une **sélection en masse** en cliquant sur la :material-checkbox-multiple-marked-outline: sur la ligne du tableau supérieur **Sélectionner** ;
- En bas à droite, cliquez sur **Ajouter au paiement** ;

![Ajouter au paiement](../assets/img/StartPayment.png)

- Un récapitulatif s'affiche avec le(s) prestataire(s) de services financiers, le nombre d'enregistrements et le montant total du paiement ; vous pouvez ajouter une note si nécessaire ;
- Le portail affichera des directives en haut du récapitulatif pour exporter les instructions de paiement PSF (comme indiqué ci-dessus) ;
- Cliquez sur **Créer un paiement**. **Cette action n'exécutera pas automatiquement ou n'enverra pas la demande de paiement au PSF. Cependant, cela préparera les instructions de paiement, y compris la liste des enregistrements destinés à recevoir des paiements.**

!!! Important "Les doublons bloquent les paiements"
    Vous ne pouvez pas créer, approuver ni lancer un paiement qui contient des enregistrements marqués comme **Doublon**. Résolvez d'abord les doublons. Consultez [Créer, approuver et lancer les paiements](./create-approve-payment.md).

### Approuver et lancer le paiement

Après avoir cliqué sur **Créer un paiement**, vous arrivez sur la page du paiement. Les transactions ont le statut **En attente d'approbation**. Vous ne pouvez pas encore exporter les instructions de paiement : l'export ne contient que les transactions au statut **En cours**.

- Les approbateurs approuvent le paiement avec **Approuver le paiement**.
- Une fois que tous les approbateurs ont approuvé, un responsable financier clique sur **Instruire les paiements**.
- Les transactions du PSF via export-import manuel (Excel) passent au statut **En cours**.

Pour les étapes détaillées, consultez [Créer, approuver et lancer les paiements](./create-approve-payment.md).

Une fois le paiement lancé, **restez sur la page de paiement sur laquelle vous veniez de travailler**. À partir de là, vous pouvez télécharger les instructions de paiement. Vous verrez toutes les transactions au statut **En cours** pour les enregistrements qui ont choisi de recevoir une aide en espèces via le PSF via export-import manuel (Excel).

### Exporter les instructions de paiement

![Statuts en attente Excel](../assets/img/PendingStatusExcel.png)

Le fichier fournira les instructions nécessaires pour que le PSF émette les paiements.

- En haut à droite de votre **page**, cliquez sur **Exporter** et sélectionnez **Exporter la liste des instructions de paiements (PSF)** ;
- Le fichier sera disponible dans votre dossier de téléchargement ;
- Vérifiez le fichier si nécessaire. *En fonction de votre accord avec le PSF, partagez le fichier à votre PSF ou importez-le dans le portail PSF (le cas échéant).*

Le statut de paiement affiché sur la page des paiements sera mis à jour en fonction de la phase de paiement. Pour le paiement manuel, le message par défaut sera **En cours** jusqu'à ce que la réconciliation des paiements ait été traitée.
![Exporter la liste de paiement PSF](../assets/img/IndividualExportReport.png)
!!! Info "Modèle d'instructions de paiement Excel"
    Chaque programme peut nécessiter un modèle différent selon le PSF avec lequel vous travaillez dans la région de vos opérations. Les colonnes du fichier et le champ utilisé pour identifier les enregistrements sont définis pour chaque PSF Excel dans les paramètres du programme, sous **Paramètres** > **Intégration FSP**. Demandez à votre administrateur du programme ou à l'équipe de soutien 121 si vous devez les modifier.

    Le fichier d'instructions de paiement ne doit contenir que les critères nécessaires au PSF pour confirmer l'identité des enregistrements et émettre les paiements, tels que les noms, les numéros de téléphone et les numéros d'ID ou tout autre critère selon vos SOP du programme. Pour la confidentialité des données, nous recommandons de n'exporter que les critères minimaux pour vérifier l'identité d'enregistrement. Toutes les autres données non pertinentes pour le processus de paiement doivent être refusées du fichier d'instructions de paiement. Après utilisation, les données exportées doivent être supprimées pour assurer la sécurité des données personnelles.

---

### Concilier les paiements dans la plateforme 121

Une fois que le PSF a partagé le fichier de données de réconciliation, vous pouvez concilier les paiements dans la plateforme 121. Cela mettra à jour le statut de paiement en téléchargeant le fichier sur la **page de paiement spécifique**.

!!! Important "Formater le fichier de réconciliation"
    Avant d'importer le fichier de réconciliation, assurez-vous qu'il répond au format requis. Vous pouvez télécharger le modèle en cliquant sur **Importer les données de réconciliation**, puis sur **Télécharger le modèle**. Assurez-vous que toutes les colonnes requises sont incluses et ajustez les statuts comme suit :

      - **Complété** → success
      - **Échoué** → error

    Le fichier doit être au format .csv. Suivez les instructions [sur cette page.](./manual-payment-reconciliation.md)

Pour mettre à jour les statuts de paiement :

- Allez à la page des paiements pour la date et le paiement sélectionnés qui correspondent au fichier ;
- En haut à droite de votre page, cliquez sur **Importer les données de réconciliation**.
  
![Exporter la liste de paiement PSF](../assets/img/IndividualExportReport.png)

- Cliquez sur le bouton d'importation pour télécharger le fichier PSF, *le fichier doit être au format .csv* ;
- **Glissez-déposez** le fichier ; ou utilisez la fonction **Choisir le fichier** ;
- Cliquez sur **Importer le fichier**. Le statut des enregistrements sera mis à jour selon que le transfert était marqué comme Réussi ou Échoué par le PSF.
![Exporter la liste de paiement PSF](../assets/img/IndividualExportReport.png)

---

### Statut de paiement

![Importation de données de réconciliation](../assets/img/ReconciliationImport.png)
Le statut de paiement affiché sur la page des paiements sera mis à jour en fonction de la phase de paiement. Pour le paiement manuel, le message par défaut sera **En cours** jusqu'à ce que la réconciliation des paiements ait été traitée.

Vous trouverez ci-dessous les différents statuts de paiement.

| Statut | Description | Actions requises |
| :------ | :----------- | :---------------- |
| **RÉUSSI** | Le transfert a été envoyé aux enregistrements et ils peuvent maintenant l'utiliser. | Aucun. |
| **EN COURS** | Le transfert n'a pas encore été confirmé pour les enregistrements sélectionnés pour ce tour de paiement, car le fichier de réconciliation n'a pas encore été importé. | Importez le fichier de réconciliation dans la plateforme 121 pour mettre à jour le statut. |
| **ÉCHEC** | La transaction a échoué. Les enregistrements n'ont pas reçu de paiements. | Veuillez vérifier le message d'erreur fourni par votre banque. L'échec du paiement peut être dû à des détails bancaires incorrects, un numéro de téléphone ou un numéro d'ID selon les méthodes de paiement choisies. Vous pouvez réessayer. Contactez notre équipe de soutien 121 si cela reste non résolu. |

!!! Info "Réconciliation manuelle des paiements"
    Une fois que le PSF revient avec les données de paiement, vous pouvez traiter la réconciliation manuelle des paiements dans la plateforme 121.
    Suivez les instructions sur [cette page.](./manual-payment-reconciliation.md)

-8<- "docs/fr/_snippets/contact-support.md"
