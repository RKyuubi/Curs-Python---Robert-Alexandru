angajati = ['Maria', 'Marius', 'Andrei', 'Bianca', 'Bogdan', 'Ana', 'Mihai']
card_combustibil = ['Maria', 'Andrei']
abonament_sala = ['Maria', 'Andrei', 'Mihai']

# set_1 = set()
# set_2 = set()
# for angajat in angajati:
#     if angajat in card_combustibil and angajat in abonament_sala:
#         set_1.add(angajat)
# print (set_1)
#
# for angajat in angajati:
#     if angajat not in card_combustibil and angajat not in abonament_sala:
#         set_2.add(angajat)
# print (set_2)

set_angajati = set(angajati)
set_card_combustibila = set(card_combustibil)
set_abonament_sala = set(abonament_sala)

set_card_abon = set_card_combustibila.intersection(abonament_sala)
print(set_card_abon)

set_nocard_noabon = set_angajati.difference(set_card_combustibila | set_abonament_sala)
print(set_nocard_noabon)