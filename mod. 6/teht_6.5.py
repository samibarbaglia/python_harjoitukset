# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki
# parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
# listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poista(paramLista):
    lista = []
    for n in paramLista:
        if n % 2 == 0:
            lista.append(n)
    return lista


lista = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10, 45, 24, 67, 75, 522, 54, 8501, 1000, 80, 57, 37, 39, 31, 33, 28]
lista2 = [73, 8, 53, 532, 896, 467]
print(lista)
print(poista(lista))
print(lista2)
print(poista(lista2))
