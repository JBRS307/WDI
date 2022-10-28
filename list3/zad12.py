#Różnica między długością najdłuższego podciągu malejącego
#i najdłuższego podciągu rosnącego w tablicy

from random import randrange


def maxLengths(arr, n):
    max_len_a = max_len_d = 0

    diff = arr[1] - arr[0]
    leng = 2
    for i in range(2, n):
        if arr[i] - arr[i-1] == diff:
            leng += 1
        else:
            if diff > 0:
                max_len_a = max(max_len_a, leng)
            elif diff < 0:
                max_len_d = max(max_len_d, leng)
            
            diff = arr[i] - arr[i-1]
            leng = 2

        if diff > 0:
            max_len_a = max(max_len_a, leng)
        elif diff < 0:
            max_len_d = max(max_len_d, leng)
    
    return max_len_a, max_len_d
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))

    arr = [randrange(1, 100, 2) for _ in range(n)]
    # arr = [15, 49, 45, 1, 91, 51, 55, 5, 89, 27]
    # arr = [9, 15, 41, 39, 15, 69, 49, 91, 21, 41]
    # arr = [9, 8, 7, 6, 5, 6]
    
    print(*arr)
    asc, desc = maxLengths(arr, n)
    print(asc, desc)
    print(abs(asc-desc))