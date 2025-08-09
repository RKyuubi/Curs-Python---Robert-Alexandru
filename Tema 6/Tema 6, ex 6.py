numar_elemente_lista = int(input("Introdu cate elemente doresti sa aiba lista:"))
lista = []

for i in range (numar_elemente_lista):
    element = input(f"Introdu elementul {i+1}:")
    lista.append(element)

print("\nLista este:", lista)

primul_element = lista[0]
sunt_diferite = False
prefix_comun = ""

for i in range (len(primul_element)):
    caracterul_curent = primul_element[i]
    for element in lista:
        if i >= len(element) or element[i] != caracterul_curent:
            sunt_diferite = True
            break
    if sunt_diferite:
        break
    prefix_comun += caracterul_curent

print(prefix_comun)
