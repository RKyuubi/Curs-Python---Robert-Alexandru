class Animal:
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def make_sound(self):
        print("General Sound")

class Dog(Animal):
    # def __init__(self, name, age, sound):
    #     super().__init__(name, age)
    #     self.sound = sound

    def make_sound(self):
        print("Cainele face ham ham!!")
    # def __str__(self):
    #     return f"Cainele scoate urmatorul sunet: {self.sound}"

class Cat(Animal):
    # def __init__(self, name, age, sound):
    #     super().__init__(name, age)
    #     self.sound = sound

    def make_sound(self):
        print("Pisica face miau miau!!")
    # def __str__(self):
    #     return f"Pisica scoate urmatorul sunet: {self.sound}"

class Cow(Animal):
    # def __init__(self, name, age, sound):
    #     super().__init__(name, age)
    #     self.sound = sound

    def make_sound(self):
        print("Vaca face mooo!!")
    # def __str__(self):
    #     return f"Vaca scoate urmatorul sunet: {self.sound}"

if __name__ == "__main__":
    # lista_animale = ["caine", "pisica", "vaca"]
    # for animal in lista_animale:
    #     if animal == "caine":
    #         animal = Dog(animal, 10, "Ham Ham!")
    #         print(animal)
    #     elif animal == "pisica":
    #         animal = Cat(animal, 10, "Miau miau!")
    #         print(animal)
    #     else:
    #         animal = Cow(animal, 10, "Moooo!")
    #         print(animal)

    lista_animale = [Dog(), Cat(), Cow()]
    for animal in lista_animale:
        animal.make_sound()

