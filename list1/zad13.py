# NWW trzech liczb

def primeFactorisation(n):
    pFactors = {}
    if n == 2:
        return {2:1}
    if n == 3:
        return {3:1}
    for i in range(2, n//2+1):
        count = 0
        while n%i == 0:
            n/=i
            count += 1
        if count > 0:
            pFactors[i] = count
    return pFactors
#=======================================
if __name__ == "__main__":
    #print(primeFactorisation(30))
    a, b, c = list(map(int, input().strip().split()))
    a = primeFactorisation(a)
    b = primeFactorisation(b)
    c = primeFactorisation(c)
    #print(a, b, c)
    