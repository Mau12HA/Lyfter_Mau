"""
2. Cree una clase abstracta de `Shape` que:
    1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
    2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
    3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height
    

if __name__ == "__main__":
    circle = Circle(5)
    print("Circle Perimeter:", circle.calculate_perimeter())
    print("Circle Area:", circle.calculate_area())

    square = Square(4)
    print("Square Perimeter:", square.calculate_perimeter())
    print("Square Area:", square.calculate_area())

    rectangle = Rectangle(4, 6)
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Rectangle Area:", rectangle.calculate_area())
