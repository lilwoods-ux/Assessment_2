import math


class Shape:

        def area(self):
            return self.area()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius ):
        self.radius = radius

    def area(self):
         return math.pi * (self.radius ** 2)

Rectangle = Rectangle(5, 6)
Circle = Circle(14)
print(Rectangle.area())
print(Circle.area())
