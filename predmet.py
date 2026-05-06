#toto je hlavna trieda, co sa bude dedit
import random

class predmet:
    def __init__(self, nazov, typ, hodnota):
        self.nazov=nazov
        self.typ=typ
        self.hodnota=hodnota

    def __str__(self):
        return f"Tento predmet sa vola: {self.nazov}, je typu: {self.typ} a jeho hodnota je: {self.hodnota}."
    
    #getters
    #vrat nazov
    def get_nazov(self):
        return(self.nazov)
    #vrat typ
    def get_typ(self):
        return(self.typ)
        #vrat hodnotu
    def get_hodnota(self):
        return(self.hodnota)