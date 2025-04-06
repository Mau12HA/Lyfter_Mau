import csv
from actions_class import Student

class Data:
    def __init__(self, students_list):
        self.students_list = students_list

    def write_csv_file(self, file_path, headers):
        """Escribe la lista de estudiantes en un archivo CSV."""
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for student in self.students_list:
                writer.writerow(student.to_dict())
            

    def export_students(self):
        """Exporta los estudiantes a un archivo CSV si hay estudiantes en la lista."""
        if self.students_list:
            self.write_csv_file('students.csv', self.students_list[0].keys())
        else:
            print("No hay estudiantes para exportar")

    def import_csv_files(self, students_file):
        """Importa los estudiantes desde un archivo CSV."""
        try:
            with open(students_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student.from_dict(row) 
                    self.students_list.append(student)
                return self.students_list
        except FileNotFoundError:
            print("¡El archivo no existe!")
            return []

students_list = []

csv_data = Data(students_list)

csv_data.export_students()

imported_students = csv_data.import_csv_files('students.csv')


for student in imported_students:
    print(student.to_dict())