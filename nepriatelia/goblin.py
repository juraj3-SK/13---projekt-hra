from nepriatel import class_Nepriatel

class class_Goblin(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="goblin", max_zivoty=20, utok=5, iniciativa=5, xp_odmena=10, zlato_odmena=10)
    
    def func_zranenie(self,hodnota_zranenia):
        super().func_zranenie(hodnota_zranenia)
        if (self.func_je_ziva()):
            print("")
            print(f"👺 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print("")
            print(f"👺 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zabity.")