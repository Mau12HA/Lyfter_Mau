"""
Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.

"""

time_secd = int(input(" Ingrese el tiempo en segundos : "))
time_Mm = int()

if(time_secd > 600):
    print("MAYOR")

elif(time_secd< 600):
    time_Mm = 600 - time_secd
    print(f'Segundos restantes : {time_Mm}')