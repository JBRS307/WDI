#Sprawdź ile liczb podzielnych przez 7 można stworzyć z n poprzez wykreślanie cyfr

def addOneBin(m):
    i = 1
    while m[-i] != "0":
        i += 1
    
    m = m[:-i] + "1" + (i-1) * "0"
    return m
#-----------------------------------------------------

def countSevenDiv(n):
    length = len(n)
    counter = 0
    mask = length * "0"
    
    for i in range(1, 2**length):
        mask = addOneBin(mask)
        subNum = ""
        for j in range(length):
            if mask[j] == "1":
                subNum += n[j]
        
        if int(subNum)%7 == 0:
            print(subNum, end=" ")
            counter += 1
    
    print("\n", counter, sep="")
#=====================================================

if __name__ == "__main__":
    n = input().strip()
    countSevenDiv(n)