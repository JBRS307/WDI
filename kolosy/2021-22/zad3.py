from os import system
from random import randrange


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#-----------------------------------------------------

def gcf(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a%b
    
    return a
#=====================================================

def rook1_rec(arr, leng, row, col, moves_made=0):
    min_moves = float('inf')
    if row == leng-1 and col == leng-1:
        return moves_made
    
    for i in range(1, leng-col):
        if gcf(arr[row][col], arr[row][col+i]) == 1:
            moves = rook1_rec(arr, leng, row, col+i, moves_made+1)
            min_moves = min(min_moves, moves)
    
    for i in range(1, leng-row):
        if gcf(arr[row][col], arr[row+i][col]) == 1:
            moves = rook1_rec(arr, leng, row+i, col, moves_made+1)
            min_moves = min(min_moves, moves)
    
    return min_moves
#-----------------------------------------------------

def rook2_rec(arr, leng, row, col, moves_made=0):
    min_moves = float('inf')
    if row == leng-1 and col == 0:
        return moves_made
    
    for i in range(1, leng-row):
        if gcf(arr[row][col], arr[row+i][col]) == 1:
            moves = rook2_rec(arr, leng, row+i, col, moves_made+1)
            min_moves = min(min_moves, moves)
        
    for i in range(1, col+1):
        if gcf(arr[row][col], arr[row][col-i]) == 1:
            moves = rook2_rec(arr, leng, row, col-i, moves_made+1)
            min_moves = min(min_moves, moves)
    
    return min_moves
#-----------------------------------------------------

def start_race(arr):
    leng = len(arr)
    rook1 = rook1_rec(arr, leng, 0, 0)
    rook2 = rook2_rec(arr, leng, 0, leng-1)

    return 1 if rook1 < rook2 else 2 if rook2 < rook1 else 0
#=====================================================

if __name__ == "__main__":
    system("clear")

    # print(gcf(101, 7))

    # arr = [[4, 4, 4, 3],
    #        [4, 4, 4, 6],
    #        [4, 4, 4, 6],
    #        [3, 6, 6, 2]]

    n, k = map(int, input("Rozmiar, zakres: ").strip().split())
    arr = [[randrange(2, k+1) for _ in range(n)] for _ in range(n)]
    system("clear")

    print_arr(arr)
    print()
    print(start_race(arr))