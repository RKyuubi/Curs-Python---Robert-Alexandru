import numpy as np

if __name__ == '__main__':
    try:
        x = int(input('Introduceti prima valoare a vectorului (start): '))
        z = int(input('Introduceti a doua valoare a vectorului (stop): '))
    except ValueError:
        print("Eroare: Va rugam introduceti numere intregi.")
        exit()

    if x < z:
        a = np.arange(x, z)
        lungime_a = len(a)

        try:
            nr_linii = int(input('Introduceti numarul de linii a matricei: '))
            nr_coloane = int(input('Introduceti numarul de coloane a matricei: '))
        except ValueError:
            print("Eroare: Va rugam introduceti numere intregi pentru dimensiuni.")
            exit()

        dimensiune_matrice = nr_linii * nr_coloane

        if lungime_a == dimensiune_matrice:
            print("\nLungimea vectorului se potriveste cu dimensiunea matricei.")
            b = a.reshape((nr_linii, nr_coloane))
            print("Matricea rezultata (b):")
            print(b)
        else:
            print(
                f"\nATENTIE: Lungimea vectorului ({lungime_a}) NU este egala cu produsul dimensiunilor matricei ({dimensiune_matrice}).")
            print("Nu se poate efectua reshape cu aceste dimensiuni.")

    else:
        print("Valoarea lui Z trebuie sa fie strict mai mare decat valoarea lui X.")