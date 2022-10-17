# NWD trzech liczb
def GCD3(inArr):
    a, b, c = sorted(inArr)[::-1]
    a = a%c
    b = b%c
    if a == 0 and b == 0:
        return c
    if a == 0:
        a = b
    if b == 0:
        b = a
    return GCD3([a, b, c])

# #=======================================
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(GCD3(arr))
