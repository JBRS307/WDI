#Czy na elementach tablicy o indeksach z ciągu fib są
#same liczby złożone? Czy spośród pozostałych jest chociaż
#jedna pierwsza

from random import randrange


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
def fib(a, b, n, arr = [0]):
    if b < n:
        arr.append(b)
        return fib(b, a+b, n, arr)
    
    return tuple(arr)
#-----------------------------------------------------
def checkCondition(arr, n, arrFib):
    for i in arrFib:
        if isPrime(arr[i]):
            return False
    
    for j in range(n):
        if j not in arrFib:
            if isPrime(arr[j]):
                return True
    
    return False
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))
    k = int(input("Zakres: "))

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [4, 4, 4, 4, 3, 4, 4, 4, 4, 4]
    
    print(*arr)
    # print(checkCondition(arr, 10, fib(0, 1, 10)))
    # print(fib(0, 1, 150))
    print(checkCondition(arr, n, fib(0, 1, n)))