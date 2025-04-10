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
            
            student_name = str(input("Full name: "))
            student_group = str(input("Group: "))
            while True:
                try:
                    spanish_grade = int(input("Score of Spanish: "))
                    english_grade = int(input("Score of English: "))
                    social_grade = int(input("Score of Social: "))
                    sciences_grade = int(input("Score of Sciences: "))

                    if( 0 <= spanish_grade <=100 and 
                        0 <= english_grade <=100 and
                        0 <= social_grade <=100 and
                        0 <= sciences_grade <=100 ):
                        break
                    else:
                        print("ERROR, The scores must be between 0 and 100, please try again.")

                except ValueError:
                    print("ERROR, You must enter a valid score, please try again.")

            
            student = Student(student_name, student_group, spanish_grade, english_grade, social_grade, sciences_grade)

            
            students_list.append(student)
            
            
            average_grade = float((spanish_grade + english_grade + social_grade + sciences_grade) / 4)
            
            add_another = input("¿Do you wnt to add another student? (s/n): ").lower()
            if add_another != 's':
                break

    # students_information(students_list)       


    def get_top_3_students(self,students_list):

        top_students = sorted(students_list, key=lambda x: x["average_grade"],reverse=True)

        print("\nTop #3 best average of students:")
        for i in range(min(3, len(top_students))):  # Si hay menos de 3 estudiantes, muestra todos
            student = top_students[i]
            print(f"\n#{i+1} - {student['student_name']} (Group {student['student_group']})")
            print(f"Averages: {student["average_grade"]}")



    def students_information(self,students_list):

        print("\nStudents Info:")
        for student in students_list:
            average_grade = float(student['average_grade'])
            print("\n-------------------------")
            print(f"Name: {student['student_name']} (Group {student['student_group']})")
            print(f"Spanish: {student['spanish_grade']}")
            print(f"English: {student['english_grade']}")
            print(f"Social: {student['social_grade']}")
            print(f"Sciences: {student['sciences_grade']}")
            print(f"Average: {student["average_grade"]:.2f}")

            

    def calculate_total_average(self,students_list):
        
        if len(students_list) == 0:
            print("There are no Students.")
            return
        
        total_average = 0

        for student in students_list:
            total_average += float(student["average_grade"])
        
        overall_average = total_average / len(students_list)
        print(f"The general average is: {overall_average:.2f}")

students_list = []

student = Student("", "", 0, 0, 0, 0)

student.get_top_3_students(students_list)

student.students_information(students_list)

student.calculate_total_average(students_list)