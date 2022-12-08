#Interpretacja - jeśli obie wieże szachują jedno pole
#szach liczy się wtedy pojedynczo.

from os import system
from random import randrange


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#=====================================================

def sum_col(leng, arr, row, col):
    res = 0
    for i in range(leng):
        res += arr[i][col]
    
    res -= arr[row][col]
    return res
#-----------------------------------------------------

def sum_row(leng, arr, row, col): #Wiem, że można użyć funkcji sum, ale chciałem zrobić to sam
    res = 0
    for i in range(leng):
        res += arr[row][i]

    res -= arr[row][col]
    return res
#-----------------------------------------------------

def chess(arr):
    leng = len(arr)

    positions = ()
    max_sum = 0
    for row_1 in range(leng):
        for col_1 in range(leng):
            checked_sum = sum_row(leng, arr, row_1, col_1) + sum_col(leng, arr, row_1, col_1)
            for row_2 in range(row_1, leng):
                if row_1 == row_2:
                    for col_2 in range(col_1+1, leng):
                        temp_sum = checked_sum + sum_col(leng, arr, row_2, col_2)
                        temp_sum -= (arr[row_1][col_1] + arr[row_2][col_2])
                        if temp_sum > max_sum:
                            positions = (row_1, col_1, row_2, col_2)
                            max_sum = temp_sum
                else:
                    for col_2 in range(leng):
                        if col_1 == col_2:
                            temp_sum = checked_sum + sum_row(leng, arr, row_2, col_2)
                            temp_sum -= (arr[row_1][col_1] + arr[row_2][col_2])
                            if temp_sum > max_sum:
                                positions = (row_1, col_1, row_2, col_2)
                                max_sum = temp_sum
                        else:
                            temp_sum = checked_sum + sum_row(leng, arr, row_2, col_2) + \
                                                     sum_col(leng, arr, row_2, col_2)
                            
                            temp_sum -= (arr[row_2][col_1] + arr[row_1][col_2])
                            if temp_sum > max_sum:
                                positions = (row_1, col_1, row_2, col_2)
                                max_sum = temp_sum

    
    return positions, max_sum
#=====================================================

if __name__ == "__main__":
    system("clear")

    # n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    # arr = [[randrange(-k, k+1) for _ in range(n)] for _ in range(n)]
    # arr = [[4,0,2],[3,0,0],[6,5,3]]
    arr = [[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]

    print_arr(arr)
    print(chess(arr))

    