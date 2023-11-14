
""" change_speed = int(input(" How much would you like to accelerate: "))
        if change_speed <= 0:
            print("Move on!")
        elif change_speed <= 30:
            print("You are in gear 1 and your speed is", {change_speed},"km/h")
        elif change_speed <= 50:
            print("You are in gear 2 and your speed is", {change_speed},"km/h")
        elif change_speed >= 70:
            print("You are into maximun speed and your speed is", {change_speed},"km/h")
        else:
            print(f"{self.change_speed} is you current speed! and your speed is", {change_speed},"km/h")
        return
new_car = Car ("ABC-123 ", 142)
print(f" Tä auton rekisteritunnus on: {new_car.register_number}\n Huippunopeus on: {new_car.max_speed}km/h")
new_car.accelerate()
"""
"""class Accelator:
    pass
    def __init__(self, change_speed):
        self.change_speed = change_speed
        change_speed = int(input("What is your current speed km/h: "))
        if change_speed <= 0:
            print("Move on!")
        elif change_speed >= 30:
            print("You are in gear 1")
        elif change_speed >= 50:
            print("You are in gear 2")
        elif change_speed >= 70:
            print("You are into maximun speed")
        else:
            print(f"{self.change_speed} is you current speed!")

"""

"""class Speed:
    gears = 0
    change = input("Auton nopeus on: km/h")
    print(change)
    def __init__(self, gear_1 = 30, gear_2 = 50, gear_3 =70):
        self.gear_1 =gear_1
        self.gear_2 = gear_2
        self.gear_3 = gear_3
        if self.gear_1 <= 30:
            print(" You are in Level 1 by " + {self.gear_1},"km/h.")
        elif self.gear_2 <= 50:
            print("You are in Level 2",{self.gear_2},"km/h.")
        elif self.gear_3 <= 70:
            print("You are in Level 3",{self.gear_3},"km/h.")
        else:
            print("Emergency speed")
"""
