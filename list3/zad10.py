#Najdłuższy spójny podciąg arytmetyczny

from random import randrange

def longestSubSeqAr(arr, n):
    start = end = length = 0
    dif = 0

    for i in range(1, n):
        if start == end:
            dif = arr[i] - arr[i-1]
            end += 1
        else:
            if arr[i] - arr[i-1] == dif:
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
    # k = int(input("Zakres: "))

    # arr = [randrange(1, k+1) for _ in range(n)]
    arr = [6, 3, 3, 2, 5, 6, 5, 7, 1, 6]
    
    print(*arr)
    print(longestSubSeqAr(arr, n))