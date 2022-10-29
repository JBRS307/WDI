#Sprawdzić czy istnieje wiersz talbicy, w którym każda
#liczba ma co najmniej jedną cyfrę parzystą

from random import randrange


def one_dig_even(n):
    while n > 0:
        if (n%10)%2 == 0:
            return True
        n //= 10
    
    return False
#-----------------------------------------------------

def check_lines(arr):
    for line in arr:
        for num in line:
            if not one_dig_even(num):
                break
        else:
            return True
    
    return False
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakes: ").strip().split())

    arr = [[randrange(1, k+1) for i in range(n)] for j in range(n)]

    print_arr(arr)
    print(check_lines(arr))