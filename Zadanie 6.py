# -*- coding: utf-8 -*-

def przetworz_listy(lista1, lista2):
  
    polaczona_lista = lista1 + lista2

    polaczona_lista = list(set(polaczona_lista))
    
    polaczona_lista = [x**3 for x in polaczona_lista]
    
    return polaczona_lista

lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6, 7]

wynik = przetworz_listy(lista1, lista2)
print(wynik)