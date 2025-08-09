employee = {
    1: {'name':'Andrei', 'salary':100},
    2: {'name':'Vlad', 'salary':500},
    3: {'name':'Ioana', 'salary':330}
}

employee_modificat = {id_angajat: {'name': emp['name'], 'salary':int(input(f"Care vrei sa fie salariul nou al angajatului {emp['name']}?"))} for id_angajat, emp in employee.items()}

print(employee_modificat)

