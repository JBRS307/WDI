#Wypisz ułamek okresowy

def findPeriod(a, b):
    digits = []
    modulo = []
    
    first = str(a//b) + '.'
    while a > 0:
        a *= 10
        digits.append(a//b)

        if a not in modulo:
            modulo.append(a)
        else:
            break
            
        a %= b
    
    if a == 0:
        return first + ''.join(map(str, digits))
    
    repeatFrom = modulo.index(a)
    return first + ''.join(map(str, digits[:repeatFrom])) + '(' + ''.join(map(str, digits[repeatFrom:-1])) + ')'
        
#==================================================
if __name__ == "__main__":
    a, b = map(int, input().strip().split())

    print(findPeriod(a, b))