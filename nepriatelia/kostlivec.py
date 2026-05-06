from nepriatel import nepriatel

class kostlivec(nepriatel):
    def __init__(self, id):
        super().__init__(id, nazov="kostlivec", zivoty=25, utok=6, xp_odmena=12, zlato_odmena=12)
    