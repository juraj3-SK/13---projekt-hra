from nepriatel import class_Nepriatel

class class_Ork(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="ork", max_zivoty=30, utok=7, iniciativa=10, xp_odmena=15, zlato_odmena=15)
    
    def func_zranenie(self,hodnota_zranenia):
        super().func_zranenie(hodnota_zranenia)
        if (self.func_je_ziva()):
            print("")
            print(f"👹 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print("")
            print(f"👹 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zabity.")