from os import system
from random import randrange


def find_set_rec(arr, leng, i=0, last=0, leng_sum=0):
    if i >= leng:
        if leng_sum == 2022:
            return True
        return False
    
    if find_set_rec(arr, leng, i+1, last, leng_sum):
        return True
    
    a = arr[i][0]
    b = arr[i][1]
    last_a = arr[last][0]
    last_b = arr[last][1]

    if leng_sum != 0:
        if not(a <= last_a <= b or \
            a <= last_b <= b or \
            last_a <= a <= last_b or \
            last_a <= b <= last_b):
            if find_set_rec(arr, leng, i+1, i, leng_sum+(b-a)):
                return True
    else:
        if find_set_rec(arr, leng, i+1, i, leng_sum+(b-a)):
            return True
    
    return False
#-----------------------------------------------------

def find_set(arr):
    leng = len(arr)
    return find_set_rec(arr, leng)
#=====================================================

if __name__ == "__main__":
    system("clear")

    arr = []
    for _ in range(15):
        a = randrange(-1000, 1001)
        b = randrange(a, 1002)
        print((a, b))
        arr.append((a, b))
    
    print(f"\n{find_set(arr)}")