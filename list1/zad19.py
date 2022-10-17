# Dziwne wyznaczenie liczby e

def find_e(n):
    temp = 1
    summ = 2
    for i in range(2, n+1):
        temp *= i
        summ += (1/temp)
    return summ
#=================================================
if __name__ == "__main__":
    n = int(input())
    print(find_e(n))
