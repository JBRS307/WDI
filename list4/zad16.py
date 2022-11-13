from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def prime_digs(n):
    primes = (2, 3, 5, 7)
    while n != 0:
        if n%10 not in primes:
            return False
        n //= 10
    
    return True
#-----------------------------------------------------

def check_arr(arr):
    leng = len(arr)
    cols = [False]*leng

    for line in arr:
        flag = False
        for j in range(leng):
            if prime_digs(line[j]):
                cols[j] = True
                flag = True
        if not flag:
            return False
    
    return not(False in cols)
#=====================================================

if __name__ == "__main__":
    # n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    # arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    arr = [[2, 2, 2],
           [1, 2, 2],
           [1, 2, 2]]

    print_arr(arr)

    print(check_arr(arr))