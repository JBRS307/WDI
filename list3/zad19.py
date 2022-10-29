#Znajdź najdłuższy wspólny podciąg, którego suma
#jest równa sumie indeksów

from random import randrange


def count_length_of_substr(arr, n):
    index_sum = 0
    elem_sum = arr[0]
    max_leng = 0

    leng = 1
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            leng += 1
            index_sum += i
            elem_sum += arr[i]
        else:
            if elem_sum == index_sum:
                max_leng = max(max_leng, leng)
            
            leng = 1
            elem_sum = arr[i]
            index_sum = i
    
    if elem_sum == index_sum:
        max_leng = max(max_leng, leng)
    
    return max_leng if max_leng >= 2 else 0
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [1, 1, 1, 3]

    print(*arr)
    print(count_length_of_substr(arr, 4))