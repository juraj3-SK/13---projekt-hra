from nepriatel import class_Nepriatel

class class_Kostlivec(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="kostlivec", max_zivoty=25, utok=6, iniciativa=10, xp_odmena=12, zlato_odmena=12)
    
    def func_zranenie(self,hodnota_zranenia):
        super().func_zranenie(hodnota_zranenia)
        if (self.func_je_ziva()):
            print("")
            print(f"💀 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zasiahnuty, zostava mu pocet zivotov: {self.zivoty}")
        else:
            print("")
            print(f"💀 Nepriatel {self.nazov}, a.k.a. id={self.id}, bol zabity.")