def decorator_mesaj (function):
    def wrapper(*args, **kwargs):
        print("Acesta este un mesaj folosit inainte de apelarea functiei")
        rezultat = function(*args, **kwargs)
        print("Acesta este un mesaj folosit dupa apelarea functiei")
        return rezultat
    return wrapper

@decorator_mesaj
def salut(nume):
    print(f'Salut {nume}!')

if __name__ == '__main__':
    salut("Robert")
