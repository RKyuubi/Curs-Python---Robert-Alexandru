class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.brand, self.model, self.year)

if __name__ == "__main__":
    masina_1 = Car("Volkswagen", "Golf", "2020")
    masina_1.display_info()
