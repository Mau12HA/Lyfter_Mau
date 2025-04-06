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
        self.head = 1
        self.right_arm = 1
        self.left_arm = 1
        self.right_leg = 1
        self.left_leg = 1
        

class Arm:
	def __init__(self):
		self.right_arm = 1
		self.left_arm = 1
		
      
class Hand:
	def __init__(self):
		self.fingers = 5
		self.right_hand = 1
		self.left_hand = 1
		
	
class Leg:
	def __init__(self):
		self.right_leg = 1
		self.left_leg = 1
		

class Feet:
	def __init__(self):
		self.toes = 5
		self.right_feet = 1
		self.left_feet = 1
	
class Human:
    def __init__(self):
            self.head = Head()
            self.torso = Torso()
            self.right_arm = Arm()
            self.left_arm = Arm()
            self.right_hand = Hand()
            self.left_hand = Hand()
            self.right_leg = Leg()
            self.left_leg = Leg()
            self.right_feet = Feet()
            self.left_feet = Feet()
        

human = Human()