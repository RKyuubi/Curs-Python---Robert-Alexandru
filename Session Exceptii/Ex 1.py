def factorial_n (numar):
    while True:
        rezultat_factorial = 1

        if numar < 0:
                print ("Error")
        elif numar == 0:
            rezultat_factorial = 1
            print ("Factorialul lui 0 este: 1\n")
        else:
            for i in range (1, numar + 1):
                rezultat_factorial *= i
            print ("Rezultatul factorial este:", rezultat_factorial)
        return rezultat_factorial

if __name__ == "__main__":
    while True:
        try:
            numar = int(input("Introduceti orice numar:"))
            rezultat = factorial_n(numar)
        except ValueError:
            print ("Error")
        else:
            break

