#NWW trzech liczb

def lcm3(a, b, c):
    a1 = a
    b1 = b
    c1 = c

    while True:
        if a == b and a == c:
            break
        if c <= a and c <= b:
            c += c1
        elif b <= a and b <= c:
            b += b1
        elif a <= c and a <= b:
            a += a1
    return a
#=====================================================
if __name__ == "__main__":
    a, b, c = list(map(int, input().strip().split()))

    print(lcm3(a, b, c))
