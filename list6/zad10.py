#Obliczenie wyznacznika metodą laplace'a

from os import system
from copy import deepcopy
from random import randrange


def make_new_arr(arr, col):
    res = deepcopy(arr)
    res.pop(0)
    # print(res)
    for i in range(len(res)):
        res[i].pop(col)
    
    return res
#-----------------------------------------------------

def laplace(arr):
    leng = len(arr)
    if leng == 1:
        return arr[0][0]
    row = arr[0]

    res = 0
    for i in range(leng):
        new_arr = make_new_arr(arr, i)
        res += (-1)**i * row[i] * laplace(new_arr)
    
    return res
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = [[randrange(1, 21) for _ in range(5)] for _ in range(5)]
    
    print(laplace(arr))
