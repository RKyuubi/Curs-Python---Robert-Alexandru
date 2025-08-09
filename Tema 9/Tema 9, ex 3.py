# lista_loto = []
# for i in range (1,50):
#     lista_loto.append(i)
#
# set_loto = set(lista_loto)
#
# lista_6din49 = []
#
# while len(lista_6din49) < 6:
#     bila_extrasa = set_loto.pop()
#     lista_6din49.append(bila_extrasa)
#
# set_6din49 = set(lista_6din49)
# print(set_6din49)

set_loto = {(i, "test") for i in range (1,50)}

set_6din49 = set()

while len(set_6din49) < 6:
    bila_extrasa = set_loto.pop()
    set_6din49.add(bila_extrasa[0])

print(set_6din49)

