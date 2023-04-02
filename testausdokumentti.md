## Testausdokumentti

### Yksikkötestauksen kattavuus
![Screenshot from 2023-04-02 23-36-33](https://user-images.githubusercontent.com/102048170/229378118-1771489d-03a7-49ee-98c0-d6ace27f259d.png)

### Mitä testataan?
Tällä hetkellä labyrinttiratkaisijan toimivuutta Wall Follower algoritmilla testataan. Testit tarkistavat, että funktio löytää oikeat
kohdat labyrintista ja että reitti muokataan oikein listaan. Tremauxin algoritmi ei vielä toimi oikein, joten sitä ei voida vielä testata.
Labyrintti visualisoidaan pygamen avulla, mutta tätä en testaa. UI-puoli jää siis testaamatta, ja testit keskittyvät itse algoritmeihin ja niiden 
tietorakenteisiin.

### Testien suoritus
Testit toimivat GitHub Actionsissa, ja testikattavuus on nähtävissä repositorion etusivulla. Testit voidaan suorittaa myös paikallisesti 
antamalla komennon ```poetry shell``` ja tämän aktivoitua antamalla komennon ```pytest src``` projektin juurihakemistossa. Kattavuusreportin voi käyttäjä
luoda komennolla ```coverage html```.

### Tulevaa
Testikattavuus on tällä hetkellä hieman heikko, sillä muutin Wall Follower-algon rakennetta ja täten testaus muuttui. En ole vielä ehtinyt kirjoittaa 
tarpeeksi kattavia testejä uudelle rakenteelle, mutta tämä sujunee verrattain nopeasti. Ensi viikolla toivon saavani Tremauxin algon toimimaan ja 
aloittaa myös sen testaamisen.
