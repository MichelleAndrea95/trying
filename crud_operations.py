

import json
from student import Student
students=[]


def load_students_from_file(file="students.json"):
    """Läser in studentdata från en JSON-fil."""
    try:
        with open(file, "r") as f:  
            data= json.load(f)
            return [Student.from_dict(student) for student in data]
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Filen {file} kunde inte läsas. Skapar en tom lista.")
        return[]#

students = load_students_from_file()


def add_student(id, name, age, grade, subjects):
    global students #
    new_student = Student(id, name, age, grade, subjects)
    students.append(new_student)


def view_students():
    if not students:  
        return "Det finns inga studenter i systemet."
    
    output = "\nLista på alla studenter:\n"
    for student in students:
        output += f"ID: {student.id}, Namn: {student.name}, Ålder: {student.age}, Betyg: {student.grade}, Ämnen: {', '.join(student.subjects)}\n"
    return output
    
def update_name(student_id, new_name):
    global student
    for student in students:
        if student.id == student_id:
            student.name = new_name
            return True
    return False

def update_age(student_id, new_age):
    global student
    for student in students:
        if student.id == student_id:
            student.age = new_age
            return True
    return False

def update_grade(student_id, new_grade):
    global student
    for student in students:
        if student.id == student_id:
            student.grade = new_grade
            return True
    return False

def update_subjects( student_id, new_subjects):
    global student
    for student in students:
        if student.id == student_id:
            student.subjects = new_subjects
            return True
    return False

def update_student_info(student_id, field, new_value):
    global student
    for student in students:
        if student.id == student_id:
            if field == 'name':
                student.name = new_value
            elif field == 'age':
                student.age = new_value
            elif field == 'grade':
                student.grade = new_value
            elif field == 'subjects':
                student.subjects = new_value.split(",")  # Om ämnen är kommaseparerade
            return

def delete_student(student_id):
    global students  # Se till att detta är inkluderat
    students[:] = [student for student in students if student.id != student_id]


"""

def delete_student(student_id):   
    global student     
    updated_student_info = [student for student in students if student.id != student_id]   
    if len(updated_student_info) == len(students):       
        print("Studenten hittades inte.")   
    else:        
        students[:] = updated_student_info
        save_and_quit(file="students.json")        
        print(f"Student med ID {student_id} har raderats.")
        """
    
def save_and_quit(file="students.json"):
    try:
      
        with open(file, "w", encoding="utf-8") as f:
            json.dump([student.to_dict() for student in students], f, indent=4)
        print("Data har sparats till fil.")
    except Exception as e:
        print(f"Ett fel uppstod vid sparandet: {e}")
    
    print(f"Studentdata har sparats i dokumentet '{file}'.")
    return