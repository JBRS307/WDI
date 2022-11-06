from random import randrange


def to_system_4(n):
    res = ''
    while n > 0:
        res = str(n%4) + res
        n //= 4
    
    return res
#-----------------------------------------------------

def convert_arr(arr, leng):
    arr_4 = ['']*leng
    for i in range(leng):
        arr_4[i] = to_system_4(arr[i])
    
    return arr_4
#-----------------------------------------------------

def find_subseq(arr, leng):
    arr = convert_arr(arr, leng)
    arr[0] = set(arr[0])
    for i in range(1, leng):
        arr[i] = set(arr[i])
    
    sets = []
    for num in arr:
        if num not in sets:
            sets.append(num)
    
    n_o_sets = len(sets)
    res = [0] * n_o_sets

    i = 0
    for num in sets:
        res[i] = arr.count(num)
    
    return max(res)
#=====================================================

if __name__ == "__main__":
    n = int(input())
    arr = [randrange(1, 1000) for _ in range(n)]
    # print(to_system_4(n))
    print(arr)
    print(find_subseq(arr, n))