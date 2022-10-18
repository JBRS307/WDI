# Wypisz podzielniki liczby

from math import isqrt

def findDiv(n):
    for i in range(1, isqrt(n)+1):
        if n%i == 0:
            print(i, end=" ")
            j = n//i
            if j != i:
                print(j, end=" ")
    print()
#=============================================
if __name__ == "__main__":
    n = int(input())
    findDiv(n)
    