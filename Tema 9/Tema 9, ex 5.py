text = input("Introduceti orice text:")

vocale = ("aeiouAEIOU")
set_vocale = set(vocale)
consoane = ("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
set_consoane = set(consoane)

set_text = set(text)
print (set_text & set_consoane)
print (set_text & set_vocale)


