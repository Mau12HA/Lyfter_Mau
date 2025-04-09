"""
1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área.
"""


import math


class Circle:

    def __init__(self):
        self.radius = 0

    def get_area(self):

        circle_area = math.pi * self.radius ** 2
        print(f"El área del círculo es: {circle_area}")
        

my_cirle = Circle()
my_cirle.get_area()
