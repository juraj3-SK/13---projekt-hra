import random

from nepriatelia.drak import drak
nepriatel_drak=drak(1)

from nepriatelia.goblin import goblin
nepriatel_goblin=goblin(2)

from nepriatelia.kostlivec import kostlivec
nepriatel_kostlivec=kostlivec(3)

from nepriatelia.ork import ork
nepriatel_ork=ork(4)

from predmet import predmet

#zadefinuj slovnik
#key bude nazov, value bude predmet
zoznam_predmetov = {
  "maly_lektvar": predmet(nazov="Maly lektvar", typ="heal", hodnota=2, konzumovatelny=1),
  "velky_lektvar": predmet(nazov="Velky lektvar", typ="heal", hodnota=50, konzumovatelny=1),
  "mana_elixir": predmet(nazov="Mana elixir", typ="mana", hodnota=20, konzumovatelny=1),
  "mec": predmet(nazov="Mec", typ="zbran", hodnota=10, konzumovatelny=0)
}

#stara inicializacia vybavy
#ked sa otestuje nova, ktora vybera zo slovnika predmetov, tak to mozem zmazat
# vybava=[]
# tempPredmet=predmet(nazov="Mec", typ="zbran", hodnota=10, konzumovatelny=0)
# vybava.append(tempPredmet)
# tempPredmet=predmet(nazov="Maly lektvar", typ="heal", hodnota=2, konzumovatelny=1)
# vybava.append(tempPredmet)
# tempPredmet=predmet(nazov="Velky lektvar", typ="heal", hodnota=50, konzumovatelny=1)
# vybava.append(tempPredmet)
# tempPredmet=predmet(nazov="Mana elixir", typ="mana", hodnota=20, konzumovatelny=1)
# vybava.append(tempPredmet)
# tempPredmet=predmet(nazov="Mana elixir", typ="mana", hodnota=20, konzumovatelny=1)
# vybava.append(tempPredmet)

vybava=[]
vybava.append(zoznam_predmetov.get("mec"))
vybava.append(zoznam_predmetov.get("maly_lektvar"))
vybava.append(zoznam_predmetov.get("velky_lektvar"))
vybava.append(zoznam_predmetov.get("mana_elixir"))
vybava.append(zoznam_predmetov.get("mana_elixir"))

from hrac import hrac
#pisat takto s menami premennych
hrac=hrac(id=5, nazov="hrac_jozko", max_zivoty=20, utok=10, iniciativa=1, mana=30, level=1, xp=10, inventar=vybava, zlato=10)
#nie takto:
#hrac=hrac(5, "hrac_jozko", 10, 10, 30, 1, 10, "mec", 10)

print (hrac)

#nie som si isty, ci to ma byt tu
#viac by sa mi to pacilo v hracovi, ale tam nemam slovnik, musel by som ho tam poslat ako parameter funkcie
#necham si poradit, kam to dat
def func_vygeneruj_predmet_odmenu(obdarovany):
    #pravdepodobnost 20% na kazdy z lektvarov; pravdepodobnost 40% ze nedostane nic
    tempVar=random.randint(1,5)
    if (tempVar==1):
        print("Dostavas extra odmenu: maly lektvar.")
        obdarovany.func_pridaj_predmet(zoznam_predmetov.get("maly_lektvar"))
    elif (tempVar==2):
        print("Dostavas extra odmenu: velky lektvar.")
        obdarovany.func_pridaj_predmet(zoznam_predmetov.get("velky_lektvar"))
    elif (tempVar==3):
        print("Dostavas extra odmenu: mana elixir.")
        obdarovany.func_pridaj_predmet(zoznam_predmetov.get("mana_elixir"))
    else:
        print("Extra odmenu neziskavas.")


def func_subojove_kolo(nepriatel):
    #poradie utoku sa urci podla vyssej premennej iniciativa (plus hod kockou)
    tempVar=hrac.iniciativa+random.randint(1,6)-nepriatel.iniciativa-random.randint(1,6)
    #ak iniciativa hraca je vyssia, tak zacina
    if (tempVar>=0):
        #hrac utoci, ak nepriatel prezil, tak utoci spat. Ak nie, tak hrac dostava odmenu a mozno aj predmet
        hrac.func_zautoc(nepriatel)
        if (nepriatel.func_je_ziva()):
            nepriatel.func_zautoc(hrac)
        else:
            hrac.func_pridaj_odmenu(nepriatel)
            func_vygeneruj_predmet_odmenu(hrac)    
    else:
    #ak ma iniciativu vyssiu nepriatel, tak zacina nepriatel.
        nepriatel.func_zautoc(hrac)
        #Hrac utoci len ak prezil.
        if hrac.func_je_ziva():
            hrac.func_zautoc(nepriatel)
            #Ak zabil nepriatela, dostane odmenu.
            if (not nepriatel.func_je_ziva()):
                hrac.func_pridaj_odmenu(nepriatel)
                func_vygeneruj_predmet_odmenu(hrac)

    #TENTO POSTUP BOL DOHODNUTY NA ONLINE HODINE
    #zadefinujem utocnika1 ako hraca
    #zadefinujem napevno utocnika2 ako priseru
    #doplnit obom postavam dve premenne (premenna postavy!!!) iniciativa1/2 a poradie sa urci podla vyssej iniciativy + nejaky random
    #doplnit + prerobit (OBOJE!!!) funkcie func_zranenie tak:
    #prerobit func_zranenie tak, aby hracova fcia zranenie pri zabiti vypisala koniec
    #a funkcia pre priseru vracia 0/1, ak nebola zabita, tak nic a ak bola zabita, tak si hned v dalsom riadku volam funkciu "daj odmenu"
    #pri zabiti prisery dala utocnikovi odmenu (ak utocnikom je hrac)
    
hrac_chce_bojovat=1
while (hrac.func_je_ziva() and nepriatel_goblin.func_je_ziva() and (hrac_chce_bojovat==1)):
    operacia = input("Zadaj operaciu (info, utok, liecenie, pouzi predmet, vypis, utek): ")
    if operacia == "info":
        print (hrac)
    elif operacia == "utok":
        func_subojove_kolo(nepriatel_goblin)
    elif operacia == "liecenie":
        hrac.func_liecenie()
        #SEM DOPLNIT UTOK PRISERY, LEBO nepriatel necaka!
    elif ((operacia == "pouzi predmet") or (operacia == "pouzi") or (operacia == "predmet")):
        #presunute z hraca - velmi sa mi to tu nepaci, ale OK
        if (len(hrac.inventar)==0):
            print("Nemas so sebou ziadne predmety.")
        else:
            tempText=hrac.func_vypis_inventar()
            print(tempText)
            print("")
            idx = int(input("Napis cislo predmetu, ktory chces pouzit): "))
            print("")
            hrac.func_pouzi_predmet(idx)
    elif operacia == "vypis":
        print(hrac.func_vypis_inventar())
    elif operacia == "utek":
        #vyskakujem z while
        hrac_chce_bojovat=0
    else:
        print("Neznama operacia")

    print (hrac)

# #def zaciatokHry():
#     #while (mojHrac.func_je_ziva()):
#         operacia = input("Zadaj operaciu (moznost1, moznost2, ): ")

#         if operacia == "koniec":
#             break
#         elif operacia == "moznost1":
#             func_operacia_moznost1(var1, var2)
#         elif operacia == "moznost2":
#             func_operacia_moznost2(varA, varB)
#         else:
#             print("Neznama operacia")

# if __name__ == "__main__":
#     #tuto volam zaciatok hry
#     zaciatokHry()