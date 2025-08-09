employee = {
    1: {'name':'Andrei', 'salary':100},
    2: {'name':'Vlad', 'salary':500},
    3: {'name':'Ioana', 'salary':330}
}
print("Dictionarul initial:")
print (employee)

id_valid = False
id_temporar = None
while id_valid is not True:
    id_valid_input = input("\nIntroduceti ID-ul angajatului pe care doriti sa il modificati:")
    if id_valid_input.isdigit():
        angajat_selectat = int(id_valid_input)
        if angajat_selectat in employee:
            id_temporar = angajat_selectat
            id_valid = True
        else:
            print("ID-ul introdus nu este al unui angajat existent. Va rog reintroduceti ID-ul corespunzator")
    else:
        print("Introdu un numar intreg valid pentru ID")
#bucla de mai sus verifica daca ID-ul introdus ca input este valid (se regaseste in dictionar) sau nu


