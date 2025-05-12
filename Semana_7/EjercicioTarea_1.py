"""
1. Cree una calculadora por linea de comando. 
    Esta debe de tener un número actual, y 
    un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado

Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

"""

def sum_add (number1,number2):
    return number1 + number2


def subtraction (number1,number2):
    return number1 - number2


def multiplication (number1,number2):
    return number1 * number2


def division (number1,number2):
    return number1 / number2


def menu_calculator():

    while True:
        try:
            operation = int(input("\nSeleccione la Operación de desea realizar:"
                                "\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Borrar\n \n"))
                               
            if(operation <=5 and operation > 0):
                
                break 
            else:
                print("Opción NO valida, ingrese una opcion valida")
        except ValueError:
            print("Ingrese un número entero para seleccionar una opcion válida \n")

        try:
            keep_going = input("Seguir (s/n): ")
            if keep_going == "n":
                break
        except ValueError:
            print("ERROR!!! Ingresar solamente (s) para Seguir ó (n) para Salir")
    
    return operation

print("\n  CALCULADORA  ")
#op = menu_calculador()
first_value = 0
upshot = 0
try:
    first_value = float(input("\nIngresar primer valor: "))
except ValueError:
    print("Introduce un número valido")


while True:
    
    option_menu = menu_calculator()
    print("Valor actual: ", first_value)
    try:
        second_value = float(input("Segundo valor: "))
    except ValueError("Introduce un número valido"):
        continue

    try:    
        if option_menu == 1:
            upshot = sum_add(first_value, second_value)
            print(f'El resultado de la suma de', first_value, '+', second_value, 'es =',upshot)
            
        elif option_menu == 2:
            upshot = subtraction(first_value, second_value)
            print(f'El resultado de la resta de', first_value, '-', second_value, 'es =',upshot)
        elif option_menu == 3:
            upshot = multiplication(first_value, second_value)
            print(f'El resultado de la multiplicación de', first_value, 'x', second_value, 'es =',upshot)
        elif option_menu == 4:
            if second_value == 0:
                raise ValueError ("ERROR!!! No se puede dividir entre cero")
            upshot = division(first_value, second_value)
            print(f'El resultado de la division de: ', first_value, '/', second_value, 'es =',upshot)
            
        elif option_menu == 5:
                first_value = 0
                second_value = 0
                upshot = 0
    except ValueError:
        print("ERROR!!! Ingresar solamente números")
    

    first_value = upshot
    print("\nNúmero actual :", upshot)

    keep_going = input("Seguir (s), Salir (n): ")
    if keep_going == "n":
        print("Saliendo del programa!!!")
        break
    elif keep_going != 's':
        print("ERROR!!! Ingresar solamente (s) para seguir ó (n) para salir")
    