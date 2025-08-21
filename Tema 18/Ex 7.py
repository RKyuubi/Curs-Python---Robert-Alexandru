class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}; {self.age};"

class Student(Person):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def __str__(self):
        return f"{self.name}; {self.age}; {self.grades}"

class Teacher(Person):
    def __init__(self, name, age, materie):
        super().__init__(name, age)
        self.materie = materie

    def __str__(self):
        return f"{self.name}; {self.age}; {self.materie}"

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, grades, materie):
        self.name = name
        self.age = age
        self.grades = grades
        self.materie = materie

    def __str__(self):
        return f"Asistent didactic: {self.name}; Varsta: {self.age}; Note: {self.grades}; Materie: {self.materie}"

if __name__ == "__main__":
    asistent = TeachingAssistant("Radu George", 23, [10,9,10], "Marketing Online")
    print(asistent)