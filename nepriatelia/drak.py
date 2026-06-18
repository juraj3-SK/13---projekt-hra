from nepriatel import class_Nepriatel

class class_Drak(class_Nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="drak", max_zivoty=50, utok=10, iniciativa=5, xp_odmena=30, zlato_odmena=30)