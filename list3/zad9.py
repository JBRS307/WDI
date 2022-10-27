#Wyznacz nadłuższy podciąg rosnący w tablicy

from random import randrange

def longestSubSeqUp(arr, n):
    length = 1
    maxLen = 0

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            length += 1
        else:
            maxLen = max(maxLen, length)
            length = 1

    return max(maxLen, length)
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))
    k = int(input("Zakres: "))

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(*arr)
    print(longestSubSeqUp(arr, n))