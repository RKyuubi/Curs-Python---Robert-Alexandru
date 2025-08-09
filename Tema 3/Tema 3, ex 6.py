import math

cateta_1 = float(input("Introduceti cateta 1:"))
cateta_2 = float(input("Introduceti cateta 2:"))

a = cateta_1
b = cateta_2
c = math.sqrt((a * a) + (b * b))

ipotenuza = c

print(f"Ipotenuza este: {ipotenuza:.2f}")
