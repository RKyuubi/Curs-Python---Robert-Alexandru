def string_inversat (string):
    """
    Returneaza un string cu toate cuvintele inversate si separate de un singur spatiu
    """
    cuvinte = string.split()
    cuvinte.reverse()

    return " ".join(cuvinte)

string = input("Introduceti orice string format din mai multe cuvinte: ")
print(string_inversat(string))