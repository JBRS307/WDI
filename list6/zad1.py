#Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
#co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
#cyfry.

from math import isqrt


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

def find_prime(n, res = 0, pos = 0, flag = False):
    if n == 0:
        if res > 9 and flag and is_prime(res):
            print(res)
        return
    
    find_prime(n//10, res, pos, True)
    find_prime(n//10, res + ((n%10)*(10**pos)), pos + 1, flag)
#=====================================================

if __name__ == "__main__":
    n = int(input())

    find_prime(n)