def numar_cuvinte_fisier():
    try:
        with open("Fisier2.txt", "r") as fisier:
            lista = fisier.readlines()
            cuvinte = []
            numar_cuvinte = 0
            for element in lista:
                cuvinte = element.split()
                numar_cuvinte += len(cuvinte)
        print (numar_cuvinte)
    except FileNotFoundError:
        print ("Eroare: Fisierul 'Fisier2.txt' nu a fost gasit.")
    except Exception as e:
        print (f"A aparut o erare: {e}")

if __name__ == "__main__":
    numar_cuvinte_fisier()