from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def circle_sum(arr):
    leng = len(arr)
    ver = (-1, 0, 1)
    hor = (-1, 0, 1)
    point = (None, None)

    res = 0
    for row in range(leng):
        for col in range(leng):
            sum = 0
            for x in ver:
                for y in hor:
                    if x != 0 or y != 0:
                        if row+x >= 0 and row+x < leng and col+y >= 0 and col+y < leng:
                            sum += arr[row+x][col+y]
            if sum > res:
                res = sum
                point = (row, col)
            
    return point
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)

    print(circle_sum(arr))

