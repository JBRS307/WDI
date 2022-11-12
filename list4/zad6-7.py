#Tablice T1[N][N] i T2[M], M = N*N
#W pierwszej tablicy w wierszach linie są uporządkowane niemalejąco
#Przypisujemy tak, żeby liczby

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

def merge_arr(arr):
    leng = len(arr)
    res = [0] * (leng*leng)
    res_i = 0
    col_index = [0] * leng

    counter = 0

    while counter < leng:
        counter = 0
        min_element = float('inf')
        min_index = 0
        for i in range(leng):
            if col_index[i] == leng:
                counter += 1
            else:
                if arr[i][col_index[i]] < min_element:
                    min_element = arr[i][col_index[i]]
                    min_index = i
        
        if min_element not in res and counter != leng:
            res[res_i] = min_element
            res_i += 1
        col_index[min_index] += 1
    
    return res
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = create_arr(n, k)

    print_arr(arr)
    print(merge_arr(arr))