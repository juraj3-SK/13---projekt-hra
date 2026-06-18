from nepriatel import class_Nepriatel

class class_Kostlivec(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="kostlivec", max_zivoty=25, utok=6, iniciativa=10, xp_odmena=12, zlato_odmena=12)