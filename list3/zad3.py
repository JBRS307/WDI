#Sito Eratostenesa

def sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False

    p = 2
    while p*p <= n:
        if primes[p] == True:
            for i in range(p*p, n, p):
                primes[i] = False
            
        p += 1
    
    return primes
#=====================================================
if __name__ == "__main__":
    n = int(input())

    primes = sieve(n)
    # counter = 0
    for i in range(n):
        if primes[i]:
            # counter += 1
            print(i, end=' ')
    
    print()