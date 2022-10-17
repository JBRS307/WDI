# Doskonałe mniejsze niż 1_000_000
def isPerfect(n):
    if n == 1:
        return True
    testSum = 1
    for i in range(2, n//2+1):
        if n%i == 0:
            testSum += i
    return testSum == n
#==========================================
if __name__ == "__main__":
    for i in range(1, 1_000_000):
        if isPerfect(i):
            print(i, end=" ")
    print()