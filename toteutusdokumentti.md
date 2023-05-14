# Toteutusdokumentti

## Rakenne

Ohjelmassa valmiiksi luotuja labyrintteja selvitetään sekä Wall Follower-, että Tremauxin algoritmilla. Labyrintit ovat
Ascii-muotoisia ja niihin on merkitty sekä aloitus- että lopetuskohta. Labyrintit ovat 'täydellisiä', eli ne eivät sisällä
irtonaisia saarekkeita tai osia.

Ohjelma avautuu pygameen, jossa käyttäjä pystyy valitsemaan eri kokoisista labyrinttivaihtoehdoista. Ohjelma kertoo suorituksista tietoa, löydetyn reitin
pituuden sekä suoritukseen kuluneen ajan. Vain ensimmäinen näistä on oikeastaan merkitsevä, ja suroitusaika on lisätty lähinnä lisäominaisuutena
mielenkiinnosta. Käyttäjä voi tämän jälkeen valita molemmista algoritmeista toisen, jonka jälkeen näytölle tulostuu visualisointi algoritmin suorituksesta
sen kulkiessa labyrintissa. Käyttäjä pääsee takaisin näkymissä painamalla ```esc```-näppäintä.

Molemmat algoritmit ovat toteutettu omissa luokissaan ```Tremaux```  ja  ```WallFollower``` , jotka ovat omissa tiedostoissaan ```tremaux.py```  ja 
```wall_follower.py``` . Molemmat luokat saavat syötteenä labyrintin, Tremaux myös aloitus- ja loppupisteet. Algoritmien toiminta ja apuvälineet ovat 
jaettu luokan sisällä erinäisiin funktioihin. mazes.py sisältää funktion, joka palauttaa halutun kokoisen labyrintin. Main2.py sisältää varisnaisen toteutuksen, 
ja se onkin suoritettava,jos haluaa käyttää ohjelmaa halutusti.

## Aika- ja tilavaativuudet

Molemmat algoritmit toteutuvat lineaarisessa ajasssa O(n), sillä ne käyvät huonoimmassa tapauksessa labyrintin kaikki vapaat solmut läpi korkeintaan kaksi kertaa.
Vierailtavat solut kasvavat siis labyrintin kasvaessa lineaarisesti, eikä aikavaatimus nouse sen suuremmin. Molemmat algoritmit toimivat siis verrattain nopeasti eikä
niiden suorituksissa pitäisi tulla ajan vastaan.

Trémauxin ja Wall Follower- algoritmien tilavaatimukset ovat aikavaatimuksien tapaan O(n), sillä niiden pitää tallettaa muistiin vieraillut 
solmut ja oikeat reitit, jotka ovat huonoimmassa tapauksessa kaikki labyrintin solmut (poislukien seinämät).

## Paranneltavaa

Ohjelman nykyiset toiminnot toimivat pääosin hyvin, varsinkin algoritmit. Pygamen nykyinen toteutus on eritätin hidas suurimalla labyrinttikoolla, ja tämän voisi toteuttaa
tehokkaammin, jolloin sen visualisointi olisi huomattavasti toimivampi. Käyttöliittymää voisi muutenkin parannella, mutta se ei ole kurssin kannalta olennaista.
Muuten ohjelmaa voisi kehittää eteenpäin lisäämällä uusia toimintoja, kuten omien labyrinttien luonnin. Tällä hetkellä niitä on vain kourallinen. Lisäksi labyrintteihin voisi 
esimerkiksi pystyä määrittämään itse aloitus- ja lopetuskohdat.


## Lähteet

Wikipedia, [Maze Solving Algorithm](https://en.wikipedia.org/wiki/Maze-solving_algorithm)

Wikipedia, [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search)

