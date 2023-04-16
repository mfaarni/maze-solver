# Toteutusdokumentti

## Rakenne

Ohjelmassa valmiiksi luotuja labyrinttejä selvitetään sekä Wall Follower-, että Tremauxin algoritmilla. Labyrintit ovat
Ascii-muotoisia ja niihin on merkitty sekä aloitus- että lopetuskohta. Labyrintit ovat 'täydellisiä', eli ne eivät sisällä
irtonaisia saarekkeita tai osia.

Ohjelmassa voi pelata Connnect Four peliä tietokonetta tai kaveria vastaan. Tietokonetta vastaan pelaaminen on toteutettu
minimax-algoritmilla, jota on tehostettu alpha-beta-karsinnalla. Pelin aloittaa aina ihmispelaaja, jonka jälkeen 
algoritmi laskelmoi parhaan mahdollisen siirron, joka johtaisi voittoon. Algoritmi olettaa myös ihmispelaajan pelaavan 
optimaalisimmalla tavalla.

Ohjelma on koodattu Pythonilla ja se koostuu sovelluslogiikasta ja käyttöliittymästä. Sovelluslogiikasta vastaavat
pääosin src/files kansiosta löytyvät tiedostot. Tiedostoissa on kutsuttavia luokkia, joiden toimintaan ohjelma perustuu. 
Käyttöliittymä on toteutetty Pyhtonin Pygame kirjastolla. Käyttöliittymästä vastaavat tiedostot löytyvät kansiosta src/UI.
Ohjelma käynnistyy tiedoston index.py avulla.


## Aika- ja tilavaativuudet
Minimaxalgoritmin, joka hyödyntää alpha-beta-karsintaa, aikavaativuus on O(sqrt(b^d)), jossa b on haarautumien määrä ja
d haun syvyys. Pelissä on 7 saraketta, johon pelinappulan voi laittaa ja tällä hetkellä kovakoodattuna syvyys 2.
Toteutuva aikavaativuus on siis O(sqrt(7²)). Toisaalta jos koko puu pitää käydä läpi eli alpha-beta-karsintaa ei voitu
hyödyntää, on aikavaativuus O(b^d) eli  O(7²).

Minimax-algortimin tilavaativuus on O(b * d), jossa b on haarautumien määrä ja d haun syvyys.


## Lähteet

Wikipedia (FI), [Neljän suora](https://fi.wikipedia.org/wiki/Nelj%C3%A4n_suora)

Wikipedia (ENG), [Minimax](https://en.wikipedia.org/wiki/Minimax)

Wikipedia (ENG), [Alpha-beta-karsinta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

GeeksForGeeks, [Minmax algorithm in game theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
