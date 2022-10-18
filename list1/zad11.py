#Zaprzyjaźnione mniejsze niż 1_000_000

from math import isqrt

def factSum(n, test):
    summ = 1

    i = 2
    root = isqrt(n)
    while i <= root:
        if summ > test:
            return False
        if n%i == 0:
            summ += i
            j = n//i
            if j != i:
                summ += j
        i+=1
    
    if summ == test:
        return True
    return False
#-----------------------------------------------------
def amicable():
    for i in range(1, 1_000_000):
        for j in range(i+1, (i+i if i+i < 1_000_000 else 1_000_000)):
            if factSum(i, j) and factSum(j, i):
                print(i, j)
#=====================================================
if __name__ == "__main__":
    amicable()