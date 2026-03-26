class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Up -> Floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Down -> Floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRun Elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)

if __name__ == "__main__":
    b = Building(1, 10, 3)
    b.run_elevator(0, 5)
    b.run_elevator(1, 8)