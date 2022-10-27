#Najdłuższy spójny podciąg arytmetyczny
#UWAGA!!! 0 NIE jest liczbą naturalną

from random import randrange

def longestSubSeqGe(arr, n):
    start = end = length = 0
    quot = 0

    for i in range(1, n):
        if start == end:
            quot = arr[i]/arr[i-1]
            end += 1
        else:
            if arr[i]/arr[i-1] == quot:
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
    arr = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    
    print(*arr)
    print(longestSubSeqGe(arr, n))