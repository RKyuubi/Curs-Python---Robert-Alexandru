import math

class Shape:
    def area(self):
        raise(NotImplementedError)

class Rectangle(Shape):
    def __init__(self, latura1, latura2):
        self.name = "Dreptunghi"
        self.latura1 = latura1
        self.latura2 = latura2

    def area(self):
        return self.latura1 * self.latura2

class Circle(Shape):
    def __init__(self, radius):
        self.name = "Cerc"
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, a, h): #a = baza triunghiului (sau una dintre laturi iar h este inaltimea corespunzatoare bazei
        self.name = "Triunghi"
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h * 0.5

if __name__ == "__main__":
    shapes = [Rectangle(5, 7), Circle(3), Triangle(4, 6)]

    aria_totala = 0
    for shape in shapes:
        aria_curenta = shape.area()
        print (f"Aria formei {shape.name}: {aria_curenta:.2f}")
        aria_totala += aria_curenta

    print (f"Aria totala a tuturor formelor geometrice: {aria_totala:.2f}")