class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def car_details(self):
        super().display_info()
        print(f"Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, year, speeds):
        super().__init__(brand, year)
        self.speeds = speeds

    def bike_details(self):
        super().display_info()
        print(f"Speeds: {self.speeds}")

if __name__ == "__main__":
    car = Car("Peugeot", 2005, 4)
    car.car_details()

    bike = Bike("Semicursiera", 2020, 8)
    bike.bike_details()

