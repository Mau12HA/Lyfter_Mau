"""
2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
    usando una para sus keys, y la otra para sus values.
   
"""

list_a = ['first_name', 'last_name', 'role']
list_b = ['Mauricio', 'Herrera', 'Software Engineer']

my_dictionary = {}

for i in range(len(list_a)):
    my_dictionary[list_a[i]] = list_b[i]

print(my_dictionary)