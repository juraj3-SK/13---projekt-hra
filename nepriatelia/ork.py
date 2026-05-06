from nepriatel import nepriatel

class ork(nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="ork", zivoty=30, utok=7, xp_odmena=15, zlato_odmena=15)