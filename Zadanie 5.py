# -*- coding: utf-8 -*-

def sprawdz_czy_zawiera(lista, wartosc):
    return wartosc in lista

lista = [1, 2, 3, 4, 5]
wartosc = 5

wynik = sprawdz_czy_zawiera(lista, wartosc)
print(wynik)

