"""
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2. Intente accesar a una variable global desde una función y cambiar su valor.

"""

variable_outside_function_scope = 7

def print_variable():

  variable_inside_function = 67

  print(f'Inside function: {variable_outside_function_scope}')

  #print(variable_inside_function)
  #variable_outside_function_scope = 54


print_variable()
print(f'Outside function: {variable_outside_function_scope}') 


#print(variable_inside_function)