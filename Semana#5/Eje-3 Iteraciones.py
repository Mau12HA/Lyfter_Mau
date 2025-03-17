"""
3.Cree un programa que intercambie el primer y ultimo elemento de una lista. 
    Debe funcionar con listas de cualquier tamaño
"""
list_size = int(input("Ingresar el tamaño de la lista : "))
my_list = []

for i in range(list_size):
    my_list.append(int((input("Ingrese un elemento a la lista : "))))

print(f'Lista : ',my_list)
fisrt_element = my_list[0]
final_element = my_list[-1]

my_list[-1] = fisrt_element
my_list [0] = final_element

print(f'La nueva lista es : ', my_list)