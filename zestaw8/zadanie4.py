import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru
    Herona. Dlugosci bokow trojkata wynosza a, b, c."""

    if not(a+b>=c or a+c>=b or b+c>=a):
        raise ValueError("Z tych bokow nie da sie utworzyc trojkata")
    else:
        p = 0.5 * (a + b + c)
        return str(math.sqrt(-(p * (p - a) * (p - b) * (p - c))))

print( "Wynik to: ", heron(2,4,8))
