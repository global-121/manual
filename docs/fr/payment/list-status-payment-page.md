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
| **EN COURS DE TRAITEMENT** | Le paiement attend la confirmation d'un ou plusieurs agents financiers. Le transfert n'a pas encore été envoyé aux enregistrements sélectionnés pour ce tour de paiement ou le fichier de réconciliation n'a pas encore été importé. | Importez le fichier de réconciliation dans la plateforme 121 pour mettre à jour le statut. |
| **ÉCHOUÉ** | La transaction a échoué. Les enregistrements n'ont pas reçu de paiements. | Veuillez vérifier le message d'erreur fourni par votre banque. L'échec du paiement peut être dû à des détails bancaires incorrects, un numéro de téléphone ou un numéro d'ID selon les méthodes de paiement choisies. Vous pouvez réessayer. Contactez notre équipe de soutien 121 si cela reste non résolu. |

---

## Statuts d'enregistrement

| Type | Description | Actions requises |
| :---- | :----------- | :---------- |
| **Nouveau** | Les enregistrements ont été enregistrés dans le programme et ne sont pas encore inclus. | Un agent CVA ou gestionnaire doit le valider et/ou l'inclure dans le programme. |
| **Validé(e)** | Les détails de l'enregistrement ont été vérifiés. L'enregistrement a été validé par un gestionnaire CVA ou un agent. Ils ne sont pas encore inclus dans le programme et ne peuvent pas recevoir de paiements. | Un gestionnaire CVA ou un agent peut inclure ou refuser les enregistrements du programme. |
| **Inclus(e)** | Les enregistrements ont été inclus dans le programme et peuvent commencer à recevoir des transferts de paiement via le portail 121. | Un gestionnaire financier ou un agent peut sélectionner les enregistrements dans les prochains tours de paiement. |
| **Décliné(e)** | Les enregistrements se sont avérés être mal enregistrés ou ne répondaient pas aux critères d'inclusion du programme. Les enregistrements ne recevront aucun paiement. | Aucune action requise, sauf si l'enregistrement a été refusé à tort. Les enregistrements peuvent être réinclus si nécessaire. |
| **Mis(e) en pause** | Les enregistrements ne sont actuellement pas inclus dans la distribution (les paiements sont en pause) mais font toujours partie du programme. | Les enregistrements peuvent être inclus ou refusés du programme selon les SOP. Un gestionnaire financier peut décider de la mise à jour du statut. |
| **Complété(e)** | Les enregistrements ont reçu le montant complet des transferts. Aucun autre paiement ne peut être envoyé. | Aucun. Ce statut est automatiquement généré par le système. Sauf si des tours de paiement supplémentaires ont été ajoutés au programme, ce statut restera inchangé. |

!!! Import "Mises à jour des statuts"
    Les rôles de gestionnaire CVA et d'agent CVA ont les autorisations de mettre à jour les statuts des enregistrements au sein de leur programme attribué. Si vous remarquez que le statut d'un enregistrement doit être mis à jour, veuillez contacter votre gestionnaire CVA ou agent CVA pour discuter des prochaines étapes.

    Seul le statut **Complété(e)** est automatiquement généré par le système une fois que tous les paiements ont été traités pour les enregistrements inclus dans le programme.

---

-8<- "docs/fr/_snippets/contact-support.md"
