"""
5.Cree un programa que le pida al usuario 10 números, 
    y al final le muestre todos los números que ingresó, 
    seguido del numero ingresado más alto.

"""

my_list = []
big_numb = 0

for i in range(10):
    my_list.append(int((input("Ingrese un número a la lista : "))))

big_numb = max(my_list)
#for num in my_list:
#    if (big_numb is None or num > big_numb):
#        big_numb = num

print(f'Lista :',my_list,' El más alto fue :', big_numb)