class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")


if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

    print("Magazine Information:")
    donald_duck.print_information()
    print("\nBook Information:")
    compartment_no_6.print_information()


# Ex 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometers_driven = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.kilometers_driven += distance

    def set_speed(self, speed):
        if speed <= self.max_speed:
            self.current_speed = speed
        else:
            self.current_speed = self.max_speed


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume

if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)  # Registration number, max speed, battery capacity
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)  # Registration number, max speed, tank volume
    electric_car.set_speed(150)
    gasoline_car.set_speed(120)
    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric Car ({electric_car.registration_number}) - Kilometers Driven: {electric_car.kilometers_driven} km")
    print(f"Gasoline Car ({gasoline_car.registration_number}) - Kilometers Driven: {gasoline_car.kilometers_driven} km")
