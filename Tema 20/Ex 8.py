if __name__ == "__main__":
    sir_caractere = "abcdefghijklmnopqrstuvwxyz"
    gen_sir = (x for x in sir_caractere)
    for x in gen_sir:
        print(x)

    # print(list(gen_sir)) daca se doreste printarea intr-o lista a fiecarui caracter

