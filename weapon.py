class Weapon:

    def __init__(self, name_passed):
        self.name = name_passed
        self.weapons = ["gun", "knife", "bazooka"]
        self.attack_power = 0
        if name_passed == "gun":
            self.attack_power = 20
        elif name_passed == "knife":
            self.attack_power = 5
        elif name_passed == "bazooka":
            self.attack_power = 50