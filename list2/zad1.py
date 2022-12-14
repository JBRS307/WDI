# Sprawdź czy iloczyn dwóch dowolnych liczb ciągu fib jest liczbą wpisaną z klawiatury

def checkFib(n):
    if n == 0 or n == 1:
        return True
    a = 0
    b = 1
    while b < n:
        a, b = b, a+b
        x = 0
        y = 1
        while b*y < n:
            x, y = y, x+y
            if b*y == n:
                return True
    return False
#========================================
if __name__ == "__main__":
    n = int(input())
    print(checkFib(n))