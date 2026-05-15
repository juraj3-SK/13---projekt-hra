from nepriatel import nepriatel

class goblin(nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="goblin", max_zivoty=20, utok=5, iniciativa=5, xp_odmena=10, zlato_odmena=10)