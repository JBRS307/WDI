from os import system


def find_rooks(arr, leng, row, col):
    in_row = False
    in_col = False
    for i in range(col+1, leng-col):
        if arr[row][col+i]:
            in_row = True
            break

    for i in range(row+1, leng-row):
        if arr[row+i][col]:
            in_col = True
            break
    
    return (in_row and in_col)
#-----------------------------------------------------

def move(arr):
    leng = len(arr)

    free_row = -1
    free_col = -1

    for row in range(leng):
        if True in arr[row]:
            continue
        free_row = row
        break
    

    for col in range(leng):
        for row in range(leng):
            if arr[row][col]:
                break
        else:
            free_col = col
            break
    

    for i in range(leng):
        for j in range(leng):
            if arr[i][j]:
                if find_rooks(arr, leng, i, j):
                    move_from = (i, j)
    
    if free_row != -1 and free_col != -1:
        return move_from, (free_row, free_col)
    
    if free_row != -1:
        for col in range(leng):
            if not(arr[free_row][col]):
                return move_from, (free_row, col)
    
    if free_col != -1:
        for row in range(leng):
            if not(arr[row][free_col]):
                return move_from (row, free_col)
#=====================================================

if __name__ == "__main__":
    system("clear")