# Test czy liczba jest pierwsza
from math import sqrt

def isPrime(n):
    if n == 2:
        return True
    if n <= 1:
        return False
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True
#===========================================================
if __name__ == "__main__":
    n = int(input().strip())
    print(isPrime(n))
