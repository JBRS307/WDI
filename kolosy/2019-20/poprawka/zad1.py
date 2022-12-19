from os import system
from random import randrange


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()
#=====================================================

def gcf(a, b):
    if b > a:
        a, b = b, a
    
    while b != 0:
        a, b = b, a%b
    
    return a
#-----------------------------------------------------

def domino(arr): #klocek1 leży poziomo, klocek2 - pionowo
    leng = len(arr)

    for row1 in range(leng): 
        for col1 in range(leng-1): #współrzędne głowy 1
            for row2 in range(leng-1):
                for col2 in range(leng): #współrzędne głowy 2
                    brick1_head = (row1, col1)
                    brick1_tail = (row1, col1+1)
                    brick2_head = (row2, col2)
                    brick2_tail = (row2+1, col2)
                    
                    if not(row1 == row2 or row1 == row2+1 or \
                       col1 == col2 or col1+1 == col2):
                        num1 = arr[brick1_head[0]][brick1_head[1]]
                        num2 = arr[brick1_tail[0]][brick1_tail[1]]
                        num3 = arr[brick2_head[0]][brick2_head[1]]
                        num4 = arr[brick2_tail[0]][brick2_tail[1]]

                        factor = gcf(num1, num2)
                        factor = gcf(factor, num3)
                        factor = gcf(factor, num4)

                        if factor == 1:
                            print((brick1_head, brick1_tail), (brick2_head, brick2_tail))
                            return True
    
    return False
#=====================================================

if __name__ == "__main__":
    system("clear")

    n = 8
    k = 20

    arr = [[randrange(1, k+1) for _ in range(n)] for _ in range(n)]

    # arr = [[2]*5 for _ in range(5)]

    print_arr(arr)
    print(domino(arr))