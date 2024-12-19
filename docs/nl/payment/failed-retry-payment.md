---
title: Betaling - Mislukte en opnieuw proberen betalingen
hide:
  - toc
---

Bij het verwerken van de betalingen worden de statussen bijgewerkt met **Succesvol**, **Wachten** en **Mislukt**.
Hieronder vindt u de stapsgewijze instructies om de redenen van **mislukte betalingen** en opnieuw proberen betalingen te begrijpen.

*Voor beschrijving van betalingsstatussen, verwijzen wij u naar deze [pagina met de statussen.](./list-status-payment-page.md)

!!! Belangrijk "Wie kan acties uitvoeren op deze pagina?"
    Financieel Manager en Financieel Medewerker rollen kunnen acties uitvoeren op de Betalingspagina.  
    Aanvullende gebruikers kunnen alleen **Bekijk**-rechten krijgen op deze pagina. [Meer informatie over Gebruikers & Rollen](../users/users-roles-page.md)

### Redenen voor mislukte betalingen

Mislukte betalingen treden op als gevolg van een fout in de gegevens. Afhankelijk van hoe de betaling in uw instantie wordt verwerkt, kunt u naar verschillende fouten kijken.

**1. Onjuiste betalingsgegevens**
    De vereiste KYC is onjuist en kan niet overeenkomen met de informatie die door de FSP vereist is om de betaling te verwerken. De onjuiste gegevens kunnen als volgt zijn:

- Volledige naam PA
- Telefoonnummers
- Bankrekeningnummer
- Identificatienummer
- Locatie

Zodra u de onjuiste gegevens hebt geïdentificeerd, kunt u de informatie binnen het PA-profiel corrigeren. Volg de instructies [op deze pagina.](../registration/edit-pa-profile.md)

**2. Verkeerd formaat van het reconciliatiebestand**
    Voor handmatige betaling is het geïmporteerde reconciliatiebestand niet correct geformatteerd. De gegevens kunnen niet overeenkomen binnen het platform. Controleer de instructies voor het formatteren van uw [handmatige reconciliatiebestand.](./manual-payment-reconciliation.md)

**3. PA's hebben hun betalingsgegevens gewijzigd**
    In het geval dat de mislukte betaling optreedt terwijl de PA's in het verleden succesvol de betaling hebben ontvangen, kan dit te wijten zijn aan het feit dat PA's hun betalingsgegevens of telefoonnummer hebben gewijzigd. Bijgevolg kan de FSP de betaling niet matchen en verwerken.

**4. Bijwerken van betaling tussen FSP-121 mislukt**
    Als uw instantie is geïntegreerd met een FSP, kan de integratie problemen ondervinden. Neem contact op met het 121 Support Team om te verifiëren of dit te wijten kan zijn aan een integratiefout.

### Opnieuw proberen betalingen

!!! Belangrijk "Goed om te weten"
    Betalingen kunnen alleen opnieuw worden geprobeerd binnen de huidige betalingsronde. Bijgevolg, als u een nieuwe betalingsronde start, moeten eventuele opnieuw proberen betalingen van de vorige ronde individueel worden gedaan in plaats van in bulk. We raden sterk aan om de gegevens voor de lopende betaling te reconciliëren voordat u doorgaat met de volgende transactie.

    Neem contact op met uw Financiële Dienstverlener (FSP) als de betalingsreconciliatie nog niet aan uw financiële team is verstrekt.

Zodra u de reden hebt geïdentificeerd, kunt u doorgaan met het opnieuw proberen van de betalingen:

- Ga naar de **Betalings** pagina
- Klik op de knop **Opnieuw proberen betalingen** gemarkeerd in rood
- De transactie wordt automatisch opnieuw geprobeerd voor begunstigden geïdentificeerd met een **mislukte betaling** status
- De betalingsstatus wordt bijgewerkt

**Wat als betalingen blijven mislukken?**

We raden aan om contact op te nemen met ons ondersteuningsteam om samen met uw financiële team de redenen van mislukte betalingen te verifiëren. We zullen begeleiding bieden in de volgende stappen.

-8<- "docs/_snippets/contact-support.md"
