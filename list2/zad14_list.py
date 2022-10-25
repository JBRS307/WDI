#Ile liczb pierwszych można zbudować z dwóch liczb

from math import isqrt

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False

    i = 5
    while i <= isqrt(n):
        if n%i == 0:
            return False
        i += 2

        if n%i == 0:
            return False
        i += 4
    
    return True
#-----------------------------------------------------
def buildNum(a, b, len_a, len_b):
    newNum = list(a+b)
    counter = 0
    if isPrime(int(''.join(newNum))):
        counter += 1
    for _ in range(len_b):
        for i in range(len_a-1, -1, -1):
            newNum[i], newNum[i+1] = newNum[i+1], newNum[i]
            if isPrime(int(''.join(newNum))):
                counter += 1
        len_a += 1
    
    return counter
#=====================================================
if __name__ == "__main__":
    a, b = input().strip().split()
    print(buildNum(a, b, len(a), len(b)))
    