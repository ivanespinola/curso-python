# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circle_area(self):
        return round(math.pi * (self.radius ** 2) , 2)

circle = Circle(5)
print(circle.circle_area())

# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return round(self.length * self.width , 2)

rectangle = Rectangle(3, 5)
print(rectangle.rectangle_area())

# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area():
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        super().__init__()
        self.lenght = length
    def area(self):
        return round(self.lenght * self.lenght, 2)

nSquare = Square(5)
print(nSquare.area())
print(Square().area())
