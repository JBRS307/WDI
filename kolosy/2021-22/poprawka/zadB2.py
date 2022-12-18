from os import system
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
#=====================================================

def rpg_rec(arr, leng, room=0, inv=0):
    if room >= leng:
        if inv == 0:
            return True
        return False
    
    for i in range(-inv, 7-inv):
        left = arr[room] - i
        if is_prime(left):
            if rpg_rec(arr, leng, room+1, inv+i):
                return True
    
    return False
#-----------------------------------------------------

def rpg(arr):
    leng = len(arr)
    return rpg_rec(arr, leng)
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [10, 20, 35]
    print(rpg(arr))