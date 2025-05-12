
"""
2.Cree un programa que le pida al usuario su 
nombre, apellido, y edad, y muestre si es un 
bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor

"""
nombre= input("Escribir Nombre : ")
apellido = input("Escribir Apellido : ")
edad =  int (input("Ingresar Edad : "))

#print (nombre.lower(),'.',apellido.lower(),'@',dominio,'.com', sep='')
if 1<= (edad)  <=3:
    print(f'{nombre } {apellido} {edad} años es un :' "Bebé")
elif 4<= (edad) <=10:
    print(f'{nombre } {apellido} {edad} años es un : ' "Niño")
elif 11<= (edad) <=15: 
    print(f'{nombre } {apellido} {edad} años es un : ' "Preadolecente")
elif 16<= (edad) <=18:
    print(f'{nombre } {apellido} {edad} años es un : ' "Adolecente")
elif 19<= (edad) <= 30:
    print(f'{nombre } {apellido} {edad} años es un : ' "Adulto Joven")
elif 30<= (edad) <=64:
    print(f'{nombre } {apellido} {edad} años es un : ' "Adulto")
elif 65<= (edad) <= 120:
    print(f'{nombre } {apellido} {edad} años es un : ' "Adulto Mayor")
else:
    print("Edad Incorrecta")


#print(f'{nombre } {apellido} {edad}')