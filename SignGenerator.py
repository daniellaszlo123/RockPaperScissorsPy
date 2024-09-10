import random
from Signs import Sign


class SignGenerator:
    def __init__(self):
        self.signs = [Sign.ROCK, Sign.PAPER, Sign.SCISSOR]

    def create(self):
        return self.signs[random.randint(0, len(self.signs) - 1)]
