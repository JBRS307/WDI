#Sprawdź czy w tablicy istnieją 2 spójne podciągi rosnące takie,
#że da się je połączyć w jeden ciąg rosnący. Każdy podciąg musi mieć długośc
#co najmniej 3

from random import randrange


def find_substrs(arr):
    leng = len(arr)

    beg = 0
    end = 0
    min_end = float('inf')
    max_beg = 0
    str_leng = 1
    for i in range(1, leng):
        if arr[i] <= arr[i-1]:
            if str_leng > 2:
                min_end = min(min_end, arr[end])
                max_beg = max(max_beg, arr[beg])
            beg = i
            end = i
            str_leng = 1
        else:
            end += 1
            str_leng += 1
    
    if str_leng > 2:
        min_end = min(min_end, arr[end])
        max_beg = max(max_beg, arr[beg])
    
    return True if max_beg > min_end else False
#=====================================================

if __name__ == "__main__":
    # arr = [7, 8, 9, 0, 0, 0, 1, 2, 3]
    # arr = [7, 2, 5, 8, 6, 3, 5, 9, 9, 2, 3, 2, 6, 1, 1, 6, 9, 6, 1, 9]

    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]


    print(arr)
    print(find_substrs(arr))

