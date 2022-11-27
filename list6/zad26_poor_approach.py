from os import system
from math import isqrt


counter = 0
created = []
#=====================================================

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True
#-----------------------------------------------------

def build_rec(leng, arr1, arr0, take1, i1=0, i0=0, res = '1'):
    global counter, created
    if len(res) == leng and res not in created:
        if res[-1] == 0:
            # print(res)
            counter += 1
            created.append(res)
        elif not is_prime(int(res, 2)):
            # print(res)
            counter += 1
            created.append(res)
    else:
        if take1 and i1 < len(arr1):
            res += '1'
            build_rec(leng, arr1, arr0, True, i1+1, i0, res)
            build_rec(leng, arr1, arr0, False, i1+1, i0, res)
        elif not take1 and i0 < len(arr0):
            res += '0'
            build_rec(leng, arr1, arr0, True, i1, i0+1, res)
            build_rec(leng, arr1, arr0, False, i1, i0+1, res)
#-----------------------------------------------------

def start_build(a, b): #a - ilość 1, b - ilość 0
    global counter
    if a == 1:
        counter += 1
    else:
        a -= 1
        arr1 = [1]*a
        arr0 = [0]*b

        build_rec(a+b+1, arr1, arr0, True)
        build_rec(a+b+1, arr1, arr0, False)

#=====================================================

if __name__ == "__main__":
    system("clear")

    a, b = map(int, input("A, B: ").strip().split())

    start_build(a, b)
    print(counter)