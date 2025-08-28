def tip_argumente (function):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                print(f'Argument "{arg}" is not an integer')
                return
        return function(*args, **kwargs)
    return wrapper

@tip_argumente
def aduna_numere(a,b,c):
    return a+b+c

if __name__ == '__main__':
    print ("Prima verificare")
    rezultat_valid= aduna_numere(10, 10, 20)
    print(f"{rezultat_valid}")

    print ("\nA doua verificare")
    aduna_numere("Robert",20,30)

    print ("\nA treia verificare")
    aduna_numere(10, 2.4, 4)

