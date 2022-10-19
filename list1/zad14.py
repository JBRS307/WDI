#cosinus z szeregu Maclaurina

from math import factorial

def cos(x, n=100):
    res = 1
    i = 2
    sign = -1
    while i <= n:
        res += sign*((1/factorial(i))*(x**i))
        i += 2
        sign *= -1
    return res

#=====================================================
if __name__ == "__main__":
    x = float(input("Podaj przyblizona wartosc w radianach: "))
    print(cos(x))