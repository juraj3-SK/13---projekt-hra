from postava import postava

import random

class nepriatel(postava):
    #nie je mi celkom jasne, ci robit novu funkciu "vytvor nahodneho", alebo len upravujem "init" - urobil som novy init
    def __init__(self, zlato_odmena):
        self.zlato_odmena=zlato_odmena
        
        #goblin=1, ork=2, kostlivec=3, drak=4
        temp=random.randint(1,4)
        if (temp==1):
            self.nazov="goblin"
            self.zivoty=20
            self.utok=5
            self.xp=10
        elif (temp==2):
            self.nazov="ork"
            self.zivoty=30
            self.utok=7
            self.xp=15
        elif (temp==3):
            self.nazov="kostlivec"
            self.zivoty=25
            self.utok=6
            self.xp=12
        #elif (temp==4):
        else:
            self.nazov="drak"
            self.zivoty=50
            self.utok=10
            self.xp=30

    def func_zautoc(self, ciel):
        #generuj poskodenie
        poskodenie=self.utok+random.randint(3,8)
        print(f"Utok nepriatela {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")
        ciel.func_zranenie(poskodenie)