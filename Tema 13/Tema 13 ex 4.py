def citeste_a_si_scrie_b():
    try:
        with open("source.txt", "r") as fisier:
            lista = fisier.readlines()
        with open("destination.txt", "x") as fisier:
            fisier.writelines(lista)
    except FileNotFoundError:
        print("Eroare: Fisierul 'source.txt' nu a fost gasit.")
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    citeste_a_si_scrie_b()