from os import system
from random import randrange


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#=====================================================

def gcf3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a

    a = a%c
    b = b%c
    if a == 0 and b == 0:
        return c
    if a == 0:
        a = b
    if b == 0:
        b = a
    
    return gcf3(a, b, c)
#-----------------------------------------------------

def compare(row1, col1, row2, col2, row3, col3, a, b, c):
    if (row1 != row2 and col1 != col2) or \
       (row2 != row3 and col2 != col3) or \
       (row3 != row1 and col3 != col1):
        if gcf3(a, b, c) == 1:
            return True
    return False
#-----------------------------------------------------

def triplets(arr):
    leng = len(arr)
    res = 0

    for row1 in range(leng):
        for col1 in range(leng):
            for row2 in range(row1, leng):
                for col2 in range(col1+1 if row1 == row2 else 0, leng):
                    for row3 in range(row2, leng):
                        for col3 in range(col2+1 if row2 == row3 else 0, leng):
                            if compare(row1, col1, row2, col2, row3, col3, arr[row1][col1], arr[row2][col2], arr[row3][col3]):
                                res += 1

    
    return res
#=====================================================

if __name__ == "__main__":
    system("clear")

    # print(gcf3(5, 3, 7))

    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)
    print(triplets(arr))