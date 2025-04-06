class Student:
    def __init__(self, student_name, student_group, spanish_grade, english_grade, social_grade, sciences_grade):
        self.student_name = student_name
        self.student_group = student_group
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.sciences_grade = sciences_grade
        self.average_grade = (spanish_grade + english_grade + social_grade + sciences_grade) / 4
        

    def to_dict(self):
        return {
            'student_name': self.student_name,
            'student_group': self.student_group,
            'spanish_grade': self.spanish_grade,
            'english_grade': self.english_grade,
            'social_grade': self.social_grade,
            'sciences_grade': self.sciences_grade,
            'average_grade': self.average_grade
        }
    
    @classmethod
    def from_dict(self, data):
        self.student_name = data['student_name']
        self.student_group = data['student_group']
        self.spanish_grade = data['spanish_grade']
        self.english_grade = data['english_grade']
        self.social_grade = data['social_grade']
        self.sciences_grade = data['sciences_grade']
        self.average_grade = (self.spanish_grade + self.english_grade + self.social_grade + self.sciences_grade) / 4



    #students_list = []
#Ingreso de info de estudiantes ------------------------------
    def add_student(self,students_list):

        #students_list = []

        while True:
            
            student_name = str(input("Ingresar nombre completo: "))
            student_group = str(input("Sección: "))
            while True:
                try:
                    spanish_grade = int(input("Nota de Español: "))
                    english_grade = int(input("Nota de Ingles: "))
                    social_grade = int(input("Nota de Sociales: "))
                    sciences_grade = int(input("Nota de Ciencias: "))

                    if( 0 <= spanish_grade <=100 and 
                        0 <= english_grade <=100 and
                        0 <= social_grade <=100 and
                        0 <= sciences_grade <=100 ):
                        break
                    else:
                        print("ERROR, las notas deben estar entre 0 y 100, inténtalo de nuevo.")

                except ValueError:
                    print("ERROR, debe ingresar una nota válida, inténtalo de nuevo.")

            
            student = Student(student_name, student_group, spanish_grade, english_grade, social_grade, sciences_grade)

            
            students_list.append(student)
            
            
            average_grade = float((spanish_grade + english_grade + social_grade + sciences_grade) / 4)
            
            add_another = input("¿Quieres ingresar otro estudiante? (s/n): ").lower()
            if add_another != 's':
                break

    # students_information(students_list)       


    def get_top_3_students(self,students_list):

        top_students = sorted(students_list, key=lambda x: x["average_grade"],reverse=True)

        print("\nTop #3 Estudiantes con Mejor Promedio:")
        for i in range(min(3, len(top_students))):  # Si hay menos de 3 estudiantes, muestra todos
            student = top_students[i]
            print(f"\n#{i+1} - {student['student_name']} (Sección {student['student_group']})")
            print(f"Promedio: {student["average_grade"]}")



    def students_information(self,students_list):

        print("\nInformación de los Estudiantes:")
        for student in students_list:
            average_grade = float(student['average_grade'])
            print("\n-------------------------")
            print(f"Nombre: {student['student_name']} (Sección {student['student_group']})")
            print(f"Español: {student['spanish_grade']}")
            print(f"Ingles: {student['english_grade']}")
            print(f"Sociales: {student['social_grade']}")
            print(f"Ciencias: {student['sciences_grade']}")
            print(f"Promedio: {student["average_grade"]:.2f}")

            

    def calculate_total_average(self,students_list):
        
        if len(students_list) == 0:
            print("No hay estudiantes para calcular el promedio.")
            return
        
        total_average = 0

        for student in students_list:
            total_average += float(student["average_grade"])
        
        overall_average = total_average / len(students_list)
        print(f"El promedio de todos los promedios es: {overall_average:.2f}")

students_list = []

student = Student("", "", 0, 0, 0, 0)

student.get_top_3_students(students_list)

student.students_information(students_list)

student.calculate_total_average(students_list)

