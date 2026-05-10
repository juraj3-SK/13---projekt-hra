from postava import postava

import random

class nepriatel(postava):
    def __init__(self, id, nazov, zivoty, utok, zlato_odmena, xp_odmena):
        super().__init__(id, nazov, zivoty, utok)
        self.zlato_odmena=zlato_odmena
        self.xp_odmena=xp_odmena

    # def func_zautoc(self, ciel):
    #     #generuj poskodenie
    #     poskodenie=self.utok+random.randint(3,8)
    #     print(f"Utok nepriatela {self.nazov}, a.k.a. id={self.id}, je {poskodenie}.")
    #     ciel.func_zranenie(poskodenie)
    #