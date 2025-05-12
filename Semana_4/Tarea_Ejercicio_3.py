"""
3. Cree un programa con un numero secreto del 1 al 10. 
    El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""
import random


secret_num = int(random.randint(1,10))
num = int(input("Adivina el Número : "))
print(secret_num)

while (num != secret_num):
    
    num = int(input("Inténtalo de nuevo : "))

    if (num<11 and num>0 ):
        if(num == secret_num):
            print(f'Felicidades, adivinaste es el # {secret_num}')          
        
    else:
        print('Ingrese un numero entre 1 y 10 : ') 



