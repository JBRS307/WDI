from os import system


def cut(arr):
    max_pieces = 0
    leng = len(arr)

    def rec(arr, start=0, pieces=0, sum_p=0):
        nonlocal leng
        if start == leng:
            nonlocal max_pieces
            max_pieces = max(pieces, max_pieces)

        if pieces == 0:
            curr_sum = 0
            for i in range(leng):
                curr_sum += arr[i]
                rec(arr, i+1, pieces+1, curr_sum)
        else:
            curr_sum = 0
            for i in range(start, leng):
                curr_sum += arr[i]
                if curr_sum == sum_p:
                    rec(arr, i+1, pieces+1, sum_p)
    #-----------------------------------------------------

    rec(arr)
    return max_pieces if max_pieces > 1 else 0
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [1, 2, 3, 1, 5, 2, 2, 2, 6]

    print(cut(arr))