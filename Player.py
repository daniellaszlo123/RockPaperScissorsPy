from SignGenerator import SignGenerator


class Player:
    def __init__(self, name):
        self.sign = None
        self.name = name
        self.generator = SignGenerator()

    def getSign(self):
        return self.sign

    def createSign(self):
        self.sign = self.generator.create()
