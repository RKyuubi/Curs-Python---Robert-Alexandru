nr_elemente = int(input("Introduceti cate elemente doriti sa aiba lista:"))

while nr_elemente < 0:
    print ("Numarul de elemente nu poate fi negativ, te rog introdu un numar pozitiv:")
    nr_elemente = int(input("Introduceti cate elemente doriti sa aiba lista:"))

lista = []

for i in range(nr_elemente):
    element = input(f"Introduceti elementul {i+1}:")
    lista.append(element)

print (f"\n",lista)

lista_lungime_caractere = []

for element in lista:
    lungime_cuvant = len(element)
    lista_lungime_caractere.append(lungime_cuvant)

print("\n",lista_lungime_caractere)

nr_elemente = len(lista)
suma_lungime_caractere = sum(lista_lungime_caractere)

if nr_elemente > 0:
    val_medie_caractere = suma_lungime_caractere/nr_elemente

print(f"\nValoarea medie este: {val_medie_caractere:.2f}")

for element in lista:
    if len(element) > val_medie_caractere:
        print(f"Cuvintele care au un numar de caractere mai mare decat valoare medie:", element)
