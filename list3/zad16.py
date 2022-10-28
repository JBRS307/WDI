#Sprawdź czy w tablicy znajduje się dokładnie 1 element najmniejszy
#i dokładnie 1 element największy

from random import randrange


def oneMin(arr, n):
    mini = arr[0]
    flag = True

    for i in range(1, n):
        if arr[i] < mini:
            mini = arr[i]
            flag = True
        elif arr[i] == mini:
            flag = False
    
    return flag
#-----------------------------------------------------

def oneMax(arr, n):
    maxi = arr[0]
    flag = True

    for i in range(1, n):
        if arr[i] > maxi:
            maxi = arr[i]
            flag = True
        elif arr[i] == maxi:
            flag = False
    
    return flag
#-----------------------------------------------------

def checkCondition(arr, n):
    return oneMin(arr, n) and oneMax(arr, n)
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]

    print(*arr)
    print(checkCondition(arr, n))