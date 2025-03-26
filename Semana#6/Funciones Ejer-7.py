"""
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
                Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

"""

def list_prime_numbers(my_list,new_list):

    
    for number in my_list:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            new_list.append(number)

    return new_list


def main():
    
    #list_size = int(input("Ingresar el tamaño de la lista : "))
    my_list = [1, 4, 6, 7, 13, 9, 67]
    new_list = []
    #for i in range(list_size):
    #    my_list.append(int((input("Ingrese un número a la lista : "))))
    print(f'Lista :',my_list, f'→ los números primos son:', list_prime_numbers(my_list,new_list))

if __name__ == "__main__":
    main()
