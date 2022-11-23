from os import system
stop = False


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = '\t')
        print()
#-----------------------------------------------------

def check_move(board, x, y, move_i):
    # moves = ((+2, +1), (+2, -1), (-2, +1), (-2, -1),
    #          (+1, +2), (+1, -2), (-1, +2), (-1, -2))
    
    # new_x = x+moves[move_i][0]
    # new_y = y+moves[move_i][1]

    ver = [2, 1, -1, -2, -2, -1, 1, 2]
    hor = [1, 2, 2, 1, -1, -2, -2, -1]

    new_x = x + ver[move_i]
    new_y = y + hor[move_i]

    if 0 <= new_x < len(board) and 0 <= new_y < len(board):
        if board[new_x][new_y] == 0:
            return (new_x, new_y)
    return None
#-----------------------------------------------------

def fill_knight(board, x=0, y=0, n=1):
    global stop
    if stop:
        return
    
    board[x][y] = n
    if n == len(board)**2:
        stop = True
        print_board(board)

    for i in range(8):
        new_pos = check_move(board, x, y, i)
        if new_pos is not None:
            fill_knight(board, new_pos[0], new_pos[1], n+1)
    
    board[x][y] = 0
#=====================================================

if __name__ == "__main__":
    system("clear")

    leng = int(input())

    # stop = False

    board = [[0]*leng for _ in range(leng)]

    fill_knight(board)
    # print_board(board)