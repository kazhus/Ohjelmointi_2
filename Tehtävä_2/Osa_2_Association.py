class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor


    def go_to_floor(self, floor):
        if floor > self.current_floor:
            self.floor_up(floor)
        elif floor < self.current_floor:
            self.floor_down(floor)
    def floor_up (self, floor):
        while self.current_floor < floor:
            self.current_floor += 1
            print(f"Hissi on: {self.current_floor} kerros")

    def floor_down (self, floor):
        while self.current_floor > floor :
            self.current_floor -= 1
            print(f"Hissi on: {self.current_floor} kerros")

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_number):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range (elevator_number):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevators(self, elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

def main():
    building = Building (1, 10, 2)
    building.run_elevators(0, 5)
    building.run_elevators(0,1)
    building.fire_alarm()
main()


