from nepriatel import class_Nepriatel

class class_Drak(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="drak", max_zivoty=50, utok=10, iniciativa=5, xp_odmena=30, zlato_odmena=30)
    
    def func_zranenie(self,hodnota_zranenia):
        super().func_zranenie(hodnota_zranenia)
        if (self.func_je_ziva()):
            print("")
            print(f"🐉 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print("")
            print(f"🐉 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zabity.")