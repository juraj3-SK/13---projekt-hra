#toto je hlavna trieda, co sa bude dedit
import random

class postava:
    def __init__(self, id, nazov, max_zivoty, utok):
        self.id=id
        self.nazov=nazov
        self.max_zivoty=max_zivoty
        self.utok=utok

        self.zivoty=self.max_zivoty

    def func_zautoc(self, ciel):
        #generuj poskodenie
        poskodenie=self.utok+random.randint(1,6)
        # Kritický zásah má 10 % šancu a dáva dvojnásobné poškodenie.
        tempVar=random.randint(1,10)
        print(f"vygenerovana pravdepodobnost sa rovna: {tempVar}")
        if (tempVar==1):
            print("Nasleduje kriticky zasah.")
            poskodenie=2*poskodenie
        print(type(self))
        if (type(self)=="class 'hrac.hrac'"):
            print(f"Utok hraca {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")
        else:
            print(f"Utok nepriatela {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")

        ciel.func_zranenie(poskodenie)

    def func_zranenie(self, damage):
        self.zivoty-=damage
        if (self.zivoty<0):
            self.zivoty=0
        if (self.func_je_ziva()):
            print(f"{self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print(f"{self.nazov}, a.k.a. id={self.id}, bol zabity.")
    
    def func_je_ziva(self):
        #nemusim robit if zivoty>0, rovno to skontroluje v returne
        return(self.zivoty>0)
    
    #getters
    #vrat autora
    def get_nazov(self):
        return(self.nazov)
    #vrat nazov
    def get_zivoty(self):
        return(self.zivoty)
    #vrat rok
    def get_utok(self):
        return(self.utok)
        #vrat id
    def get_id(self):
        return(self.id)