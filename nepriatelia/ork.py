from nepriatel import class_Nepriatel

class class_Ork(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="ork", max_zivoty=30, utok=7, iniciativa=10, xp_odmena=15, zlato_odmena=15)