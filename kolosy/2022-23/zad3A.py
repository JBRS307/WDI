from os import system


def make_board(leng, pawns):
    res = [[0]*leng for _ in range(leng)]
    
    for i in range(leng):
        for j in range(leng):
            if (i, j) in pawns:
                res[i][j] = 1
    
    for line in res:
        for elem in line:
            print(elem, end='\t')
        print()
#-----------------------------------------------------
def rook_rec(leng, pawns, last_move, row=0, col=0, moves_made=0):
    if row == leng-1 and col == leng-1:
        return moves_made
    
    min_moves = float('inf')
    if last_move == "vert":
        for i in range(1, leng):
            if col+i >= leng or (row, col+i) in pawns:
                break
            moves = rook_rec(leng, pawns, "hor", row, col+i, moves_made+1)
            min_moves = min(moves, min_moves)
    
    if last_move == "hor":
        for i in range(1, leng):
            if row+i >= leng or (row+i, col) in pawns:
                break
            moves = rook_rec(leng, pawns, "vert", row+i, col, moves_made+1)
            min_moves = min(moves, min_moves)
    
    return min_moves
#-----------------------------------------------------

def rook(leng, pawns):
    moves = min(rook_rec(leng, pawns, "hor"), rook_rec(leng, pawns, "vert"))

    return moves if moves != float('inf') else None
#=====================================================

if __name__ == "__main__":
    system ("clear")

    leng = 5

    pawns = [(0, 1), (2, 0), (1, 2)]

    make_board(leng, pawns)
    print(rook(leng, pawns))
