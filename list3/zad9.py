#Wyznacz nadłuższy podciąg rosnący w tablicy

from random import randrange

def longestSubSeqUp(arr, n):
    start = 0
    end = 0
    length = 0

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            end += 1
        else:
            if (end-start)+1 > length:
                length = (end-start)+1
            start = end = i
    
    if (end-start)+1 > length:
        length = (end-start)+1

    return length
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))
    k = int(input("Zakres: "))

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(*arr)
    print(longestSubSeqUp(arr, n))