"""
1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

"""

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

counter = 0

while counter<len(first_list):
    print(first_list[counter], second_list[counter])
    counter += 1

#first_list.extend(second_list)
#print(first_list)s

#for index in range(0, len(first_list)):
#	record = first_list[index]
	#print(f'{index}: {record}')
    