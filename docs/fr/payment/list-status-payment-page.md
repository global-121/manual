---
title: Paiement - Messages de paiement et statuts dans 121
hide:
  - toc
---

Lors d'un paiement, la plateforme 121 notifiera les utilisateurs sur leurs actions à travers un certain nombre de statuts et messages mis à jour. Voici la liste et les explications associées.

## Statuts de paiement dans la page Paiements

Le statut sera mis à jour automatiquement pour les PSF intégrés, ou après réconciliation manuelle une fois que le PSF a partagé le fichier de réconciliation de paiement de retour à votre équipe financière et qu'ils l'ont téléchargé dans la plateforme 121.

| Statut | Description | Actions requises |
| :------ | :----------- | :---------------- |
| **EN ATTENTE D'APPROBATION** | La demande de paiement a été créée mais attend toujours l'approbation de tous les approbateurs. | Les approbateurs doivent approuver le paiement pour continuer. |
| **APPROUVÉ** | La demande de paiement a été approuvée par tous les approbateurs. | Le paiement doit être lancé pour continuer. |
| **RÉUSSI** | Le paiement a été envoyé aux enregistrements et ils peuvent maintenant l'utiliser. | Aucun. |
| **EN COURS DE TRAITEMENT** | Le paiement attend la confirmation d'un ou plusieurs gestionnaires financiers. Le transfert n'a pas encore été envoyé aux enregistrements sélectionnés pour ce tour de paiement ou le fichier de réconciliation n'a pas encore été importé. | Importez le fichier de réconciliation dans la plateforme 121 pour mettre à jour le statut. |
| **ÉCHOUÉ** | La transaction a échoué. Les enregistrements n'ont pas reçu de paiements. | Veuillez vérifier le message d'erreur fourni par votre banque. L'échec du paiement peut être dû à des détails bancaires incorrects, un numéro de téléphone ou un numéro d'ID selon les méthodes de paiement choisies. Vous pouvez réessayer. Contactez notre équipe de soutien 121 si cela reste non résolu. |

---

## Statuts d'enregistrement

| Type | Description | Actions requises |
| :---- | :----------- | :---------- |
| **Nouveau** | Les enregistrements ont été ajoutés au programme mais ne sont pas encore inclus. | Un responsable CVA ou un gestionnaire CVA peut les valider ; seul un responsable CVA peut les inclure dans le programme. |
| **Validé(e)** | Les détails des enregistrements ont été vérifiés. L'enregistrement a été validé par un responsable CVA ou un gestionnaire CVA. Ils ne sont pas encore inclus dans le programme et ne peuvent pas recevoir de paiements. | Un responsable CVA peut inclure les enregistrements dans le programme, ou un responsable CVA ou un gestionnaire CVA peut les décliner. |
| **Inclus(e)** | Les enregistrements ont été inclus dans le programme et peuvent commencer à recevoir des transferts de paiement via le portail 121. | Un responsable CVA ou un responsable financier peut sélectionner les enregistrements pour les prochains tours de paiement. |
| **Décliné(e)** | Les enregistrements se sont avérés être mal enregistrés ou ne répondaient pas aux critères d'inclusion du programme. Les enregistrements ne recevront aucun paiement. | Aucune action requise, sauf si l'enregistrement a été décliné à tort. Les enregistrements peuvent être réinclus si nécessaire. |
| **Mis(e) en pause** | Les enregistrements ne sont actuellement pas inclus dans la distribution (les paiements sont en pause) mais font toujours partie du programme. | Les enregistrements peuvent être inclus ou déclinés du programme selon les SOP. Un responsable CVA ou un gestionnaire CVA peut décider de la mise à jour du statut. |
| **Complété(e)** | Les enregistrements ont reçu le montant complet des transferts. Aucun autre paiement ne peut être envoyé. | Aucun. Ce statut est automatiquement généré par le système. Sauf si des tours de paiement supplémentaires ont été ajoutés au programme, ce statut restera inchangé. |

!!! Important "Mises à jour des statuts"
    Les rôles de responsable CVA et de gestionnaire CVA ont les autorisations de mettre à jour les statuts des enregistrements au sein de leur programme attribué. Si vous remarquez que le statut d'un enregistrement doit être mis à jour, veuillez contacter votre responsable CVA ou gestionnaire CVA pour discuter des prochaines étapes.

    Seul le statut **Complété(e)** est automatiquement généré par le système une fois que tous les paiements ont été traités pour les enregistrements inclus dans le programme.

---

-8<- "docs/fr/_snippets/contact-support.md"
