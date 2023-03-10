# Basisproject API
Voor dit project heb ik gekozen om een API te maken die kan dienen voor het maken van een voetbalklassement voor een bepaalde competitie.
In dit project kies ik ervoor om te werken rond de Belgische voetbalcompetitie, met name de Jupiler Pro League.
De API beschikt over vier verschillende tabellen binnen mijn database.
Ik maak namelijk gebruik van een algemene tabel voor het aanmaken van een ploeg, een volgende tabel met de bijhorende trainer en een tabel
over het bijhorende stadion hieraan gekoppeld. 
Je bent in staat om elke ploeg, trainer en stadion te bewerken en te verwijderen. Ook is het mogelijk om een overzicht van elke tabel te krijgen.

De vierde tabel die is aangemaakt richt zicht tot de security van bepaalde stappen.
In deze tabel zal je namelijk een gebruiker van de voetbalbond kunnen aanmaken. 
Deze gegevens (email en wachtwoord) zijn nodig om je te kunnen inloggen. 
Er wordt gebruik gemaakt van hashing om de wachtwoorden te beveiligen. 
Ik heb er bewust voor gekozen om deze beveiliging niet op de GET en POST methodes toe te passen zodat deze nog in de front-end gebruikt kunnen worden.
Deze security is wel op alle PUT en DELETE functies toegepast.

Ik ben er als extraatje ook in geslaagd een werkende front-end te maken.
Hierop staan de 3 verplichte GET en de verplichte POST functies. 
De front-end wordt ook op netlify gehoste.

## Informatie
* GitHub repository voor de API: https://github.com/jentelliekens/API_Eindproject
* Github repository voor de front-end: https://github.com/jentelliekens/API_Eindproject_Frontend 
* Hosted API link: https://useritem-api-service-api-eindproject-jentelliekens.cloud.okteto.net/
* Hosted website link met netlify: https://eindproject-api-liekens-jentel.netlify.app/

## Screenshots OpenAPI docs
* Overzicht van alle opties ![OpenAPI_overzicht.PNG](Afbeeldingen/Overzicht_OpenAPI.PNG)
* Het toevoegen van een gebruiker voor de autorisatie binnen de API ![Aanmaken_User.PNG](Afbeeldingen/Aanmaken_User.PNG)
* Inloggen van een aangemaakte gebruiker ![Inloggen_User.PNG](Afbeeldingen/Inloggen_User.PNG)
* Het weergeven van alle gebruikers die zijn aangemaakt ![Weergeven_Users.PNG](Afbeeldingen/Weergeven_Users.PNG)
* Het weergeven van de ingelogde gebruiker ![Weergeven_Ingelogde_User.PNG](Afbeeldingen/Weergeven_Ingelogde_User.PNG)
* Het weergeven van een gebruiker opgevraagd met zijn ID ![Weergeven_ID_User.PNG](Afbeeldingen/Weergeven_ID_User.PNG) 
* Het verwijderen van een gebruiker aan de hand van zijn ID ![Verwijderen_ID_User.PNG](Afbeeldingen/Verwijderen_ID_User.PNG)  ![Delete_Bewijs2.PNG](Afbeeldingen/Weergeven_ID2_User.PNG)
* Het aanmaken van een ploeg ![Aanmaken_Ploeg.PNG](Afbeeldingen/Aanmaken_Ploeg.PNG)
* Het aanmaken van een stadion ![Aanmaken_Stadion.PNG](Afbeeldingen/Aanmaken_Stadion.PNG)
* Het weergeven van de bestaande stadions ![Weergeven_Stadions.PNG](Afbeeldingen/Weergeven_Stadions.PNG)
* Het updaten van een stadion aan de hand van zijn ID ![Bewerken_Stadion.PNG](Afbeeldingen/Bewerken_Stadion.PNG)  ![Bewijs_Bewerken_Stadion.PNG](Afbeeldingen/Bewijs_Bewerken_Stadion.PNG)
* Het verwijderen van een stadion aan de hand van zijn ID ![Verwijderen_Stadion.PNG](Afbeeldingen/Verwijderen_Stadion.PNG)  ![Bewijs_Verwijderen_Stadion.PNG](Afbeeldingen/Bewijs_Verwijderen_Stadion.PNG)
* Het aanmaken van een trainer ![Aanmaken_Trainer.PNG](Afbeeldingen/Aanmaken_Trainer.PNG)
* Het weergeven van de bestaande trainer ![Weergeven_Trainers.PNG](Afbeeldingen/Weergeven_Trainers.PNG)
* Het updaten van een trainer aan de hand van zijn ID ![Bewerken_Trainer.PNG](Afbeeldingen/Bewerken_Trainer.PNG)  ![Bewijs_Bewerken_Trainer.PNG](Afbeeldingen/Bewijs_Bewerken_Trainer.PNG)
* Het verwijderen van een trainer aan de hand van zijn ID ![Verwijderen_Trainer.PNG](Afbeeldingen/Verwijderen_Trainer.PNG)  ![Bewijs_Verwijderen_Trainer.PNG](Afbeeldingen/Bewijs_Verwijderen_Trainer.PNG)
* Het weergeven van de bestaande ploegen ![Weergeven_ploegen.PNG](Afbeeldingen/Weergeven_Ploegen.PNG)
* Het updaten van een ploeg aan de hand van zijn ID ![Bewerken_Ploeg.PNG](Afbeeldingen/Bewerken_Ploeg.PNG)  ![Bewijs_Bewerken_Ploeg.PNG](Afbeeldingen/Bewijs_Bewerken_Pleog.PNG)
* Het verwijderen van een ploeg aan de hand van zijn ID ![Verwijderen_Ploeg.PNG](Afbeeldingen/Verwijderen_Ploeg.PNG)  ![Bewijs_Verwijderen_Ploeg.PNG](Afbeeldingen/Bewijs_Verwijderen_Ploeg.PNG)

