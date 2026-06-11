#toto je hlavna trieda, co sa bude dedit
import random

class postava:
    def __init__(self, id, nazov, max_zivoty, utok, iniciativa):
        self.id=id
        self.nazov=nazov
        self.max_zivoty=max_zivoty
        self.utok=utok
        self.iniciativa=iniciativa

        self.zivoty=self.max_zivoty

    def func_zautoc(self, ciel):
        #mohol by som mat spolocnu funkciu_zautoc a cez #if (isinstance(self, hrac)) zistit,
        #ci ide o hraca alebo priseru a funkciu napasovat (napr. sila), ale prehladnejsie je
        #urobit len pass a zdedit len "placeholder" (a napasovat funkciu pre kazde dieta)
        pass

    def func_zranenie(self, damage):
        #davam sem pass, rovnaky dovod ako vo funkcii zautoc
        pass
    
    def func_je_ziva(self):
        #nemusim robit if zivoty>0, rovno to skontroluje v returne
        return(self.zivoty>0)
    
    #getters
    #vrat nazov
    def get_nazov(self):
        return(self.nazov)
    #vrat zivoty
    def get_zivoty(self):
        return(self.zivoty)
    #vrat max_zivoty
    def get_max_zivoty(self):
        return(self.max_zivoty)
    #vrat utok
    def get_utok(self):
        return(self.utok)
    #vrat iniciativu
    def get_iniciativa(self):
        return(self.iniciativa)
    #vrat id
    def get_id(self):
        return(self.id)