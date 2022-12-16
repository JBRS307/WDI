#Nie jestem w stanie sprawdzić, czy to działa

from os import system
from random import randrange

def squares_rec(squares, leng, curr=0, good=1, surf_sum=0):
    if good == 13:
        if surf_sum == 2012:
            return True
        return False
    
    if curr >= leng:
        return False
    
    surf_sum += (x2-x1)*(y2-y1)
    for i in range(curr+1, leng):
        if 0 <= curr+i < leng:
            if not(squares[curr][0] <= squares[curr+i][0] <= squares[curr][1] or \
                   squares[curr][0] <= squares[curr+i][1] <= squares[curr][1] or \
                   squares[curr][2] <= squares[curr+i][2] <= squares[curr][3] or \
                   squares[curr][2] <= squares[curr+i][3] <= squares[curr][3]):
                if squares_rec(squares, leng, curr+1, good+1, surf_sum):
                    return True
    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    n, k = map(int, input("Ilosc, zakres: ").strip().split())

    arr = []
    for i in range(n):
        x1 = randrange(-k, k+1)
        x2 = randrange(x1+1, k+2)
        y1 = randrange(-k, k+1)
        y2 = randrange(y1+1, k+2)

        arr.append((x1, x2, y1, y2))

    print(arr)

    print()
    print(squares_rec(arr, len(arr)))