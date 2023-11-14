"""

class Car:
    pass

    def __init__(self, register_number, max_speed, current_speed = 0, travelled_distance = 0):
        self.register_number = register_number
        self.max_speed = max_speed

    def accelerate(self, speed_change):
        if speed_change > 0:
            self.current_speed = max(self.current_speed + speed_change)
        else:
            self.current_speed = min(self.current_speed + speed_change)

new_car = Car ("ABC-123 ", 142)
print(f"Tää autoon rekisterinumero on: {new_car.register_number} \nHuippunopeus on: {new_car.max_speed} km/h.")
"""
import random

class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(self.current_speed + speed_change)
        else:
            self.current_speed = min(self.max_speed, self.current_speed + speed_change)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def main():
    car = Car("ABC-123", 142)
    print("Registration number:", car.reg_num)
    print("Maximum speed:", car.max_speed, "km/h")
    print("Current speed:", car.current_speed, "km/h")
    print("Travelled distance:", car.travelled_distance, "km")

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Current speed:", car.current_speed, "km/h")

    car.accelerate(-200)
    print("Final speed:", car.current_speed, "km/h")

    cars = []
    for i in range(1, 11):
        reg_num = "ABC-" + str(i)
        max_speed = random.randint(100, 200)
        car = Car(reg_num, max_speed)
        cars.append(car)

    hours = 0
    while True:
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                print("Car", car.reg_num, "has won the race!")
                print("Registration number:", car.reg_num)
                print("Maximum speed:", car.max_speed, "km/h")
                print("Current speed:", car.current_speed, "km/h")
                print("Travelled distance:", car.travelled_distance, "km")
                return
        hours += 1
if __name__ == "__main__":
    main()