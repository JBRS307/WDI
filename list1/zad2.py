def isNumInSeq(a, b, num):
    while b <= num:
        a, b = b, a+b
        if b == num:
            return True
    return False
#-----------------------------------------------------
def findBeginningPair(year):
    currSum = 1
    while True:
        for a in range(currSum):
            b = currSum-a
            if isNumInSeq(a, b, year):
                return a, b
        currSum += 1
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(*findBeginningPair(n))