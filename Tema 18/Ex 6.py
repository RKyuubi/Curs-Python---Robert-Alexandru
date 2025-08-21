class Vehicles:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def informatii_vehicul(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

class Car(Vehicles):
    def __init__(self, brand, year, seats):
        super().__init__(brand, year)
        self.seats = seats

    def informatii_vehicul(self):
        super().informatii_vehicul()
        print(f"Seats: {self.seats}")

class ElectricCar(Car):
    def __init__(self, brand, year, seats, battery_capacity):
        super().__init__(brand, year, seats)
        self.battery_capacity = battery_capacity

    def autonomie(self):
        range_in_km = self.battery_capacity * 5
        return range_in_km

    def informatii_vehicul(self):
        super().informatii_vehicul()
        print(f"Battery capacity: {self.battery_capacity} kWh")
        car_range = self.autonomie()
        print(f"Autonomia vehicului electric este de: {car_range} km")

if __name__ == "__main__":

    masina_electrica = ElectricCar("Tesla", 2025, 5, 100)

    print ("---Detalii masina electrica (sau frigider ca e tot aia)---")
    masina_electrica.informatii_vehicul()