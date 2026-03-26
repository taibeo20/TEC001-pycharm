import random

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def drive(self, hours):
        self.distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.current_speed += change

            if car.current_speed < 0:
                car.current_speed = 0
            if car.current_speed > car.max_speed:
                car.current_speed = car.max_speed

            car.drive(1)

    def print_status(self):
        print("\n===== RACE STATUS =====")
        print(f"{'Car':<10}{'Speed':<10}{'Distance':<10}")
        for car in self.cars:
            print(f"{car.name:<10}{car.current_speed:<10}{car.distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(100, 200)
        cars.append(Car(f"Car{i}", max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)
    hour = 0

    while not race.race_finished():
        hour += 1
        race.hour_passes()

        if hour % 10 == 0:
            print(f"\n--- Hour {hour} ---")
            race.print_status()

    print("\n RACE FINISHED!")
    race.print_status()