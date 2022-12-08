from os import system
from math import log10, isqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True
#-----------------------------------------------------

def divide(num, pieces = 0, digits = 0):
    if num == 0:
        if is_prime(pieces):
            return True
        return False
    
    leng = int(log10(num))+1

    for i in range(1, leng+1):
        piece = num // 10**(leng-i)
        if is_prime(piece):
            if divide(num%(10**(leng-i)), pieces+1, digits+i):
                return True
    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    n = int(input())

    print(divide(n))