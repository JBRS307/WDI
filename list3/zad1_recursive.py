#Zamień liczbę na system liczbowy od 2-16

def toSystem(n, system):
    if n//system != 0:
        toSystem(n//system, system)
    
    x = n%system
    if x >= 10:
        print(chr(x+55), end='')
    else:
        print(x, end='')
#=====================================================
if __name__ == "__main__":
    n, system = list(map(int, input().strip().split()))
    toSystem(n, system)
    print()
