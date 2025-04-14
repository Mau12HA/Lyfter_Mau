"""
4. Cree las siguientes clases:
    1. `Head`
    2. `Torso`
    3. `Arm`
    4. `Hand`
    5. `Leg`
    6. `Feet`
    7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.
"""

class Head:
    def __init__(self):
        self.eyes =2
        self.nose = 1
        self.mouth = 1
        

class Torso:
    def __init__(self):
        self.head = Head()
        self.right_arm = Arm()
        self.left_arm = Arm()
        self.right_leg = Leg()
        self.left_leg = Leg()

class Arm:
	def __init__(self):
		self.hand = Hand()
		self.fingers = 5
		
class Hand:
	def __init__(self):
		self.fingers = 5
		
class Leg:
	def __init__(self):
		self.feet = Feet()
		self.toes = 5
		

class Feet:
	def __init__(self):
		self.toes = 5

class Human:
    def __init__(self):
        self.torso = Torso()
        
human = Human()