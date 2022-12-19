from os import system


def check_move(board, leng, ignore, row, col):
    if not(0 <= row < leng and 0 <= col < leng):
        return False

    if board[row][col] or (row, col) in ignore:
        return False

    return True     
#-----------------------------------------------------

def knight_travel(board):
    leng = len(board)

    ver = (2, 1, 2, 1, -2, -1, -2, -1)
    hor = (1, 2, -1, -2, 1, 2, -1, -2)

    def rec(board, ignore, row, col):
        nonlocal leng, ver, hor
        if row == leng-1:
            return True
        
        for i in range(8):
            if check_move(board, leng, ignore, row+ver[i], col+hor[i]):
                if rec(board, [*ignore, (row, col)], row+ver[i], col+hor[i]):
                    return True
        
        return False
    #-----------------------------------------------------

    for i in range(4, min(21, leng)):
        if not board[0][i]:
            if rec(board, [], 0, i):
                return True
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [[True, False, False, True, False],
           [False, True, True, True, True],
           [False, False, False, False, False],
           [True, False, True, True, False],
           [False, True, False, False, False]]
    
    # arr = [[True, False, False, True, False],
    #        [False, True, True, True, True],
    #        [False, False, False, False, False],
    #        [True, False, True, True, False],
    #        [True, True, True, True, True]]

    
    print(knight_travel(arr))