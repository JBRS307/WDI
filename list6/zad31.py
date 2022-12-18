from os import system


subset_sum = 0
#=====================================================

def prime_fact(n):
    res = [0]*20
    res_i = 0

    if n%2 == 0:
        res[res_i] = 2
        res_i += 1
        while n%2 == 0:
            n //= 2
        
    if n%3 == 0:
        res[res_i] = 3
        res_i += 1
        while n%3 == 0:
            n //= 3
    
    i = 5
    while n != 1:
        if n%i == 0:
            res[res_i] = i
            res_i += 1
            while n%i == 0:
                n //= i
        i += 2

        if n%i == 0:
            res[res_i] = i
            res_i += 1
            while n%i == 0:
                n //= i
        i += 4

    return res
#=====================================================

def sum_factors_rec(n, factors, i=0, prod=1):
    global subset_sum
    
    if i >= len(factors) or factors[i] == 0:
        if prod != 1:
            subset_sum += prod
        return
    
    sum_factors_rec(n, factors, i+1, prod*factors[i])
    sum_factors_rec(n, factors, i+1, prod)
#-----------------------------------------------------

def sum_factors(n):
    global subset_sum
    factors = prime_fact(n)
    sum_factors_rec(n, factors)

    return subset_sum
#=====================================================

if __name__ == "__main__":
    system("clear")

    n = int(input())

    print(sum_factors(n))