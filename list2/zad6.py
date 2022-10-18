from math import isqrt

def divs(n):
    for i in range(isqrt(n)+1, 0, -1):
        if n%i == 0:
            return i, n//i
#==========================================
if __name__ == "__main__":
    n = int(input())
    print(*divs(n))