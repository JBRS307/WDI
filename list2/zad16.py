#Liczby Smitha mniejsze niż 1_000_000

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2

        if n%i == 0:
            return False
        i += 4
    
    return True
#-----------------------------------------------------
def sumDigit(n):
    res = 0
    while n > 0:
        res += n%10
        n //= 10
    return res
#-----------------------------------------------------
def primeFactors(n, i):
    res = 0
    while n%i == 0:
        res += sumDigit(i)
        n //= i
    return n, res
#-----------------------------------------------------
def primeFactSum(n):
    res = 0
    while n%2 == 0:
        res += 2
        n //= 2
    
    while n%3 == 0:
        res += 3
        n //= 3
    
    i = 5
    while True:
        if n <= 1:
            break
        
        n, temp = primeFactors(n, i)
        res += temp
        i += 2
        
        if n <= 1:
            break
        
        n, temp = primeFactors(n, i)
        res += temp
        i += 4
    
    return res
#-----------------------------------------------------
def smith():
    for n in range(1, 1_000_000):
        if primeFactSum(n) == sumDigit(n) and not isPrime(n):
            print(n, end=" ")
    print()
#=====================================================
if __name__ == "__main__":
    smith()