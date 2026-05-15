from postava import postava

import random

class nepriatel(postava):
    def __init__(self, id, nazov, max_zivoty, utok, iniciativa, zlato_odmena, xp_odmena):
        super().__init__(id, nazov, max_zivoty, utok, iniciativa)
        self.zlato_odmena=zlato_odmena
        self.xp_odmena=xp_odmena

    def func_zautoc(self, ciel):
        #ak by som potreboval volat funkciu rodica, tak to dam sem
        #super().func_zautoc(ciel)
        
        #generuj poskodenie
        poskodenie=self.utok+random.randint(3,8)

        # Kritický zásah má 10 % šancu a dáva dvojnásobné poškodenie.
        tempVar=random.randint(1,10)
        print(f"vygenerovana pravdepodobnost sa rovna: {tempVar}")
        if (tempVar==1):
            print("Nasleduje kriticky zasah.")
            poskodenie=2*poskodenie

        #vypis info a zautoc
        print(f"Utok nepriatela {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")
        ciel.func_zranenie(poskodenie)

    def func_zranenie(self, damage):
        self.zivoty-=damage
        if (self.zivoty<0):
            self.zivoty=0
        if (self.func_je_ziva()):
            print(f"Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print(f"Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zabity.")