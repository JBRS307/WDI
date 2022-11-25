from math import isqrt
from os import system


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if n%i == 0 or n%(i+2) == 0:
            return False
    return True

def to_int(arr, start, end):
    res = 0
    n = 0
    for i in range(end, start-1, -1):
        res += arr[i]*(2**n)
        n += 1

    # return res
    return is_prime(res)
#-----------------------------------------------------

def check_cut(arr, i=0):
    flag = False #flag dzięki niemu możemy zwracać co chcemy
    if i >= len(arr): #Jeżeli dojechaliśmy do końca, znaczy, że tablice da się podzielić zgodnie z warunkiem
        return True   #zadania
    for j in range(1, min(30, len(arr)-i)):
        start = i
        end = i+j
        if to_int(arr, start, end): #Jeżeli fragment jest pierwszy to sprawdzaj dalej
            flag = check_cut(arr, end+1)
    
    return flag
#=====================================================

if __name__ == "__main__":
    # print(to_int([1, 0, 1], 0, 2))

    print(check_cut([1, 1, 1, 0, 1, 1]))
    print(check_cut([1, 1, 0, 1, 0, 0]))
