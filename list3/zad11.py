#Najdłuższy spójny podciąg arytmetyczny
#UWAGA!!! 0 NIE jest liczbą naturalną

from random import randrange

def longestSubSeqGe(arr, n):
    maxLen = 1
    length = 2

    quot = arr[1]/arr[0]
    for i in range(2, n):
        if arr[i]/arr[i-1] == quot:
            length += 1
        else:
            maxLen = max(maxLen, length)
            length = 2
            quot = arr[i]/arr[i-1]
    
    return max(maxLen, length)
#=====================================================
if __name__ == "__main__":
    n = int(input("Rozmiar: "))
    # k = int(input("Zakres: "))

    # arr = [randrange(1, k+1) for _ in range(n)]
    arr = [1, 2, 4, 8, 16, 32, 64, 128, 25622]
    
    print(*arr)
    print(longestSubSeqGe(arr, n))