from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def is_prime_digit(n):
    primes = (2, 3, 5, 7)

    while n != 0:
        if n%10 in primes:
            return True
        n //= 10
    
    return False
#-----------------------------------------------------

def check_arr(arr):
    for line in arr:
        for num in line:
            if not is_prime_digit(num):
                return False
    
    return True
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)
    
    print(check_arr(arr))