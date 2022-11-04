#Wypisz wszystkie liczby z kwadratu, rosnąco

from random import randrange


def create_arr(n, k):
    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i].sort()
    
    return arr
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def task(arr, n, k):
    res = [0]*(n*n)
    temp = [0]*(k+1)

    for line in arr:
        for num in line:
            temp[num] += 1
    
    res_i = 0
    for i in range(len(temp)):
        if temp[i] != 0:
            res[res_i] = i
            res_i += 1
    
    return res
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = create_arr(n, k)
    print_arr(arr)
    print()
    print(task(arr, n, k))