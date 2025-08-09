paths = {
    'C://Downloads//Images': ['jpg', 'png', 'jpeg'],
    'C://Downloads//Text': ['txt'],
    'C://Downloads//Python_files': ['py'],
    'C://Downloads//PDF': ['pdf'],
}

files = ['mare_2023.jpeg', 'test.txt', 'liste.py', 'cv.pdf']

# extensie_elemente = []
# for element in files:
#     extensie_elemente.append(element.split('.')[-1])
#
# print(extensie_elemente)
# ^ mai sus am crezut ca pot face ceva daca extrag doar extensiile dar mi-am dat seama ca nu mai pot actiona dupa elementele din lista si devenea mai complicat

for element in files:
    pozitie_punct = element.rfind(".") #cautam pozitia punctului din elementul listei
    extensie_element = ""
    if pozitie_punct != -1:
        extensie_element = element[pozitie_punct + 1:]

    apartine_categoriei = False #plecam de la premiza ca elementul din lista nu apartine niciunei categorii

    for path, extensie in paths.items():
        if extensie_element in extensie:
            print(f"\nFisierul '{element}' cu extensia '.{extensie_element}' se potriveste cu categoria '{path}")
            apartine_categoriei = True
            break

    if not apartine_categoriei:
        print(f"\nFisierul '{element}' cu extensia '.{extensie_element}' nu se potriveste cu categoria '{path}")
