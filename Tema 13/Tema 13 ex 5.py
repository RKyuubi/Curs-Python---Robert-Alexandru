def scrie_fisier_output():
    try:
        cuvant_cerut = input("Scrie orice cuvant:")
        cuvant_gasit = False
        with open("text.txt", "r") as fisier:
            for line in fisier:
                if cuvant_cerut.lower() in line.lower():
                    print(line)
                    cuvant_gasit = True
        if not cuvant_gasit:
            print(f"Nicio line din fisier nu contine cuvantul: {cuvant_cerut}")
    except FileNotFoundError:
        print("Eroare: Fișierul 'text.txt' nu a fost găsit.")
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    scrie_fisier_output()