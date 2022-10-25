#wypełnia tablice losowo

from random import randrange

def createArr(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = randrange(1, 1001)
    
    return arr
#-----------------------------------------------------
def checkIfOdd(arr):
    for n in arr:
        while n != 0:
            if n%2 == 0:
                break
            n //= 10
        else:
            return True
        
    return False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    arr = createArr(n)
    print(*arr)
    print(checkIfOdd(arr))