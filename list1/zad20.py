#Średnia arytmetoczno-geometryczna (AGM)

from math import sqrt

def AGM(a, b, eps=0.00000001):
    while abs(a-b) > eps:
        a, b = (a+b)/2, sqrt(a*b)
    return a
#=====================================================
if __name__ == "__main__":
    a, b = list(map(int, input().strip().split()))
    print(AGM(a, b))