## Screenshots Postman
Het is belangrijk om te weten dat je ook via Postman je eerst dient aan te melden. Dit doe je door de variabelen zoals op onderstaande afbeelding te zetten.
Als deze correct zijn kan je op "Get New Access Token" klikken wat je een nieuwe acces token geeft.
Deze dien je bovenaan bij de "Access Token" in te vullen en deze zal ik ook gebruiken bij de onderstaande stappen indien nodig. 
![Opzetten Postman](Afbeeldingen/Postman1.PNG)
* Toevoegen van een gebruiker via Postman ![Opzetten Postman](Afbeeldingen/Postman2.PNG)
* Opvragen van de huidige gebruiker via Postman ![Opvragen_Huidige_Gebruiker](Afbeeldingen/Postman3.PNG)
* Opvragen van een gebruiker op basis van ID via Postman ![Opvragen_Gebruiker](Afbeeldingen/Postman4.PNG)
* Opvragen van alle gebruikers via Postman ![Opvragen_Gebruikers](Afbeeldingen/Postman5.PNG)
* Verwijderen van een gebruiker op basis van ID via Postman ![Verwijderen_Gebruiker](Afbeeldingen/Postman6.PNG) ![Bewijs_Verwijderen_Gebruiker](Afbeeldingen/Postman7.PNG)
* Toevoegen van een ploeg via Postman ![Toevoegen_Ploeg](Afbeeldingen/Postman8.PNG)
* Toevoegen van een stadion via Postman ![Toevoegen_Stadion](Afbeeldingen/Postman9.PNG)
* Opvragen van alle stadions via Postman ![Opvragen_Stadions](Afbeeldingen/Postman10.PNG)
* Bewerken van een stadion op basis van ID via Postman ![Bewerken_Stadion](Afbeeldingen/Postman11.PNG) ![Bewijs_Bewerken_Stadion](Afbeeldingen/Postman12.PNG)
* Verwijderen van een stadion op basis van ID via Postman ![Verwijderen_Stadion](Afbeeldingen/Postman13.PNG) ![Bewijs_Verwijderen_Stadion](Afbeeldingen/Postman14.PNG)
* Toevoegen van een trainer via Postman ![Toevoegen_Trainer](Afbeeldingen/Postman15.PNG)
* Opvragen van alle trainers via Postman ![Opvragen_Trainers](Afbeeldingen/Postman16.PNG)
* Bewerken van een trainer op basis van ID via Postman ![Bewerken_Trainer](Afbeeldingen/Postman17.PNG) ![Bewijs_Bewerken_Trainer](Afbeeldingen/Postman18.PNG)
* Verwijderen van een trainer op basis van ID via Postman ![Verwijderen_Trainer](Afbeeldingen/Postman19.PNG) ![Bewijs_Verwijderen_Trainer](Afbeeldingen/Postman20.PNG)
* Opvragen van alle ploegen via Postman ![Opvragen_Ploegen](Afbeeldingen/Postman21.PNG)
* Bewerken van een ploeg op basis van ID via Postman ![Bewerken_Ploeg](Afbeeldingen/Postman22.PNG) ![Bewijs_Bewerken_Ploeg](Afbeeldingen/Postman23.PNG)
* Verwijderen van een ploeg op basis van ID via Postman ![Verwijderen_Ploeg](Afbeeldingen/Postman24.PNG) ![Bewijs_Verwijderen_Ploeg](Afbeeldingen/Postman25.PNG)

## Screenshots Front-end
Wanneer we naar onze front-end gaan kunnen we ook een ploeg toevoegen via hier. 
Als we alle gegevens hebben ingevuld en op "Maak ploeg" klikken zal deze worden toegevoegd.
Deze komt ook bij in de lijst te staan wanneer we de pagina herladen.

![Toevoegen_Ploeg_Frontend](Afbeeldingen/Toevoegen_Ploeg_Frontend.PNG) ![Bewijs_Toevoegen_Ploeg_Frontend](Afbeeldingen/Bewijs_Toevoegen_Ploeg_Frontend.PNG)
