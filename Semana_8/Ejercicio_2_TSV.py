"""
2. Cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

"""

import csv


videogames = []

number_of_videogames= int(input("\nCuantos video juegos desea ingresar: "))


for i in range(number_of_videogames):
    print(f'\nIngreso del videojuego {i + 1}:')

    name = str((input("Nombre del video juego: ")))
    vg_gender = str(input("Género: "))
    developer = str(input("Desarrollador: "))
    clasificationESRB = str(input("Clasificación: "))
                
    video_game ={
        "Nombre": name,
        "Género": vg_gender,
        "Desarrollador": developer,
        "Clasificación": clasificationESRB
    }

    videogames.append(video_game)
    
games_headers =[
        "Nombre",
        "Género",
        "Desarrollador",
        "Clasificación",
]

def write_csv_file(file_path,data,headers):
    with open(file_path, 'w',encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

write_csv_file('videosgames.tsv',videogames, games_headers) # se cambia el nombre del archivo en la extension por .tsv

