class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def note(self):
        numar_note_lista = int(input("Introdu cate note doresti sa aiba studentul:"))
        self.grades = []
        for i in range(numar_note_lista):
            nota_elev = int(input(f"Introdu nota {i + 1}:"))
            self.grades.append(nota_elev)

    def medie(self):
        medie_note = sum(self.grades) / len(self.grades)
        return round(medie_note)

if __name__ == "__main__":
    nume_student = Name("Robert", "Alexandru")
    student = Student(Name, 30, [])
    student.nota()
    print(f"Media studentului {nume_student} este {student.medie()}")
