#Sprawdź czy wyraz jest wielokrotnością dowolnego wyrazu ciągu an

def checkSeries(num):
    a = 3
    n = 1
    while a <= num//2:
        if num%a == 0:
            return True
        n += 1
        a = n*n+n+1
    
    return False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(checkSeries(n))