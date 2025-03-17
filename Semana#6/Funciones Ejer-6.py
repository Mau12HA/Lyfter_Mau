"""
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

"""


def order_words_alpha(text_string):
    
    string_to_list = text_string.split(sep='-') #convertir a lista

    string_to_list.sort() #ordenar
    
    new_string_list = "-".join(string_to_list)

    return(new_string_list)


def main():
    
    text_string = str(input("Ingresar texto: "))
    
    print(f'Texto ordenado: ',order_words_alpha(text_string))

if __name__ == "__main__":
    main()
