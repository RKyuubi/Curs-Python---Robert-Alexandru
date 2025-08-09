for i in range (0, 1000):
    este_prim = True
    for d in range (2, i): # d=un divizor
        if i % d == 0:
            este_prim = False
            break
    if este_prim == True and i > 1:
        print (i)