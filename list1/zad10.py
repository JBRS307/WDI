# Doskonałe mniejsze niż 1_000_000

from math import isqrt

def isPerfect(n):
    summ = 1
    
    for i in range(2, isqrt(n)+1):
        if n%i == 0:
            summ += i
            j = n//i
            if j != i:
                summ += j
    
    if summ == n:
        return True
    return False
#-----------------------------------------------------
def perfects():
    for i in range(1, 1_000_000):
        if isPerfect(i):
            print(i, end=" ")
    print()
#=====================================================
if __name__ == "__main__":
    perfects()