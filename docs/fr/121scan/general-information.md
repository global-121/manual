---
title: 121 Scan - Informations générales
hide:
  - toc
---

- [À quoi 121 Scan peut-il servir ?](#%C3%A0-quoi-121-scan-peut-il-servir)
- [Comment 121 Scan fonctionne-t-il avec la plateforme 121 ?](#comment-121-scan-fonctionne-t-il-avec-la-plateforme-121)
- [Sécurité des données](#s%C3%A9curit%C3%A9-des-donn%C3%A9es)
- [Prérequis pour utiliser 121 Scan](#pr%C3%A9requis-pour-utiliser-121-scan)
- [Utiliser 121 Scan pour la vérification d'identité](#utiliser-121-scan-pour-la-v%C3%A9rification-didentit%C3%A9)
- [Utiliser 121 Scan pour mettre à jour des informations dans 121](#utiliser-121-scan-pour-mettre-%C3%A0-jour-des-informations-dans-121)

---

121 Scan est une application hors ligne développée par le 510 (la Croix-Rouge néerlandaise). Elle permet de générer automatiquement des cartes de bénéficiaire avec des codes QR pour chaque personne d'un programme. Le personnel ouvre ensuite 121 Scan sur un téléphone, une tablette ou un ordinateur portable, scanne ce code QR (ou saisit le code unique de la personne), et l'application affiche les informations relatives à la personne concernée : par exemple son nom, sa photo et toute autre information que le programme a choisi d'afficher. Le personnel peut alors confirmer si la personne est bien celle qu'elle prétend être, ajouter ou modifier des informations dans son enregistrement 121, et enregistrer qu'une transaction a eu lieu.

121 Scan ne remplace **pas** la plateforme 121 ; il fonctionne en complément de 121. Il s'agit d'un outil de terrain qui communique avec 121 en arrière-plan, afin que le personnel travaillant sur un site de distribution, qui ne dispose pas nécessairement d'un compte 121 ou d'une connexion internet fiable, puisse quand même effectuer les actions de vérification et de paiement. L'application 121 Scan se synchronise ensuite avec la plateforme 121, via une connexion internet.

!!! Info "121 Scan est un outil en constante évolution"
    Il a été conçu pour résoudre des problèmes spécifiques sur le terrain, en attendant qu'une solution permanente soit développée au sein de 121 lui-même. Il n'est actuellement utilisé que dans un nombre limité de contextes pilotes. Pour en savoir plus, parlez-en à votre Responsable de compte, et consultez [**Intégration et assistance**](./distribution-staff-portal.md#int%C3%A9gration-et-assistance) sur la page Portail du personnel de distribution.

---

<a id="%C3%A0-quoi-121-scan-peut-il-servir"></a>

## À quoi 121 Scan peut-il servir ?

121 Scan est utile dans les situations où des distributions sont organisées sur site, par exemple pour des paiements en espèces ou des cartes prépayées, et où le flux de paiement standard de 121 ne convient pas à tous les besoins. Par exemple, parce qu'il n'y a pas de connexion internet, ou parce que le prestataire de services financiers (PSF) qui gère les espèces n'a pas d'accès direct à 121. Il peut aider à :

- **Vérifier l'identité d'une personne**, en scannant un code QR ou en saisissant un code unique et en affichant sa photo et ses informations, plutôt que de se fier uniquement à des listes papier ou de demander aux personnes de prouver leur identité d'une autre manière.
- **Permettre à un PSF de participer au processus de paiement** sans lui donner accès à la plateforme 121 ni partager de fichiers Excel supplémentaires : il ne voit que les informations dont il a besoin pour faire son travail.
- **Enregistrer des informations manquantes sur le moment**, comme un numéro de carte ou de carte SIM qu'une personne ne reçoit qu'au moment de la distribution, afin de ne pas avoir à le noter sur papier puis à le saisir dans 121 plus tard.
- **Mettre à jour automatiquement les statuts de transaction grâce à une synchronisation avec le paiement de la plateforme 121**, afin que le personnel n'ait pas à réconcilier manuellement une liste papier ou un tableau après coup.

---

## Comment 121 Scan fonctionne-t-il avec la plateforme 121 ?

121 Scan se situe entre 121 et le terrain. Il ne stocke ni ne conserve aucune donnée de façon permanente sur l'appareil : il emprunte des informations à 121 (et parfois à Kobo) pour la durée nécessaire sur le terrain, puis renvoie les résultats à 121 dès que l'utilisateur clique sur **Send (Envoyer)**, lorsqu'une connexion internet est disponible.

Deux groupes de personnes l'utilisent, avec accès à 2 portails différents :

- **Le personnel de la Croix-Rouge** se connecte en tant qu'« Administrateur » pour relier 121 Scan au bon programme 121, choisir les informations que le PSF est autorisé à voir (s'il est impliqué dans 121 Scan), et générer les codes QR ou les bons qui seront scannés.
- **Le PSF ou le personnel de la Croix-Rouge** se connecte en tant que « Personnel de distribution » pour scanner les codes des personnes sur le site de distribution et enregistrer ce qui s'y passe.

### Le parcours de l'argent, et où 121 Scan s'intègre

Le schéma ci-dessous montre un parcours type de l'argent à travers 121, et les points où 121 Scan intervient. Les étapes exactes peuvent varier légèrement d'un programme à l'autre, par exemple selon que les personnes reçoivent un bon imprimé, une carte prépayée ou une carte SIM, mais le déroulement global reste le même.

![Le parcours standard de l'argent à travers 121, et où 121 Scan est utilisé.](../assets/img/121Scan-ParcoursCash.png)

**1. Configuration dans 121.** Comme pour tout programme d'assistance monétaire, les personnes sont enregistrées, vérifiées et incluses dans le programme. Un paiement est créé et approuvé dans 121.

**2. Préparer 121 Scan.** Un membre du personnel exporte la liste de paiement depuis 121 vers 121 Scan dans le Portail de l'administrateur, configure les informations qui seront montrées au PSF, et génère un code QR ou un bon imprimé au format PDF pour chaque personne.

**3. Sur le site de distribution.** Avant la distribution sur site, et tant qu'une connexion internet est disponible, le PSF ou le personnel de la Croix-Rouge doit se connecter via le Portail du personnel de distribution, sélectionner le bon programme sur lequel il travaille, et synchroniser son appareil afin qu'il puisse fonctionner hors ligne. Une fois les données synchronisées, il scanne ensuite le code de chaque personne avec 121 Scan. Cela fonctionne même sans connexion internet. Il vérifie l'identité de la personne et, selon le programme, peut aussi ajouter des informations à son enregistrement et enregistrer le statut de la transaction (réussie/échouée). (Voir [**Utiliser 121 Scan pour la vérification d'identité**](#utiliser-121-scan-pour-la-v%C3%A9rification-didentit%C3%A9) ci-dessous pour les étapes exactes.)

**4. Retour vers 121.** Dès que l'appareil est de nouveau en ligne, le PSF envoie à 121 toutes les informations collectées, y compris les statuts de transaction et les informations d'enregistrement mises à jour. Cela boucle le processus et facilite la réconciliation, sans travail manuel supplémentaire. Les statuts de paiement du programme sélectionné sont mis à jour dans la plateforme 121.

---

<a id="s%C3%A9curit%C3%A9-des-donn%C3%A9es"></a>

## Sécurité des données

121 Scan est utilisé sur des téléphones, tablettes et ordinateurs portables ordinaires sur le terrain ; il est donc conçu pour protéger les informations même si un appareil est perdu ou volé :

- **Rien n'est stocké de façon permanente.** 121 Scan ne conserve qu'une copie de travail de la liste du jour, et l'efface une fois les résultats renvoyés à 121.
- **Cette copie de travail est entièrement chiffrée** et ne peut être déchiffrée que par 121 Scan lui-même, de sorte qu'un appareil perdu ou volé n'expose aucune information personnelle.
- **L'accès est limité.** Les PSF ne voient que les informations dont ils ont besoin (définies par un administrateur), et l'accès aux bons et aux exports est limité au programme et à la zone propres à chaque membre du personnel.

121 Scan ne conserve pas de registre permanent séparé ; 121 reste la seule source de vérité. Signalez immédiatement un appareil perdu ou volé à votre point focal IM, afin que toute donnée non envoyée puisse être prise en compte.

!!! Important "Perte de données si un appareil est endommagé ou volé avant l'envoi"
    Bien que ce cas reste limité, comme l'application fonctionne hors ligne et sur des appareils locaux, il est important de savoir que si l'appareil est endommagé ou volé, toutes les données qui n'ont pas encore été envoyées — via le bouton **Send (Envoyer)** — seront perdues. Nous recommandons donc d'en discuter avec notre équipe CVA IM afin qu'elle puisse partager quelques bonnes pratiques à adopter pour votre distribution avec 121 Scan.

---

<a id="pr%C3%A9requis-pour-utiliser-121-scan"></a>

## Prérequis pour utiliser 121 Scan

Avant d'utiliser 121 Scan dans un programme, assurez-vous de disposer de :

- Un smartphone, une tablette ou un ordinateur portable équipé d'une caméra et d'un navigateur raisonnablement à jour (Chrome, Safari, Firefox ou Edge). L'application fonctionne dans le navigateur, sans rien à installer ; les appareils très anciens peuvent être plus lents.
- Une connexion internet (Wi-Fi, données mobiles ou satellite tel que Starlink) pour **Sync (Synchroniser)** avant de commencer et **Send (Envoyer)** une fois terminé. Cela n'est toutefois pas nécessaire pendant le scan du code QR lui-même.
- Un compte utilisateur 121 avec le bon programme sélectionné.
- Suffisamment d'espace de stockage libre pour la liste et les photos du jour ; une liste longue et riche en photos prend plus de temps à synchroniser, faites-le donc sur une connexion correcte.
- Les pilotes actuels sont généralement configurés pour un seul PSF à la fois.

!!! Important "Tester vos appareils avant une distribution réelle"
    Il est recommandé d'effectuer des tests avant une distribution réelle. Nous recommandons de tester l'application 121 Scan (Android) ou le navigateur sur l'appareil que vous utiliserez pendant la distribution. Pour un test réussi, demandez à l'équipe de soutien 121 de planifier une session de test avec vous. Nous 1) donnerons des conseils sur le programme à tester, 2) ajouterons autant d'enregistrements que prévu pour votre distribution, 3) nous connecterons à l'application web 121 Scan via le lien sur votre appareil, et 4) synchroniserons et résoudrons les éventuels problèmes de connexion. Cette étape est essentielle : si elle n'est pas correctement testée avant une distribution réelle, cela peut affecter votre expérience sur le terrain. **Ne sautez pas cette étape !**

---

<a id="utiliser-121-scan-pour-la-v%C3%A9rification-didentit%C3%A9"></a>

## Utiliser 121 Scan pour la vérification d'identité

L'usage le plus courant de 121 Scan est de confirmer que la personne présente devant un PSF est bien celle qui a droit au paiement. Le personnel de la Croix-Rouge comme les agents PSF peuvent utiliser le Portail du personnel de distribution.

- Avant le début de la journée, tant qu'il est encore en ligne, le PSF se connecte en tant que « Personnel de distribution », sélectionne le bon programme, et appuie sur **Sync (Synchroniser)**.
- Le personnel de distribution ouvre 121 Scan et appuie sur **Scan (Scanner)**.
- Il pointe la caméra vers le code QR de la personne, imprimé sur un bon ou une carte. Si le code est endommagé ou illisible, son numéro de référence peut être saisi dans le champ prévu à cet effet (voir [**Autoriser l'accès à la caméra sur votre appareil**](./distribution-staff-portal.md#autoriser-lacc%C3%A8s-%C3%A0-la-cam%C3%A9ra-sur-votre-appareil) si la caméra ne s'ouvre pas).
- 121 Scan affiche les informations de la personne : généralement une photo, un nom et toute autre information que le programme a choisi d'afficher, par exemple la réponse à une question de sécurité.
- Le PSF compare ces informations à la personne présente et appuie sur **Paiement approuvé** ou **Paiement refusé**.
- Conservez le bon physique ; remettez tous les bons QR utilisés à votre point focal en fin de journée, avec la réconciliation numérique.

---

<a id="utiliser-121-scan-pour-mettre-%C3%A0-jour-des-informations-dans-121"></a>

## Utiliser 121 Scan pour mettre à jour des informations dans 121

Il arrive qu'une personne ne reçoive certaines informations qu'au moment de la distribution, par exemple un nouveau numéro de carte prépayée ou un numéro de carte SIM pour la monnaie mobile. Plutôt que de le noter sur papier puis de le saisir dans 121 plus tard, cela peut être enregistré directement dans 121 Scan.

- Lorsque le code QR de la personne est scanné, le personnel peut ajouter les informations manquantes (par exemple le numéro de la carte qui vient de lui être remise) sur le même écran que celui utilisé pour la vérification.
- Cela est enregistré sur l'appareil, même sans connexion internet (voir [**Sécurité des données**](#s%C3%A9curit%C3%A9-des-donn%C3%A9es) ci-dessus).
- Une fois l'appareil de nouveau connecté à internet, le PSF peut envoyer la mise à jour à 121, où elle est ajoutée à l'enregistrement de la personne. Cela part avec les résultats de paiement du jour, via la même étape **Send (Envoyer)**.

Cela évite une double saisie et réduit le risque qu'un numéro de carte ou de carte SIM ne soit jamais renvoyé vers 121.

**Rôle du PSF :** c'est généralement le PSF qui remet la carte ou la carte SIM ; il est donc pratique que lui (ou le personnel de la Croix-Rouge présent) enregistre le numéro à ce moment-là, plutôt que de le transmettre séparément par la suite.

---

-8<- "docs/fr/_snippets/contact-support.md"
