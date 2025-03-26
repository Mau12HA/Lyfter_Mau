"""
EJERCICIO JSON

2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON

    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.

"""

import json

def read_pokemons(poke_file):
    try:
        with open(poke_file,'r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

print()



def ask_info_pokemon():
     
    print(f'\nINGRESAR NUEVO POKEMON\n')
    
    name = str(input("Nombre del Pokemon: "))
    type = str(input("Pokemon tipo: "))
    try:
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        sp_attack = int(input("Sp. Attack: "))
        sp_defense = int(input("Sp. Defense: "))
        speed = int(input("Speed: "))
    except ValueError:
        print("Debes ingresar valores númericos para estos campos")
        return None

    new_pokemon = {
        "name":{
            "english": name
    },
    "type": [
      type
    ],
    "base": {
      "HP": hp,
      "Attack": attack,
      "Defense": defense,
      "Sp. Attack": sp_attack,
      "Sp. Defense": sp_defense,
      "Speed": speed
        }
    }
    
    return new_pokemon


def save_pokemons(poke_file, pokes):

    with open(poke_file, 'w', encoding='utf-8')as file:
        json.dump(pokes,file, indent=4)



def main():
     
    poke_file = 'Pokemon.json'

    pokes = read_pokemons(poke_file)

    new_pokemon = ask_info_pokemon()
    pokes.append(new_pokemon)

    save_pokemons(poke_file, pokes)
    print(f'Se ha agregado al Pokemon: {new_pokemon['name']['english']}')



if __name__== "__main__":

    main()