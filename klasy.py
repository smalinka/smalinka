
def funkcja(a):
    print('wywolano')

funkcja('1')

class Zwierze:

    def __init__(self, gatunek, wiek, glos):
        self.gatunek = gatunek
        self.wiek = wiek
        self.glos = glos

    def __str__(self):
        return f"Gatunek to {self.gatunek} ma {self.wiek} lat"

    def daj_glos(self, ilosc=1, *args, **kwargs):
        print(f"{self.gatunek} daje głos {self.glos*ilosc}")


# print(Zwierze)

pies = Zwierze("pies", 10, 'hau')
kot = Zwierze("kot", 5, 'miau')
# print(pies)
# print(pies.gatunek)
# print(pies.wiek)
pies.daj_glos(5)
# print(kot)
# print(kot.gatunek)
kot.daj_glos(10)

