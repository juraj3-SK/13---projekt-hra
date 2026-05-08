from nepriatelia.drak import drak
nepriatel_drak=drak(1)

from nepriatelia.goblin import goblin
nepriatel_goblin=goblin(2)

from nepriatelia.kostlivec import kostlivec
nepriatel_kostlivec=kostlivec(3)

from nepriatelia.ork import ork
nepriatel_ork=ork(4)

from predmet import predmet
mec=predmet(nazov="mec", typ="zbran", hodnota=10, consumable=0)
lektvar=predmet(nazov="jahodovy lektvar", typ="lektvar", hodnota=5, consumable=1)


vybava=[]
vybava.append(mec)
vybava.append(lektvar)

from hrac import hrac
#pisat takto s menami premennych
hrac=hrac(id=5, nazov="hrac_jozko", max_zivoty=10, utok=10, mana=30, level=1, xp=10, inventar=vybava, zlato=10)
#nie takto:
#hrac=hrac(5, "hrac_jozko", 10, 10, 30, 1, 10, "mec", 10)

print (hrac)
#hrac.func_liecenie()
#print (hrac)
#hrac.func_pridaj_xp(nepriatel_drak)
#print (hrac)
#hrac.func_pridaj_xp(nepriatel_drak)
#print (hrac)