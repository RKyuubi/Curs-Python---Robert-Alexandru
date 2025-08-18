import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def aria(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    c1 = Circle(1)
    c2 = Circle(5)

    print (c1.aria(), c1.circumference())
    print (c2.aria(), c2.circumference())