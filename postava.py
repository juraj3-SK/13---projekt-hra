#toto je hlavna trieda, co sa bude dedit
import random

class postava:
    def __init__(self, id, nazov, zivoty, utok):
        self.id=id
        self.nazov=nazov
        self.zivoty=zivoty
        self.utok=utok

    def func_zautoc(self, ciel):
        #generuj poskodenie
        poskodenie=self.utok+random.randint(1,6)
        print(f"Utok hraca {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")
        ciel.func_zranenie(poskodenie)
        
    def func_zranenie(self, damage):
        self.zivoty-=damage
        if (self.zivoty<0):
            self.zivoty=0
        if (self.func_je_ziva):
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