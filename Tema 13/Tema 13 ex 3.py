def scrie_fisier_output():
    try:
        string_cerut = input("Scrie orice string:")
        with open("Fisier3.txt", "w") as fisier:
            fisier.write(string_cerut)
    except Exception as e:
        print(f"A aparut o erare: {e}")

if __name__ == "__main__":
    scrie_fisier_output()