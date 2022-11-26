#Zakaz oddalania się nie oznacza, że są tylko 3 ruchy możliwe.
#Od celu oddalamy się wtedy, kiedy zwiększamy liczbę ruchów
#potrzebnych do osiągnięcia go, przez co ruch w lewo czy
#w gorę w tej sytuacji nie zawsze oddala nas od prawego narożnika.

from random import randrange
from os import system
from math import log10


arr = [[randrange(1, 101) for _ in range(8)] for _ in range(8)]
# arr = [[47, 25, 23], [81, 13, 91], [49, 64, 93]] #testy, zmienić 7 na 2 w kodzie
#=====================================================

def print_arr():
    global arr
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#=====================================================

def first(n):
    return n//(10**int(log10(n)))
#-----------------------------------------------------
def find_route(row, col, been_on=[[False]*8 for _ in range(8)]):
    global arr
    if row == 7 and col == 7:
        return True
    
    been_on[row][col] = True
    
    dist = max(7-col, 7-row)

    row_changes = (-1, 0, 1)
    col_changes = (-1, 0, 1)

    for row_ch in row_changes:
        for col_ch in col_changes:
            if (row_ch != 0 or col_ch != 0) and (row_ch != -1 or col_ch != -1):
                new_row = row+row_ch
                new_col = col+col_ch
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and not been_on[new_row][new_col]:
                    if 7-new_row <= dist and 7-new_col <= dist:
                        if arr[row][col]%10 < first(arr[new_row][new_col]):
                            if find_route(new_row, new_col, been_on):
                                return True
    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    print_arr()
    row, col = map(int, input('\n').strip().split())

    print(find_route(row, col))

    # print(first(42))

