from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon


class Battlefield:

    def __init__ (self):
        self.dinosaur = Dinosaur("T-Rex", 50)
        self.gun = Weapon("gun")
        self.robot = Robot()

    def attack_robot(self):
        print(self.robot.health)
        self.robot.health -= self.dinosaur.attack_power
        print(self.robot.health)
