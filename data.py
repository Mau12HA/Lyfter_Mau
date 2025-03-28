import csv
from actions import students_list

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
if students_list:
    write_csv_file('students.csv', students_list, students_list[0].keys())
else:
   print("No hay estudiantes para exportar")

def import_csv_files(students_files):
  try:
    with open(students_files,'r',encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
  except FileNotFoundError:
    print("EL ARCHIVO NO EXISTE!!!")
    return[] 