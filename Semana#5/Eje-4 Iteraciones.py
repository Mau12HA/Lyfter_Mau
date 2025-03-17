"""
4.Cree un programa que elimine todos los números impares de una lista.
"""

list_size = int(input("Ingresar el tamaño de la lista : "))
my_list = []
new_list = []

for i in range(list_size):
    my_list.append(int((input("Ingrese un número a la lista : "))))

print(f'Lista : ',my_list)

for number in my_list:
    if number%2==0:
        new_list.append(number)

print(new_list)