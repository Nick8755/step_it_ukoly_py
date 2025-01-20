'''
Vytvořte simulaci nákupního košíku:

chceme vytvořit nakupní košík pro eshop
do kterého můžeme přidávat zboží

košík by měl umět:
- přidat zboží
- odebrat zboží
- vypočítat celkovou sumu
- vytisknout fakturu pomocí printu

Ostatní implementaci a návh nechám na vás
Snažte se, aby to bylo jednoduché a přímočaré na použití

soubor pojmenujte 16_kosik.py
'''
# fhffggfggf
class Zbozi:
    counter = 0
    def __init__(self, nazev: str, cena: float): # produkty v e-shopu
        self.__class__.counter += 1 # vypocet ID produktu
        self.id = self.__class__.counter # prirazeni ID
        self.nazev = nazev
        self.cena = cena

class Kosik:
    def __init__(self):
        self.nakup = {}

    def pridej_zbozi(self, zbozi: Zbozi, pocet: int=1):
        if zbozi.id in self.nakup: #kontrola zda je zbozi v kosiku
            self.nakup[zbozi] += pocet # pokud ano, prida se pocet
        else:
            self.nakup[zbozi] = pocet

    def odeber_zbozi(self, zbozi: Zbozi, pocet: int=1):
        if zbozi in self.nakup: # kontrola zda je zbozi v kosiku
            self.nakup[zbozi] -= pocet # pokud ano, odebere se pocet
            if self.nakup[zbozi] <= 0:
                del self.nakup[zbozi]

    def celkova_suma(self) -> float:
        suma = 0
        for zbozi, pocet in self.nakup.items():
            suma += zbozi.cena * pocet
        return suma

    def vytiskni_fakturu(self):
        for zbozi, pocet in self.nakup.items():
            mezisoucet = zbozi.cena * pocet
            print(f"{zbozi.nazev} x {pocet}ks = {mezisoucet} Kč")
        print(f"Celkova suma: {self.celkova_suma()} Kč")



if __name__ == "__main__":
    kosik = Kosik()

    kafe = Zbozi("Kafe", 100)
    pivo = Zbozi("Pivo", 50)
    kebab = Zbozi("Kebab", 120)

    kosik.pridej_zbozi(kafe, 2)
    kosik.pridej_zbozi(pivo)

    kosik.vytiskni_fakturu()