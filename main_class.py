from  menu_class import menu_system_student
from actions_class import Student
from data_class import  Data

students_list = []
student = Student("", "", 0, 0, 0, 0)
data = Data(students_list)
while True:

    option_menu = menu_system_student()

    if option_menu == 1:
        print("Ingresar Estudiante\n")
        student.add_student(students_list) 
    elif option_menu == 2:
        student.students_information(students_list)
    elif option_menu == 3:
        student.get_top_3_students(students_list)
    elif option_menu == 4:
        print("PROMEDIO GENERAL\n")
        student.calculate_total_average(students_list)
    elif option_menu == 5:
        print("Exportando info en archivo .csv\n")
        data.write_csv_file('students.csv', students_list[0].keys())
        print("Listo!!!")
    elif option_menu == 6:
        print("Importando info del archivo .csv")
        students_list = data.import_csv_files('students.csv')
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