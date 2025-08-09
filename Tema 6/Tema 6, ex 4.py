numar_elemente_lista = int(input("Introdu cate elemente doresti sa aiba lista:"))
lista1 = []

for i in range (numar_elemente_lista):
    element = input(f"Introdu elementul {i+1}:")
    lista1.append(element)

print("\nLista este:", lista1)

lista2 = []

for char in lista1:
    if char.isdigit():
        numar = int(char)
        if numar > 0:
            lista2.append(numar)

lista2.sort()
print(lista2)
suma_2nr_mici = 0
if len(lista2) >1:
    suma_2nr_mici = lista2[0] + lista2[1]
elif len(lista2) ==1:
    suma_2nr_mici = lista2[0]
else:
    print ("Nu sunt numere pozitive in lista pentru a calcula suma.")

print(suma_2nr_mici)
