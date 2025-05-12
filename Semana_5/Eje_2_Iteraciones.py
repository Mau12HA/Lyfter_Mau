"""
2.Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
"""


my_string = 'Pizza con Piña'

#for char in my_string:
#    print (char)

for char in range(len(my_string)-1,-1,-1):
    
    print(my_string[char])    
