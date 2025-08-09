numar_elemente_lista = int(input("Introdu cate elemente doresti sa aiba lista:"))
lista1 = []

for i in range (numar_elemente_lista):
    element = int(input(f"Introdu elementul {i+1}:"))
    lista1.append(element)

print("\nLista este:", lista1)

dict1 = {}

for element in lista1:
    if element in dict1:
        dict1[element] +=1
    else:
        dict1[element] = 1

print(dict1)