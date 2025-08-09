nr_elemente = int(input("Introduceti cate elemente doriti sa aiba lista:"))

while nr_elemente < 0:
    print ("Numarul de elemente nu poate fi negativ, te rog introdu un numar pozitiv:")
    nr_elemente = int(input("Introduceti cate elemente doriti sa aiba lista:"))

lista = []

for i in range(nr_elemente):
    element = input(f"Introduceti elementul {i+1}:")
    lista.append(element)

print (f"\n",lista)

cuvant_inversat = ""
lista_cuvinte_inversate = []

for element in lista:
    cuvant_inversat = element[::-1] #se creeaza cuvantul inversat cu ajutorul slicing-ului de pe ultima pozitie a cuvantului
    lista_cuvinte_inversate.append(cuvant_inversat)

print(f"\n",lista_cuvinte_inversate)
