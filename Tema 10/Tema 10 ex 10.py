def printeaza_piramida (n):
    """
    Printează o formă triunghiulară cu n rânduri.
    Fiecare rând are cu 2 asteriscuri mai mult decât precedentul, centrate.
    """
    if not isinstance(n, int) or n<=0:
        print ("Introdu un numar intreg pozitiv pentru numarul de randuri al piramidei: ")
        return


    for i in range (1, n+1):
        numar_astericsuri = (2*i) - 1
        print ("*" * numar_astericsuri)

n = input ("Introdu numarul de randuri: ")
printeaza_piramida(int(n))