from postava import postava

import random

#toto nam hovori, ze class hrac dedi funkcie aj premenne od postavy
class hrac(postava):

def __init__(self, id, nazov, zivoty, utok):

    def __init__(self, id, nazov, zivoty, utok, mana, level, xp, inventar, zlato):
        
        #toto len ako reminder
        #funkcia super bere (init) od parenta
        super().__init__(id, nazov, zivoty, utok)
        self.mana=mana
        
        #tu by som chcel mat toto: Ak level bol poslany TAK ho nastav, inak 1
        #zatial natvrdo kodujem prvu uroven
        self.level=1
        self.xp=0
        self.inventar=[]
        self.zlato=zlato

    def func_liecenie(self):
        if(self.mana>=10):
            self.mana-=10
            liecenie=4+random.randint(1,6)
            self.zivoty+=liecenie
            print(f"Pridal si si zivoty: {liecenie}. Tvoj pocet zivotov je {self.zivoty}. Mnozstvo many, ktora Ti zostala je: {self.mana}.")
            print("")
        else:
            print("Nemas dost many na liecenie")
    
    def func_vypis_stav(self):
        print(f"Volas sa {self.nazov}, a.k.a. id={self.id}. Tvoje parametre su (zivoty / utok / mana / level / xp / zlato): {self.zivoty}, {self.utok}, {self.mana}, {self.xp}, {self.zlato}.")
        print("")
        if (len(inventar)==0):
            print("Nemas so sebou ziadne predmety.")
        elif(len(inventar)==1):
            print("Mas so sebou tento predmet:")
            print(inventar[0])
        else:
            print("Mas so sebou tieto predmety:")
            for i in inventar:
                print(i)
    
              

            