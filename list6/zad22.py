from os import system
from random import randrange
from math import isqrt
import sys


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

def check_jumps_rec(arr, i=0, jumps=0):
    if i == len(arr)-1:
        return True, jumps
    
    for k in range(2, len(arr)-i):
        if i+k <= len(arr):
            if k < arr[i] and arr[i]%k == 0 and is_prime(k):
                possible, total_jumps = check_jumps_rec(arr, i+k, jumps+1)
                if possible:
                    return True, total_jumps
    
    return False, -1

#=====================================================

if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    system("clear")

    n, k = map(int, input("Rozmiar, zakres: ").strip().split())
    system("clear")
    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [21, 20, 30, 12, 14, 8, 12, 23, 7, 7]
    # arr = [6,5,1,2,4,3]

    print(*arr, end="\n\n")
    print(check_jumps_rec(arr))
    