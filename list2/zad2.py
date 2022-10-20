#Wypisz liczbę z dokładnością do n miejsc po przecinku

def writeNumber(a, b, n):
    print(a//b, "." if a%b != 0 else "", sep="", end="")
    a %= b
    while a > 0 and n > 0:
        a *= 10
        print(a//b, end="")
        a %= b
        n -= 1
    print()
#=====================================================
if __name__ == "__main__":
    a, b, n = list(map(int, input().strip().split()))
    writeNumber(a, b, n)