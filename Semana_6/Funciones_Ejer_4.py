"""
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”

"""


def string_back_way(normal_way_string):
    return normal_way_string[::-1]


def main():
    
    normal_way_string = str(input("Ingresar texto : "))
    
    print(f'Texto inverso : ', string_back_way(normal_way_string))


if __name__ == "__main__":
    main()
