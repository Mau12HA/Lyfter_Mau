"""
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
"""


hotel_information = {
    'name': 'MGM',
    'numb_stars': 4,
    'rooms': [
            {
                'number':17,
                'floor':2,
                'price _for_nigth': 50000
            },
            {
                'number':5,
                'floor':1,
                'price _for_nigth': 45000
            },
            {
                'number':23,
                'floor':3,
                'price _for_nigth': 55000
            }
    ],
    
}

print(hotel_information['rooms'][1])
print(hotel_information['rooms'][2])
print(hotel_information['rooms'][0])