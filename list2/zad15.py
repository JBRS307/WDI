#Liczba n-cyfrowa która jest sumą n-tych potęg cyfr

def power(n, k):
    res = 1
    for _ in range(k):
        res *= n
    
    return res
#-----------------------------------------------------
def findNumbers(n):
    for x in range(power(10, n-1), power(10, n)-1):
        num = x
        summ = 0
        while num > 0:
            summ += power(num%10, n)
            num //= 10
        
        if x == summ:
            print(x, end = " ")
    
    print()
#=====================================================
if __name__ == "__main__":
    n = int(input())
    findNumbers(n)