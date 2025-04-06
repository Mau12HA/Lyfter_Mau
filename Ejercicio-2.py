"""
2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). 
    **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    3. Un método para bajar pasajeros uno por uno (en cualquier orden).
"""

class Person:
    
    def __init__(self, name):
        self.name = name


class Bus:

    def __init__(self,max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f'{person.name} ha subido al bus')
        else:
            print("El bus está lleno, no se puede agregar más pasajeros")


    def remove_passenger(self,person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} ha bajado del bus.")
        else:
            print(f"{person.name} no está en el bus.")


    def list_passengers(self):
        if self.passengers:
            print("Pasajeros actuales en el bus:")
            for passenger in self.passengers:
                print(f"- {passenger.name}")
        else:
            print("El bus está vacío.")

bus = Bus(max_passengers = 3)
person1 = Person("Juan")
person2 = Person("Ana")
person3 = Person("Luis")
person4 = Person("Carlos")


bus.add_passenger(person1) 
bus.add_passenger(person2)  
bus.add_passenger(person3)  
bus.add_passenger(person4)  

bus.list_passengers()

bus.remove_passenger(person2) 

bus.list_passengers()

bus.add_passenger(person4)
bus.list_passengers()