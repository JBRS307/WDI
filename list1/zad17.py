#Wyznaczenie złotej proporcji

def fib(a,b):
    while b < 1_000_000:
        a, b = b, b+a
        print(b/a)
#=====================================================
if __name__ == "__main__":
    a, b = list(map(int, input().strip().split()))
    fib(a, b)