from os import system


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end='\t')
        print()
#-----------------------------------------------------

def fill_knight(board, leng, x, y, n = 1):
    # moves = ((+2, +1), (+2, -1), (-2, +1), (-2, -1),
    #          (+1, +2), (+1, -2), (-1, +2), (-1, -2))

    ver = (2, 2, -2, -2, 1, 1, -1, -1)
    hor = (1, -1, 1, -1, 2, -2, 2, -2)

    # if board[x][y] == 0:
    board[x][y] = n
    # else:
    #     return False

    if n == leng*leng:
        return True
            
    # for move in moves:
    #     if x+move[0] >= 0 and x+move[0] < leng and y+move[1] >= 0 and y+move[1] < leng:
    #             stop = fill_knight(board, leng, x+move[0], y+move[1], n+1)
    #             if stop:
    #                 return True

    for i in range(8):
        if 0 <= x+ver[i] < len(board) and 0 <= y+hor[i] < len(board):
            if board[x+ver[i]][y+hor[i]] == 0:
                if fill_knight(board, leng, x+ver[i], y+hor[i], n+1):
                    return True
    
    board[x][y] = 0

    return False
#-----------------------------------------------------

def start(leng):
    board = [[0]*leng for _ in range(leng)]
    res = fill_knight(board, leng,  0, 0)
    return res, board
#=====================================================

if __name__ == "__main__":
    system("clear")

    leng = int(input())
    possible, board = start(leng)

    print_board(board)
    print(possible)