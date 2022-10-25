#Sprawdzenie czy liczby składają się z tych samych cyfr

def sameDigits(a, b):
    digits = [0] * 10
    
    for dig in a:
        digits[int(dig)] += 1
    
    for dig in b:
        digits[int(dig)] -= 1
    
    for dig in digits:
        if dig != 0:
            return False
    
    return True
#=====================================================
if __name__ == "__main__":
    a, b = input().strip().split()

    print(sameDigits(a, b))
