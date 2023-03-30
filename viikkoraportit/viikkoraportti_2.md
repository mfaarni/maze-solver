# Viikkoraportti 2

## Mitä tein?
Tällä viikolla aloitin koodin pohjan rakentamisesta. Loin yksinkertaisen ascii-muotoisen labyrintin, jonka tallensin merkkijonoina listaan siten,
että jokainen merkkijono vastaa yhtä "kerrosta" labyrintissa. Seuraavaksi aloin heti kokeilemaan yksinkertaisemman Wall Follower- algoritmin kirjoittamista,
ja sainkin sen lopulta toteutettua. Loin vielä toisen testilabyrintin, jotta toimivuus olisi selkeämpää. Muutin melko sotkuisesti kirjoitetun algoritmin luokaksi 
ja jaottelin toiminnot funktioihin. 

Halusin visualisoida algoritmin reitin, jotta sitä olisi helpompi tarkastella. Toteutin tämän pygamen avulla, sillä se on 
minulle ennestään tuttu ja siksi toteutus oli kohtalaisen helppo. Nyt pygame piirtää labyrintin ja näyttää reitin, jota algoritmi on kulkenut maaliin. 
Viimeisenä vielä kirjoitin muutaman testin ja alustin CI-putken sekä codecovin. 

Aikaa prokjektiin käytin tämän viikon aikana noin 12 tuntia.

## Aikaan saatua
- Yksinkertaiset labyrintin testausta varten
- Toimiva Wall Follower- algoritmi
- Pygamella toteutettu visualisointi
- Testejä

## Onnistumiset ja haasteet

Sain projektin nopeasti aluilleen ja olen melko tyytyväinen ensimmäisen varsinaista koodausta sisältävän työviikon tuotokseen. 
Algortimin sain melko nopeasti toimimaan, toisaalta Wall Follower onkin melko yksinkertainen. Tremauxissa tulee luultavasti olemaan hieman enemmän haastetta. 
Viikolla eniten tuskaa tuotti algoritmin uudelleenformatointi luokaksi. Tyhmyyttäni en heti aluksi kirjoittanut toteutusta luokkaan, ja jouduin rakentamaan 
algoritmin siksi osittain uudelleen. Luokkaan jakamisen yhteydessä tein pienen virheen, joiden löytämisessä kesti huomattavan pitkään. Olin kuitenkin saanut 
algoritmin toimivaksi nopeammin kuin luulin, joten luokkaan jaon mutkat eivät haitanneet hirveästi.

## Ensi viikolla

Ensi viikolla parannan testikattavuutta ja siistin hieman koodia, otan pylintin käyttöön tätä varten. Kun edellä mainitut ovat valmiita, 
aloitan varmaan Tremauxin algoritmiin perehtymisen ja lähden koodaamaan sen toteutusta. Haluaisin myös parantaa pygame-ruudun käyttöliittymää,
jotta tuloksia olisi helpompi tutkia.
