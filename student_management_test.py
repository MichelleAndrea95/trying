import unittest
from crud_operations import Student, students, add_student, view_students, update_name, update_age, update_grade, update_subjects, delete_student, save_and_quit, load_students_from_file

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Förbered testmiljö genom att skapa testdata."""
        global students  
        students.clear()  

        # Skapa teststudenter
        self.test_students = [
            Student(1, "Florence", 28, "MVG", ["MA", "FY"]),
            Student(2, "Michelle", 29, "B", ["FY", "ID"]),
        ]
        students.extend(self.test_students)  

    def test_add_student(self):
        """Testar att lägga till en ny student."""
        add_student(3, "Charlie", 21, "C", ["Physics", "Chemistry"])
        self.assertEqual(len(students), 3)  # Kontrollera att en ny student har lagts till
        self.assertEqual(students[-1].name, "Charlie")  # Kolla om namnet stämmer

    def test_view_students(self):
        """Testar att visa alla studenter."""
        output = view_students()
        self.assertIn("Florence", output)
        self.assertIn("Michelle", output)

    def test_update_name(self):
        """Testar att uppdatera en students namn."""
        result = update_name(1, "Florence")
        self.assertTrue(result)
        self.assertEqual(students[0].name, "Florence")

    def test_update_age(self):
        """Testar att uppdatera en students ålder."""
        result = update_age(1, 25)
        self.assertTrue(result)
        self.assertEqual(students[0].age, 25)

    def test_update_grade(self):
        """Testar att uppdatera en students betyg."""
        result = update_grade(1, "VG")
        self.assertTrue(result)
        self.assertEqual(students[0].grade, "VG")

    def test_update_subjects(self):
        """Testar att uppdatera en students ämnen."""
        result = update_subjects(1, ["Biology", "Music"])
        self.assertTrue(result)
        self.assertEqual(students[0].subjects, ["Biology", "Music"])

    def test_delete_student(self):
        """Testar att radera en student."""
        delete_student(1)
        self.assertEqual(len(students), 1)  # Bara en student ska vara kvar
        self.assertNotIn("Florence", [student.name for student in students])  # Alice ska vara borta

    def test_save_and_load_students(self):
        """Testar att spara och ladda studenter från en fil."""
        save_and_quit(file="test_students.json")  # Spara till en testfil
        loaded_students = load_students_from_file(file="test_students.json")  # Ladda testfilen
        self.assertEqual(len(loaded_students), len(self.test_students))  # Kontrollera att antalet stämmer

if __name__ == "__main__":
    unittest.main()
