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
mec=predmet(nazov="mec", typ="zbran", hodnota=10, konzumovatelny=0)
lektvar=predmet(nazov="jahodovy lektvar", typ="lektvar", hodnota=5, konzumovatelny=1)

vybava=[]
vybava.append(mec)
vybava.append(lektvar)

from hrac import hrac
#pisat takto s menami premennych
hrac=hrac(id=5, nazov="hrac_jozko", max_zivoty=10, utok=10, mana=30, level=1, xp=10, inventar=vybava, zlato=10)
#nie takto:
#hrac=hrac(5, "hrac_jozko", 10, 10, 30, 1, 10, "mec", 10)

print (hrac)

def func_subojove_kolo(utocnik1, utocnik2):
    #zacina utocnik1
    utocnik1.func_zautoc(utocnik2)
    #ak je utocnik 2 mrtvy
    if (not utocnik2.func_je_ziva()):
        #tak idem skontrolovat, ci utocnik2 je hrac
        #ak ano, tak koncim hru, inak davam odmenu
        if (type(utocnik2)=="class 'hrac.hrac'"):
            print("Prisiel si o vsetky zivoty")
        else:
            print ("Podarilo sa Ti zabit nepriatela, dostanes odmenu.")
            utocnik1.func_pridaj_odmenu(utocnik2)
            #TODO: tu vygenerujem nahodny predmet
    #ak je utocnik2 zivy, tak utoci
    else:
        utocnik2.func_zautoc(utocnik1)
        if (not utocnik1.func_je_ziva()):
            #tak idem skontrolovat, ci utocnik1 je hrac
            #ak ano, tak koncim hru, inak davam odmenu
            if (type(utocnik1)=="class 'hrac.hrac'"):
                print("Prisiel si o vsetky zivoty")
            #else:
            if (type(utocnik1)=="class 'nepriatelia.goblin.goblin'"):
                print ("Podarilo sa Ti zabit nepriatela, dostanes odmenu.")
                utocnik2.func_pridaj_odmenu(utocnik1)
                #TODO: tu vygenerujem nahodny predmet

hrac_chce_bojovat=1
while (hrac.func_je_ziva() and nepriatel_goblin.func_je_ziva() and (hrac_chce_bojovat==1)):
    operacia = input("Zadaj operaciu (utok, liecenie, pouzi predmet, vypis, utek): ")
    if operacia == "utok":
        func_subojove_kolo(hrac, nepriatel_goblin)
    elif operacia == "liecenie":
        hrac.func_liecenie()
    elif operacia == "pouzi predmet":
        #func_pouzi_predmet(varB)
        pass
    elif operacia == "vypis":
        print(hrac.func_vypis_inventar())
    elif operacia == "utek":
        #vyskakujem z while
        hrac_chce_bojovat=0
        #otestovat neskor ci mozem tu dummy variable nahradit dalsim riadkom?
        # Alebo to uz vyskocim z dvoch while-ov naraz?
        #break
    else:
        print("Neznama operacia")


# Pravidlá:
# ● Hráč útočí za:
# ● Ak hráč vyhrá:
# ○ môže dostať predmet,
# ● Ak prehrá:
# ○ hra vypíše koniec,
# ○ hráč sa už nemôže ďalej hrať, alebo sa načíta posledný save.























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