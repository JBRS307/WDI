#Rekursywne skakanie po tablicy

from random import randrange

def createArr(n, k):
    return [randrange(1, k+1) for _ in range(n)]
#-----------------------------------------------------
def factorSplit(n):
    divs = set()

    div = 2
    while n > 1:
        while n%div == 0:
            divs.add(div)
            n //= div
        div += 1
    
    return divs
#-----------------------------------------------------
def isEndPossible(arr, i=0):
    length = len(arr)
    if i >= length or arr[i] <= 1:
        return False
    if i == length-1:
        return True
    
    divs = factorSplit(arr[i])
    for div in divs:
        return isEndPossible(arr, i+div)
    
    return False
#=====================================================
if __name__ == "__main__":
    length = int(input("Wielkosc tablicy: "))
    end = int(input("Zakres: "))

    arr = createArr(length, end)

    print(*arr)
    print(isEndPossible(arr))