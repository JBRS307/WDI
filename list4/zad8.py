#Sprawdź czy istnieje ciąg geometryczny w kierunku "prawo-dół"

from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def from_first_column(arr, n):
    max_leng = 0
    for i in range(n-1):
        leng = 2
        quot = arr[i+1][1]/arr[i][0]
        col = 2
        for j in range(i+2, n):
            if arr[j][col]/arr[j-1][col-1] == quot:
                leng += 1
                col += 1
            else:
                max_leng = max(leng, max_leng)
                quot = arr[j][col]/arr[j-1][col-1]
                leng = 2
                col += 1
        
        max_leng = max(leng, max_leng)
    
    return max_leng
#-----------------------------------------------------

def from_first_row(arr, n):
    max_leng = 0
    for i in range(1, n-1):
        leng = 2
        quot = arr[1][i+1]/arr[0][i]
        row = 2
        for j in range(i+2, n):
            if arr[row][j]/arr[row-1][j-1] == quot:
                leng += 1
                row += 1
            else:
                max_leng = max(leng, max_leng)
                quot = arr[row][j]/arr[row-1][j-1]
                leng = 2
                row += 1
        
        max_leng = max(leng, max_leng)
    
    return max_leng
#-----------------------------------------------------

def find_seq(arr, n):
    max_leng =  max(from_first_column(arr, n), from_first_row(arr, n))

    return max_leng if max_leng > 2 else 0
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)
    print()
    print(find_seq(arr, n))

    # arr = [[1, 1, 3, 4],
    #        [1, 2, 2, 4],
    #        [1, 2, 4, 4],
    #        [1, 2, 3, 8]]
    
    # print(from_first_column(arr, 4))
    # print(from_first_row(arr, 4))

    # print(find_seq(arr, 4))