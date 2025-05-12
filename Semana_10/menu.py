def menu_system_student():

    while True:
        try:
            operation = int(input("\nSELECCIONE LA OPCION QUE DESEA REALIZAR\n"
                                "\n1. Ingresar estudiante"
                                "\n2. Ver los estudiantes ingresados"
                                "\n3. TOP #3 mejores promedio"
                                "\n4. Promedio General"
                                "\n5. Exportar datos en un archivo CSV"
                                "\n6. Importar datos en un archivo CSV\n \n"))

                               
            if(operation <=6 and operation > 0):
                
                break 
            else:
                print("Opción NO valida, ingrese una opcion valida del menu")
        except ValueError:
            print("Ingrese un número entero del 1 al 6 para seleccionar una opcion válida del menu \n")

    return operation