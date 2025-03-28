students_list = []


#Ingreso de info de estudiantes ------------------------------
def add_student(students_list):

    #students_list = []

    while True:
        student={}
        student['student_name'] = str(input("Ingresar nombre completo: "))
        student['student_group'] = str(input("Sección: "))
        while True:
            try:
                student['spanish_grade'] = int(input("Nota de Español: "))
                student['english_grade'] = int(input("Nota de Ingles: "))
                student['social_grade'] = int(input("Nota de Sociales: "))
                student['sciences_grade'] = int(input("Nota de Ciencias: "))

                if( 0 <= student['spanish_grade'] <=100 and 
                    0 <= student['english_grade'] <=100 and
                    0 <= student['social_grade'] <=100 and
                    0 <= student['sciences_grade'] <=100 ):
                    break
                else:
                    print("ERROR, las notas deben estar entre 0 y 100, inténtalo de nuevo.")

            except ValueError:
                print("ERROR, debe ingresar una nota válida, inténtalo de nuevo.")

        student['average_grade'] = float((student['spanish_grade'] + student['english_grade'] + student['social_grade'] + student['sciences_grade']) / 4)
        
        students_list.append(student)
        
        add_another = input("¿Quieres ingresar otro estudiante? (s/n): ").lower()
        if add_another != 's':
            break

   # students_information(students_list)       


def get_top_3_students(students_list):

    top_students = sorted(students_list, key=lambda x: x["average_grade"],reverse=True)

    print("\nTop #3 Estudiantes con Mejor Promedio:")
    for i in range(min(3, len(top_students))):  # Si hay menos de 3 estudiantes, muestra todos
        student = top_students[i]
        print(f"\n#{i+1} - {student['student_name']} (Sección {student['student_group']})")
        print(f"Promedio: {student['average_grade']}")



def students_information(students_list):

    print("\nInformación de los Estudiantes:")
    for student in students_list:
        average_grade = float(student['average_grade'])
        print("\n-------------------------")
        print(f"Nombre: {student['student_name']} (Sección {student['student_group']})")
        print(f"Español: {student['spanish_grade']}")
        print(f"Ingles: {student['english_grade']}")
        print(f"Sociales: {student['social_grade']}")
        print(f"Ciencias: {student['sciences_grade']}")
        print(f"Promedio: {average_grade:.2f}")

        

def calculate_total_average(students_list):
    
    if len(students_list) == 0:
        print("No hay estudiantes para calcular el promedio.")
        return
    
    total_average = 0

    for student in students_list:
        total_average += float(student["average_grade"])
    
    overall_average = total_average / len(students_list)
    print(f"El promedio de todos los promedios es: {overall_average:.2f}")