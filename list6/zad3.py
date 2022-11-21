from random import randrange


def find_path(board, cost_arr, cost, row, col, leng):
    if row >= leng:
        return
    
    cost += board[row][col]

    if cost_arr[row][col] > cost:
        cost_arr[row][col] = cost

        if col > 0:
            find_path(board, cost_arr, cost, row+1, col-1, leng)
        if col+1 < leng:
            find_path(board, cost_arr, cost, row+1, col+1, leng)
        find_path(board, cost_arr, cost, row+1, col, leng)
#-----------------------------------------------------

def find_min_cost(board, col):
    leng = len(board)
    cost = [[float('inf')]*leng for _ in range(leng)]

    find_path(board, cost, 0, 0, col, leng)

    return min(cost[-1])
#=====================================================

if __name__ == "__main__":
    leng, k = map(int, input().strip().split())
    start_col = int(input())

    board = [[randrange(1, k+1) for _ in range(leng)] for _ in range(leng)]

    print(find_min_cost(board, start_col))
