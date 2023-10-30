# -*- coding: utf-8 -*-
def wyswietl_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)

# Przykładowe użycie
lista_liczb = list(range(10))
wyswietl_parzyste(lista_liczb)

