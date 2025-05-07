from menu import menu_system_student
from actions import add_student, students_information, get_top_3_students,calculate_total_average
from data import write_csv_file, import_csv_files

students_list = []
while True:

    option_menu = menu_system_student()

    if option_menu == 1:
        print("Ingresar Estudiante\n")
        add_student(students_list) 
    elif option_menu == 2:
        students_information(students_list)
    elif option_menu == 3:
        get_top_3_students(students_list)
    elif option_menu == 4:
        print("PROMEDIO GENERAL\n")
        calculate_total_average(students_list)
    elif option_menu == 5:
        print("Exportando info en archivo .csv\n")
        write_csv_file('students.csv', students_list, students_list[0].keys())
        print("Listo!!!")
    elif option_menu == 6:
        print("Importando info del archivo .csv")
        students_list = import_csv_files('students.csv')
    else:
        print("Opción no válida, por favor ingrese una opción correcta.")

    keep_going = input("\nPara ir al Menu y seguir digíte (m), "
                        "\nPara salir digíte (s): ")
    if keep_going == "s":
        print("Saliendo del programa!!!")
        break
    elif keep_going == 'm':
        print("Volviendo al menú...")
        continue
    else:    
        print("ERROR!!! Ingresar solamente (m) para seguir ó (s) para salir")