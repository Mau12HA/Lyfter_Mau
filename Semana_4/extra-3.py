"""
3. Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.

"""

number = int(input("Ingrese un número : "))
result_suma = 0
contador = 1
for contador in range(1, number+1):
    print(contador)
    result_suma = result_suma + contador

print(f'[ {result_suma} ] es resultado de la suma de los {number} números')