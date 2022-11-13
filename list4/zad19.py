from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def condition(n1, n2, cond):
    return n1*n2 == cond
#-----------------------------------------------------

def find_prods(arr, cond):
    leng = len(arr)
    counter = 0

    for i in range(leng):
        for j in range(leng):
            point = arr[i][j]

            for i2, j2 in [(i+1, j+2), (i+2, j+1), (i-1, j+2), (i+2, j-1), (i-2, j+1), (i+1, j-2), (i-1, j-2), (i-2, j-1)]:
                if i2 < 0 or i2 > leng-1 or j2 < 0 or j2 > leng-1:
                    continue

                if condition(point, arr[i2][j2], cond):
                    counter += 1
    
    return counter//2

#=====================================================

if __name__ == "__main__":
    n, k, cond = map(int, input("Rozmiar, zakres, iloczyn: ").strip().split())

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    print_arr(arr)
    print(find_prods(arr, cond))