#je dán dict, která má klíč název státu a hodnotu počet obyvatel
#zjistěte průměrný počet obyvatel z těctho dat
#stát s nejvyšším počtem a nejnižším počtem

import numpy as np
import matplotlib.pyplot as plt

countries = {
    "Irsko": 4593100,
    "Chorvatsko": 4290612,
    "Moldavsko": 3559500,
    "Litva": 2941953,
    "Albánie": 2821977,
    "Slovensko": 5415949,
    "Norsko": 5109056,
    "Itálie": 59943933,
    "Španělsko": 46609700,
    "Ukrajina": 45426200,
    "Polsko": 38502396,
    "Mkedonie": 2062294,
    "Slovinsko": 2061963,
    "Lotyšsko": 2003900,
    "Kosovo": 1815606,
    "Estonsko": 1311870,
    "Rusko": 143700000,
    "Německo": 80619000,
    "Turecko": 76667864,
    "Francie": 65844000,
    "Velká Británie": 63705000,
    "Portugalsko": 10487289,
    "Maďarsko": 9906000,
    "Švédsko": 9651531,
    "Bělorusko": 9468100,
    "Rakousko": 8504850,
    "Švýcarsko": 8112200,
    "Bulharsko": 7282041,
    "Srbsko": 7181505,
    "Dánsko": 5627235,
    "Finsko": 5452821,
    "Rumunsko": 20121641,
    "Nizozemsko": 16842200,
    "Belgie": 11132269,
    "Řecko": 10815197,
    "Česko": 10513800,
}
# 1. řešení (numpy)
'''
print(f"Průměrný počet obyvatel: {np.mean(list(countries.values())).round(2)}")
print(f"Stát s nejvyšším počtem obyvatel: {max(countries, key=countries.get)}")
print(f"Stát s nejnižším počtem obyvatel: {min(countries, key=countries.get)}")
'''

#2. řešení (s for cyklem)
avg = sum(countries.values()) / len(countries)
print(f"Průměrný počet obyvatel: {avg.__round__(2)}")
for k, v in countries.items():
    if v == max(countries.values()):
        print(f"Stát s nejvyšším počtem obyvatel: {k}")
    if v == min(countries.values()):
        print(f"Stát s nejnižším počtem obyvatel: {k}")

# 3. řešení (s funkcí)
'''
def countries_avg():
    avg = sum(countries.values()) / len(countries)
    return avg
print(f"Průměrný počet obyvatel: {countries_avg().__round__(2)}")

def countries_max():
    max_country = max(countries, key=countries.get)
    return max_country
print(f"Stát s nejvyšším počtem obyvatel: {countries_max()}")

def countries_min():
    min_country = min(countries, key=countries.get)
    return min_country
print(f"Stát s nejnižším počtem obyvatel: {countries_min()}")
'''



