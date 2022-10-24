#Program do sprawdzenia czy liczba zawiera cyfrę równą liczbie swoic cyfr

def countDigits(n):
    counter = 0
    while n != 0:
        n //= 10
        counter += 1
    
    return counter
#-----------------------------------------------------
def checkDigit(n):
    numOfDigits = countDigits(n)
    while n != 0:
        if n%10 == numOfDigits:
            return True
        n //= 10

    return False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    #print(countDigits(n))
    print(checkDigit(n))