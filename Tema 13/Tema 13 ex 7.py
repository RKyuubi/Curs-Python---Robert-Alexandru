def scrie_numere_fisier(cate_numere):
    try:
        with open("numbers.txt", "w") as fisier:
            for i in range (1, cate_numere + 1):
                fisier.write(str(i) + "\n")
    except Exception as e:
        print(f"A aparut o eroare: {e}")

def numere_pare():
    try:
        with open("numbers.txt", "r") as fisier:
            lista = fisier.readlines()
        lista_numere_pare = []
        for element in lista:
            try:
                if float(element) % 2 ==0:
                    lista_numere_pare.append(element)
            except ValueError:
                pass
        with open ("EvenNumbers.txt", "w") as fisier:
            fisier.writelines(lista_numere_pare)

    except FileNotFoundError:
        print("Eroare: Fișierul 'text.txt' nu a fost găsit.")
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    # numere = int(input("Cate numere sa contina fisierul:"))
    # scrie_numere_fisier(numere)
    numere_pare()
