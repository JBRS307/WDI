#Podaj kordy elementu, dla którego iloraz sumy kolumny
#do sumy wiersza jest największy

from random import randrange


def sum_rows(arr, n):
    res = [0]*n
    for i in range(n):
        for num in arr[i]:
            res[i] += num
    
    return res
#-----------------------------------------------------

def sum_columns(arr, n):
    res = [0]*n
    for line in arr:
        for i in range(n):
            res[i] += line[i]
    
    return res
#-----------------------------------------------------

def find_quot(rows, columns, n):
    
    max_elem = [0, 0]
    max_quot = 0

    for i in range(n):
        for j in range(n):
            quot = columns[j]/rows[i]
            if quot > max_quot:
                max_quot = quot
                max_elem[0], max_elem[1] = i, j
    
    return max_elem
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for i in range(n)] for j in range(n)]
    # arr = [[10, 10, 10], 
    #        [1, 100, 100], 
    #        [1, 100, 100]]

    print_arr(arr)
    row, column = find_quot(sum_rows(arr, n), sum_columns(arr, n), n)

    print("Row:", row)
    print("Column:", column)
