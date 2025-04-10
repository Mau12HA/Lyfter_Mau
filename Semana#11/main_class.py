from  menu_class import menu_system_student
from actions_class import Student
from data_class import  Data

students_list = []
student = Student("", "", 0, 0, 0, 0)
data = Data(students_list)
while True:

    option_menu = menu_system_student()

    if option_menu == 1:
        print("Add Student\n")
        student.add_student(students_list) 
    elif option_menu == 2:
        student.students_information(students_list)
    elif option_menu == 3:
        student.get_top_3_students(students_list)
    elif option_menu == 4:
        print("GENERAL AVERAGE\n")
        student.calculate_total_average(students_list)
    elif option_menu == 5:
        print("Exporting info in file.csv\n")
        data.write_csv_file('students.csv', students_list[0].keys())
        print("Ready!!!")
    elif option_menu == 6:
        print("Import info from file.csv")
        students_list = data.import_csv_files('students.csv')
    else:
        print("Wrong option, please choose a right option.")

    keep_going = input("\nFor go to menu, write (m), "
                        "\nExit (s): ")
    if keep_going == "s":
        print("Going Out!!!")
        break
    elif keep_going == 'm':
        print("Come back to menu...")
        continue
    else:    
        print("ERROR!!! Write only (m) for keep going or (s) for go out")