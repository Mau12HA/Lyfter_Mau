"""
3. Cree un programa que use una lista para eliminar keys de un diccionario

"""

list_of_keys = ['access_level', 'age']

employee = {
            'name': 'John', 
            'email': 'john@ecorp.com', 
            'access_level': 5, 
            'age': 28

}

print(employee)

for key in list_of_keys:
    key = employee.pop(key)
    
#    for i in range(len(list_of_keys)):
        
#        if (key == i):
#            employee.pop(list_of_keys[i]) 
    
print(employee)