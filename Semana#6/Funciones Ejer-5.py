"""
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

"""

def counter_lower_upper(text_string):

    words_in_text = {'Mayusculas': 0, 'minusculas': 0}
    
    for word in text_string:
        if word.isupper():
            words_in_text['Mayusculas'] +=1

        elif word.islower():
            words_in_text['minusculas'] +=1

    return words_in_text


def main():
    
    text_string = str(input("Ingresar una frase : "))
    
    print(text_string, f' → ', counter_lower_upper(text_string))


if __name__ == "__main__":
    main()
