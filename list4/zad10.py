#Czy w każdej kolumnie i w każdym wierszu jest 0?

from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------
def check_zero(arr, n):
    zero_in_column = [False] * n
    for line in arr:
        flag = False
        for i in range(n):
            if line[i] == 0:
                flag = True
                zero_in_column[i] = True
        
        if not flag:
            return False
    
    if False in zero_in_column:
        return False
    return True
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(-k, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)
    print()
    print(check_zero(arr, n))

