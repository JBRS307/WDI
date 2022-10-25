#Zamiana na dowolny system 2-16, w stringu

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

#=====================================================
if __name__ == "__main__":
    n, system = list(map(int, input().strip().split()))
    print(toSystem(n, system))