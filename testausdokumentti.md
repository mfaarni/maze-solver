## Testausdokumentti

### Yksikkötestauksen kattavuus
![coverage_maze-solver](https://github.com/mfaarni/maze-solver/assets/102048170/f41660f2-1f8e-4034-bed1-85139657624a)

### Mitä testataan?
Testeissä testataan labyrinttiratkaisijan toimivuutta Wall Follower- ja Tremauxin algoritmeilla. Testit tarkistavat, että funktiot löytävät oikeat
kohdat labyrintista ja että reitti muokataan oikein listaan. Testit tarkistavat myös, että palautuksissa reittien pituudet ja arvot ovat oikeita. 
Testaus toteutetaan kaikille sovelluksessa käytettäville labyrinteille, sekä joillekkin testausta varten muodostetuille erityisille labyrinteille.
Esimerkiksi Tremauxin algoritmia testataan usealla labyrintilla jotka eivät ole täydellisiä, eli sisältävät syklisyyttä ja irtonaisia osia.

Testeissä käydään läpi myös erilaisia muita tilanteita, kuten tyhjiä syötteitä ja reittejä sekä tilanteita joissa ollaan jumissa labyrintissa. 
Testit pyrkivät tarkistamaan, että algoritmit löytävät reitin aina oikein eri kokoisissa ja muotoisissa labyrinteissa eivätkä toimi poikkeustilanteissa väärin.

Labyrintti visualisoidaan pygamen avulla, mutta tätä osuutta ei testata. UI-puoli jää siis testaamatta, ja testit keskittyvät itse algoritmeihin ja niiden 
tietorakenteisiin. Visualisoinnin pohjalla toimivat ascii-taulut kuitenkin ovat osana testausta.

### Testien suoritus
Testit toimivat GitHub Actionsissa, ja testikattavuus on nähtävissä repositorion etusivulla. Testit voidaan suorittaa myös paikallisesti 
antamalla komennon ```poetry shell``` ja tämän aktivoitua antamalla komennon ```pytest src``` projektin juurihakemistossa. Kattavuusreportin voi käyttäjä
luoda komennolla ```coverage html```. Nämä ovat myös mahdollista toteuttaa komennoilla ```poetry run invoke test``` ja ```poetry run invoke coverage-reprort``` .

