#Zadanie 12 z tablicą

def checkDigit(n):
    num = []
    counter = 0
    while n != 0:
        num.append(n%10)
        n //= 10
        counter += 1
    
    if counter in num:
        return True
    return False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(checkDigit(n))