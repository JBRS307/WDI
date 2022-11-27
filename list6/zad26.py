from math import isqrt
from os import system


counter = 0
#=====================================================

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%3 == 0 or n%2 == 0 or n <= 1:
        return False

    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True
#-----------------------------------------------------

def build_rec(leng, a, b, take1, res = '1'):
    global counter
    if take1 and a > 0:
        res += '1'
        if len(res) == leng:
            if res[-1] == '0':
                # print(res)
                counter += 1
            elif not is_prime(int(res, 2)):
                # print(res)
                counter += 1
        else:        
            build_rec(leng, a-1, b, True, res)
            build_rec(leng, a-1, b, False, res)
    elif not take1 and b > 0:
        res += '0'
        if len(res) == leng:
            if res[-1] == '0':
                # print(res)
                counter += 1
            elif not is_prime(int(res, 2)):
                # print(res)
                counter += 1
        else:
            build_rec(leng, a, b-1, True, res)
            build_rec(leng, a, b-1, False, res)
#-----------------------------------------------------

def start_build(a, b):
    global counter
    if a == 1:
        counter += 1
    else:
        a -= 1
        build_rec(a+b+1, a, b, True)
        build_rec(a+b+1, a, b, False)
#=====================================================

if __name__ == "__main__":
    system("clear")

    a, b = map(int, input("A, B: ").strip().split())

    start_build(a, b)
    print(counter)