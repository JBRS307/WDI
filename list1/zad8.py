#Test czy liczba jest pierwsza
from math import isqrt

def isPrime(n):
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False

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
    n = int(input())
    print(isPrime(n))
