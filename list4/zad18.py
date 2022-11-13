from random import randrange


def find_substr(arr):
    leng = len(arr)
    res = 0
    for row in range(leng):
        for col in range(leng):
            for i in range(1, 11):
                if i+row < leng:
                    sum = 0
                    for x in range(row, i+row+1):
                        sum += arr[x][col]
                    res = max(res, sum)

                if i+col < leng:
                    sum = 0
                    for x in range(col, i+col+1):
                        sum += arr[row][x]
                    res = max(res, sum)
    
    return res
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(-k, 1+k) for _ in range(n)] for _ in range(n)]

    print(find_substr(arr))