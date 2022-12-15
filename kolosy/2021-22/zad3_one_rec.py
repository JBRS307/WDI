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

def rook_rec(arr, leng, rook, row, col, moves_made=0):
    min_moves = float('inf')
    if rook == 0 and row == leng-1 and col == leng-1:
        return moves_made
    if rook == 1 and row == leng-1 and col == 0:
        return moves_made
    
    for i in range(1, leng):
        if not (0 <= col+(i*(-1)**rook) < leng):
            break
        if gcf(arr[row][col], arr[row][col+(i*(-1)**rook)]) == 1:
            moves = rook_rec(arr, leng, rook, row, col+(i*(-1)**rook), moves_made+1)
            min_moves = min(min_moves, moves)
    
    for i in range(1, leng-row):
        if gcf(arr[row][col], arr[row+i][col]) == 1:
            moves = rook_rec(arr, leng, rook, row+i, col, moves_made+1)
            min_moves = min(min_moves, moves)
    
    return min_moves
#-----------------------------------------------------

def start_race(arr):
    leng = len(arr)
    rook0 = rook_rec(arr, leng, 0, 0, 0)
    rook1 = rook_rec(arr, leng, 1, 0, leng-1)

    return 1 if rook0 < rook1 else 2 if rook1 < rook0 else 0
#=====================================================

if __name__ == "__main__":
    system("clear")

    # print(gcf(101, 7))

    # arr = [[4, 4, 4, 2],
    #        [4, 4, 4, 6],
    #        [4, 4, 4, 6],
    #        [3, 6, 6, 2]]

    n, k = map(int, input("Rozmiar, zakres: ").strip().split())
    arr = [[randrange(2, k+1) for _ in range(n)] for _ in range(n)]
    system("clear")

    print_arr(arr)
    print()
    print(start_race(arr))