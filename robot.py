from weapon import Weapon


class Robot:

    def __init__(self):
        self.name = "hi my name is Bob"
        self. health = 200
        self.weapon = Weapon(input("Would you like to use a gun, knife, or bazooka? "))
