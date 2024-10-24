import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def main():
    cars = []
    for i in range(10):
        registration_number = f"ABC-{i + 1}"
        max_speed = random.randint(100, 200)
        cars.append(Car(registration_number, max_speed))

    race_in_progress = True
    hours = 0
    while race_in_progress:
        hours += 1
        print(f"\nHour {hours}:")

        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            print(
                f"{car.registration_number} | Speed: {car.current_speed} km/h | Distance: {car.travelled_distance} km")

        for car in cars:
            if car.travelled_distance >= 10000:
                race_in_progress = False
                break

    print("\nRace over! Final standings:")
    print(f"{'Car':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<20} {'Distance Travelled (km)':<20}")
    for car in cars:
        print(f"{car.registration_number:<10} {car.max_speed:<15} {car.current_speed:<20} {car.travelled_distance:<20}")


if __name__ == "__main__":
    main()
