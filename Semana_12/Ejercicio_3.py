"""
Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
"""
class Flying:
    def fly(self):
        return "Flying."


class Swimmer:
    def swim(self):
        return "Swimming."


class Duck(Flying, Swimmer):
    def squawk(self):
        return "¡Cuack cuack!"


donald = Duck()
print(donald.fly())    
print(donald.swim())    
print(donald.squawk()) 