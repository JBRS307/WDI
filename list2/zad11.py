#Wypisanie czy cyfry w liczbie stanowią ciąg rosnący

def checkIfAscending(n):
    while n != 0:
        last = n%10
        next = (n%100)//10
        if last <= next:
            return False
        n //= 10
    
    return True
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(checkIfAscending(n))