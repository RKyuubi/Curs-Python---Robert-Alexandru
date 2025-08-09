def numar_linii_fisier():
    try:
        with open("Fisier1.txt", "r") as fisier:
            # lista = fisier.readlines() #Varianta 1
            # numar_linii = len(fisier.readlines())
            numar_linii = 0
            for line in fisier:  #Varianta 2 # puteai sa pui _ in loc de linie (din moment ce nu folosesti variabila
                numar_linii += 1
        print (numar_linii)
    except FileNotFoundError:
        print ("Eroare: Fisierul 'Fisier1.txt' nu a fost gasit.")
    except Exception as e:
        print (f"A aparut o erare: {e}")

if __name__ == "__main__":
    numar_linii_fisier()