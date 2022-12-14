#Zakaz oddalania się nie oznacza, że są tylko 3 ruchy możliwe.
#Od celu oddalamy się wtedy, kiedy zwiększamy liczbę ruchów
#potrzebnych do osiągnięcia go, przez co ruch w lewo czy
#w gorę w tej sytuacji nie zawsze oddala nas od prawego narożnika.

#Nie wiedziałem o co chodzi z liczbami od 0 do 7, więc ruchy
#zrobiłem tekstowo.

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
def find_route(row, col, dest_row, dest_col, been_on, route):
    global arr
    if row == dest_row and col == dest_col:
        return True, route
    
    been_on[row][col] = True
    
    dist = max(abs(dest_row - row), abs(dest_col - col))

    row_changes = (-1, 0, 1)
    col_changes = (-1, 0, 1)

    for row_ch in row_changes:
        for col_ch in col_changes:
            if (row_ch != 0 or col_ch != 0):
                new_row = row+row_ch
                new_col = col+col_ch
                if 0 <= new_row <= 7 and 0 <= new_col <= 7 and not been_on[new_row][new_col]:
                    if abs(dest_row - new_row) <= dist and abs(dest_col - new_col) <= dist:
                        if arr[row][col]%10 < first(arr[new_row][new_col]):
                            match (row_ch, col_ch):
                                case (-1, -1): #1
                                    route.append("upper left")
                                case (0, -1): #2
                                    route.append("left")
                                case (1, -1): #3
                                    route.append("lower left")
                                case (1, 0): #4
                                    route.append("down")
                                case (1, 1): #5
                                    route.append("lower right")
                                case (0, 1): #6
                                    route.append("right")
                                case (-1, 1): #7
                                    route.append("upper right")
                                case (-1, 0): #8
                                    route.append("up")

                            if find_route(new_row, new_col, dest_row, dest_col, been_on, route):
                                return True, route
    
    been_on[row][col] = False
    if len(route) >= 1:
        route.pop()
    
    return False
#-----------------------------------------------------

def start_route(row, col):
    print("Lewy gorny:", find_route(row, col, 0, 0, [[False]*8 for _ in range(8)], []))
    print("Prawy gorny:", find_route(row, col, 0, 7, [[False]*8 for _ in range(8)], []))
    print("Prawy dolny:", find_route(row, col, 7, 7, [[False]*8 for _ in range(8)], []))
    print("Lewy dolny:", find_route(row, col, 7, 0, [[False]*8 for _ in range(8)], []))

#=====================================================

if __name__ == "__main__":
    system("clear")

    # print(first(143%10))

    print_arr()
    row, col = map(int, input('\n').strip().split())
    # dest_row, dest_col = map(int, input().strip().split())

    # print("Lewy gorny:", find_route(row, col, 0, 0))
    # print("Prawy gorny:", find_route(row, col, 0, 7))
    # print("Prawy dolny:", find_route(row, col, 7, 7))
    # print("Lewy dolny:", find_route(row, col, 7, 0))

    start_route(row, col)
