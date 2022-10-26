#Sprawdź czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą

from random import randrange

def createArr(n):
    return [randrange(1, 1001) for _ in range(n)]
#-----------------------------------------------------
def oddDigits(arr):
    for num in arr:
        while num > 0:
            if (num%10)%2:
                break
            num //= 10
        else:
            return False
    
    return True
#=====================================================
if __name__ == "__main__":
    n = int(input())
    arr = createArr(n)
    print(*arr)
    print(oddDigits(arr))