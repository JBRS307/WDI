#Sprawdź czy w każdym wierszu tablicy występuje co najmniej
#jedna liczba złożona z nieparzystych cyfr

from random import randrange


def all_digs_odd(n):
    while n > 0:
        if (n%10)%2 == 0:
            return False
        n //= 10
    
    return True
#-----------------------------------------------------

def check_lines(arr):
    for line in arr:
        for num in line:
            if all_digs_odd(num):
                break
        else:
            return False
    
    return True
#-----------------------------------------------------

def print_arr(arr):
    for line in arr:
        print(line)
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(1, k+1) for i in range(n)] for j in range(n)]

    print_arr(arr)
    print(check_lines(arr))