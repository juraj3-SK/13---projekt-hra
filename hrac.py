from postava import postava
import random


#toto nam hovori, ze class hrac dedi funkcie aj premenne od postavy
class hrac(postava):

    def __init__(self, id, nazov, max_zivoty, utok, mana, level=1, xp=0, inventar=[], zlato=0):
        #toto len ako reminder
        #funkcia super bere (init) od parenta
        super().__init__(id, nazov, max_zivoty, utok)

        self.mana=mana
        self.level=level
        self.xp=xp
        self.inventar=inventar
        self.zlato=zlato

    def func_liecenie(self):
        if (self.zivoty<self.max_zivoty):
            if (self.mana>=10):
                self.mana-=10
                liecenie=4+random.randint(1,6)
                if (liecenie>self.max_zivoty-self.zivoty):
                    liecenie=self.max_zivoty-self.zivoty
                self.zivoty+=liecenie
                print(f"Pridal si si zivoty: {liecenie}, Tvoj pocet zivotov je {self.zivoty} a mnozstvo many, ktora Ti zostala je: {self.mana}.")
                print("")
            else:
                print("Nemas dost many na liecenie")
                print("")
        else:
            print("Uz mas maximalny pocet zivotov. Nemozes plytvat manou len-tak.")
            print("")

    def func_pridaj_odmenu(self, nepriatel):
        self.zlato+=nepriatel.zlato_odmena
        self.xp+=nepriatel.xp_odmena
        if (self.xp>=20*self.level):
            self.xp-=20*self.level
            self.level+=1
            self.max_zivoty+=10
            self.zivoty+=10
            self.utok+=2
            self.mana+=5    

    #ak dam print hraca, tak sa vola toto
    def __str__(self):
        text=""
        text+=("\n")
        text+=(f"Volas sa {self.nazov}, a.k.a. id={self.id}. Tvoje parametre su:")
        text+=("\n")
        text+=(f"zivoty: {self.zivoty}")
        text+=(f"\nmax. zivoty: {self.max_zivoty}")
        text+=(f"\nutok: {self.utok}")
        text+=(f"\nmana: {self.mana}")
        text+=(f"\nlevel: {self.level}")
        text+=(f"\nxp: {self.xp}")
        text+=(f"\nzlato: {self.zlato}")
        text+=("\n")
        
        # if (len(self.inventar)==0):
        #     text+=("\nNemas so sebou ziadne predmety.")
        # elif(len(self.inventar)==1):
        #     text+=("\nMas so sebou tento predmet:")
        #     text+=(f"\n{self.inventar[0]}")
        # else:
        #     text+=("\nMas so sebou tieto predmety:")
        #     for i in self.inventar:
        #         text+=(f"\n{i}")
        text+=self.func_vypis_inventar()
        return text

    def func_vypis_inventar(self):
        text=""
        if (len(self.inventar)==0):
            text+=("\nNemas so sebou ziadne predmety.")
        elif(len(self.inventar)==1):
            text+=("\nMas so sebou tento predmet:")
            text+=(f"\n{self.inventar[0]}")
        else:
            text+=("\nMas so sebou tieto predmety:")
            counter=0
            for i in self.inventar:
                counter+=1
                text+=(f"\n{counter}. {i}")
        text+=("\n")
        return text

    def func_pridaj_predmet(self, predmet):
        self.inventar.append(predmet)
    
    def func_pouzi_predmet(self, idx):
        #ak je predmet konzumovatelny, tak ho po pouziti zmaz zo zonamu predmetov
        if (self.inventar(idx).konzumovatelny==1):
            self.inventar.remove(idx)