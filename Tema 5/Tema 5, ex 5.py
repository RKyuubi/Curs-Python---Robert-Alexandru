text = input("Introduceti orice text:")

vocale = ("aeiouAEIOU")
consoane = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
numar_vocale = 0
numar_consoane = 0
for char in (text):
    if char.lower() in vocale:
        numar_vocale += 1
    elif char.lower() in consoane:
        numar_consoane+= 1

print("Numarul vocalelor este:", numar_vocale)
print("Numarul consoane  este:", numar_consoane)