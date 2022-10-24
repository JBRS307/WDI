#Sprawdź czy liczba kończy się unikalną cyfrą

def checkUnique(n):
    last = n%10
    n //= 10
    while n > 0:
        if n%10 == last:
            return False
        n //= 10
    
    return True
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(checkUnique(n))