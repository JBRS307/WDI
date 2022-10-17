# Wypisz podzielniki liczby
def findDiv(n):
    res = [1]
    if n%2 == 0:
        res.append(2)
        for i in range(3, n//2+1):
            if n%i == 0:
                res.append(i)
        res.append(n)
        return res
    else:
        for i in range(3, n//2+1, 2):
            if n%i == 0:
                res.append(i)
        res.append(n)
        return res
#=============================================
if __name__ == "__main__":
    n = int(input().strip())
    print(*findDiv(n))
    