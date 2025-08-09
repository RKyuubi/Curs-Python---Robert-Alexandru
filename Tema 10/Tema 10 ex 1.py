import time

def append_in_lista(numar_elemente):
    """
    Masoara timpul necesar pentru a adauga elemente intr-o lista folosind append()
    """
    lista1=[]
    start_time = time.time()
    for i in range(numar_elemente):
        lista1.append(i)
    end_time = time.time()
    return end_time - start_time

# print(append_in_lista(int(input("Introduceti cate elemente doriti sa aiba lista: "))))

def list_comprehension(numar_elemente):
    """
    Masoara timpul necesar pentru a adauga elemente intr-o lista folosind list comprehension
    """
    start_time = time.time()
    lista2 = [i for i in range (numar_elemente)]
    end_time = time.time()
    return end_time - start_time

# print (list_comprehension(int(input("Introduceti acelasi numar de elemente ca mai sus pentru a putea compara rezultatele: "))))

numar_elemente_liste = int(input("Introduceti cate elemente doriti sa aiba lista pentru aplicarea celor doua functii: "))

timp_append = append_in_lista(numar_elemente_liste)
timp_comprehension = list_comprehension(numar_elemente_liste)

print (f"\nTimpul necesar pentru append() este de: {timp_append}")
print (f"\nTimpul necesar pentru comprehension este de: {timp_comprehension}")

if timp_append < timp_comprehension:
    print ("\nMetoda append() a fost mai rapida")
elif timp_append > timp_comprehension:
    print ("\nMetoda comprehension a fost mai rapida")
else:
    print ("\nAmbele metode au avut acelasi timp")
