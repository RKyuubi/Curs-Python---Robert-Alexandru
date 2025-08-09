string_1 = input ("Introduceti orice propozitie:")
string_1 = string_1.lower()
lista = []

for char in string_1:
    if char.isalpha() and char not in lista:
        lista.append(char)

print (lista)