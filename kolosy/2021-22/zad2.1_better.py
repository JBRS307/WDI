from random import randrange
from math import isqrt


def is_prime(n):
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if not n%i or not n%(i+2):
            return False
    
    return True
#-----------------------------------------------------

def check(arr):
    prod = 0
    index = None

    for i, num in enumerate(arr):
        if is_prime(num):
            if prod == 0:
                prod = num
            else:
                prod *= num
        elif prod == num:
            index = i
    
    return index
#=====================================================
if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]

    print(arr, end="\n\n")
    print(check(arr))