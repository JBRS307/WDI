#Znalezienie systemu w jakim dwie liczby są różnocyfrowe

def toSystem(n, system):
    mask = ord('A')-10 #Maska do używania w wypadku systemów większych niż 10
    res = ''
    while n > 0:
        bit = n%system
        if bit >= 10:
            res = chr(mask+bit)+res
        else:
            res = str(bit) + res
        n //= system
    
    return res
#-----------------------------------------------------
def checkDiff(a, b):
    for sys in range(2, 17):
        sys_a, sys_b = toSystem(a, sys), toSystem(b, sys)
        for char in sys_a:
            if char in sys_b:
                break
        else:
            return sys
    
    return None
#=====================================================
if __name__ == "__main__":
    a, b = list(map(int, input().strip().split()))

    print(checkDiff(a, b))
