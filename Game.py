from Player import Player
from Signs import Sign


class Game:
    def __init__(self):

        print("Hello! Do you want to play alone or with a friend? ")
        print("1. Alone")
        print("2. With Friend")
        mode = int(input("Choose a number from above: "))

        while mode != 1 and mode != 2:
            print("Hello! Do you want to play alone or with a friend? ")
            print("1. Alone")
            print("2. With Friend")
            mode = int(input("Choose a number from above: "))

        if mode == 2:
            self.playerF = Player(input("Enter username: "))
            self.playerS = Player(input("Enter username: "))
        else:
            self.playerF = Player(input("Enter username: "))
            self.playerS = Player("Machine")

        self.start()

    def createSigns(self):
        self.playerF.createSign()
        self.playerS.createSign()

    def returnWinner(self):
        if self.playerS.sign == self.playerF.sign:
            return "is tie!"
        return self.checkWinner()

    def checkWinner(self):
        if self.playerF.sign == Sign.ROCK and self.playerS.sign == Sign.SCISSOR \
                or self.playerF.sign == Sign.PAPER and self.playerS.sign == Sign.ROCK \
                or self.playerF.sign == Sign.SCISSOR and self.playerS.sign == Sign.PAPER:
            return "winner is " + self.playerF.name
        return "winner is " + self.playerS.name

    def start(self):
        print("Choose an option below: ")
        print("1. Start a new game")
        print("2. Quit")
        option = int(input("Enter the number: "))

        while option != 1 and option != 2:
            print("Wrong, you can only choose from these options: ")
            print("1. Start a new game")
            print("2. Quit")
            option = int(input("Enter the number: "))

        while option != 2:
            self.createSigns()
            print(f"{self.playerF.name}: {self.playerF.sign.name}")
            print(f"{self.playerS.name}: {self.playerS.sign.name}")
            print(f"The game", self.returnWinner())
            print("Do you want to play again? ")
            print("1. Start a new game")
            print("2. Quit")
            option = int(input("Enter the number: "))
