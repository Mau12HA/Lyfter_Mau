"""
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y 
        retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41

"""


def get_sum_list(number_list):
    return sum(number_list)


def main():
    number_list = [23,4,5,7,78,61] 
    print(number_list)
    print(f'La suma es: ', get_sum_list(number_list))


if __name__ == "__main__":
    main()