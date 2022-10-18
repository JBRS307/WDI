#Test czy liczba jest pierwsza
from math import isqrt

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True

    i = 5
    while i <= isqrt(n):
        if n%i == 0:
            return False
        i+=2
        if n%i == 0:
            return False
        i+=4

    return True
#===========================================================
if __name__ == "__main__":
    n = int(input().strip())
    print(isPrime(n))
