"""
4.Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

print("Ingresar 3 números enteros")

num1 = int(input("1° : "))
num2 = int(input("2° : "))
num3 = int(input("3° : "))

mayor = num1

if (num2 > mayor):
    mayor= num2

if(num3 > mayor):
    mayor = num3

print(f'El Número MAYOR es : {mayor}')