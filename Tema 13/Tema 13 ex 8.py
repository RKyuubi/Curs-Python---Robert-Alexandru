def scrie_litere_mari():
    try:
        with open("Fisier8.txt", "r") as fisier:
            lista = fisier.readlines()
        linii_mari = []
        for element in lista:
            linii_mari.append(element.upper())

        with open ("Fisier8 output.txt", "w") as fisier:
            fisier.writelines(linii_mari)
    except FileNotFoundError:
        print("Eroare: Fișierul 'text.txt' nu a fost găsit.")
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    scrie_litere_mari()