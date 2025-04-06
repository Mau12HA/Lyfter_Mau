"""
1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área.
"""

class Circle:

    radius = 0

    def get_area(self,radius):

        circle_area = 3.14 * radius ** 2
        print(f"El área del círculo es: {circle_area}")
        

my_cirle = Circle()
my_cirle.get_area(8)
