# -*- coding: utf-8 -*-
def wyswietl_co_drugi(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])

# Przykładowe użycie
lista_liczb = list(range(10))
wyswietl_co_drugi(lista_liczb)