'''
kde bude funkce check_phone_number,
která dokáže zkontrolovat,
zda zadaný text je validní telefonní číslo

příklady validních čísel:

777777777
777 777 777
+420777777777
+420 777 777 777

pro všechny tyto formáty vrátí True, jinak False

print(check_phone_number('test')) # -> False
print(check_phone_number('608 192 292')) # -> True (True pro všechny formáty uvedené výše)
print(check_phone_number('608 192 292...')) # -> False
print(check_phone_number('+420777598763')) # -> True
print(check_phone_number('+420 777 598 763')) # -> True

'''

import re

def check_phone_number(phone_number: str) -> bool:
    pattern = re.compile(r'^(\+420)?\s?\d{3}\s?\d{3}\s?\d{3}$')
     # přidáme format (+420) 777 77 77 77
    pattern_a = re.compile(r'^(\+420)?\s?\d{3}\s?\d{2}\s?\d{2}\s?\d{2}$')
    return bool(pattern.match(phone_number)) or bool(pattern_a.match(phone_number))

# zadame telefonni cislo
phone_number = input("Zadejte telefonní číslo: ")
# zavolame funkci check_phone_number a vypiseme vysledek
print(check_phone_number(phone_number))