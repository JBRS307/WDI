#Piąte przez szukanie maksa

def createArr():
    res = [int(input())]
    while True:
        n = int(input())
        if n == 0:
            return res
        res.append(n)
#-----------------------------------------------------
def findTenth(arr):
    for _ in range(9):
        minn = float('inf')
        indexMinn = 0
        for i in range(len(arr)):
            if arr[i] <= minn:
                minn = arr[i]
                indexMinn = i
        arr.pop(indexMinn)
    
    minn = float('inf')
    for i in range(len(arr)):
        if arr[i] <= minn:
            minn = arr[i]
    
    return minn
#=====================================================
if __name__ == "__main__":
    arr = createArr()
    print(findTenth(arr))
