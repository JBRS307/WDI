#Najdłuższy spójny podciąg arytmetyczny

from random import randrange

def longestSubSeqAr(arr, n):
    maxLen = 1
    length = 2
    
    dif = arr[1] - arr[0]
    for i in range(2, n):
        if arr[i] - arr[i-1] == dif:
            length += 1
        else:
            maxLen = max(maxLen, length)
            length = 2
            dif = arr[i] - arr[i-1]
    
    return max(maxLen, length)
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))
    k = int(input("Zakres: "))

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [2, 1, 2, 3, 4, 3]
    
    print(*arr)
    print(longestSubSeqAr(arr, n))