class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Nume: {self.name}; \nSalariu: {self.salary} RON\n"

class Developer(Employee):
    def __init__(self, name, salary, lb_programare):
        super().__init__(name,salary)
        self.lb_programare = lb_programare

    def __str__(self):
        return f"Nume: {self.name}; \nSalariu: {self.salary} RON; \nLimbaj de programare: {self.lb_programare}\n"

class Designer(Employee):
    def __init__(self, name, salary, soft_de_design):
        super().__init__(name, salary)
        self.soft_de_design = soft_de_design

    def __str__(self):
        return f"Nume: {self.name}; \nSalariu: {self.salary} RON; \nSoft de design folosit: {self.soft_de_design}\n"

if __name__ == "__main__":
    employee = Employee("Ion Marin", 5000)
    developer = Developer("George Tanase", 10000, "Python")
    designer = Designer("Ecaterina Teodoroiu", 9000, "Adobe Photoshop")

    print("---Detalii despre angajati---")
    print(employee)
    print(developer)
    print(designer)

