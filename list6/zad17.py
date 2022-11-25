from math import log10, isqrt
from os import system


counter = 0

# def to_int(arr):
#     res = 0
#     for i in range(1, len(arr)+1):
#         res += arr[-i]*(10**(i-1))
    
#     return res
#-----------------------------------------------------

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True
#=====================================================

def build_num(leng, arr1, arr2, num1, num2, i1=0, i2=0, res_num=0):
    global counter
    if num1 and i1 < len(arr1):
        res_num = 10*res_num + arr1[i1]
        if res_num != 0 and int(log10(res_num))+1 == leng and is_prime(res_num):
            counter += 1
            return
        build_num(leng, arr1, arr2, True, False, i1+1, i2, res_num)
        build_num(leng, arr1, arr2, False, True, i1+1, i2, res_num)
    elif num2 and i2 < len(arr2):
        res_num = 10*res_num + arr2[i2]
        if res_num != 0 and int(log10(res_num))+1 == leng and is_prime(res_num):
            counter += 1
            return
        build_num(leng, arr1, arr2, True, False, i1, i2+1, res_num)
        build_num(leng, arr1, arr2, False, True, i1, i2+1, res_num)
#-----------------------------------------------------

def start(num1, num2):
    leng1 = int(log10(num1))+1
    leng2 = int(log10(num2))+1


    arr1 = [0]*leng1
    arr2 = [0]*leng2

    for i in range(-1, -leng1-1, -1):
        arr1[i] = num1%10
        num1 //= 10

    for i in range(-1, -leng2-1, -1):
        arr2[i] = num2%10
        num2 //= 10
    
    build_num(leng1+leng2, arr1, arr2, True, False)
    build_num(leng1+leng2, arr1, arr2, False, True)
#=====================================================

if __name__ == "__main__":
    system("clear")
    num1, num2 = map(int, input().strip().split())

    start(num1, num2)
    print(counter)

    # print(to_int([1, 2, 3]))

    # print(is_prime(63))


