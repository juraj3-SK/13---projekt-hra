import random

from nepriatelia.drak import class_Drak
nepriatel_drak=class_Drak(1)

from nepriatelia.goblin import class_Goblin
nepriatel_goblin=class_Goblin(2)

from nepriatelia.kostlivec import class_Kostlivec
nepriatel_kostlivec=class_Kostlivec(3)

from nepriatelia.ork import class_Ork
nepriatel_ork=class_Ork(4)

from predmet import class_Predmet

#zadefinuj slovnik
#key bude nazov, value bude predmet
zoznam_predmetov = {
  "maly_lektvar": class_Predmet(nazov="Maly lektvar", typ="heal", hodnota=2, konzumovatelny=1),
  "velky_lektvar": class_Predmet(nazov="Velky lektvar", typ="heal", hodnota=50, konzumovatelny=1),
  "mana_elixir": class_Predmet(nazov="Mana elixir", typ="mana", hodnota=20, konzumovatelny=1),
  "mec": class_Predmet(nazov="Mec", typ="zbran", hodnota=10, konzumovatelny=0)
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

from hrac import class_Hrac

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


def func_subojove_kolo(hrac, nepriatel):
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

def func_spustena_hra(hrac):
    operacia2 = input("Zadaj operaciu (1 - info, 2 - vypis inventar, 3 - liecenie za manu, 4 - pouzi predmet, 5 - bojovat, , 6 - obchod, 7 - ulozit hru, 0 - koniec): ")
    operacia2 = int(operacia2)
    
    if (operacia2 == 1):
        print (hrac)
    elif (operacia2 == 2):
        print(hrac.func_vypis_inventar())
    elif (operacia2 == 3):
        #ak sa lieci mimo boja, ziadny nepriatel neutoci
        hrac.func_liecenie()
    
    elif (operacia2 == 4):
        print("")
        if (len(hrac.inventar)==0):
            print("Nemas so sebou ziadne predmety.")
        else:
            tempText=hrac.func_vypis_inventar()
            print(tempText)
            print("")
            idx = int(input("Napis cislo predmetu, ktory chces pouzit): "))
            print("")
            hrac.func_pouzi_predmet(idx)
    elif (operacia2 == 5):
        hrac_chce_bojovat=1
        while (hrac.func_je_ziva() and nepriatel_goblin.func_je_ziva() and (hrac_chce_bojovat==1)):
            operacia3 = input("Zadaj operaciu (1 - info, 2 - vypis inventar, 3 - liecenie za manu, 4 - pouzi predmet, 5 - utok, 6 - utek): ")
            operacia3 = int(operacia3)
            if (operacia3 == 1):
                print (hrac)
        
            elif (operacia3 == 2):
                print(hrac.func_vypis_inventar())
        
            elif (operacia3 == 3):
                #ak sa lieci pocas boja, nepriatel moze zautocit
                hrac.func_liecenie()
           
                #nepriatel necaka a skusi zautocit, davam 50%, ze to stihne
                tempVar=random.randint(1,2)
                if (tempVar==1):
                    print("")
                    print("Kym sa liecis, nepriatel necaka. Prichadza utok!")
                    nepriatel_goblin.func_zautoc(hrac)
                    if (hrac.func_je_ziva()):
                        print("")
                        print ("Prezil si.")
                    else:
                        print("")
                        print ("Nepriatel Ta fatalne zasiahol!")
                else:
                    print("")
                    print ("Nepriatel zakopol o prazdnu flasticku od lektvaru a nestihol zautocit.")
        
            elif (operacia3 == 4):
                if (len(hrac.inventar)==0):
                    print("")
                    print("Nemas so sebou ziadne predmety.")
                else:
                    tempText=hrac.func_vypis_inventar()
                    print(tempText)
                    print("")
                    idx = int(input("Napis cislo predmetu, ktory chces pouzit): "))
                    print("")
                    hrac.func_pouzi_predmet(idx)

                    #nepriatel necaka a skusi zautocit, davam 50%, ze to stihne
                    tempVar=random.randint(1,2)
                    if (tempVar==1):
                        print("Kym sa babres s vybavou, nepriatel necaka. Prichadza utok!")
                        nepriatel_goblin.func_zautoc(hrac)
                        if (hrac.func_je_ziva()):
                            print ("Nastastie si prezil.")
                        else:
                            print ("Kym si hladal vybavu, nepriatel Ta fatalne zasiahol!")
                    else:
                        print ("Nepriatel sa posmykol na supke z jablka a nestihol zautocit.")
        
            elif (operacia3 == 5):
                prebieha_utok=1
                func_subojove_kolo(hrac, nepriatel_goblin)
 
            elif (operacia3 == 6):
                hrac_chce_bojovat=0
                print("Snazis sa nepriatelovi utiect. Mozno na Teba vsak este stihne zautocit...")
                #ale pred vyskocenim z while este davam 50% sancu nepriatelovi na utok
                tempVar=random.randint(1,2)
                if (tempVar==1):
                    nepriatel_goblin.func_zautoc(hrac)
                    if (hrac.func_je_ziva()):
                        print ("Nepriatel na Teba zautocil, ale podarilo sa Ti utiect.")
                    else:
                        print ("Nepodarilo sa Ti utiect. Nepriatel Ta stihol este zasiahnut pri uteku.")
                else:
                    print ("Nepriatel sa posmykol a nestihol zautocit. Podarilo sa Ti utiect.")
            
            else:
                print("Neznama operacia3")
        
            print (hrac)

    elif (operacia2 == 6):
        #tu raz bude samoosbluha
        pass        
    elif (operacia2 == 7):
        #tu raz bude ukladanie do DB
        pass
    elif (operacia2 == 0):
        #mam sem nieco dat?
        pass
    else:
        print("Neznama operacia2")
    

#tu zacina hra
koniec=0
while (koniec==0):
    operacia1 = input("Zadaj operaciu: 1 - nova hra, 2 - nacitaj hru, 3 - zoznam ulozenych hracov, 4 - koniec): ")
    operacia1 = int(operacia1)
    if (operacia1 == 1):
        print("Vytvaram noveho hraca.")
        print("toto este ide1")
    
        #pisat takto s menami premennych
        #vygenerovanyHrac=hrac(id=5, nazov="hrac_jozko", max_zivoty=20, utok=10, iniciativa=10, mana=30, level=1, xp=10, inventar=vybava, zlato=10)
        hrac=class_Hrac(id=5, nazov="hrac_jozko", max_zivoty=20, utok=10, iniciativa=10, mana=30, level=1, xp=10, inventar=vybava, zlato=10)
        print("toto este ide2")
        #nie takto:
        #hrac=hrac(5, "hrac_jozko", 10, 10, 30, 1, 10, "mec", 10)
        #print (vygenerovanyHrac)
        print (hrac)
        #func_spustena_hra(vygenerovanyHrac)
        func_spustena_hra(hrac)

    elif (operacia1 == 2):
        #tu sa bude citat databaza
        pass
    elif (operacia1 == 3):
        #tu sa nacita zoznam hracov z databazy
        pass
    elif (operacia1 == 4):
        koniec=1
        print ("Koniec hry.")
    else:
        print ("Neznama operacia")