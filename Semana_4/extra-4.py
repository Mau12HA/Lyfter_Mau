"""
2. Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
y le pida al usuario adivinar ese número. 
El algoritmo no debe terminar hasta que el usuario adivine el numero.

"""

control = 0
secret_num = 7

while (control == 0):

    num = int(input("Ingresar un número : "))
    if(num == secret_num):    
        print("Adivinaste el Número")
        control = 1
    else:
        print("Intentalo de nuevo")