# Toteutusdokumentti

## Rakenne

Ohjelmassa valmiiksi luotuja labyrintteja selvitetään sekä Wall Follower-, että Tremauxin algoritmilla. Labyrintit ovat
Ascii-muotoisia ja niihin on merkitty sekä aloitus- että lopetuskohta. Labyrintit ovat 'täydellisiä', eli ne eivät sisällä
irtonaisia saarekkeita tai osia.

Ohjelma suoritetaan komentorivillä ja se kysyy käyttäjältä syötettä, jonka perusteella ohjelma suoritetaan. Valittavana
on tällä hetkellä kolme eri kokoista labyrinttia. Ohjelma tulostaa molempien algoritmien löytämät reitit visualisoituna
Ascii-tyylillä, sekä reittien pituudet.Toteutuksessa on myös pygamella tehty visualisointi, mutta se on vielä hieman virheellinen,
joten se ei ole toistaiseksi käytössä.

Molemmat algoritmit ovat toteutettu omissa luokissaan, jotka saavat syötteenä labyrintin. Algoritmien toiminta ja apuvälineet
ovat jaettu luokan sisällä erinäisiin funktioihin. mazes.py sisältää funktion, joka palauttaa halutun kokoisen labyrintin.
Main.py sisältää varisnaisen toteutuksen, ja se onkin suoritettava, jos haluaa ohjelmaa käyttää halutusti.

## Aika- ja tilavaativuudet

Molemmat algoritmit toteutuvat ajasssa O(|N||M|), missä N on labyrintin rivien ja M sarakkeiden määrä. Tämä on epäedullisin tilanne,
jossa algoritmi joutuu vierailemaan kaikissa solmuissa. Aikavaatimus määräytyy siis suoraan labyrintin koon mukaan, mutta käytännössä 
algoritmit toimivat erittäin nopeasti järkevän kokoisilla labyrinteilla.

Trémauxin ja Wall Follower- algoritmien tilavaatimukset ovat aikavaatimuksien tapaan O(NM), sillä niidenn pitää tallettaa muistiin vieraillut 
solmut ja oikeat reitit, jotka ovat huonoimmassa tapauksessa kaikki labyrintin solmut (poislukien seinämät).

## Lähteet

Wikipedia, [Maze Solving Algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm)

Wikipedia, [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)

