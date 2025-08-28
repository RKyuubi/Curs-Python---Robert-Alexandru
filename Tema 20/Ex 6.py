def decorator_mesaj (function):
    def wrapper(*args, **kwargs):
        for _ in range (3):
            function(*args, **kwargs)
    return wrapper

@decorator_mesaj
def salut(nume):
    print(f'Salut {nume}!')

if __name__ == '__main__':
    salut("Robert")
