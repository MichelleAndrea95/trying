# Meny för att interagera med användaren
from crud_operations import add_student,update_student_info, update_age, update_grade, update_name, update_subjects,view_students,delete_student,load_students_from_file,save_and_quit
   
def main_menu():      
    global students 
    students= load_students_from_file()

    while True:
        print("\nStudent Management System")
        print("1. Lägg till student")
        print("2. Lista på alla studenter")
        print("3. Uppdatera studentinformation")
        print("4. Radera student")
        print("5. Stäng ner och spara data")
        choice = input("Välj ett alternativ: ")

        if choice == "1":
            # Lägg till student
            id = int(input("Välj ett id för student: "))
            name = input("Välj ett namn för student: ")
            age = int(input("Välj en ålder för student: "))
            grade = input("Välj ett betyg för student: ")
            subjects = input("Välj kommaseparerade ämnen för student: ").split(",")
            add_student(id, name, age, grade, subjects)
            save_and_quit(file="students.json")

        elif choice == "2":
            print(view_students())  # Skriv ut resultatet av view_students
            
        elif choice == "3":
            student_id = int(input("Ange studentens ID att uppdatera: "))
            update_student_info(student_id)  # Se till att du skickar student_id
            save_and_quit(file="students.json")  # Spara efter uppdatering
            
        elif choice == "4":
            # Radera student
            student_id = int(input("Ange ID för den student du vill ta bort: "))
            students = delete_student(student_id)
            save_and_quit(file= "students.json")

        elif choice == "5":
            save_and_quit(file="students.json")
            break

        else:
            print("Ogiltigt val.")

def update_student_info(student_id):
      
        print("Vilken information vill du uppdatera?")
        print("1. Namn")
        print("2. Ålder")
        print("3. Betyg")
        print("4. Ämnen")
   

        update_choice = input("Välj ett alternativ (1-4): ")

        if update_choice == '1':
            new_name = input("Ange det nya namnet: ")
            if update_name(student_id, new_name):
                print("Studentens namn har uppdaterats.")
            else:
                print("Ingen student hittades med det ID:t.")
    
        elif update_choice == '2':
            new_age = int(input("Ange den nya åldern: "))
            if update_age(student_id, new_age):
                print("Studentens ålder har uppdaterats.")
            else:
                print("Ingen student hittades med det ID:t.")

        elif update_choice == '3':
            new_grade = input("Ange det nya betyget: ")
            if update_grade(student_id, new_grade):
                print("Studentens betyg har uppdaterats.")
            else:
                print("Ingen student hittades med det ID:t.")

        elif update_choice == '4':
            new_subjects = input("Ange de nya ämnena, separerade med kommatecken: ").split(",")
            if update_subjects(student_id, new_subjects):
                print("Studentens ämnen har uppdaterats.")
            else:
                print("Ingen student hittades med det ID:t.")
    
        else:
            print("Ogiltigt val.")

    
if __name__ == "__main__":
    main_menu()