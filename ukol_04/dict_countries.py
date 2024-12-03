# Jako cvičení máte zadaný dict countries:
countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}
print(countries)

# ukol_A
# převtraťte klíče a hodnoty v novém dict cities:
# countries_name = {
#     "Česko": "CZ",
#     "Slovensko": "SK",
#     "Německo": "DE",
#     "Rakousko": "AT",
#     "Polsko": "PL",
# }
''' 
# 1. řešení
countries_name = {}
for k, v in countries.items():
    countries_name[v] = k
print(countries_name)


# 2. řešení
countries_name = {v: k for k, v in countries.items()}
print(countries_name)
'''
# 3. řešení
for k, v in countries.items():
    print(f"'{v}': '{k}'")


# ukol_B
#zjistete počet znaků pro každý stát
#countries_len = {
#    "CZ": 5,
#    "SK": 9,
#    "DE": 7,
#    "AT": 8,
#    "PL": 6,
#}
'''
# 1. řešení
countries_len = {}
for k, v in countries.items():
    countries_len[k] = len(v)
print(countries_len)


# 2. řešení
countries_len = {k: len(v) for k, v in countries.items()}
print(countries_len)
'''
# 3. řešení
for k, v in countries.items():
    print(f"'{k}': {len(v)}")