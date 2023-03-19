# Määrittelydokumentti
Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti (TKT)

Ohjelmointikieli: Python

Dokumentaatiokieli: Suomi

Sovellus on labyrintin ratkaisija, joka etsii parhaimman reitin 
ulos labyrintista.Reitin etsii kaksi eri algoritmia, joiden eroja 
tarkastellaan.

Ratkaisun löytämiseen käytän ainakin alogritmeja Wall Follower ja Trémaux. 
Ajan salliessa olisi mielenkiintoista lisätä vertailtavaksi jokin muu näiden lisäksi.
Sovellus toteuttaa reitin etsinnän näillä algoritmeilla ja vertailee 
tuloksia keskenään.

Käyttäjä voi valita useasta labyrintin kokovaihtoehdosta haluamansa, ja 
algoritmit etsivät lyhyimmän reitin alusta loppuun. Sovellus näyttää käyttäjälle
reitit ja tietoa suorituksesta.

## Tietorakenteet

Käytän toteutuksessa tietorakenteena listoja sekä joukkoja.

## Aika- ja tilavaatimukset

Wall Follower ja Tremaux toteutuvat molemmat ajassa O(|E|+|V|), missä E on 
kaarien määrä ja V on solmujen määrä.


Wall Followerin tialvaatimus on O(1), sillä sen ei tarvitse hyödyntää
tietorakenteita toiminnassaan.


Trémauxin algoritmin tilavaatimus on myös O(1), sillä sen pitää 
muistaa ainoastaan ennestään kuljetut polut,mihin ei tarvita 
ylimääräistä tilaa. 
