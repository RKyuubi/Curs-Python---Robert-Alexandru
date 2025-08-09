string = input("Introduceti orice propoizitie:")
lista = string.split()
lista_noua = []

for element in lista:
    if element[0].lower() != 'a':
        lista_noua.append(element)

propozitie_noua = " ".join(lista_noua)
print (propozitie_noua)
