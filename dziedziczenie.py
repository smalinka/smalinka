
class Zwierze:
    def __init__(self, ilosc_nog, waga, glos):
        self.ilosc_nog = ilosc_nog
        self.waga = waga
        self.glos = glos

    def daj_glos(self):
        print(self.glos)

    def ustaw_gatunek(self, gatunek):
        self.gatunek = gatunek


class Pies(Zwierze):

    def daj_glos(self):
        print("Wrrrr", end=" ")
        super().daj_glos()


class Owczarek(Zwierze):

    def __init__(self, gatunek, glos):
        self.gatunek = gatunek
        self.glos = glos

    def daj_glos(self):
        print("GRRRRR", end=" ")
        super(Owczarek, self).daj_glos()


class OwczarekNiemiecki(Pies, Owczarek):
    pass

rex = Pies(4, 30, 'hauhau')
zwierze = Zwierze(2, 50, 'krakra')
zwierze.daj_glos()
rex.daj_glos()
rex.ustaw_gatunek('pies')
print(rex.gatunek)

owczarek = Owczarek(100, "HAUHAU")
owczarek.daj_glos()

owczniem = OwczarekNiemiecki('owczarek niemiecki', 'HAŁ hał')
owczniem.daj_glos()
