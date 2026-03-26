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
        print(f"\nGo to floor {target}")
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


if __name__ == "__main__":
    e = Elevator(1, 10)
    e.go_to_floor(5)
    e.go_to_floor(1)