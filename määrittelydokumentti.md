# Määrittelydokumentti
Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

Ohjelmointikieli: Python

Dokumentaatiokieli: Suomi

Sovellus on labyrintin ratkaisija, joka etsii parhaimman reitin 
ulos labyrintista. Reitin etsii kaksi eri algoritmia, joiden eroja 
tarkastellaan.

Ratkaisun löytämiseen käytän ainakin alogritmeja Wall Follower ja Trémaux. 
Ajan salliessa olisi mielenkiintoista lisätä vertailtavaksi jokin muu näiden lisäksi.
Sovellus toteuttaa reitin etsinnän näillä algoritmeilla ja vertailee 
tuloksia keskenään.

Valitsin kyseiset algoritmit, sillä ne olivat labyrintin ratakisuun soveltuvista 
algoritmeista itseäni kiinnostavimmat. Wall Follower on looginen ja yksinkertainen ratkaisu,
joka olisi ihmiseltäkin luonteva ratkaisu, jos joutuisi labyrinttiin. Tremaux taas oli
mielenkiintoinen ratkaisu, jonka visualistointi kiinnitti heti huomioni. On mielenkiintoista
nähdä, miten algoritmit vertautuvat toisiinsa.

Käyttäjä voi valita useasta labyrintin kokovaihtoehdosta haluamansa, ja 
algoritmit etsivät lyhyimmän reitin alusta loppuun. Sovellus näyttää käyttäjälle
reitit ja tietoa suorituksesta. Labyrintit on tarkoitus toteuttaa taulukkoina, jotka ovat
valmiiksi luotuina. Lopputulos on vähintään reitin pituus lukuarvona, mutta pyrin
toteuttamaan jonkinlaisen visualisoinnin.

## Tietorakenteet

Alustavasti käytän toteutuksessa tietorakenteena ainoastaan listoja ja joukkoja, 
ellei jokin muu osoittaudu järkevämmäksi.


## Aika- ja tilavaatimukset

Wall Follower ja Tremaux toteutuvat molemmat ajassa O(|E|+|V|), missä E on 
kaarien määrä ja V on solmujen määrä.


Wall Followerin tialvaatimus on O(1), sillä sen ei tarvitse hyödyntää
tietorakenteita toiminnassaan.


Trémauxin algoritmin tilavaatimus on myös O(1), sillä sen pitää 
muistaa ainoastaan ennestään kuljetut polut,mihin ei tarvita 
ylimääräistä tilaa. 

## Lähteet
[Wikipedia Maze-Solving algoritm](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
[Maze Escape with Wall-Followin Algorithm](https://andrewyong7338.medium.com/maze-escape-with-wall-following-algorithm-170c35b88e00) (Tämä tarkoitettu roboteille mutta selviää hyvin logiikka)

