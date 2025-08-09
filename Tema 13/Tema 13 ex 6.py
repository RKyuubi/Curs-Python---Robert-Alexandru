def citeste_a_si_scrie_b():
    try:
        with open("input.txt", "r") as fisier:
            lista = fisier.readlines()
        lista.reverse()
        with open("output.txt", "w") as fisier:
            fisier.writelines(lista)
    except FileNotFoundError:
        print("Eroare: Fisierul 'source.txt' nu a fost gasit.")
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    citeste_a_si_scrie_b()