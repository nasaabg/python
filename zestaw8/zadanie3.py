from random import random


def calc_pi(n=100):
    """Obliczanie liczby pi metoda Monte Carlo.
    n oznacza liczbe losowanych punktow."""

    a = 1.0 #bok kwadratu
    r = a/2.0 #promien kola
    liczba_trafien = 0

    for i in range(0, n):
        x = random()
        y = random()
        if((x*x) + (y*y)<=(r*r)):
            liczba_trafien += 1.0
    pi=(16 * liczba_trafien)/n
    return pi

print("Liczba PI wynosi ~",calc_pi(1000000))
