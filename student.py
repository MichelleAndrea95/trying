

class students_list:
    def __init__(self):
        self.students = []


class Student:
    def __init__(self, id, name, age, grade, subjects):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects

    def __repr__(self):
        return f"Student(ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)})"

    def update_info(self, attribute, new_value):
        if hasattr(self, attribute):
            setattr(self, attribute, new_value)
        else:
            print("")

    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Grade: {self.grade}, Subjects: {', '.join(self.subjects)}")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects":self.subjects
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["age"], data["grade"], data["subjects"])







