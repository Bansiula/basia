# -*- coding: utf-8 -*-

#def pomnoz_przez_2_for(lista_liczb):
#    nowa_lista = []
#    for liczba in lista_liczb:
#        nowa_lista.append(liczba * 2)
#    return nowa_lista
#
#lista_liczb = [1, 2, 3, 4, 5]
#wynik = pomnoz_przez_2_for(lista_liczb)
#print(wynik)


def pomnoz_przez_2_list_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]

lista_liczb = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_2_list_skladana(lista_liczb)
print(wynik)

