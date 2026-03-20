class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


car = Car("ABC-123", 142)

print(car.registration_number)
print(car.max_speed)
print(car.current_speed)
print(car.travelled_distance)