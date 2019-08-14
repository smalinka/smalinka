napis = "Ajvgfj"
if napis.isnumeric:
    print(False)
else:
    print(True)



a = "ala ma kota"
a = a.replace('ala', 'agnieszka'), ('kota', 'psa')
print(a)



a = "10, 9, 8, 7, 3"
print(tuple(a.split(", ")))


plik="C:users:aa:pli.k.txt"
print(plik.split(".")[-1])





a = "1, 2, 3, 4, 5"
a.replace(", ", "+")

b = {"a1":"liczbaa1","a2":"liczbaa2"}

a = {"klucz":"liczba","klucz1":"liczba1"}
a["klucz2"]=123
print(a["klucz1"])

a.update({"klucz10":"liczba10"})
print(a)
