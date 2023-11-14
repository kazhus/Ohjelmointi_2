class Parrot:
    def sing (self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now danced".format(self.name)
class Penguin:
    def run(self):
        return "{} is no".format(self.name)








"""class Car:
    color = "Beige"

    def __init__(self,color, module):
        self.color = color
        self.module = module
    def greeting(self):
        print("Say Hello ")
    def car_color(self, color):
        self.color = color
        print(self.color)

Car1 = Car("Red", "2002")
Car2 = Car("Blue", "2023")

Car1.greeting()
print(f"your car color is:", Car1.color, "and the module is:", Car1.module)
print(f"your car color is:", Car2.color, "and the module is:", Car2.module)
"""
