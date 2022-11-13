#Znajdź kwadrat, którego iloczyn narożników jest równy k


from random import randrange


def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def find_square(arr, leng, k):
    n = 0
    while n < leng:
        for i in range(leng):
            a = arr[i][n]
            for j in range(2, min(leng-i, leng-n), 2):
                b = arr[i][n+j]
                c = arr[i+j][n+j]
                d = arr[i+j][n]
                prod = a*b*c*d
                if prod == k:
                    return i, n
        n += 1
    
    return None
#=====================================================

if __name__ == "__main__":
    # n, k, zak = map(int, input("Rozmiar, 'k', zakres: ").strip().split())

    # arr = [[randrange(1, zak+1) for _ in range(n)] for _ in range(n)]


    arr = [[1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5]]

    # arr = [[0, 1, 0, 1, 0],
    #        [0, 0, 0, 0, 0],
    #        [0, 1, 0, 1, 0],
    #        [0, 0, 0, 0, 0],
    #        [0, 0, 0, 0, 0]]

    print_arr(arr)

    print(find_square(arr, 5, 9))
    print(find_square(arr, 5, 64))
    print(find_square(arr, 5, 25))
    print(find_square(arr, 5, 225))
    print(find_square(arr, 5, 10010293939))
    print(find_square(arr, 5, 9))

    # print(find_square(arr, 5, 1))

