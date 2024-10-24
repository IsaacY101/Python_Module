# Phase 1
class Elevator:
    def __init__(self, bottom, top):
        self.current = bottom
        self.bottom = bottom
        self.top = top

    def floor_up(self):
        if self.current < self.top:
            print(f"Elevator is moving from {self.current} to {self.current + 1}")
            self.current += 1
            return True
        else:
            print("Elevator is already at the top floor.")
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            print("Elevator is already at the bottom floor.")
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for _ in range(floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for _ in range(self.current - floor):
                if not self.floor_down():
                    break
        else:
            print(f"Elevator is already at the required floor ({self.current})")

# Main program
def main():
    eleva = Elevator(1, 10)

    print("\nMoving to the 5th floor:")
    eleva.go_to_floor(5)

    print("\nReturning to the bottom floor:")
    eleva.go_to_floor(1)

if __name__ == "__main__":
    main()

# Phase 2
class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number + 1} to floor {destination_floor}:")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number + 1} does not exist in this building.")

    def fire_alarm(self):
        print("Fire alarm is ringing!")
        for e in self.elevators:
            e.go_to_floor(e.bottom)

def main():
    building = Building(1, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.run_elevator(1, 1)

if __name__ == "__main__":
    main()

#Ex 4
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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<20} {'Distance Travelled (km)':<20}")
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.max_speed:<15} {car.current_speed:<20} {car.travelled_distance:<20}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

def main():
    cars = []
    for i in range(10):
        registration_number = f"ABC-{i+1}"
        max_speed = random.randint(100, 200)
        cars.append(Car(registration_number, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        # Print status every 10 hours
        if hours % 10 == 0:
            print(f"\n--- Hour {hours} ---")
            race.print_status()

    # Print final status
    print("\nRace finished!")
    race.print_status()

if __name__ == "__main__":
    main()


