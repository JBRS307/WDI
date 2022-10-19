#Zaprzyjaźnione mniejsze niż 1_000_000

from math import isqrt

def factSum(n):
    summ = 1

    i = 2
    root = isqrt(n)
    while i <= root:
        if n%i == 0:
            summ += i
            j = n//i
            if j != i:
                summ += j
        i+=1
    
    return summ
#-----------------------------------------------------
def amicable():
    for i in range(2, 1_000_000):
        j = factSum(i)
        if i > j and factSum(j) == i:
            print(i, j)
#=====================================================
if __name__ == "__main__":
    amicable()