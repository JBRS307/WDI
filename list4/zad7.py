from random import randrange


def create_arr(n, k):
    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        arr[i].sort()
    
    return arr
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#-----------------------------------------------------

def merge_lines(arr, n):
    res = [0]*(n*n)

    res_i = 0
    for _ in range(n*n):
        min_elem = float('inf')
        min_index = 0
        for i in range(n):
            try:
                if arr[i][0] < min_elem:
                    min_elem = arr[i][0]
                    min_index = i
            except:
                pass
        
        if min_elem not in res:
            res[res_i] = min_elem
            res_i += 1
        del arr[min_index][0]
    
    return res            
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = create_arr(n, k)
    print_arr(arr)

    print(merge_lines(arr, n))